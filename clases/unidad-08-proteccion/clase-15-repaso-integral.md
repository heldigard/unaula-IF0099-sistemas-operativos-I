---
marp: true
theme: default
paginate: true
header: 'IF0099 - Sistemas Operativos I | Repaso'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
---

# Clase 15: Repaso Integral
## Conectando Todos los Conceptos del Curso

**Objetivo:** Integrar y sintetizar todo el conocimiento adquirido para el examen final

---

<style>
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
    font-size: 0.75em;
  }
  section th, section td {
    padding: 0.3em 0.4em;
  }
}
</style>

## 🗺️ Mapa Conceptual del Curso

### 8 Unidades Conectadas

```
┌─────────────────────────────────────────────────────────┐
│                  SISTEMA OPERATIVO                      │
├─────────────────────────────────────────────────────────┤
│  ┌────────────┐  ┌────────────┐  ┌────────────┐      │
│  │ Unidad 1-2 │  │ Unidad 3-4 │  │ Unidad 5-6 │      │
│  │ PROCESOS   │→ │PLANIFICACIÓN│→│  MEMORIA   │      │
│  │ & HILOS    │  │& SINCRONIA. │  │& ARCHIVOS  │      │
│  └────────────┘  └────────────┘  └────────────┘      │
│         ↓               ↓               ↓             │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐      │
│  │ Unidad 7   │  │ Unidad 8   │  │ Integración│      │
│  │  E/S       │→ │ PROTECCIÓN │→ │& REPASO    │      │
│  │  & DISCOS  │  │& SEGURIDAD │  │            │      │
│  └────────────┘  └────────────┘  └────────────┘      │
└─────────────────────────────────────────────────────────┘
```

---

## Objetivos y Estructura

### Objetivos de Aprendizaje

1. **Consolidar** conceptos fundamentales del curso
2. **Identificar** temas débiles y fortalezas
3. **Resolver** ejercicios tipo examen
4. **Conectar** conceptos de diferentes unidades
5. **Aplicar** conocimientos teóricos a problemas prácticos

### Agenda

| Sección | Tiempo |
|---------|--------|
| Repaso unidades 1-8 | 35 min |
| Ejercicios integradores | 30 min |
| Quiz y estrategias | 15 min |
| Actividad práctica | 10 min |

---

## 📚 Unidad 1-2: Procesos y Planificación

<div class="columns">
<div>

### Conceptos Clave

- **Proceso:** Programa en ejecución (PCB + código + datos)
- **Estados:** Nuevo → Listo → Ejecución → Espera → Terminado
- **Context Switch:** Guardar/restaurar registros y estado
- **Métricas:**
  - Turnaround = Fin - Llegada
  - Waiting = Turnaround - CPU
  - Throughput = Procesos/tiempo

### Algoritmos de Planificación

| Algoritmo | Tipo | Ventaja |
|-----------|------|---------|
| FCFS | No-apropiativo | Simple |
| SJF | No-apropiativo | Óptimo TT |
| RR | Apropiativo | Equitativo |
| Prioridad | Ambos | Flexible |

</div>
<div>

### Fórmulas Esenciales

```
Turnaround = Fin - Llegada
Waiting = Turnaround - Ráfaga
Response = Primera_exec - Llegada
```

### Estados del Proceso

```
    Nuevo
     ↓
  Listo ⇄ Ejecución
     ↑      ↓
Espera ─────┘
```

</div>
</div>

---

## 🔒 Unidad 3-4: Sincronización

<div class="columns">
<div>

### Sección Crítica - Requisitos

1. **Exclusión mutua:** Solo 1 proceso en SC
2. **Progreso:** Si nadie en SC, alguien puede entrar
3. **Espera limitada:** No inanición

### Mecanismos

```c
// MUTEX
pthread_mutex_lock(&mutex);
// SC
pthread_mutex_unlock(&mutex);

// SEMÁFORO
sem_wait(&sem);    // P()
// SC
sem_post(&sem);    // V()
```

</div>
<div>

### Deadlock - 4 Condiciones Necesarias

1. **Exclusión mutua**
2. **Hold and wait**
3. **No apropiación**
4. **Espera circular**

⚠️ **Romper UNA = Prevenir deadlock**

```
P1: tiene R1, espera R2
     ↓
P2: tiene R2, espera R1
     ↑──────────┘
```

</div>
</div>

---

## 💾 Unidad 5-6: Memoria y Archivos

<div class="columns">
<div>

### Gestión de Memoria

**Jerarquía:**
```
Registro < Cache < RAM < SSD < HDD
Velocidad: ↓        Capacidad: ↓
```

**Paginación:**
- Tamaño fijo (potencia de 2)
- Elimina fragmentación externa
- Crea fragmentación interna

**Traducción:**
```
Página = Dir_Lógica / Tamaño_Página
Offset = Dir_Lógica % Tamaño_Página
Dir_Física = (Marco × Tamaño) + Offset
```

### Sistemas de Archivos

| Sistema | Max Archivo | Journaling |
|---------|------------|------------|
| FAT32 | 4GB | ❌ |
| NTFS | 16EB | ✅ |
| ext4 | 16TB | ✅ |

**Inodo:** Metadatos + punteros (12 directos, 3 indirectos)

</div>
<div>

### Estructura Inodo ext4

```
┌────────────────────────────┐
│ INODO (128 bytes)           │
├────────────────────────────┤
│ Permisos: rwxr-xr-x         │
│ UID/GID                     │
│ Tamaño: 4096 bytes          │
│ Timestamps                  │
├────────────────────────────┤
│ Bloques:                    │
│  - Directos: 12             │
│  - Indirecto simple: 1      │
│  - Indirecto doble: 1       │
│  - Indirecto triple: 1      │
└────────────────────────────┘
```

**Acceso bloque 14:** 3 lecturas (inodo → indirecto → dato)

</div>
</div>

---

## 🖥️ Unidad 7-8: E/S y Protección

<div class="columns">
<div>

### E/S y DMA

**Sin DMA:** CPU copia byte por byte (100% ocupada)

**Con DMA:** CPU inicia transferencia → libre

### Niveles de Protección

| Nivel | Ejemplo |
|-------|---------|
| Físico | Guardias, cerraduras |
| Usuario | Login/password |
| Proceso | Espacios de direcciones |
| Archivo | Permisos rwx |
| Red | Firewall, TLS |

### DMA

```
Sin DMA:    Con DMA:
CPU→RAM×1000  CPU→Iniciar→Libre
             DMA→RAM×1000→Interrumpir
```

</div>
<div>

### Sistemas Distribuidos

**Tipos:**
- **SO de red:** NFS, montaje remoto
- **SO distribuido:** Transparencia total

**Teorema CAP (2 de 3):**
- **C**onsistencia
- **A**vailability
- **P**artition tolerance

**Ejemplo:** Google File System, HDFS

### Permisos Unix

```bash
-rw-r--r-- 1 juan users 1024 archivo
│││ │││ │││
│││ │││ └└└─ Otros: r--
│││ └└└───── Grupo: r--
└└└───────── Dueño: rw-

chmod 755 = rwxr-xr-x
```

</div>
</div>

---

## 🧠 Ejercicio 1: Planificación FCFS

<div class="columns">
<div>

### Enunciado

| Proceso | Llegada | Ráfaga |
|---------|---------|--------|
| P1 | 0 | 8 |
| P2 | 1 | 4 |
| P3 | 2 | 9 |
| P4 | 3 | 5 |

**Calcular Turnaround promedio con FCFS**

### Solución

**Gantt:**
```
| P1 | P1 | P1 | P1 | P2 | P2 | P3 | P3 | P3 | P4 | P4 |
0   2   4   6   8  10  12  15  18  21  24  26
```

| Proc | Fin | TT | Espera |
|------|-----|-------|--------|
| P1 | 8 | 8 | 0 |
| P2 | 12 | 11 | 7 |
| P3 | 21 | 19 | 10 |
| P4 | 26 | 23 | 18 |

**TT promedio = 15.25**

</div>
<div>

### Preguntas para Practicar

**¿Y con SJF no-apropiativo?**

Orden: P1(0), P2(4), P4(5), P3(9)

**¿Y con Round Robin (q=2)?**

Secuencia: P1,P2,P3,P4,P1,P2,P3,P4,P1,P3,P3...

**¿Cuál es mejor?**

RR → Mejor tiempo de espera
SJF → Mejor turnaround
FCFS → Más simple

</div>
</div>

---

## 🧠 Ejercicio 2: Memoria Virtual

<div class="columns">
<div>

### Enunciado

- Tamaño página: **4KB** (4096 bytes)
- Dirección lógica: **0x00012A3F**

**Preguntas:**
1. ¿Bits para offset?
2. ¿Número de página?
3. ¿Desplazamiento?
4. Si página → marco 5, ¿dirección física?

### Solución Paso a Paso

**1. Bits offset:**
```
4KB = 2^12 → 12 bits
```

**2. Dividir dirección:**
```
0x00012A3F = 0001 0010 1010 0011 1111
Página: 0001 0010 = 0x12 = 18
Offset: 1010 0011 1111 = 0xA3F = 2623
```

**3. Dirección física:**
```
Dir_Física = (5 × 4096) + 2623
           = 20480 + 2623
           = 23103
           = 0x5A3F
```

</div>
<div>

### Fórmulas de Traducción

```
# Dividir dirección
Número_página = Dir_Lógica / Tamaño_Página
Offset = Dir_Lógica % Tamaño_Página

# Reconstruir
Dir_Física = (Marco × Tamaño_Página) + Offset
```

### Ejemplo Adicional

Si Dir_lógica = 0x00305B7C:

```
Página = 0x00305B7C / 4096 = 0x305 (773)
Offset = 0x00305B7C % 4096 = 0x7C (124)

Si Marco = 10:
Dir_Física = (10 × 4096) + 124 = 41084 = 0xA0BC
```

**Key insight:** Los bits inferiores (offset) NO cambian en la traducción

</div>
</div>

---

## 🧠 Ejercicio 3: Inodos y Archivos

<div class="columns">
<div>

### Enunciado

Archivo de **15 bloques**, inodo con:
- 12 bloques directos
- 1 indirecto simple (256 punteros)
- 1 indirecto doble

**Preguntas:**
1. ¿Cuántos bloques directos se usan?
2. ¿Cuántos bloques indirectos se necesitan?
3. ¿Lecturas de disco para bloque 14?

### Solución

**Distribución:**
```
Bloques 0-11: Directos (12 bloques)
Bloque 12-14: Indirecto simple (3 bloques)
```

**Respuestas:**
1. **12 directos** usados
2. **3 indirectos** simples
3. **3 lecturas** para bloque 14:
   - Leer inodo (1)
   - Leer bloque indirecto (1)
   - Leer dato (1)

</div>
<div>

### Estructura de Acceso

```
Acceso bloque 5 (directo):
  INODO → Dato (2 lecturas)

Acceso bloque 14 (indirecto):
  INODO → Indirecto → Dato (3 lecturas)

Acceso bloque 1000 (indirecto doble):
  INODO → Indirecto1 → Indirecto2 → Dato
  (4 lecturas)
```

### Máxima Capacidad

```
Directos: 12 bloques
Indirecto simple: 256 bloques
Indirecto doble: 256² = 65,536 bloques
Indirecto triple: 256³ = 16,777,216 bloques

Total: ~16.8M bloques × 4KB ≈ 64 GB
```

</div>
</div>

---

## 📖 Los 10 Mandamientos de SO

1. **Proceso = Programa en ejecución** (código + datos + estado)
2. **Context switch es costoso** (guardar/restaurar registros)
3. **Deadlock necesita 4 condiciones** (romper 1 = prevenir)
4. **Paginación elimina fragmentación externa** (pero crea interna)
5. **Cache L1 es 100× más rápido que RAM**
6. **Inodo ≠ Archivo** (inodo = metadatos, archivo = datos)
7. **DMA libera CPU** durante transferencias I/O
8. **Journaling previene corrupción** tras crash
9. **Syscalls cambian a modo kernel** (overhead)
10. **Multiprogramación ≠ Multiprocesamiento** (tiempo vs espacio)

---

## ⚠️ Errores Comunes en Exámenes

<div class="columns">
<div>

### Top 5 Errores

1. **Confundir paginación con segmentación**
   - Paginación: tamaño **FIJO**
   - Segmentación: tamaño **VARIABLE**

2. **Calcular mal Turnaround Time**
   - ❌ TT = Ráfaga
   - ✅ TT = Fin - Llegada

3. **Olvidar context switch en RR**
   - Cada cambio tiene overhead

4. **No diferenciar inodo de archivo**
   - Inodo: metadatos (permisos, fechas)
   - Archivo: datos reales

5. **Confundir prevención con detección de deadlock**
   - Prevención: eliminar condiciones
   - Detección: grafo de asignación

</div>
<div>

### Consejos de Oro

- **Leer TODO antes de responder**
- **Mostrar trabajo** en cálculos (puntos parciales)
- **Usar unidades** (ms, segundos, etc.)
- **Verificar** respuestas con lógica
- **Administrar tiempo:** 90 min / examen

### Fórmulas para Memorizar

```
TT = Fin - Llegada
Waiting = TT - CPU
Dir_Física = (Marco × PageSize) + Offset
Page_Faults = # de veces que página no está en memoria
```

</div>
</div>

---

## 🧪 Quiz Rápido

### Pregunta 1
**Un proceso en "Espera" puede pasar directamente a "Ejecución"?**
- A) Sí, siempre
- B) No, debe pasar por "Listo" ✅
- C) Depende del scheduler
- D) Solo si tiene prioridad alta

### Pregunta 2
**¿Cuántos punteros tiene un bloque indirecto simple (4KB, punteros 4B)?**
- A) 256
- B) 512
- C) 1024 ✅
- D) 2048

### Pregunta 3
**RR con q=1, 3 procesos (P1=5, P2=3, P3=4). ¿Context switches?**
- A) 10
- B) 11 ✅
- C) 12
- D) 13

---

## 🎓 Estrategias de Estudio

<div class="columns">
<div>

### Técnicas Efectivas

1. **Método Feynman:** Explica en voz alta
2. **Mapas mentales:** Conecta temas
3. **Flashcards:** 50+ preguntas clave
4. **Resolución:** 10+ ejercicios/tema
5. **Grupos:** 3-4 personas, 2 horas

### Distribución 7 Días

```
Día 1-2: Procesos + Planificación (30%)
Día 3-4: Memoria + Archivos (35%)
Día 5-6: E/S + Protección (25%)
Día 7: Repaso general (10%)
```

</div>
<div>

### Recursos Recomendados

**Libros:**
- Silberschatz: Cap 3, 5, 9, 13

**Videos:**
- Neso Academy: OS Playlist
- Gate Smashers: Scheduling

**Práctica:**
- GeeksforGeeks: 100+ ejercicios
- TutorialsPoint: Tests

### Checklist Pre-Examen

**48h antes:**
- [ ] Repasé presentaciones
- [ ] Resolví 5+ ejercicios/tema
- [ ] Creé resumen 2 páginas
- [ ] Identifiqué 3 temas débiles

**24h antes:**
- [ ] Dormí 8 horas
- [ ] Revisé errores comunes
- [ ] Preparé materiales

</div>
</div>

---

## 🎯 Actividad Práctica (15 min)

### Trabajo en Parejas

**Instrucciones:**
1. Formen parejas
2. Resuelvan 1 ejercicio:
   - Deadlock: 4 procesos, 2 recursos
   - Paginación: 64KB RAM, procesos
   - Scheduling: RR multicore
3. Preparen explicación de 2 min

**Discusión:** 3 parejas presentan, clase comenta

---

## 📝 Formato del Examen Final

<div class="columns">
<div>

### Estructura

- **Duración:** 90 minutos
- **10 selección múltiple** (30%)
- **3 ejercicios prácticos** (50%)
- **2 preguntas análisis** (20%)

### Temas con Mayor Peso

1. Planificación CPU (25%)
2. Memoria Virtual (25%)
3. Archivos (20%)
4. Sincronización (15%)
5. E/S y Protección (15%)

### Materiales Permitidos

- ✅ Calculadora básica
- ✅ 1 hoja resumen (2 caras)
- ❌ Celular/Laptop

</div>
<div>

### Preguntas Frecuentes

**P:** ¿Memorizar todas las syscalls?
**R:** No, solo las principales (fork, exec, wait, read, write, open, close)

**P:** ¿Cálculos complejos?
**R:** No, matemáticas básicas (sumas, divisiones, potencias de 2)

**P:** ¿Historia de SO?
**R:** Mínimas, enfoque técnico

**P:** ¿Preguntas de código?
**R:** Sí, pseudocódigo C para sincronización

</div>
</div>

---

## ✅ Cierre y Acción Inmediata

### Resumen de Hoy

✅ Repasamos 8 unidades temáticas
✅ Resolvimos 3 ejercicios integradores
✅ Identificamos errores comunes
✅ Definimos estrategia de estudio

### Acción Inmediata (Hoy)

1. **Crear** resumen personal de 2 páginas
2. **Identificar** 3 temas débiles
3. **Formar** grupo de estudio (3-4 personas)
4. **Programar** sesiones de repaso

---

## 🚀 ¡Están Preparados!

### Recuerda

> "El éxito es la suma de pequeños esfuerzos repetidos día tras día"

**Han visto:**
- 15 clases de contenido
- 8 unidades temáticas
- 50+ conceptos fundamentales
- 100+ ejemplos prácticos

**¡Mucho éxito en su examen final!** 💪

---

## Referencias

### Para Profundizar

- **Silberschatz, A.** (2018). *Operating System Concepts*, 10th Ed.
- **Tanenbaum, A.** (2015). *Modern Operating Systems*, 4th Ed.
- **OSDev.org** - Wiki de desarrollo de SO
- **Linux Kernel** - Código fuente

### Contacto

**Email:** [profesor@unaula.edu.co]
**Horario oficina:** [Horario]
**Plataforma:** [LMS del curso]

**¡Nos vemos en el examen final!** 💪
