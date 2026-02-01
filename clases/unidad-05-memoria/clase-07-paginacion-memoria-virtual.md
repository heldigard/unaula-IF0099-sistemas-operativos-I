---
marp: true
theme: default
paginate: true
header: 'IF0099 - Sistemas Operativos I | Unidad 5'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
---

# Clase 7: Paginación y Memoria Virtual

<style>
section {
  font-size: 20px;
  overflow: hidden;
}
img {
  max-width: 70% !important;
  max-height: 50vh !important;
  object-fit: contain !important;
  height: auto !important;
  display: block !important;
  margin: 0 auto !important;
}
section h1 {
  font-size: 1.8em;
}
section h2 {
  font-size: 1.4em;
}
section h3 {
  font-size: 1.2em;
}
section ul, section ol {
  font-size: 0.9em;
  margin-left: 1em;
}
section li {
  margin-bottom: 0.3em;
}
section pre {
  font-size: 0.7em;
  max-height: 60vh;
  overflow-y: auto;
}
section code {
  font-size: 0.85em;
}
section p {
  margin: 0.5em 0;
}
/* Estilos para tablas responsivas */
section table {
  width: 100%;
  max-width: 100%;
  font-size: 0.95em;
  border-collapse: collapse;
  margin: 0.5em auto;
  table-layout: auto;
}
section th {
  background-color: #1e40af;
  color: white;
  padding: 0.4em 0.6em;
  text-align: left;
  font-size: 0.95em;
  border: 1px solid #ddd;
}
section td {
  padding: 0.4em 0.6em;
  border: 1px solid #ddd;
  vertical-align: top;
  word-wrap: break-word;
  font-size: 0.9em;
}
section tbody tr:nth-child(even) {
  background-color: #f8f9fa;
}
section tbody tr:hover {
  background-color: #e9ecef;
}
section {
  padding: 1em 2em;
  box-sizing: border-box;
}
@media screen and (max-width: 1280px) {
  section table {
    font-size: 0.85em;
  }
  section th, section td {
    padding: 0.3em 0.4em;
  }
}
</style>

---
## Páginas, Marcos, Tablas y Page Faults

**IF0099 - Sistemas Operativos I**
*4° Semestre - Ingeniería Informática*

![Paginación de Memoria](../../../assets/infografias/clase-07-tabla-paginas.png)

**Conceptos fundamentales que veremos:**
- **Páginas**: Bloques de memoria lógica del proceso
- **Marcos**: Bloques de memoria física en RAM
- **Tablas de páginas**: Mapa páginas → marcos
- **Page Fault**: Cuando una página no está en RAM
- **Memoria virtual**: Procesos más grandes que la RAM disponible

---

## Objetivos de la Clase

Al finalizar esta clase, el estudiante será capaz de:

1. **Explicar** el mecanismo de paginación
2. **Traducir** direcciones usando tablas de páginas
3. **Describir** el funcionamiento de la memoria virtual
4. **Analizar** algoritmos de reemplazo de páginas

**Duración:** 90 minutos

---

## El Problema de la Fragmentación Externa

### Recordatorio de la clase anterior

```
Con asignación contigua:
┌─────┐
│  A  │
├─────┤
│HUECO│ 50KB
├─────┤
│  B  │
├─────┤
│HUECO│ 30KB     Total libre: 120KB
├─────┤          Proceso nuevo: 100KB
│  C  │          ¿Puede cargarse? NO
├─────┤
│HUECO│ 40KB
└─────┘
```

### Solución: **Paginación**
¡No necesitamos memoria contigua!

---

## Idea de la Paginación

### Dividir memoria en bloques de tamaño fijo

```
MEMORIA LÓGICA (Proceso)          MEMORIA FÍSICA
      PÁGINAS                         MARCOS
┌─────────────┐                 ┌─────────────┐ Marco 0
│   Página 0  │                 │   Página 2  │
├─────────────┤                 ├─────────────┤ Marco 1
│   Página 1  │                 │   Página 0  │
├─────────────┤                 ├─────────────┤ Marco 2
│   Página 2  │                 │    (libre)  │
├─────────────┤                 ├─────────────┤ Marco 3
│   Página 3  │                 │   Página 3  │
└─────────────┘                 ├─────────────┤ Marco 4
                                │   Página 1  │
                                └─────────────┘
```

**Página** = Bloque de memoria lógica
**Marco** = Bloque de memoria física
**Tamaño típico:** 4KB (4096 bytes)

---

## Traducción de Direcciones

### Dirección lógica = Número de página + Desplazamiento

```
Dirección lógica: 5000 (en bytes)
Tamaño de página: 4096 bytes

Número de página = 5000 / 4096 = 1
Desplazamiento   = 5000 % 4096 = 904

         TABLA DE PÁGINAS
        ┌───────┬────────┐
        │Página │ Marco  │
        ├───────┼────────┤
        │   0   │   1    │
        │   1   │   4    │ ← Página 1 está en Marco 4
        │   2   │   0    │
        │   3   │   3    │
        └───────┴────────┘

Dirección física = Marco 4 × 4096 + 904 = 16384 + 904 = 17288
```

---

## Diagrama de Traducción

```
        DIRECCIÓN LÓGICA
    ┌────────────┬──────────────┐
    │ # Página   │ Desplazamiento│
    │    (p)     │     (d)       │
    └─────┬──────┴───────┬───────┘
          │              │
          ▼              │
    ┌───────────┐        │
    │  TABLA    │        │
    │    DE     │        │
    │  PÁGINAS  │        │
    └─────┬─────┘        │
          │              │
          ▼              ▼
    ┌────────────┬──────────────┐
    │ # Marco    │ Desplazamiento│
    │    (f)     │     (d)       │
    └────────────┴──────────────┘
        DIRECCIÓN FÍSICA
```

---

## Ejemplo Completo

```
Memoria física: 64 KB (16 marcos de 4 KB)
Proceso: 16 KB (4 páginas de 4 KB)

Tabla de páginas del proceso:
┌───────┬────────┬────────┐
│Página │ Marco  │ Válido │
├───────┼────────┼────────┤
│   0   │   5    │   1    │
│   1   │   9    │   1    │
│   2   │   2    │   1    │
│   3   │  12    │   1    │
└───────┴────────┴────────┘

Traducir dirección lógica: 8500

Página = 8500 / 4096 = 2
Desplazamiento = 8500 % 4096 = 308

Marco de página 2 = 2
Dirección física = 2 × 4096 + 308 = 8500 ✓
```

---

## Ventajas de la Paginación (1/2)

### ✅ Elimina fragmentación externa

```
ANTES (contigua):               DESPUÉS (paginación):
┌─────┐                         ┌─────┐ Marco 0: P1.pág0
│  A  │                         ├─────┤ Marco 1: P2.pág0
├─────┤                         ├─────┤ Marco 2: P1.pág1
│HUECO│ No podemos usar         ├─────┤ Marco 3: P3.pág0
├─────┤                         ├─────┤ Marco 4: P2.pág1
│  B  │                         ├─────┤ Marco 5: P1.pág2
├─────┤                         └─────┘
│HUECO│ estos espacios
├─────┤ para P4
│  C  │
└─────┘
```

---

## Ventajas de la Paginación (2/2)

### Con paginación, P4 puede usar marcos no contiguos

### ⚠️ Aún puede haber fragmentación interna
(Si un proceso no usa toda su última página)

---

## Memoria Virtual

### Más memoria de la que físicamente existe

```
    MEMORIA VIRTUAL                    MEMORIA FÍSICA
    (por proceso)                         (real)
┌─────────────────┐                 ┌─────────────────┐
│                 │                 │                 │
│   4 GB          │                 │   8 GB          │
│   de espacio    │ ──parcialmente──│   compartida    │
│   de direcciones│     cargada     │   entre todos   │
│                 │                 │   los procesos  │
└─────────────────┘                 └─────────────────┘

Cada proceso CREE que tiene 4GB
Solo las páginas en uso están en RAM
El resto está en DISCO (swap)
```

---

## Demand Paging (Paginación por Demanda)

### Solo cargar páginas cuando se necesitan

```
1. Proceso intenta acceder a dirección
2. Buscar en tabla de páginas
3. Si válido=1 → página en RAM → acceder
4. Si válido=0 → PAGE FAULT:
   a. Buscar página en disco
   b. Cargar en marco libre
   c. Actualizar tabla de páginas
   d. Reintentar acceso

┌───────┬────────┬────────┐
│Página │ Marco  │ Válido │
├───────┼────────┼────────┤
│   0   │   5    │   1    │ ← En RAM
│   1   │   -    │   0    │ ← En disco (page fault si se accede)
│   2   │   2    │   1    │ ← En RAM
│   3   │   -    │   0    │ ← En disco
└───────┴────────┴────────┘
```

---

## Page Fault (Fallo de Página)

### Diagrama del proceso

```
┌─────────────────────────────────────────────────────────────┐
│  1. CPU genera dirección lógica                             │
│                    ↓                                        │
│  2. MMU consulta tabla de páginas                           │
│                    ↓                                        │
│  3. Bit válido = 0 → TRAP (page fault)                      │
│                    ↓                                        │
│  4. SO busca página en disco (swap)                         │
│                    ↓                                        │
│  5. SO elige un marco (puede requerir reemplazo)            │
│                    ↓                                        │
│  6. SO carga página del disco al marco                      │
│                    ↓                                        │
│  7. SO actualiza tabla de páginas (válido=1)                │
│                    ↓                                        │
│  8. Se reinicia la instrucción                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Algoritmos de Reemplazo de Páginas

### Cuando no hay marcos libres, ¿cuál página sacar?

| Algoritmo | Descripción | Optimalidad |
| ----------- | ------------- | ------------- |
| **FIFO** | Primera en entrar, primera en salir | Simple pero malo |
| **Óptimo** | Sacar la que se usará más tarde | Imposible de implementar |
| **LRU** | Least Recently Used (menos usada recientemente) | Bueno pero costoso |
| **Clock** | Aproximación a LRU con bit de referencia | Práctico |

---

## Ejemplo: FIFO (Parte 1)

```
| Marcos: 3 | Secuencia de páginas: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5 |

Paso │ Página │ Marco1 │ Marco2 │ Marco3 │ Page Fault?
─────┼────────┼────────┼────────┼────────┼────────────
  1  │   1    │   1    │        │        │    ✓
  2  │   2    │   1    │   2    │        │    ✓
  3  │   3    │   1    │   2    │   3    │    ✓
  4  │   4    │   4    │   2    │   3    │    ✓ (sale 1)
  5  │   1    │   4    │   1    │   3    │    ✓ (sale 2)
  6  │   2    │   4    │   1    │   2    │    ✓ (sale 3)
```

---

## Ejemplo: FIFO (Parte 2)

```
Paso │ Página │ Marco1 │ Marco2 │ Marco3 │ Page Fault?
─────┼────────┼────────┼────────┼────────┼────────────
  7  │   5    │   5    │   1    │   2    │    ✓ (sale 4)
  8  │   1    │   5    │   1    │   2    │    ✗
  9  │   2    │   5    │   1    │   2    │    ✗
 10  │   3    │   5    │   3    │   2    │    ✓ (sale 1)
 11  │   4    │   5    │   3    │   4    │    ✓ (sale 2)
 12  │   5    │   5    │   3    │   4    │    ✗

Page Faults: 9
```

---

## Ejemplo: LRU

```
| Marcos: 3 | Secuencia de páginas: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5 |
```

---

## Ejemplo: LRU (Parte 1)

```
Paso │ Página │ Marco1 │ Marco2 │ Marco3 │ Page Fault? │ Orden LRU
─────┼────────┼────────┼────────┼────────┼─────────────┼──────────
  1  │   1    │   1    │        │        │    ✓        │ 1
  2  │   2    │   1    │   2    │        │    ✓        │ 1,2
  3  │   3    │   1    │   2    │   3    │    ✓        │ 1,2,3
  4  │   4    │   4    │   2    │   3    │    ✓        │ 2,3,4 (1 era LRU)
  5  │   1    │   4    │   1    │   3    │    ✓        │ 3,4,1 (2 era LRU)
  6  │   2    │   4    │   1    │   2    │    ✓        │ 4,1,2 (3 era LRU)
```

---

## Ejemplo: LRU (Parte 2)

```
Paso │ Página │ Marco1 │ Marco2 │ Marco3 │ Page Fault? │ Orden LRU
─────┼────────┼────────┼────────┼────────┼─────────────┼──────────
  7  │   5    │   5    │   1    │   2    │    ✓        │ 1,2,5 (4 era LRU)
  8  │   1    │   5    │   1    │   2    │    ✗        │ 2,5,1
  9  │   2    │   5    │   1    │   2    │    ✗        │ 5,1,2
 10  │   3    │   3    │   1    │   2    │    ✓        │ 1,2,3 (5 era LRU)
 11  │   4    │   3    │   4    │   2    │    ✓        │ 2,3,4 (1 era LRU)
 12  │   5    │   3    │   4    │   5    │    ✓        │ 3,4,5 (2 era LRU)

Page Faults: 10 (¡más que FIFO en este caso!)
```

---

## Thrashing

### Cuando el sistema pasa más tiempo haciendo page faults que ejecutando

```
     Utilización
     de CPU
        │
    100%│          ┌────────────────
        │         /
        │        /
        │       /
        │      /
        │     /
        │    /         THRASHING
        │   / ──────────────────────
        │  /           ▼
      0 │─┴─────────────────────────────
        └──────────────────────────────→
                Grado de multiprogramación
                   (# de procesos)
```

**Causa:** Demasiados procesos compitiendo por pocos marcos

---

## Working Set (Conjunto de Trabajo)

### Páginas activamente usadas por un proceso

```
Si un proceso usa las páginas: 1, 2, 1, 3, 2, 1, 4, 1, 2, 3

En una ventana de tiempo Δ=4:
Posición 10: páginas usadas en posiciones 7-10 = {4, 1, 2, 3}
Working Set = {1, 2, 3, 4}  (4 páginas)

El SO debe asegurar que el proceso tenga al menos
4 marcos para evitar thrashing.
```

---

## TLB (Translation Lookaside Buffer)

### Caché de traducciones de páginas

```
Sin TLB:
CPU → Tabla de páginas (RAM) → Memoria física (RAM)
      ↑ Lento (2 accesos a RAM)

Con TLB:
CPU → TLB (caché) → Si hit: Memoria física (1 acceso)
         ↓
    Si miss: Tabla de páginas → actualizar TLB
```

**TLB típico:** 64-1024 entradas, tiempo de acceso ~1 ns

---

## 📝 Ejercicio: Traducción de Direcciones

### Datos:

- Memoria física: 32 KB (8 marcos de 4 KB)
- Proceso con 3 páginas
- Tabla de páginas: P0→M5, P1→M2, P2→M7

**Traducir las siguientes direcciones lógicas:**
1) 2048
2) 5000  
3) 10240

### Solución:

```
Tamaño de página = 4096 bytes

1) Dirección 2048:
   Página = 2048 / 4096 = 0
   Desplazamiento = 2048 % 4096 = 2048
   Marco = 5 (desde tabla)
   Dir. Física = 5 × 4096 + 2048 = 22528 ✓

2) Dirección 5000:
   Página = 5000 / 4096 = 1
   Desplazamiento = 5000 % 4096 = 904
   Marco = 2 (desde tabla)
   Dir. Física = 2 × 4096 + 904 = 9096 ✓

3) Dirección 10240:
   Página = 10240 / 4096 = 2
   Desplazamiento = 10240 % 4096 = 2048
   Marco = 7 (desde tabla)
   Dir. Física = 7 × 4096 + 2048 = 30720 ✓
```

---

## Working Set: Ejemplo Detallado

### Secuencia de referencias a páginas:
```
1 2 3 4 1 2 5 1 2 3 4 5 | Ventana Δ=4

Posición  Referencias       Working Set    Tamaño
   4:     {1, 2, 3, 4}     {1, 2, 3, 4}      4
   5:     {2, 3, 4, 1}     {1, 2, 3, 4}      4
   6:     {3, 4, 1, 2}     {1, 2, 3, 4}      4
   7:     {4, 1, 2, 5}     {1, 2, 4, 5}      4
   8:     {1, 2, 5, 1}     {1, 2, 5}         3
   9:     {2, 5, 1, 2}     {1, 2, 5}         3
  10:     {5, 1, 2, 3}     {1, 2, 3, 5}      4
```

**Observación:** El proceso necesita al menos 4 marcos para
evitar thrashing en este patrón de acceso.

---

## 🎯 Ventajas y Desventajas de la Paginación

### ✅ Ventajas

| Ventaja | Explicación |
|---------|-------------|
| **No fragmentación externa** | Cualquier marco puede alojar cualquier página |
| **Multiprogramación eficiente** | Procesos comparten memoria fácilmente |
| **Protección simple** | Bits de control en tabla de páginas |
| **Memoria virtual** | Procesos más grandes que RAM |

### ❌ Desventajas

| Desventaja | Explicación |
|-----------|-------------|
| **Fragmentación interna** | Última página puede no usar todo el marco |
| **Sobrecarga de tabla** | Tablas grandes consumen memoria |
| **Tiempo de acceso** | Doble acceso: tabla + dato |

---

## 💡 Ejemplo Real: Linux vs Windows

### Gestión de Memoria Virtual

**Linux:**
```bash
# Ver uso de memoria virtual
$ free -h
              total   usado   libre   compartido   búfer/caché   disponible
Memoria:      8.0Gi   4.2Gi   1.1Gi   256Mi        2.7Gi         3.8Gi
Swap:         2.0Gi   128Mi   1.9Gi

# Ver page faults
$ vmstat 1 5
procs -----------memoria---------- ---swap-- -----io---- -sistema- ------cpu-----
r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
1  0 131072 1048576  ...   ...     0    4     50   100  200  500 10  5 80  5  0
```

**Windows (Task Manager):**
- Memoria confirmada vs física
- Caché en espera vs modificada
- Page file: `C:\pagefile.sys`

---

## 🔍 Comparación de Algoritmos de Reemplazo

### Análisis Visual

| Algoritmo | Complejidad | Eficiencia | Uso Real |
|-----------|-------------|------------|----------|
| **Óptimo** | O(n²) | 5/5 | Solo teórico |
| **FIFO** | O(1) | 2/5 | Sistemas simples |
| **LRU** | O(n) | 4/5 | Variantes tipo LRU/Clock |
| **Clock** | O(n) | 4/5 | Sistemas modernos |
| **LFU** | O(n log n) | 3/5 | Cachés especializadas |

### 💡 Observación
LRU es el más usado en producción por su balance
eficiencia/complejidad.

---

## 📊 Cálculo de Overhead de Paginación

### Ejemplo Real: Sistema de 32 bits

**Datos:**
- Espacio de direcciones: 4 GB (2³² bytes)
- Tamaño de página: 4 KB (2¹² bytes)
- Número de páginas: 4GB / 4KB = 1M páginas
- Entrada de tabla: 4 bytes (32 bits)

**Overhead:**
```
Tamaño de tabla = 1M páginas × 4 bytes = 4 MB por proceso

Con 100 procesos:
Memoria solo para tablas = 100 × 4 MB = 400 MB 😱
```

**Solución:** Tablas de páginas multinivel
(usadas por Intel x86)

---

## 🔧 Ejercicio Guiado: TLB Miss Rate

### Escenario
- TLB: 64 entradas
- Tiempo acceso TLB: 2 ns
- Tiempo acceso RAM: 100 ns
- Hit rate TLB: 95%

### Cálculo del EMAT (Effective Memory Access Time)

```
Caso TLB hit (95%):
  Tiempo = 2 ns (TLB) + 100 ns (RAM) = 102 ns

Caso TLB miss (5%):
  Tiempo = 2 ns (TLB) + 100 ns (Tabla) + 100 ns (RAM) = 202 ns

EMAT = 0.95 × 102 + 0.05 × 202
     = 96.9 + 10.1
     = 107 ns
```

**Sin TLB:** 200 ns  
**Con TLB:** 107 ns  
**Mejora:** 46.5% más rápido 🚀

---

## Actividad Práctica (10 min)

### En parejas:

**Dado:**
- 3 marcos disponibles
- Secuencia de páginas: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3

**Calcular page faults usando:**
1. FIFO
2. LRU

**Comparar resultados y discutir.**

---

## Resumen de la Clase

| Concepto | Descripción |
| ---------- | ------------- |
| **Página** | Bloque de memoria lógica (ej: 4KB) |
| **Marco** | Bloque de memoria física |
| **Page Fault** | Acceso a página no cargada |
| **Demand Paging** | Cargar páginas solo cuando se necesitan |
| **TLB** | Caché de traducciones |
| **Thrashing** | Exceso de page faults |

---

## Evaluación (20% - Eval 3)

### Proyecto: Simulador de Paginación - Semana 10

1. Implementar simulador en Python/C
2. Soportar FIFO y LRU
3. Mostrar estadísticas de page faults
4. **Sustentación oral** (10 min por pareja)

**Trabajo en parejas**

---

## Próxima Clase

### Clase 8: Memoria Secundaria y Discos

- Discos magnéticos y SSD
- Tiempo de acceso y latencia
- Planificación de disco
- RAID y almacenamiento

**¡Nos vemos!**
