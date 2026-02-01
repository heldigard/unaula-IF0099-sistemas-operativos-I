---
marp: true
theme: default
paginate: true
header: 'IF0099 - Sistemas Operativos I | Unidad 3'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
---

# Clase 4: Algoritmos de Planificación de CPU
## Algoritmos FCFS, SJF, Prioridad y Round Robin

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

---

<!--
[2026-01-31] - Clase enriquecida con infografías

IMÁGENES GENERADAS:
- clase-04-algoritmos-planificacion.png: Comparación visual de FCFS, SJF, Prioridad, Round Robin
- clase-04-round-robin.png: Diagrama circular del algoritmo Round Robin
- clase-04-gantt-algoritmos.png: Diagrama de Gantt comparativo de algoritmos
-->


**IF0099 - Sistemas Operativos I**
*4° Semestre - Ingeniería Informática*

---

## Objetivos de la Clase

Al finalizar esta clase, el estudiante será capaz de:

1. **Explicar** el concepto de planificación de CPU
2. **Calcular** métricas de rendimiento (turnaround, waiting, response)
3. **Comparar** los algoritmos FCFS, SJF, Prioridad y Round Robin
4. **Aplicar** cada algoritmo a problemas prácticos
5. **Describir** algoritmos de tiempo real (RMS, EDF)
6. **Explicar** planificación en multiprocesadores (SMP, afinidad)
7. **Evaluar** algoritmos mediante simulación

**Duración:** 90 minutos

---

## Agenda

1. ¿Qué es la planificación de CPU? (10 min)
2. Métricas de rendimiento (10 min)
3. Algoritmo FCFS (10 min)
4. Algoritmo SJF (10 min)
5. Algoritmo por Prioridad (10 min)
6. Algoritmo Round Robin (10 min)
7. Planificación en tiempo real (10 min)
8. Planificación multiprocesador (10 min)
9. Actividad práctica (10 min)

---

## 1. ¿Qué es la Planificación de CPU?

### El problema en el mundo real

Imagina una ventanilla de banco con una sola persona atendiendo:
- 👥 Múltiples clientes esperando (procesos)
- 💼 Cada uno con diferentes necesidades (tiempo de ejecución)
- ⏰ Algunos tienen urgencia (prioridad)
- 🎯 Queremos atender a todos eficientemente

**¿Cómo decidimos el orden de atención?**

Esto es exactamente lo que hace el scheduler del SO con la CPU.


### El problema

![Algoritmos de Planificación](../../assets/infografias/clase-04-algoritmos-planificacion.png)

---

### Representación ASCII:
```
        Cola de procesos LISTOS
┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐
│ P1  │ │ P2  │ │ P3  │ │ P4  │ ──→ ? ──→ [CPU]
└─────┘ └─────┘ └─────┘ └─────┘
                                     │
                    ¿Quién va primero?
```

### El planificador (scheduler) decide:
- **¿Qué proceso** ejecutar?
- **¿Por cuánto tiempo?**
- **¿Cuándo** cambiar de proceso?

---

## Tipos de Planificación

### Según el momento de decisión

| Tipo | Cuándo actúa | Frecuencia |
| ------ | -------------- | ------------ |
| **Largo plazo** | Admitir procesos nuevos | Minutos/horas |
| **Mediano plazo** | Swap in/out de memoria | Segundos/minutos |
| **Corto plazo** | Elegir proceso para CPU | Milisegundos |

### Nosotros nos enfocamos en **planificación de corto plazo**

---

## Preemptive vs Non-Preemptive

```
┌─────────────────────────────────────────────────────────┐
│                NON-PREEMPTIVE (Cooperativo)             │
│                                                         │
│  Proceso ejecuta hasta que:                             │
│  - Termina                                              │
│  - Se bloquea voluntariamente                           │
│                                                         │
│  El SO NO puede quitarle la CPU                         │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                PREEMPTIVE (Apropiativo)                 │
│                                                         │
│  El SO PUEDE interrumpir un proceso para:               │
│  - Dar turno a otro proceso                             │
│  - Responder a eventos de mayor prioridad               │
│                                                         │
│  Usado en sistemas modernos                             │
└─────────────────────────────────────────────────────────┘
```

---

## Diagrama de Gantt Comparativo

![Diagrama de Gantt - Algoritmos de Planificación](../../assets/infografias/clase-04-gantt-algoritmos.png)

---

## 2. Métricas de Rendimiento

### Datos de entrada

| Proceso | Tiempo de llegada | Tiempo de ráfaga (CPU) |
| --------- | ------------------- | ------------------------ |
| P1 | 0 | 5 |
| P2 | 1 | 3 |
| P3 | 2 | 8 |

### Métricas a calcular

| Métrica | Fórmula |
| --------- | --------- |
| **Turnaround Time** | Tiempo de finalización - Tiempo de llegada |
| **Waiting Time** | Turnaround Time - Tiempo de ráfaga |
| **Response Time** | Primera ejecución - Tiempo de llegada |

---

## 3. FCFS - First Come, First Served

### "El primero que llega, primero se atiende"

**Características:**
- Non-preemptive
- Simple de implementar
- Puede causar el **efecto convoy**

```
Llegada:  P1(0), P2(1), P3(2)
Ráfaga:   P1=5,  P2=3,  P3=8

Tiempo:  0    5    8         16
         │────│────│─────────│
         │ P1 │ P2 │   P3    │
         │────│────│─────────│
```

---

## FCFS - Cálculo de métricas

| Proceso | Llegada | Ráfaga | Inicio | Fin | Turnaround | Waiting |
| --------- | --------- | -------- | -------- | ----- | ------------ | --------- |
| P1 | 0 | 5 | 0 | 5 | 5-0=**5** | 5-5=**0** |
| P2 | 1 | 3 | 5 | 8 | 8-1=**7** | 7-3=**4** |
| P3 | 2 | 8 | 8 | 16 | 16-2=**14** | 14-8=**6** |

### Promedios:
- **Turnaround promedio:** (5+7+14)/3 = **8.67**
- **Waiting promedio:** (0+4+6)/3 = **3.33**

---

## Efecto Convoy en FCFS

### Cuando un proceso largo bloquea a los cortos

```
Procesos: P1(ráfaga=100), P2(ráfaga=1), P3(ráfaga=1)

FCFS:
│──────────────────────────────────────────│─│─│
│                  P1 (100)                │P2│P3│
0                                         100 101 102

P2 espera 100 unidades para ejecutar solo 1
P3 espera 101 unidades para ejecutar solo 1

¡MUY INEFICIENTE!
```

---

## 4. SJF - Shortest Job First

### "El más corto primero"

**Características:**
- Puede ser preemptive (SRTF) o non-preemptive
- **Óptimo** en términos de waiting time promedio
- Problema: ¿Cómo saber el tiempo de ráfaga?

```
Llegada:  P1(0), P2(1), P3(2)
Ráfaga:   P1=5,  P2=3,  P3=8

SJF Non-preemptive:
Tiempo:  0    5    8         16
         │────│────│─────────│
         │ P1 │ P2 │   P3    │  (P1 ya empezó)
         │────│────│─────────│
```

---

## SJF - Ejemplo con llegadas diferentes

```
| Proceso | Llegada | Ráfaga |
| --------- | --------- | -------- |
| P1 | 0 | 7 |
| P2 | 2 | 4 |
| P3 | 4 | 1 |
| P4 | 5 | 4 |

SJF Non-preemptive:
t=0: Solo P1 disponible → ejecuta P1
t=7: P2, P3, P4 disponibles → P3 es más corto
t=8: P2, P4 disponibles → P2 = P4 → P2 (llegó primero)
t=12: Solo P4 → ejecuta P4

Tiempo:  0       7  8    12      16
         │───────│──│────│───────│
         │  P1   │P3│ P2 │  P4   │
```

---

## SRTF - Shortest Remaining Time First

### SJF Preemptive

```
|  | P1(0,7) | P2(2,4) | P3(4,1) | P4(5,4) |  |

t=0: P1 inicia (restante=7)
t=2: P2 llega (restante=4), 4<7 → P2 interrumpe
t=4: P3 llega (restante=1), 1<2 → P3 interrumpe
t=5: P3 termina, P4 llega. P2(2) < P4(4) < P1(5) → P2
t=7: P2 termina. P4(4) < P1(5) → P4
t=11: P4 termina → P1
t=16: P1 termina

Tiempo:  0    2    4 5    7       11      16
         │────│────│─│────│───────│───────│
         │ P1 │ P2 │P3│P2 │  P4   │  P1   │
```

---

## 5. Planificación por Prioridad

### Cada proceso tiene un número de prioridad

**Convención:** Menor número = Mayor prioridad (en este curso)

```
| Proceso | Llegada | Ráfaga | Prioridad |
| --------- | --------- | -------- | ----------- |
| P1 | 0 | 5 | 3 |
| P2 | 0 | 3 | 1 (alta) |
| P3 | 0 | 8 | 2 |

Orden de ejecución: P2 → P3 → P1

Tiempo:  0    3         11      16
         │────│─────────│───────│
         │ P2 │   P3    │  P1   │
```

---

## Problema: Starvation (Inanición)

### Procesos de baja prioridad pueden no ejecutarse nunca

```
Si constantemente llegan procesos de alta prioridad...

P1 (prioridad=5) ───────────────→ NUNCA EJECUTA
                    ↑ ↑ ↑ ↑ ↑
         P_alta P_alta P_alta P_alta P_alta
         (prioridad=1)
```

### Solución: **Aging (Envejecimiento)**

Aumentar gradualmente la prioridad de procesos que esperan mucho tiempo.

---

## 6. Round Robin (RR)

### "Turnos rotativos" - El más usado

![Round Robin](../../assets/infografias/clase-04-round-robin.png)

---

### Características:
- Preemptive
- Cada proceso recibe un **quantum** (tiempo máximo)
- Después del quantum, va al final de la cola
- **Justo**: todos reciben CPU eventualmente

---

## Round Robin - Ejemplo

```
| Proceso | Llegada | Ráfaga | Quantum = 4 |
| --------- | --------- | -------- |  |
| P1 | 0 | 10 |  |
| P2 | 0 | 4 |  |
| P3 | 0 | 5 |  |

Cola inicial: [P1, P2, P3]

t=0-4:   P1 ejecuta 4, restante=6, cola=[P2,P3,P1]
t=4-8:   P2 ejecuta 4, TERMINA,    cola=[P3,P1]
t=8-12:  P3 ejecuta 4, restante=1, cola=[P1,P3]
t=12-16: P1 ejecuta 4, restante=2, cola=[P3,P1]
t=16-17: P3 ejecuta 1, TERMINA,    cola=[P1]
t=17-19: P1 ejecuta 2, TERMINA

Tiempo: 0    4    8    12   16 17   19
        │────│────│────│────│──│────│
        │ P1 │ P2 │ P3 │ P1 │P3│ P1 │
```

---

## Round Robin - Cálculo de métricas

```
| Proceso | Llegada | Ráfaga | Fin | Turnaround | Waiting |
| --------- | --------- | -------- | ----- | ------------ | --------- |
| P1 | 0 | 10 | 19 | 19 | 9 |
| P2 | 0 | 4 | 8 | 8 | 4 |
| P3 | 0 | 5 | 17 | 17 | 12 |

Promedios:
- Turnaround: (19+8+17)/3 = 14.67
- Waiting: (9+4+12)/3 = 8.33
```

---

## ¿Qué quantum elegir?

### Trade-off importante

| Quantum | Efecto |
| --------- | -------- |
| **Muy pequeño** | Muchos context switches → overhead |
| **Muy grande** | Se comporta como FCFS |
| **Típico** | 10-100 ms |

```
Quantum muy pequeño (1ms):
│P1│P2│P3│P1│P2│P3│P1│P2│P3│...
  ↑  ↑  ↑  ↑  ↑  ↑
  Demasiados cambios de contexto

Quantum óptimo:
│────P1────│────P2────│────P3────│────P1────│
  Suficiente trabajo entre cambios
```

---

## Comparación de Algoritmos

### Comparación visual de diagramas de Gantt para todos los algoritmos estudiados

![Diagrama de Gantt - Algoritmos de Planificación](../../assets/infografias/clase-04-gantt-algoritmos.png)

| Algoritmo | Tipo | Starvation | Turnaround | Respuesta |
| ----------- | ------ | ------------ | ------------ | ----------- |
| **FCFS** | Non-preemptive | No | Alto si hay convoy | Variable |
| **SJF** | Ambos | Sí (procesos largos) | Óptimo | Variable |
| **Prioridad** | Ambos | Sí | Variable | Alta prioridad: buena |
| **Round Robin** | Preemptive | No | Medio | Buena para todos |

---

## 7. Planificación en Tiempo Real

### Características de sistemas de tiempo real

> Sistemas donde el **tiempo de respuesta** es crítico

| Tipo | Característica | Ejemplo |
|------|----------------|---------|
| **Hard Real-Time** | Cumplimiento estricto obligatorio | Frenos de automóvil, control de reactores |
| **Soft Real-Time** | Cumplimiento deseable pero no crítico | Streaming de video, juegos |

### Algoritmos de Tiempo Real

#### Rate Monotonic Scheduling (RMS)
- Prioridad basada en el **periodo** del proceso
- Menor periodo = Mayor prioridad
- Óptimo para procesos periódicos

```
Proceso A: Periodo=50ms, Tiempo_ejecución=20ms
Proceso B: Periodo=100ms, Tiempo_ejecución=30ms

Prioridad: A > B (porque 50 < 100)

Diagrama:
0-20ms:  A ejecuta (deadline: 50ms) ✓
20-50ms: B ejecuta (deadline: 100ms) ✓
50-70ms: A ejecuta (2da instancia, deadline: 100ms) ✓
70-100ms: B termina (deadline: 100ms) ✓
```

**Condición de schedulabilidad:**
```
Σ(Ci/Pi) ≤ n * (2^(1/n) - 1)

Donde:
- Ci = Tiempo de ejecución del proceso i
- Pi = Periodo del proceso i
- n = Número de procesos
```

#### Earliest Deadline First (EDF)
- Prioridad dinámica: proceso con **deadline más cercano** primero
- Más flexible que RMS
- Utilización del CPU hasta 100%

```
Proceso A: Deadline=50ms, Tiempo=20ms
Proceso B: Deadline=60ms, Tiempo=25ms

En t=0:
- A deadline=50, B deadline=60 → Ejecuta A (0-20ms)

En t=20:
- A terminó, B deadline=60 → Ejecuta B (20-45ms)

En t=45:
- B terminó antes del deadline ✓
```

---

## 8. Planificación en Multiprocesadores

### Enfoques para múltiples CPUs

#### Multiprocesador Simétrico (SMP)
```
┌─────────────────────────────────────────┐
│              Cola única                 │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐       │
│  │ P1  │ │ P2  │ │ P3  │ │ P4  │       │
│  └─────┘ └─────┘ └─────┘ └─────┘       │
│       ↓         ↓         ↓             │
│    ┌─────┐   ┌─────┐   ┌─────┐         │
│    │CPU 0│   │CPU 1│   │CPU 2│         │
│    └─────┘   └─────┘   └─────┘         │
└─────────────────────────────────────────┘

Ventaja: Balance de carga automático
Desventaja: Contención en la cola
```

#### Colas Privadas por CPU
```
┌─────────────────────────────────────────┐
│  Cola CPU 0   Cola CPU 1   Cola CPU 2   │
│  ┌─────┐      ┌─────┐      ┌─────┐     │
│  │ P1  │      │ P2  │      │ P3  │     │
│  │ P4  │      │ P5  │      │ P6  │     │
│  └─────┘      └─────┘      └─────┘     │
│    ↓            ↓            ↓          │
│  ┌─────┐      ┌─────┐      ┌─────┐     │
│  │CPU 0│      │CPU 1│      │CPU 2│     │
│  └─────┘      └─────┘      └─────┘     │
└─────────────────────────────────────────┘

Ventaja: Menos contención
Desventaja: Desbalance de carga posible
Solución: **Migración de procesos** entre colas
```

#### Afinidad a Procesador
```
Proceso P1 ha estado ejecutando en CPU 0
Su caché L1/L2 contiene datos de P1

Opción A: Migrar P1 a CPU 1
- Pérdida de caché (cache misses)
- Penalidad de rendimiento

Opción B: Mantener P1 en CPU 0
- Aprovecha caché caliente
- Mejor rendimiento

Decisión: Afinidad blanda vs afinidad dura
```

### Algoritmos para Multiprocesadores

#### Partitioned Scheduling
- Cada procesador tiene su propia cola
- Procesos asignados a procesadores específicos
- Simple pero puede causar desbalance

#### Global Scheduling
- Una cola global para todos los procesadores
- Procesos migran entre CPUs
- Mejor balance pero más overhead

#### Gang Scheduling
- Threads de un mismo proceso ejecutan simultáneamente
- Útil para aplicaciones paralelas
- Todos empiezan y terminan juntos

```
Tiempo: 0        1        2        3
CPU 0: [P1.T1] [P2.T1] [P1.T1] [P2.T1]
CPU 1: [P1.T2] [P2.T2] [P1.T2] [P2.T2]
CPU 2: [P1.T3] [P2.T3] [P1.T3] [P2.T3]

P1 y P2 alternan, todos sus threads juntos
```

---

## 9. Evaluación de Algoritmos

### Modelos de Evaluación

| Modelo | Descripción | Uso |
|--------|-------------|-----|
| **Determinístico** | Carga fija conocida | Análisis teórico |
| **Queueing Models** | Modelos matemáticos de colas | Predicción de comportamiento |
| **Simulación** | Simular carga real | Estudio detallado |
| **Implementación real** | Probar en sistema real | Validación final |

### Métricas de Comparación

```
Sistema con:
- 10,000 procesos
- Mix: 80% CPU-bound, 20% I/O-bound
- Distribución de ráfagas: exponencial

Resultados simulación:
┌─────────────────┬──────────┬──────────┬──────────┐
│    Algoritmo    │ Turnaround│  Waiting │ CPU Use  │
├─────────────────┼──────────┼──────────┼──────────┤
│ FCFS            │   45.2   │   23.1   │   89%    │
│ SJF             │   38.7   │   16.6   │   91%    │
│ RR (q=10)       │   42.1   │   20.0   │   90%    │
│ RR (q=100)      │   44.8   │   22.7   │   92%    │
│ Prioridad       │   41.5   │   19.4   │   88%    │
└─────────────────┴──────────┴──────────┴──────────┘
```

---

## Actividad Práctica (10 min)

### En parejas, calculen para Round Robin (Q=3):

| Proceso | Llegada | Ráfaga |
| --------- | --------- | -------- |
| P1 | 0 | 8 |
| P2 | 1 | 4 |
| P3 | 2 | 9 |
| P4 | 3 | 5 |

1. Dibujen el diagrama de Gantt
2. Calculen Turnaround y Waiting para cada proceso
3. Calculen los promedios

**Tiempo: 10 minutos**

---

## Resumen de la Clase

| Algoritmo | Idea principal | Tipo |
| ----------- | ---------------- | ---- |
| **FCFS** | Orden de llegada | Non-preemptive |
| **SJF** | El más corto primero | Ambos |
| **Prioridad** | Según importancia asignada | Ambos |
| **Round Robin** | Turnos con quantum fijo | Preemptive |
| **RMS** | Menor periodo = Mayor prioridad | Tiempo real |
| **EDF** | Deadline más cercano primero | Tiempo real dinámico |

### Fórmulas:
- **Turnaround** = Fin - Llegada
- **Waiting** = Turnaround - Ráfaga
- **Response** = Primera ejecución - Llegada

### Multiprocesadores:
- **SMP**: Cola única o colas privadas
- **Afinidad**: Mantener proceso en mismo CPU para aprovechar caché

---

## Tarea / Evaluación

### Taller en parejas (15% - Eval 1)

1. Resolver 3 ejercicios de planificación (FCFS, SJF, RR)
2. Implementar un simulador simple en Python o C
3. **Sustentación en clase** (5 min por pareja)

**Fecha de entrega:** Semana 4
**Fecha de sustentación:** Semana 4

---

## Próxima Clase

### Clase 5: Sincronización de Procesos

- Sección crítica
- Condiciones de carrera
- Semáforos y Mutex
- Problema del productor-consumidor

**¡Nos vemos!**
