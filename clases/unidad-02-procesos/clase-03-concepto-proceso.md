---
marp: true
theme: default
paginate: true
header: 'IF0099 - Sistemas Operativos I | Unidad 2'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
---

# Clase 3: Concepto de Proceso
## Programa vs Proceso, PCB y Estados

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

<!--
[2026-01-31] - Clase enriquecida con infografías
[2026-01-31] - Revisión completa y mejora de contenido

CAMBIOS REALIZADOS:
1. Sección "Estructura de Memoria" - Agregada explicación de crecimiento de stack/heap
2. Sección "Estados de Proceso" - Dividida en 3 diapositivas para mejor claridad
   - Modelo de 5 estados (imagen + transiciones)
   - Diagrama detallado ASCII
   - Ejemplo real con Firefox
3. Sección "PCB" - Agregada sección "Importancia del PCB" y ejemplo real de /proc
4. Sección "Context Switch" - Dividida en 2 diapositivas
   - Explicación del proceso
   - Costo del context switch con causas y ejemplo de vmstat
5. Sección "Threads vs Procesos" - Agregadas 3 diapositivas nuevas
   - Ejemplo visual comparativo
   - Cuándo usar procesos vs threads
   - Ejemplos reales de aplicaciones
6. Sección "Modelos de Threads" - Expandida de 1 a 4 diapositivas
   - Tabla comparativa de modelos
   - Modelo 1:1 con ventajas/desventajas
   - Modelo M:1 con ventajas/desventajas
   - Modelo M:N con ventajas/desventajas
7. Sección "Problemas Clásicos de IPC" - Expandida de 1 a 3 diapositivas
   - Productor-Consumidor con detalles de semáforos
   - Filósofos Comensales con diagrama visual y soluciones
   - Lectores-Escritores con explicación de inanición
8. Sección "Pipes" - Agregada tabla de características
9. Nueva sección "Otros Mecanismos de IPC" con 3 subsecciones
   - Shared Memory con ejemplo de código
   - Signals con tabla de señales comunes
   - Message Queues con ejemplo de código

IMÁGENES GENERADAS:
- so-estados-proceso.png: Diagrama de estados de un proceso
- clase-03-pcb.png: Infografía del Bloque de Control de Proceso
- clase-03-estructura-memoria.png: Diagrama de segmentos de memoria
- clase-03-cswitch-timeline.png: Timeline de context switch
-->

---

**IF0099 - Sistemas Operativos I**
*4° Semestre - Ingeniería Informática*

---

## Objetivos de la Clase

Al finalizar esta clase, el estudiante será capaz de:

1. **Diferenciar** entre programa, proceso y thread
2. **Describir** la estructura del PCB (Process Control Block)
3. **Explicar** los estados de un proceso y sus transiciones
4. **Comparar** los modelos de threads (1:1, M:1, M:N)
5. **Describir** los mecanismos de comunicación entre procesos (IPC)
6. **Reconocer** los problemas clásicos de IPC
7. **Identificar** procesos en un sistema operativo real

**Duración:** 90 minutos

---

## Agenda

1. Programa vs Proceso vs Thread (20 min)
2. Estructura de un proceso en memoria (15 min)
3. Process Control Block - PCB (15 min)
4. Estados de un proceso (20 min)
5. Modelos de threads (15 min)
6. Comunicación entre procesos - IPC (15 min)
7. Actividad práctica (10 min)

---

## 1. Programa vs Proceso

### Definiciones

| Concepto | Descripción |
| ---------- | ------------- |
| **Programa** | Código ejecutable almacenado en disco (estático) |
| **Proceso** | Programa en ejecución (dinámico) |

```
┌─────────────┐          ┌─────────────┐
│   PROGRAMA  │  cargar  │   PROCESO   │
│  (en disco) │ ───────→ │ (en memoria)│
│   .exe      │          │             │
│   estático  │          │  dinámico   │
└─────────────┘          └─────────────┘
```

### Analogía:
- **Programa** = Receta de cocina (instrucciones)
- **Proceso** = Acto de cocinar (ejecución)

---

## Un programa, múltiples procesos

### Ejemplo: Chrome

```
┌───────────────────────────────────────────────┐
│               chrome.exe (programa)            │
│                      │                         │
│         ┌───────────┬┴───────────┐            │
│         ▼           ▼            ▼            │
│   ┌─────────┐ ┌─────────┐ ┌─────────┐        │
│   │Proceso 1│ │Proceso 2│ │Proceso 3│        │
│   │ (Tab 1) │ │ (Tab 2) │ │ (Tab 3) │        │
│   │ PID:1234│ │ PID:1235│ │ PID:1236│        │
│   └─────────┘ └─────────┘ └─────────┘        │
└───────────────────────────────────────────────┘
```

Cada pestaña de Chrome es un **proceso separado** con su propio PID.

---

## 2. Estructura de un Proceso en Memoria

El espacio de direcciones de un proceso se divide en segmentos con propósitos específicos:

### Vista general de la memoria:

    Direcciones altas (Stack)
         │
         ▼

![Estructura de Memoria de un Proceso](../../assets/infografias/clase-03-estructura-memoria.png)

    Direcciones bajas (Text)

**Crecimiento:**
- Stack crece hacia abajo (direcciones decrecientes)
- Heap crece hacia arriba (direcciones crecientes)

---

## Segmentos de Memoria

| Segmento | Contenido | Tamaño |
| ---------- | ----------- | -------- |
| **TEXT** | Código ejecutable | Fijo |
| **DATA** | Variables globales inicializadas | Fijo |
| **BSS** | Variables globales no inicializadas | Fijo |
| **HEAP** | Memoria dinámica (malloc/new) | Variable |
| **STACK** | Variables locales, parámetros, retornos | Variable |

```c
int global = 5;         // DATA
int sin_inicializar;    // BSS

int main() {
    int local = 10;     // STACK
    int *ptr = malloc(100); // HEAP
    return 0;
}
```

---

## 3. Process Control Block (PCB)

### La "ficha" de cada proceso

El SO mantiene un **PCB** por cada proceso. Contiene TODA la información necesaria para gestionar el proceso.

![PCB - Bloque de Control de Proceso](../../assets/infografias/clase-03-pcb.png)

### Importancia del PCB

> 💡 **El PCB es la estructura de datos más importante en la gestión de procesos**
> - Sin PCB, el SO no podría suspender y reanudar procesos
> - El contexto switch es básicamente guardar/cargar PCBs
> - Cada proceso tiene exactamente un PCB

---

## PCB: Estructura Detallada

### Representación ASCII:

```
┌─────────────────────────────────────┐
│        PROCESS CONTROL BLOCK        │
├─────────────────────────────────────┤
│  PID: 1234                          │
│  Estado: RUNNING                    │
│  Contador de programa: 0x00400120   │
│  Registros CPU: [R1=5, R2=100, ...] │
│  Límites de memoria: 0x1000-0x9000  │
│  Lista de archivos abiertos: [...]  │
│  Información de E/S: [...]          │
│  Información de planificación: [...]│
│  Información de contabilidad: [...] │
│  Puntero a PCB del padre            │
│  Puntero a PCBs de hijos            │
└─────────────────────────────────────┘
```

### Ver PCB real en Linux

```bash
# El PCB de un proceso está expuesto en /proc/[PID]/
$ cat /proc/self/status
Name:   cat
State:  R (running)
Pid:    1234
PPid:   5678
Uid:    1000(1000)   1000(1000)   1000(1000)   1000(1000)
VmSize:     12345 kB
VmRSS:        678 kB
...
```

---

## Campos del PCB

| Campo | Descripción |
| ------- | ------------- |
| **PID** | Identificador único del proceso |
| **Estado** | Running, Ready, Blocked, etc. |
| **Program Counter** | Siguiente instrucción a ejecutar |
| **Registros CPU** | Valores actuales de registros |
| **Info de memoria** | Límites, tablas de páginas |
| **Info de E/S** | Archivos abiertos, dispositivos |
| **Info de planificación** | Prioridad, tiempo de CPU usado |
| **Info de contabilidad** | Tiempo de inicio, recursos usados |

---

## Context Switch (Cambio de Contexto)

### Cuando el SO cambia de un proceso a otro

> El **context switch** es el proceso de guardar el estado de un proceso y cargar el estado de otro

### ¿Qué sucede durante un context switch?

```
┌─────────────────────────────────────────────────────────┐
│  1. Proceso A se ejecuta                                │
│     → Guarda sus registros CPU en su PCB               │
│     → Guarda su contador de programa                   │
│     → Actualiza su estado a "LISTO"                     │
│                                                           │
│  2. El SO selecciona Proceso B                           │
│     → Carga los registros CPU del PCB de B              │
│     → Carga el contador de programa de B                │
│     → Cambia estado de B a "EJECUTANDO"                 │
│                                                           │
│  3. Proceso B continúa ejecutando                        │
└─────────────────────────────────────────────────────────┘
```

### Analogía: Cambio de contextos = Cambio de jugador en un partido

```
Jugador A sale           ↓             Jugador B entra
─────────────────        │        ─────────────────
- Se sienta en banco     │        - Se levanta del banco
- Descansa               │        - Entra a la cancha
- Entiende la táctica    → Tiempo de → - Conoce la táctica
                        cambio
                        ↓
                        ¡El árbitro silba!
```

---

## Costo del Context Switch

### Impacto en el rendimiento

| Aspecto | Impacto |
|---------|---------|
| **Tiempo** | 1-10 microsegundos (parece poco, pero acumula) |
| **CPU** | La CPU NO hace trabajo útil durante el cambio |
| **Frecuencia** | Cientos o miles de veces por segundo |

> 💡 **Por qué importa**: Demasiados context switches = bajo rendimiento

### Causas de Context Switch

1. **Timeout**: Proceso agotó su quantum de tiempo
2. **E/S**: Proceso solicita entrada/salida (se bloquea)
3. **Interrupción**: Evento de hardware requiere atención
4. **Prioridad**: Proceso de mayor prioridad debe ejecutarse

### Optimización

```bash
# Ver context switches en Linux
$ vmstat 1
procs -----------memory---------- ---swap-- -----io---- -system-- ----cpu----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa
 1  0      0 524288  81920 786432    0    0    10     5  120  250  5  2 92  1
# ↑ cs = context switches por segundo
```

![Diagrama de Context Switch](../../assets/infografias/clase-03-cswitch-timeline.png)

---

## 4. Estados de un Proceso

### Modelo de 5 estados

> Un proceso **siempre está en uno de estos 5 estados** durante su vida útil

![Estados de un Proceso](../../assets/infografias/so-estados-proceso.png)

### Transiciones principales:
- **Admisión**: Nuevo → Listo
- **Dispatch**: Listo → Ejecutando
- **Preemption/Timeout**: Ejecutando → Listo
- **Solicitud E/S**: Ejecutando → Bloqueado
- **E/S completada**: Bloqueado → Listo

---

## Estados de un Proceso: Diagrama Detallado

### Resumen visual de los estados:

```
       ┌─────────┐
       │  NUEVO  │  Proceso creado, espera admisión
       └────┬────┘
            │ Admisión
            ▼
     ┌───────────┐
     │   LISTO   │  Esperando CPU (en cola)
     └─────┬─────┘
           │ Dispatch (seleccionado)
           ▼
    ┌─────────────┐
    │ EJECUTANDO  │  Usando CPU ahora mismo ← Solo 1 por núcleo
    └──┬──────┬───┘
       │      │
       │      │ Timeout o Preemption
       │      ▼
       │   ┌───────────┐
       │   │   LISTO   │
       │   └───────────┘
       │
       │ Solicita E/S o recurso
       ▼
  ┌───────────┐
  │ BLOQUEADO │  Esperando evento (disco, red, etc.)
  └─────┬─────┘
        │ Evento completado
        ▼
     ┌───────────┐
     │   LISTO   │
     └───────────┘
```

---

## Estados de un Proceso: Ejemplo Real

### Ciclo de vida de Firefox:

```bash
1. NUEVO      → $ firefox &          # fork() crea proceso
2. LISTO       → [en cola de CPU]     # Espera turno
3. EJECUTANDO  → [cargando página]     # Usando CPU
4. BLOQUEADO   → [esperando red]      # Pide datos web
5. LISTO       → [en cola de nuevo]   # Datos llegaron
6. EJECUTANDO  → [renderizando]       # CPU de nuevo
7. TERMINADO   → $ exit               # Usuario cierra
```

> 💡 **Nota**: Un proceso puede pasar de Ejecutando a Listo **múltiples veces** antes de completar su tarea

---

## Estados en Detalle

| Estado | Descripción | Ejemplo |
| -------- | ------------- | --------- |
| **NUEVO** | Proceso recién creado, aún no admitido | fork() acaba de ejecutarse |
| **LISTO** | Esperando CPU para ejecutar | En cola de procesos listos |
| **EJECUTANDO** | Usando la CPU actualmente | Solo 1 por CPU/núcleo |
| **BLOQUEADO** | Esperando un evento (E/S, recurso) | Esperando lectura de disco |
| **TERMINADO** | Proceso ha finalizado, pendiente de limpieza | exit() ejecutado |

---

## Transiciones de Estado

| Transición | Causa |
| ------------ | ------- |
| Nuevo → Listo | SO admite el proceso |
| Listo → Ejecutando | Planificador selecciona el proceso (**dispatch**) |
| Ejecutando → Listo | Timeout, proceso cede CPU (**preemption**) |
| Ejecutando → Bloqueado | Proceso solicita E/S o recurso |
| Bloqueado → Listo | E/S completada, recurso disponible |
| Ejecutando → Terminado | Proceso finaliza (exit) |

---

## Ver procesos en Linux

### Comando `ps`

```bash
$ ps aux
USER    PID  %CPU %MEM    VSZ   RSS TTY  STAT START   TIME COMMAND
root      1   0.0  0.1 169584 13256 ?    Ss   Jan30   0:02 /sbin/init
root      2   0.0  0.0      0     0 ?    S    Jan30   0:00 [kthreadd]
user   1234   2.5  1.2 456789 98765 ?    Sl   10:00   0:30 /usr/bin/code
user   5678   0.5  0.8 234567 65432 ?    Sl   10:15   0:10 /usr/bin/firefox
```

### Significado de STAT:
- **R**: Running (ejecutando)
- **S**: Sleeping (bloqueado, esperando)
- **D**: Uninterruptible sleep (E/S)
- **Z**: Zombie (terminado, esperando padre)
- **T**: Stopped (detenido)

---

## Ver procesos en tiempo real

### Comando `htop` (Linux)

```
┌──────────────────────────────────────────────────────────┐
│  CPU[||||||||||||||||||||           45.2%]    │
│  Mem[||||||||||||||||||||||||       62.5%]    │
│  Swp[                                          0.0%]    │
├──────────────────────────────────────────────────────────┤
│  PID USER      PRI  NI  VIRT   RES   SHR S CPU% MEM%    │
│ 1234 user       20   0  456M   98M   45M S  2.5  1.2    │
│ 5678 user       20   0  234M   65M   30M S  0.5  0.8    │
│    1 root       20   0  169M   13M    8M S  0.0  0.1    │
└──────────────────────────────────────────────────────────┘
```

### Comando equivalente en Windows:
```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10
```

---

## Creación de Procesos en Linux

### System Call: `fork()`

```c
#include <stdio.h>
#include <unistd.h>

int main() {
    pid_t pid = fork();  // Crea proceso hijo
    
    if (pid == 0) {
        // Código del HIJO
        printf("Soy el hijo, mi PID es %d\n", getpid());
    } else {
        // Código del PADRE
        printf("Soy el padre, mi hijo tiene PID %d\n", pid);
    }
    
    return 0;
}
```

---

## Árbol de Procesos

### En Linux, todos los procesos forman un árbol

```
                    init (PID 1)
                         │
         ┌───────────────┼───────────────┐
         │               │               │
      systemd         sshd            cron
         │               │
    ┌────┴────┐      ┌───┴───┐
    │         │      │       │
  gdm      pulseaudio bash   bash
    │                  │
 gnome-shell        vim
```

### Ver el árbol:
```bash
pstree -p
```

---

## 5. Threads (Hilos)

### Proceso vs Thread

| Aspecto | Proceso | Thread (Hilo) |
|---------|---------|---------------|
| **Definición** | Programa en ejecución | Unidad de ejecución dentro de un proceso |
| **Memoria** | Espacio propio | Comparte memoria del proceso |
| **Recursos** | Archivos, sockets, etc. | Stack propio, registros propios |
| **Cambio de contexto** | Costoso | Más rápido |
| **Comunicación** | IPC (pipes, sockets) | Memoria compartida directa |
| **Fallo** | No afecta a otros | Puede afectar todo el proceso |

---

## Proceso vs Thread: Ejemplo Visual

### Múltiples Procesos (Pesados)

```
┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐
│    Proceso A        │  │    Proceso B        │  │    Proceso C        │
├─────────────────────┤  ├─────────────────────┤  ├─────────────────────┤
│ Código (TEXT)       │  │ Código (TEXT)       │  │ Código (TEXT)       │
│ Datos (DATA)        │  │ Datos (DATA)        │  │ Datos (DATA)        │
│ Heap                │  │ Heap                │  │ Heap                │
│ Stack               │  │ Stack               │  │ Stack               │
│ PCB                 │  │ PCB                 │  │ PCB                 │
│ Archivos abiertos   │  │ Archivos abiertos   │  │ Archivos abiertos   │
└─────────────────────┘  └─────────────────────┘  └─────────────────────┘
     Memoria propia           Memoria propia           Memoria propia
         ↑ Costoso ↑              ↑ Costoso ↑              ↑ Costoso ↑
```

### Un Proceso con Múltiples Threads (Ligeros)

```
                    ┌─────────────────────────────────┐
                    │      Proceso (Contenedor)       │
                    ├─────────────────────────────────┤
                    │  Código (TEXT)  ← Compartido    │
                    │  Datos (DATA)   ← Compartido    │
                    │  Heap           ← Compartido    │
                    │  Archivos        ← Compartido    │
                    ├─────────────────────────────────┤
                    │  PCB                             │
                    ├─────────────────────────────────┤
                    │                                 │
        ┌───────────┼───────────┬───────────┐        │
        │           │           │           │        │
    ┌───┴───┐   ┌───┴───┐   ┌───┴───┐   ┌───┴───┐    │
    │Thread 1│   │Thread 2│   │Thread 3│   │Thread 4│   │
    │ Stack  │   │ Stack  │   │ Stack  │   │ Stack  │   │
    │Regs    │   │Regs    │   │Regs    │   │Regs    │   │
    │PC      │   │PC      │   │PC      │   │PC      │   │
    └────────┘   └────────┘   └────────┘   └────────┘   │
        ↑             ↑             ↑             ↑       │
      Comparten memoria y recursos                    │
                    ↓ Más rápido ↓                     │
                    └─────────────────────────────────┘
```

> 💡 **Analogía:**
> - **Proceso** = Casa independiente (paredes, techo, servicios propios)
> - **Thread** = Habitación dentro de la casa (comparten paredes y servicios)

---

## Cuándo usar Procesos vs Threads

### Usar Procesos cuando:
- Necesitas **aislamiento total** (fallos no afectan a otros)
- Requieres **seguridad** entre tareas
- Tareas son **independientes**
- Tienes suficientes recursos

### Usar Threads cuando:
- Tareas **comparten datos** frecuentemente
- Necesitas **bajo overhead** de creación
- Requieres **respuesta rápida**
- Tareas son **parte de la misma aplicación**

### Ejemplos reales:

| Aplicación | Enfoque | Por qué |
|-----------|---------|---------|
| **Chrome** | Múltiples procesos (una pestaña = un proceso) | Aislamiento: si una pestaña crashea, las otras siguen funcionando |
| **VS Code** | Un proceso, múltiples threads | Comparten el mismo documento y estado del editor |
| **Servidor Web** | Proceso master + procesos/threads workers | Master gestiona, workers atienden peticiones |
| **Base de Datos** | Múltiples procesos | Cada conexión es un proceso para seguridad y aislamiento |

---

## Modelos de Threads: Comparación

| Modelo | Threads Usuario | Threads Kernel | ¿Concurrencia Múltiples Núcleos? | ¿Bloqueo Afecta a Todos? |
|--------|----------------|----------------|-----------------------------------|---------------------------|
| **1:1** | 1 → 1 | Igual cantidad | ✅ Sí | ❌ No |
| **M:1** | Muchos → 1 | 1 solo | ❌ No | ✅ Sí |
| **M:N** | Muchos → Muchos | Pool variable | ✅ Sí | ❌ No |

---

## Modelo 1:1 (One-to-One)

```
Proceso
├── Thread 1 (user) ────────► Thread 1 (kernel)
├── Thread 2 (user) ────────► Thread 2 (kernel)
└── Thread 3 (user) ────────► Thread 3 (kernel)
```

**Ventajas:**
- ✅ Concurrencia real en múltiples núcleos
- ✅ Si un thread se bloquea, otros continúan
- ✅ Escalabilidad en sistemas multi-core

**Desventajas:**
- ❌ Mayor overhead (cada thread es un proceso ligero)
- ❌ Costoso crear y destruir threads

**Sistemas que lo usan:** Linux (NPTL), Windows, macOS

---

## Modelo M:1 (Many-to-One)

```
Proceso
├── Thread 1 ──┐
├── Thread 2 ──┼──► Thread único en kernel
└── Thread 3 ──┘
```

**Ventajas:**
- ✅ Rápido cambio entre threads (no requiere kernel)
- ✅ Bajo overhead de gestión
- ✅ Portabilidad (no depende del SO)

**Desventajas:**
- ❌ Bloqueo de un thread bloquea todos
- ❌ No aprovecha múltiples núcleos
- ❌ No puede ejecutar en paralelo

**Sistemas que lo usan:** Green threads (Java antiguo), Ruby (antiguo)

---

## Modelo M:N (Many-to-Many)

```
Proceso
├── Thread 1 ──┐
├── Thread 2 ──┼──► Threads kernel (pool)
├── Thread 3 ──┤      (menos que user threads)
└── Thread 4 ──┘
```

**Ventajas:**
- ✅ Balance entre concurrencia y eficiencia
- ✅ Threads en kernel < Threads en usuario
- ✅ Aprovecha múltiples núcleos
- ✅ Flexible y eficiente

**Desventajas:**
- ❌ Complejo de implementar
- ❌ Requiere scheduler a nivel de usuario

**Sistemas que lo usan:** Solaris, IRIX, GNU Pth

---

## Ejemplo de Threads en C (pthreads)

```c
#include <pthread.h>
#include <stdio.h>

void* funcion_hilo(void* arg) {
    int id = *(int*)arg;
    printf("Hilo %d ejecutándose\n", id);
    return NULL;
}

int main() {
    pthread_t hilo1, hilo2;
    int id1 = 1, id2 = 2;
    
    // Crear threads
    pthread_create(&hilo1, NULL, funcion_hilo, &id1);
    pthread_create(&hilo2, NULL, funcion_hilo, &id2);
    
    // Esperar a que terminen
    pthread_join(hilo1, NULL);
    pthread_join(hilo2, NULL);
    
    return 0;
}
```

**Compilar:** `gcc -o threads threads.c -lpthread`

---

## 6. Comunicación entre Procesos (IPC)

### Mecanismos de IPC

| Mecanismo | Tipo | Uso típico |
|-----------|------|------------|
| **Pipes** | Unidireccional | Comandos encadenados (`ls \| grep`) |
| **Named Pipes (FIFO)** | Unidireccional | Procesos sin relación de parentesco |
| **Sockets** | Bidireccional | Comunicación en red o local |
| **Shared Memory** | Memoria compartida | Datos grandes, alta velocidad |
| **Message Queues** | Cola de mensajes | Mensajes tipificados |
| **Semáforos** | Sincronización | Control de acceso a recursos |
| **Signals** | Asíncrono | Notificaciones de eventos |

---

## Pipes en Linux

### Pipe anónimo (entre padre e hijo)

```c
#include <unistd.h>

int pipe_fd[2];  // pipe_fd[0] = lectura, pipe_fd[1] = escritura
pipe(pipe_fd);

if (fork() == 0) {
    // Hijo: cierra lectura, escribe
    close(pipe_fd[0]);
    write(pipe_fd[1], "Hola", 4);
    close(pipe_fd[1]);
} else {
    // Padre: cierra escritura, lee
    close(pipe_fd[1]);
    read(pipe_fd[0], buffer, 4);
    close(pipe_fd[0]);
}
```

### Comando en shell:

```bash
ls -la | grep "\.txt" | wc -l
```

### Características de los Pipes

| Característica | Descripción |
|---------------|-------------|
| **Unidireccional** | El flujo de datos es en una sola dirección |
| **FIFO** | First In, First Out (el primero en entrar es el primero en salir) |
| **Buffer limitado** | Tamaño fijo (típicamente 64KB en Linux) |
| **Bloqueante** | Si está lleno, el escritor espera; si vacío, el lector espera |
| **Relación** | Comúnmente usado entre procesos padre-hijo |

---

## Otros Mecanismos de IPC

### Shared Memory (Memoria Compartida)

```c
#include <sys/shm.h>

// Crear segmento de memoria compartida
int shmid = shmget(IPC_PRIVATE, 1024, IPC_CREAT | 0666);

// Adjuntar al espacio de direcciones del proceso
char *shared_mem = shmat(shmid, NULL, 0);

// Escribir
strcpy(shared_mem, "Hola desde otro proceso");

// Otro proceso puede leer desde la misma memoria
```

**Ventajas:**
- ✅ Más rápido (no hay copia de datos)
- ✅ Ideal para grandes volúmenes de datos

**Desventajas:**
- ❌ Requiere sincronización explícita (semáforos, mutex)

### Signals (Señales)

```bash
# Enviar señal SIGTERM (terminar) a un proceso
kill -15 1234

# Enviar señal SIGKILL (matar inmediatamente)
kill -9 1234
```

**Señales comunes:**
- **SIGINT (2)**: Interrupción (Ctrl+C)
- **SIGTERM (15)**: Terminación graceful
- **SIGKILL (9)**: Terminación forzada (no se puede ignorar)
- **SIGSTOP (19)**: Pausar proceso
- **SIGCONT (18)**: Continuar proceso pausado

### Message Queues (Colas de Mensajes)

```c
#include <sys/msg.h>

// Crear cola de mensajes
int msqid = msgget(IPC_PRIVATE, IPC_CREAT | 0666);

// Enviar mensaje
msgsnd(msqid, &message, sizeof(message.data), 0);

// Recibir mensaje
msgrcv(msqid, &buffer, sizeof(buffer.data), 0, 0);
```

**Características:**
- Mensajes con **tipos** (prioridad)
- Lectura **selectiva** por tipo
- Persiste aunque el proceso termine

---

## Problemas Clásicos de IPC: Productor-Consumidor

### Problema Productor-Consumidor (Bounded Buffer)

```
┌──────────┐      Pipe      ┌──────────┐
│ Productor│ ─────────────► │Consumidor│
│ (escribe)│   (buffer)     │ (lee)    │
└──────────┘                └──────────┘
```

**El problema:**
- Productor escribe datos en un buffer finito
- Consumidor lee datos del mismo buffer
- ¿Qué pasa si el buffer está **lleno** y el productor quiere escribir?
- ¿Qué pasa si el buffer está **vacío** y el consumidor quiere leer?

**Solución:**
- Sincronización con semáforos:
  - `empty`: cuenta espacios libres en buffer
  - `full`: cuenta elementos disponibles
  - `mutex`: protege acceso exclusivo al buffer

---

## Problemas Clásicos de IPC: Filósofos Comensales

### Problema de los Filósofos Comensales

```
      Tenedor 1
         │
   Filósofo 1 ─── Tenedor 2 ─── Filósofo 2
        │                           │
   Tenedor 5                   Tenedor 3
        │                           │
   Filósofo 5 ─── Tenedor 4 ─── Filósofo 3
```

**El escenario:**
- 5 filósofos sentados en una mesa redonda
- 5 tenedores entre ellos (recursos compartidos)
- Cada filósofo necesita **2 tenedores** para comer
- Solo puede tomar los tenedores a su izquierda y derecha

**El problema: Deadlock**
- Si todos toman el tenedor izquierdo simultáneamente
- Nadie puede tomar el derecho (está ocupado)
- Todos esperan para siempre → **Deadlock**

**Soluciones:**
1. Orden de adquisición de recursos (siempre tomar primero el tenedor con número menor)
2. Límite de filósofos comiendo simultáneamente (máximo 4)
3. Asimetría: un filósofo toma izquierda primero, otro derecha primero

---

## Problemas Clásicos de IPC: Lectores-Escritores

### Problema de Lectores-Escritores

**El escenario:**
- Base de datos compartida por múltiples procesos
- Dos tipos de procesos:
  - **Lectores**: solo leen datos (no modifican)
  - **Escritores**: leen y modifican datos

**Reglas de acceso:**
- ✅ Múltiples lectores pueden acceder **simultáneamente**
- ❌ Solo **un escritor** puede acceder (exclusión mutua)
- ❌ Escritor no puede acceder si hay lectores activos

**El problema: Inanición (Starvation)**

```
Caso: Escritores esperan mientras lectores llegan constantemente

[Escritor esperando] ← [Lector1] [Lector2] [Lector3] ...
                        ↓ nuevos lectores llegan
                        Escritor nunca escribe
```

**Soluciones:**
1. **Prioridad a escritores**: Cuando un escritor espera, no se admiten nuevos lectores
2. **Fairness**: Cola FIFO, primero en llegar es atendido (lector o escritor)
3. **Lectores con prioridad**: Escritores esperan a que todos los lectores actuales terminen

---

## Resumen: Procesos vs Threads

```
PROCESO (Contenedor de recursos)
├─ Memoria (código, datos, heap)
├─ Archivos abiertos
├─ Sockets
├─ Permisos
│
├─ THREAD 1 ─────┐
│   ├─ Stack     │
│   ├─ Registros │
│   └─ PC        │
│                ├──► Ejecución concurrente
├─ THREAD 2 ─────┤    (comparten memoria)
│   ├─ Stack     │
│   ├─ Registros │
│   └─ PC        │
└─ THREAD 3 ─────┘
```

---

## Actividad Práctica (10 min)

### En parejas, ejecuten:

> **Nota para usuarios Windows:** Se recomienda usar **WSL** (Windows Subsystem for Linux) o una Máquina Virtual con Ubuntu.
> Para instalar WSL, abre PowerShell como administrador y ejecuta: `wsl --install`

**Linux (WSL/Ubuntu/VirtualBox):**
```bash
# Ver procesos con estados
ps aux | head -20

# Ver árbol de procesos
pstree -p | head -30

# Información de un proceso específico
cat /proc/self/status
```

**Windows (PowerShell):**
```powershell
# Ver procesos
Get-Process | Select-Object -First 20

# Información detallada
Get-Process -Name explorer | Format-List *
```

---

## Resumen de la Clase

| Concepto | Descripción |
| ---------- | ------------- |
| **Programa** | Código estático en disco |
| **Proceso** | Programa en ejecución (con recursos propios) |
| **Thread** | Unidad de ejecución (comparte memoria del proceso) |
| **PCB** | Estructura con toda la info del proceso |
| **PID** | Identificador único de proceso |
| **Estados** | Nuevo, Listo, Ejecutando, Bloqueado, Terminado |
| **Context Switch** | Cambio de un proceso a otro |
| **IPC** | Mecanismos: pipes, sockets, shared memory |
| **Modelos de threads** | 1:1, M:1, M:N |

---

## Tarea para próxima clase

### Investigación (en parejas)

1. **Investiguen** qué es un "proceso zombie" en Linux
2. **Expliquen** por qué ocurre y cómo se soluciona
3. **Escriban** un programa en C que cree un zombie (código + explicación)

**Entrega:** Documento PDF, máximo 2 páginas
**Sustentación:** Próxima clase, 5 minutos por pareja

---

## Próxima Clase

### Clase 4: Planificación de Procesos

- Algoritmos de planificación
- FCFS, SJF, Prioridad, Round Robin
- Métricas: Turnaround, Waiting Time, Response Time

**¡Nos vemos!**
