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

IMÁGENES GENERADAS:
- so-estados-proceso.png: Diagrama de estados de un proceso
- clase-03-pcb.png: Infografía del Bloque de Control de Proceso
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

    Direcciones altas
         │
         ▼

![Estructura de Memoria de un Proceso](../../assets/infografias/clase-03-estructura-memoria.png)

    Direcciones bajas

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

---

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

![Diagrama de Context Switch](../../assets/infografias/clase-03-cswitch-timeline.png)

**El context switch tiene costo** (overhead)

---

## 4. Estados de un Proceso

### Modelo de 5 estados

![Estados de un Proceso](../../assets/infografias/so-estados-proceso.png)

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

## Modelos de Threads

### Modelo de 1 a 1 (One-to-One)
```
Proceso
├── Thread 1 (user) ────────► Thread 1 (kernel)
├── Thread 2 (user) ────────► Thread 2 (kernel)
└── Thread 3 (user) ────────► Thread 3 (kernel)

✅ Concurrencia real en múltiples núcleos
✅ Si un thread se bloquea, otros continúan
❌ Mayor overhead (cada thread es un proceso ligero)

Ejemplo: Linux (NPTL), Windows
```

### Modelo de Muchos a 1 (Many-to-One)
```
Proceso
├── Thread 1 ──┐
├── Thread 2 ──┼──► Thread único en kernel
└── Thread 3 ──┘

✅ Rápido cambio entre threads (no requiere kernel)
❌ Bloqueo de un thread bloquea todos
❌ No aprovecha múltiples núcleos

Ejemplo: Green threads (Java antiguo)
```

### Modelo de Muchos a Muchos
```
Proceso
├── Thread 1 ──┐
├── Thread 2 ──┼──► Threads kernel (pool)
├── Thread 3 ──┤      (menos que user threads)
└── Thread 4 ──┘

✅ Balance entre concurrencia y eficiencia
✅ Threads en kernel < Threads en usuario

Ejemplo: Solaris, IRIX
```

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

---

## Problemas Clásicos de IPC

### 1. Productor-Consumidor (con pipe)
```
┌──────────┐      Pipe      ┌──────────┐
│ Productor│ ─────────────► │Consumidor│
│ (escribe)│   (buffer)     │ (lee)    │
└──────────┘                └──────────┘

Problema: ¿Qué pasa si el buffer está lleno o vacío?
Solución: Sincronización con semáforos
```

### 2. Problema de los Filósofos Comensales
```
5 filósofos, 5 tenedores (recursos)
Cada filósofo necesita 2 tenedores para comer

Problema: Deadlock si todos toman el tenedor izquierdo
Solución: Orden de adquisición de recursos
```

### 3. Lectores-Escritores
```
Múltiples lectores pueden acceder simultáneamente
Solo un escritor puede acceder (y sin lectores)

Problema: Inanición de escritores si llegan lectores constantemente
Solución: Prioridad a escritores o fairness
```

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
