---
marp: true
theme: default
paginate: true
| header: 'IF0099 - Sistemas Operativos I | Unidad 5' |
footer: 'UNAULA - Ingeniería Informática - 2026-I'

  section {
    font-size: 24px;
  }

---
## Conceptos, Partición y Fragmentación
img {
  max-width: 70% !important;
  max-height: 50vh !important;
  object-fit: contain !important;
  height: auto !important;
  display: block !important;
  margin: 0 auto !important;
}
section {
  font-size: 20px;
  overflow: hidden;
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
  font-size: 0.85em;
  border-collapse: collapse;
  margin: 0.5em auto;
  table-layout: auto;
}
section th {
  background-color: #1e40af;
  color: white;
  padding: 0.4em 0.6em;
  text-align: left;
  font-size: 0.9em;
  border: 1px solid #ddd;
}
section td {
  padding: 0.4em 0.6em;
  border: 1px solid #ddd;
  vertical-align: top;
  word-wrap: break-word;
  font-size: 0.85em;
}
section tbody tr:nth-child(even) {
  background-color: #f8f9fa;
}
section tbody tr:hover {
  background-color: #e9ecef;
}
/* Asegurar que el contenido no desborde */
section {
  padding: 1em 2em;
  box-sizing: border-box;
}
/* Responsividad para tablas anchas */
@media screen and (max-width: 1280px) {
  section table {
    font-size: 0.75em;
  }
  section th, section td {
    padding: 0.3em 0.4em;
  }
}
</style>

---
## Conceptos, Partición y Fragmentación

*(continuación...)*


<!--
[2026-01-31] - Clase enriquecida con infografías

IMÁGENES GENERADAS:
- clase-06-jerarquia-memoria.png: Pirámide de jerarquía de memoria
- clase-06-fragmentacion.png: Comparación fragmentación interna vs externa
- clase-06-traduccion-direcciones.png: Diagrama de traducción lógica a física
-->


**IF0099 - Sistemas Operativos I**
*4° Semestre - Ingeniería Informática*

---

## Objetivos de la Clase

Al finalizar esta clase, el estudiante será capaz de:

1. **Explicar** la jerarquía de memoria
2. **Diferenciar** direcciones lógicas y físicas
3. **Describir** técnicas de partición de memoria
4. **Identificar** fragmentación interna y externa

**Duración:** 90 minutos

---

## ¿Por qué es importante la gestión de memoria?

```
┌─────────────────────────────────────────────────────────┐
│                    PROBLEMA                             │
├─────────────────────────────────────────────────────────┤
│  - Múltiples procesos quieren usar la memoria           │
│  - La memoria es un recurso LIMITADO y CARO             │
│  - Cada proceso cree que tiene toda la memoria          │
│  - Debemos proteger procesos entre sí                   │
└─────────────────────────────────────────────────────────┘

El SO debe:
✓ Asignar memoria a procesos
✓ Liberar memoria cuando terminan
✓ Proteger la memoria de cada proceso
✓ Optimizar el uso de memoria disponible
```

---

## Jerarquía de Memoria

![Jerarquía de Memoria](../../assets/infografias/clase-06-jerarquia-memoria.png){: style="max-width: 60%; max-height: 400px; display: block; margin: 0 auto;"}

---
### Representación ASCII:
                    ▲
                    │  Más rápido
                    │  Más caro
                    │  Menor capacidad
        ┌───────────────────┐
        │    Registros      │  ~1 ns, ~KB
        ├───────────────────┤
        │    Caché L1       │  ~2 ns, ~64KB
        ├───────────────────┤
        │    Caché L2/L3    │  ~10 ns, ~MB
        ├───────────────────┤
        │    RAM (Principal)│  ~100 ns, ~GB
        ├───────────────────┤
        │    SSD            │  ~100 µs, ~TB
        ├───────────────────┤
        │    HDD            │  ~10 ms, ~TB
        └───────────────────┘
                    │
                    │  Más lento
                    │  Más barato
                    │  Mayor capacidad
                    ▼
```

---
### Representación ASCII:

*(continuación...)*

---

## Direcciones Lógicas vs Físicas

### Traducción de Direcciones con MMU

![Traducción de Direcciones](../../assets/infografias/clase-06-traduccion-direcciones.png){: style="max-width: 60%; max-height: 400px; display: block; margin: 0 auto;"}

---

### Dos perspectivas de la memoria (ASCII):
     PROCESO                          MEMORIA FÍSICA
  (ve direcciones                   (direcciones reales)
    lógicas)
                    
┌─────────────┐                    ┌─────────────┐ 0x0000
│   Código    │ 0x0000             │     SO      │
├─────────────┤                    ├─────────────┤ 0x1000
│   Datos     │ 0x1000  ────────→  │  Proceso A  │
├─────────────┤            MMU    ├─────────────┤ 0x3000
│   Heap      │ 0x2000             │  Proceso B  │
├─────────────┤                    ├─────────────┤ 0x5000
│   Stack     │ 0x3000             │    Libre    │
└─────────────┘                    └─────────────┘
```

**MMU** (Memory Management Unit): Traduce direcciones lógicas a físicas

---

## Traducción de Direcciones

```
┌─────────────┐      ┌──────────────┐      ┌─────────────┐
│   CPU       │      │     MMU      │      │   Memoria   │
│             │      │              │      │   Física    │
│ Dir. Lógica │─────→│  + Base      │─────→│ Dir. Física │
│   0x0500    │      │  (0x4000)    │      │   0x4500    │
└─────────────┘      └──────────────┘      └─────────────┘

Fórmula simple (reubicación):
    Dirección Física = Dirección Lógica + Registro Base
    0x4500 = 0x0500 + 0x4000
```

---

## Asignación Contigua

### Cada proceso ocupa un bloque continuo de memoria

```
           MEMORIA FÍSICA
    ┌─────────────────────┐ 0
    │   Sistema Operativo │
    ├─────────────────────┤ 100KB
    │                     │
    │     Proceso A       │
    │     (200KB)         │
    ├─────────────────────┤ 300KB
    │                     │
    │     Proceso B       │
    │     (150KB)         │
    ├─────────────────────┤ 450KB
    │       LIBRE         │
    │     (550KB)         │
    └─────────────────────┘ 1MB
```

---

## Partición Fija

### Memoria dividida en particiones de tamaño fijo

```
    PARTICIONES FIJAS              ASIGNACIÓN
    ┌─────────────────┐         ┌─────────────────┐
    │ Partición 1     │         │ Proceso A       │
    │ (256 KB)        │         │ (200 KB)        │
    │                 │         │ █████░░░░ 56KB  │ ← Frag. Interna
    ├─────────────────┤         ├─────────────────┤
    │ Partición 2     │         │ Proceso B       │
    │ (256 KB)        │         │ (256 KB)        │
    │                 │         │ █████████       │
    ├─────────────────┤         ├─────────────────┤
    │ Partición 3     │         │    LIBRE        │
    │ (256 KB)        │         │                 │
    │                 │         │                 │
    └─────────────────┘         └─────────────────┘
```

**Problema**: Fragmentación interna (espacio desperdiciado dentro de particiones)

---

## Partición Variable (Dinámica)

### Particiones del tamaño exacto que necesita cada proceso

```
INICIAL:                    DESPUÉS DE LIBERAR B:
┌───────────────┐           ┌───────────────┐
│      SO       │           │      SO       │
├───────────────┤           ├───────────────┤
│   Proceso A   │           │   Proceso A   │
│   (200 KB)    │           │   (200 KB)    │
├───────────────┤           ├───────────────┤
│   Proceso B   │           │    HUECO      │
│   (150 KB)    │           │   (150 KB)    │
├───────────────┤           ├───────────────┤
│   Proceso C   │           │   Proceso C   │
│   (300 KB)    │           │   (300 KB)    │
├───────────────┤           ├───────────────┤
│    LIBRE      │           │    LIBRE      │
└───────────────┘           └───────────────┘
```

**Problema**: Fragmentación externa (huecos entre procesos)

---

## Fragmentación

### Dos tipos de desperdicio de memoria

![Tipos de Fragmentación](../../assets/infografias/clase-06-fragmentacion.png){: style="max-width: 60%; max-height: 400px; display: block; margin: 0 auto;"}

---
| Tipo | Causa | Dónde ocurre |
| ------ | ------- | -------------- |
| **Interna** | Proceso no usa toda su partición | Partición fija |
| **Externa** | Huecos entre procesos | Partición variable |

```
FRAGMENTACIÓN EXTERNA:
┌──────┐
│  A   │
├──────┤
│HUECO │ ← 50KB libre
├──────┤
│  B   │
├──────┤
│HUECO │ ← 30KB libre
├──────┤
│  C   │
├──────┤
│HUECO │ ← 40KB libre
└──────┘

---


*(continuación...)*

Total libre: 120KB
Pero NO podemos cargar un proceso de 100KB
(huecos no son contiguos)
```

---

## Estrategias de Asignación

### ¿Qué hueco elegir para un nuevo proceso?

```
Proceso nuevo: 80KB
Huecos disponibles: 100KB, 200KB, 90KB, 150KB
```

| Estrategia | Descripción | Elige |
| ------------ | ------------- | ------- |
| **First Fit** | Primer hueco suficiente | 100KB |
| **Best Fit** | Hueco más pequeño suficiente | 90KB |
| **Worst Fit** | Hueco más grande | 200KB |

### ¿Cuál es mejor?
- **First Fit**: Rápido, buenos resultados generales
- **Best Fit**: Deja huecos pequeños (inútiles)
- **Worst Fit**: Deja huecos grandes (útiles)

---

## Compactación

### Solución a la fragmentación externa

```
ANTES:                      DESPUÉS (compactación):
┌──────┐                    ┌──────┐
│  A   │                    │  A   │
├──────┤                    ├──────┤
│HUECO │                    │  B   │
├──────┤       ───→         ├──────┤
│  B   │                    │  C   │
├──────┤                    ├──────┤
│HUECO │                    │      │
├──────┤                    │      │
│  C   │                    │ LIBRE│
├──────┤                    │(120KB│
│HUECO │                    │contig│
└──────┘                    └──────┘
```

**Problema**: Costoso (hay que mover procesos en memoria)

---

## Swapping

### Mover procesos entre RAM y disco

```
        MEMORIA RAM                    DISCO (Swap)
    ┌─────────────────┐            ┌─────────────────┐
    │       SO        │            │                 │
    ├─────────────────┤            │                 │
    │    Proceso A    │            │                 │
    ├─────────────────┤  swap out  │  ┌───────────┐  │
    │    Proceso B    │ ─────────→ │  │ Proceso D │  │
    ├─────────────────┤            │  └───────────┘  │
    │    Proceso C    │            │                 │
    ├─────────────────┤  swap in   │  ┌───────────┐  │
    │    [espacio]    │ ←───────── │  │ Proceso E │  │
    └─────────────────┘            │  └───────────┘  │
                                   └─────────────────┘
```

Permite ejecutar más procesos de los que caben en RAM.

---

## Protección de Memoria

### Evitar que un proceso acceda a memoria de otro

```
        REGISTROS DE PROTECCIÓN
    ┌──────────────────────────────────────┐
    │  Base  = 0x4000   Límite = 0x2000    │
    └──────────────────────────────────────┘
                      │
                      ▼
    Dirección lógica: 0x0500
    
    ¿0x0500 < 0x2000?  → SÍ (válida)
    Dirección física = 0x4000 + 0x0500 = 0x4500 ✓

    Dirección lógica: 0x3000
    
    ¿0x3000 < 0x2000?  → NO (inválida)
    → TRAP: Segmentation Fault! ✗
```

---

## Ejemplo Práctico: Ver memoria en Linux

```bash
# Ver uso de memoria del sistema
$ free -h
              total        used        free      shared  buff/cache   available
Mem:           16Gi       5.2Gi       3.8Gi       512Mi       7.0Gi       10Gi
Swap:          2.0Gi       0.0Gi       2.0Gi

# Ver mapa de memoria de un proceso
$ cat /proc/self/maps
00400000-00452000 r-xp  /bin/cat     (código)
00651000-00652000 r--p  /bin/cat     (datos)
00652000-00653000 rw-p  /bin/cat     (datos)
7f8a...          r-xp  /lib/libc.so  (biblioteca)
7ffc...          rw-p  [stack]       (pila)

# Ver estadísticas de memoria
$ vmstat 1
procs -----------memory---------- ---swap--
 r  b   swpd   free   buff  cache   si   so
 1  0      0 3887264 234567 7340928   0    0
```

---

## Actividad Práctica (10 min)

### En parejas, resuelvan:

**Problema de partición dinámica:**

Memoria total: 1000KB (SO ocupa 200KB → 800KB libres)

Llegan procesos en orden:
1. P1: 300KB
2. P2: 200KB  
3. P3: 150KB
4. P2 termina
5. P4: 250KB

**Usando First Fit**, dibujen el estado de la memoria después de cada paso.

¿Puede cargarse P4? ¿Por qué?

---

## Resumen de la Clase

| Concepto | Descripción |
| ---------- | ------------- |
| **Dir. Lógica** | Dirección generada por CPU |
| **Dir. Física** | Dirección real en RAM |
| **MMU** | Traduce direcciones |
| **Frag. Interna** | Espacio desperdiciado dentro de partición |
| **Frag. Externa** | Huecos entre procesos |
| **Swapping** | Mover procesos a/desde disco |

---

## Tarea para próxima clase

### Investigación en parejas

1. Investigar qué es la **paginación** de memoria
2. ¿Cómo resuelve el problema de fragmentación externa?
3. ¿Qué es una **tabla de páginas**?

**Entrega:** Resumen de 1 página
**Sustentación:** Inicio de próxima clase

---

## Próxima Clase

### Clase 7: Paginación y Segmentación

- Paginación: páginas y marcos
- Tabla de páginas
- Segmentación
- Memoria virtual

**¡Nos vemos!**
