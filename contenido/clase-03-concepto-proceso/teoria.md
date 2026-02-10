# Teoría Expandida - Clase 3: Concepto de Proceso

**IF0099 - Sistemas Operativos I**

---

## 1. Programa vs Proceso

### Definiciones

| Concepto | Descripción |
|----------|-------------|
| **Programa** | Código ejecutable almacenado en disco (estático) |
| **Proceso** | Programa en ejecución (dinámico) |

```
┌─────────────┐          ┌─────────────┐
│   PROGRAMA  │  cargar  │   PROCESO   │
│  (en disco) │ ───────→ │ (en memoria)│
│   estático  │          │  dinámico   │
└─────────────┘          └─────────────┘
```

### Analogía culinaria

- **Programa** = Receta de cocina (instrucciones en papel)
- **Proceso** = Acto de cocinar (ejecución de la receta)

> La receta no cambia; la cocina sí.
> El programa es inerte; el proceso está vivo.

### Diferencias clave

| Aspecto | Programa | Proceso |
|---------|----------|---------|
| **Ubicación** | Disco | Memoria RAM |
| **Estado** | Estático | Dinámico |
| **Recursos** | Ninguno | PCB, memoria, archivos |
| **Vida** | Permanente | Temporal |
| **Cantidad** | 1 archivo | N instancias |

---

## 2. Estructura de Memoria de un Proceso

El espacio de direcciones de un proceso se divide en segmentos:

### Los 5 segmentos

| Segmento | Contenido | Tamaño |
|----------|-----------|--------|
| **TEXT** | Código ejecutable | Fijo |
| **DATA** | Variables globales inicializadas | Fijo |
| **BSS** | Variables globales no inicializadas | Fijo |

> **¿Qué significa BSS?** BSS viene de "Block Started by Symbol" (Bloque iniciado por símbolo). Es el segmento donde se almacenan variables globales que no tienen un valor inicial explícito en el código. El SO las inicializa a cero automáticamente al iniciar el programa.

| Segmento | Contenido | Tamaño |
|----------|-----------|--------|
| **HEAP** | Memoria dinámica (malloc/new) | Variable ↑ (crece hacia arriba) |
| **STACK** | Variables locales, parámetros, retornos | Variable ↓ (crece hacia abajo) |

### Dirección de crecimiento

```
Direcciones ALTAS
        ↓
┌─────────────────────────┐
│       STACK             │ ← Crece hacia ABAJO
│      (locales)          │    (direcciones ↓)
├─────────────────────────┤
│         ↑               │
│         │               │
│    Espacio libre        │
│         │               │
│         ↓               │
├─────────────────────────┤
│       HEAP             │ ← Crece hacia ARRIBA
│    (dinámica)           │    (direcciones ↑)
├─────────────────────────┤
│       BSS              │
│    (no inicializadas)   │
├─────────────────────────┤
│      DATA             │
│   (inicializadas)      │
├─────────────────────────┤
│      TEXT             │
│    (código)            │
└─────────────────────────┘
        ↓
Direcciones BAJAS
```

### Stack Overflow

> **¿Qué es Stack Overflow?** El **desbordamiento de pila** ocurre cuando el stack crece más allá de su límite asignado.

**Causas comunes:**
- Recursión infinita (una función que se llama a sí misma sin condición de parada)
- Arrays locales muy grandes
- Demasiadas funciones anidadas

**Error típico:** `Segmentation fault` o `Stack overflow` en C/C++

---

## 3. Process Control Block (PCB)

### La "ficha" de cada proceso

El SO mantiene un **PCB** por cada proceso. Contiene TODA la información necesaria para gestionar el proceso.

### Importancia del PCB

> 💡 **El PCB es la estructura de datos más importante en la gestión de procesos**
> - Sin PCB, el SO no podría suspender y reanudar procesos
> - El context switch es básicamente guardar/cargar PCBs
> - Cada proceso tiene exactamente un PCB

### Campos del PCB

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

## 4. Context Switch (Cambio de Contexto)

### ¿Qué es el context switch?

> El **context switch** es el proceso de guardar el estado de un proceso y cargar el estado de otro. Es como "pausar" un juego para jugar otro.

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

### Costo del Context Switch

| Aspecto | Impacto |
|---------|---------|
| **Tiempo** | 1-10 microsegundos (parece poco, pero acumula) |
| **CPU** | La CPU NO hace trabajo útil durante el cambio |
| **Frecuencia** | Cientos o miles de veces por segundo |

> 💡 **Por qué importa**: Demasiados context switches = bajo rendimiento

### Causas de Context Switch

1. **Timeout (Quantum expirado):** Proceso agotó su tiempo asignado
2. **E/S:** Proceso solicita entrada/salida (se bloquea)
3. **Interrupción:** Evento de hardware requiere atención
4. **Prioridad:** Proceso de mayor prioridad debe ejecutarse

> **¿Qué es un Quantum?** El **quantum** (o "time slice") es la unidad máxima de tiempo que un proceso puede ejecutar continuamente antes de ser obligado a ceder la CPU. Típicamente varía de 10-100ms.

---

## 5. Estados de un Proceso

### Modelo de 5 estados

> Un proceso **siempre está en uno de estos 5 estados** durante su vida útil

| Estado | Descripción | Ejemplo |
|--------|-------------|---------|
| **NUEVO** | Proceso recién creado, aún no admitido | `fork()` acaba de ejecutarse |
| **LISTO** | Esperando CPU para ejecutar | En cola de procesos listos |
| **EJECUTANDO** | Usando la CPU actualmente | Solo 1 por CPU/núcleo |
| **BLOQUEADO** | Esperando un evento (disco, red, etc.) | Esperando lectura de disco |
| **TERMINADO** | Proceso ha finalizado, pendiente de limpieza | `exit()` ejecutado |

### Transiciones principales:

- **Admisión:** Nuevo → Listo
- **Dispatch:** Listo → Ejecutando
- **Preemption/Timeout:** Ejecutando → Listo
- **Solicitud E/S:** Ejecutando → Bloqueado
- **E/S completada:** Bloqueado → Listo

---

## 6. Threads (Hilos)

### Proceso vs Thread

| Aspecto | Proceso | Thread (Hilo) |
|---------|---------|---------------|
| **Definición** | Programa en ejecución | Unidad de ejecución dentro de un proceso |
| **Memoria** | Espacio propio | Comparte memoria del proceso |
| **Recursos** | Archivos, sockets, etc. | Stack propio, registros propios |
| **Cambio de contexto** | Costoso | Más rápido |
| **Comunicación** | IPC (pipes, sockets) | Memoria compartida directa |
| **Fallo** | No afecta a otros | Puede afectar todo el proceso |

> **Analogía:**
> - **Proceso** = Casa independiente (paredes, techo, servicios propios)
> - **Thread** = Habitación dentro de la casa (comparten paredes y servicios)

---

## 7. Comunicación entre Procesos (IPC)

### Mecanismos de IPC

| Mecanismo | Tipo | Uso típico |
|-----------|------|------------|
| **Pipes** | Unidireccional | Comandos encadenados (`ls \| grep`) |
| **Named Pipes (FIFO)** | Unidireccional | Procesos sin relación de parentesco |
| **Sockets** | Bidireccional | Comunicación en red o local |
| **Shared Memory** | Memoria compartida | Datos grandes, alta velocidad |
| **Message Queues** | Cola de mensajes | Mensajes tipificados |
| **Semáforos** | Sincronización | Control de acceso a recursos compartidos |
| **Signals** | Asíncrono | Notificaciones de eventos |

### Problemas Clásicos de IPC

#### Productor-Consumidor (Bounded Buffer)

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

## 8. Modelos de Threads

### Comparación de Modelos

| Modelo | Threads Usuario | Threads Kernel | ¿Concurrencia Múltiples Núcleos? | ¿Bloqueo Afecta a Todos? |
|--------|----------------|----------------|-----------------------------------|---------------------------|
| **1:1** | 1 → 1 | Igual cantidad | ✅ Sí | ❌ No |
| **M:1** | Muchos → 1 | 1 solo | ❌ No | ✅ Sí |
| **M:N** | Muchos → Muchos | Pool variable | ✅ Sí | ❌ No |

### Modelo 1:1 (One-to-One)

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

**Última actualización**: 2026-02-01
