---
marp: true
theme: default
paginate: true
header: 'IF0099 - Sistemas Operativos I | Repaso'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
---

# Clase 15: Repaso Integral

<style>
section {
  font-size: 24px;
}
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

## Objetivos de Aprendizaje

Al finalizar esta clase, el estudiante será capaz de:

1. **Consolidar** todos los conceptos fundamentales del curso mediante mapas conceptuales
2. **Identificar** temas débiles y fortalezas en su comprensión
3. **Resolver** ejercicios integradores tipo examen con confianza
4. **Conectar** conceptos de diferentes unidades (visión holística)
5. **Aplicar** conocimientos teóricos a problemas prácticos reales

**Duración:** 90 minutos

---

## 🗺️ Mapa Conceptual del Curso

### 8 Unidades Temáticas

```
┌─────────────────────────────────────────────────────────┐
│                  SISTEMA OPERATIVO                      │
├─────────────────────────────────────────────────────────┤
│                                                         │
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

## 📚 Unidad 1-2: Introducción y Procesos

### Conceptos Clave

- **Definición SO:** Intermediario entre usuario y hardware
- **Funciones:** Gestión de CPU, memoria, E/S, archivos
- **Proceso:** Programa en ejecución (código + datos + PCB)
- **PCB:** Contiene PID, estado, registros, prioridad
- **Estados:** Nuevo, Listo, Ejecución, Espera, Terminado

### Pregunta de Repaso 1

**¿Cuál es la diferencia fundamental entre proceso e hilo?**

<details>
<summary>💡 Ver respuesta</summary>

- **Proceso:** Unidad de recursos (memoria, archivos, espacio de direcciones)
- **Hilo:** Unidad de ejecución (comparte recursos del proceso)
- **Ventaja hilos:** Menor overhead en cambio de contexto
- **Ejemplo:** Navegador = 1 proceso, cada pestaña = 1 hilo

</details>

---

## 🕐 Unidad 3: Planificación de CPU

### Algoritmos Fundamentales

| Algoritmo | Tipo | Ventaja | Desventaja |
|-----------|------|---------|------------|
| **FCFS** | No apropiativo | Simple | Convoy effect |
| **SJF** | No apropiativo | Óptimo T.Espera | Inanición |
| **RR** | Apropiativo | Equitativo | Overhead |
| **Prioridad** | Ambos | Flexible | Inanición |

### Métricas de Desempeño

- **Tiempo de espera (Waiting Time):** Tiempo en cola de listos
- **Tiempo de retorno (Turnaround Time):** Tiempo total (llegada → salida)
- **Tiempo de respuesta:** Primera respuesta del sistema
- **Utilización CPU:** % tiempo CPU ocupada
- **Throughput:** Procesos completados por unidad de tiempo

---

## 🔒 Unidad 4: Sincronización

### Problema de la Sección Crítica

**Requisitos:**
1. **Exclusión mutua:** Solo 1 proceso en SC
2. **Progreso:** Si nadie en SC, alguien puede entrar
3. **Espera limitada:** No inanición

### Mecanismos

```c
// MUTEX
pthread_mutex_t mutex;
pthread_mutex_lock(&mutex);
// Sección crítica
pthread_mutex_unlock(&mutex);

// SEMÁFORO
sem_t semaforo;
sem_wait(&semaforo);  // P(s) o wait(s)
// Sección crítica
sem_post(&semaforo);  // V(s) o signal(s)
```

### Deadlock: 4 Condiciones Necesarias

1. **Exclusión mutua**
2. **Hold and wait** (retener y esperar)
3. **No apropiación**
4. **Espera circular**

**Romper UNA condición = Prevenir deadlock**

---

## 💾 Unidad 5-6: Gestión de Memoria

### Jerarquía de Memoria

```
Velocidad  Capacidad   Costo      Nivel
↑          ↓           ↓
Registros  < 1KB       $$$$$      CPU
Cache L1   32-64KB     $$$$       Chip
Cache L2   256KB-1MB   $$$        Chip
RAM        4-32GB      $$         Placa
SSD        256GB-2TB   $          Periférico
HDD        1-8TB       ¢          Periférico
```

### Paginación vs Segmentación

| Aspecto | Paginación | Segmentación |
|---------|------------|--------------|
| **División** | Fija (páginas) | Variable (segmentos) |
| **Fragmentación** | Interna | Externa |
| **Protección** | Por página | Por segmento |
| **Compartición** | Difícil | Fácil |
| **Tamaño** | Potencia de 2 | Variable |

### Traducción de Direcciones

**Ejemplo:** Dirección lógica `0x3A2F`, tamaño página = 4KB (0x1000)

```
Dirección lógica: 0x3A2F
├─ Página: 0x3A2F / 0x1000 = 0x3 (página 3)
└─ Offset: 0x3A2F % 0x1000 = 0xA2F (offset 2607)

Tabla de páginas: Página 3 → Marco 7
Dirección física: (7 × 4096) + 2607 = 0x7A2F
```

---

## 📁 Unidad 6-7: Sistemas de Archivos

### Estructura de Inodos (ext4)

```
┌─────────────────────────────────────┐
│ INODO (128 bytes)                   │
├─────────────────────────────────────┤
│ Metadatos:                          │
│  - Permisos: rwxr-xr-x              │
│  - Dueño: UID 1000                  │
│  - Tamaño: 4096 bytes               │
│  - Timestamps: ctime, mtime, atime  │
├─────────────────────────────────────┤
│ Bloques de datos:                   │
│  - Directos (12): Bloques 0-11      │
│  - Indirecto simple: Bloque 12      │
│  - Indirecto doble: Bloque 13       │
│  - Indirecto triple: Bloque 14      │
└─────────────────────────────────────┘
```

### Comparación de Sistemas de Archivos

| Sistema | SO | Max Archivo | Max Volumen | Journaling |
|---------|----|-----------|--------------| ----------|
| FAT32 | Todos | 4GB | 2TB | ❌ |
| NTFS | Windows | 16TB | 256TB | ✅ |
| ext4 | Linux | 16TB | 1EB | ✅ |
| APFS | macOS | 8EB | 8EB | ✅ |

---

## 🖥️ Unidad 7-8: E/S y Protección

### DMA (Direct Memory Access)

**Sin DMA:**
```
CPU → Leer byte → Copiar a RAM → Repetir × 1000
(CPU ocupada 100% del tiempo)
```

**Con DMA:**
```
CPU → Iniciar DMA → Hacer otra tarea
DMA → Transferir 1000 bytes → Interrumpir CPU
(CPU libre durante transferencia)
```

### Niveles de Protección

| Nivel | Descripción | Ejemplo |
|-------|-------------|---------|
| **Físico** | Acceso al edificio | Guardias, cerraduras |
| **Usuario** | Autenticación | Login/password |
| **Proceso** | Memoria aislada | Espacios de direcciones |
| **Archivo** | Permisos rwx | chmod 755 |
| **Red** | Firewall/cifrado | TLS, IPsec |

---

## 🧠 Ejercicio Integrador 1: Planificación

### Enunciado

4 procesos llegan al sistema:

| Proceso | Llegada | Ráfaga CPU | Prioridad |
|---------|---------|------------|-----------|
| P1 | 0 | 8 | 3 |
| P2 | 1 | 4 | 1 |
| P3 | 2 | 9 | 4 |
| P4 | 3 | 5 | 2 |

**Tareas:**
1. Calcular Turnaround promedio con **FCFS**
2. Calcular Turnaround promedio con **SJF** (no apropiativo)
3. Calcular Turnaround promedio con **Round Robin (q=2)**
4. ¿Cuál algoritmo es mejor? ¿Por qué?

---

## 💡 Solución Ejercicio 1: FCFS

### Diagrama de Gantt

```
|  P1  |  P1  |  P1  |  P1  |  P2  |  P2  |  P3  |  P3  |  P3  |  P4  |  P4  |
0      2      4      6      8     10     12     15     18     21     24     26
```

### Cálculos

| Proceso | Llegada | Ráfaga | Inicio | Fin | Turnaround | Espera |
|---------|---------|--------|--------|-----|------------|--------|
| P1 | 0 | 8 | 0 | 8 | 8 | 0 |
| P2 | 1 | 4 | 8 | 12 | 11 | 7 |
| P3 | 2 | 9 | 12 | 21 | 19 | 10 |
| P4 | 3 | 5 | 21 | 26 | 23 | 18 |

**Turnaround promedio:** (8 + 11 + 19 + 23) / 4 = **15.25**
**Espera promedio:** (0 + 7 + 10 + 18) / 4 = **8.75**

---

## 🧠 Ejercicio Integrador 2: Memoria Virtual

### Enunciado

Sistema con:
- Tamaño de página: **4KB** (4096 bytes)
- Dirección lógica: **0x00012A3F**

**Preguntas:**
1. ¿Cuántos bits para el offset?
2. ¿Cuál es el número de página?
3. ¿Cuál es el desplazamiento (offset)?
4. Si la página está en el marco 5, ¿cuál es la dirección física?

---

## 💡 Solución Ejercicio 2

### Paso 1: Bits del offset

```
Tamaño página = 4KB = 4096 bytes = 2^12
Bits offset = 12 bits
```

### Paso 2: Dividir dirección

```
Dirección: 0x00012A3F = 0001 0010 1010 0011 1111 (binario)

Página (bits superiores): 0001 0010 = 0x12 = 18 (decimal)
Offset (12 bits inferiores): 1010 0011 1111 = 0xA3F = 2623 (decimal)
```

### Paso 3: Dirección física

```
Marco físico = 5
Dirección física = (Marco × Tamaño_página) + Offset
                 = (5 × 4096) + 2623
                 = 20480 + 2623
                 = 23103
                 = 0x5A3F
```

**Respuesta:** La dirección física es **0x5A3F**

---

## 🧠 Ejercicio Integrador 3: Sistemas de Archivos

### Enunciado

Un archivo ocupa 15 bloques de datos. El sistema usa inodos con:
- 12 bloques directos
- 1 bloque indirecto simple (apunta a 256 bloques)
- 1 bloque indirecto doble

**Preguntas:**
1. ¿Cuántos bloques directos se usan?
2. ¿Cuántos bloques indirectos se necesitan?
3. ¿Cuántas lecturas de disco para acceder al bloque 14?

---

## 💡 Solución Ejercicio 3

### Distribución de bloques

```
Archivo: 15 bloques totales

Bloques 0-11: Directos (12 bloques) ✅
Bloque 12: Indirecto simple (1 bloque)
Bloque 13: Indirecto simple (1 bloque)
Bloque 14: Indirecto simple (1 bloque)

Total directos usados: 12
Total indirectos usados: 3 (del bloque indirecto simple)
```

### Acceso al bloque 14

```
Lecturas necesarias:
1. Leer INODO (obtener puntero a bloque indirecto simple)
2. Leer BLOQUE INDIRECTO (obtener dirección del bloque 14)
3. Leer BLOQUE DE DATOS 14 (datos reales)

Total: 3 lecturas de disco
```

---

## 🎯 Actividad Práctica en Clase (30 min)

### Parte 1: Trabajo en Parejas (20 min)

**Instrucciones:**
1. Formen parejas
2. Seleccionen 2 ejercicios del banco de abajo
3. Resuelvan paso a paso
4. Preparen explicación de 3 minutos

### Banco de Ejercicios

**Opción A: Deadlock**
```
4 procesos (P1-P4) necesitan 2 recursos (R1, R2)
Estado actual:
- P1 tiene R1, necesita R2
- P2 tiene R2, necesita R1
- P3 espera R1
- P4 espera R2

¿Hay deadlock? ¿Por qué? ¿Cómo resolverlo?
```

**Opción B: Paginación**
```
Sistema con 64KB RAM, páginas de 4KB
Proceso A: 12KB
Proceso B: 20KB
Proceso C: 8KB

¿Cuántos marcos de página se necesitan en total?
¿Hay fragmentación interna? Calcúlala.
```

**Opción C: Scheduling Multicore**
```
CPU con 2 núcleos, 5 procesos:
P1(5), P2(3), P3(6), P4(2), P5(4)

Diseñar scheduling Round Robin (q=2)
Calcular tiempo total de ejecución.
```

---

## 📊 Parte 2: Presentaciones (10 min)

- 3 parejas presentan sus soluciones
- Clase discute alternativas
- Profesor aclara dudas

---

## 📖 Conceptos de Último Momento

### Los 10 Mandamientos de Sistemas Operativos

1. **Un proceso = Programa en ejecución** (código + datos + estado)
2. **Context switch es costoso** (guardar/restaurar registros)
3. **Deadlock necesita 4 condiciones** (romper 1 = prevención)
4. **Paginación elimina fragmentación externa** (pero crea interna)
5. **Cache L1 es 100× más rápido que RAM**
6. **Inodo ≠ Archivo** (inodo = metadatos, archivo = datos)
7. **DMA libera CPU** durante transferencias I/O
8. **Journaling previene corrupción** tras crash
9. **Syscalls cambian a modo kernel** (overhead)
10. **Multiprogramación ≠ Multiprocesamiento** (tiempo vs espacio)

---

## 🧪 Quiz Rápido (5 min)

### Pregunta 1
**Un proceso en estado "Espera" puede pasar directamente a "Ejecución"?**
- A) Sí, siempre
- B) No, debe pasar por "Listo"
- C) Depende del scheduler
- D) Solo si tiene prioridad alta

<details>
<summary>✅ Respuesta</summary>
**B) No, debe pasar por "Listo"**

El flujo es: Espera → Listo → Ejecución
</details>

---

## 🧪 Quiz Rápido (cont.)

### Pregunta 2
**¿Cuántos bloques indirectos simples puede direccionar un inodo si cada bloque es 4KB y cada puntero es 4 bytes?**
- A) 256
- B) 512
- C) 1024
- D) 2048

<details>
<summary>✅ Respuesta</summary>
**C) 1024**

Cálculo: 4096 bytes / 4 bytes = 1024 punteros
</details>

---

### Pregunta 3
**En Round Robin con q=1, 3 procesos (P1=5, P2=3, P3=4). ¿Cuántos context switches?**
- A) 10
- B) 11
- C) 12
- D) 13

<details>
<summary>✅ Respuesta</summary>
**B) 11**

Ejecución: P1→P2→P3→P1→P2→P3→P1→P2→P3→P1→P3→P1
Context switches = cambios = 11
</details>

---

## 🎓 Estrategias de Estudio para el Examen

### Técnicas Efectivas

1. **Método Feynman:** Explica conceptos en voz alta como si enseñaras
2. **Mapas mentales:** Dibuja conexiones entre temas
3. **Flashcards:** 50 tarjetas con preguntas clave
4. **Resolución de ejercicios:** 10+ problemas por tema
5. **Grupos de estudio:** 3-4 personas, 2 horas

### Distribución de Tiempo (Próximos 7 días)

```
┌─────────────────────────────────────────────────┐
│ Día 1-2: Procesos + Planificación (30%)        │
│ Día 3-4: Memoria + Archivos (35%)              │
│ Día 5-6: E/S + Protección + Distribuidos (25%) │
│ Día 7: Repaso general + ejercicios (10%)       │
└─────────────────────────────────────────────────┘
```

---

## 📚 Recursos de Estudio Recomendados

### Libros (capítulos clave)

- **Silberschatz** - Operating System Concepts:
  - Cap 3: Procesos
  - Cap 5: Scheduling
  - Cap 9: Memoria Virtual
  - Cap 13: Sistemas de Archivos

### Videos (YouTube)

- **Neso Academy:** Playlist "Operating Systems"
- **Gate Smashers:** Algoritmos de planificación
- **CodeHelp:** Memoria virtual explicada

### Práctica Online

- **GeeksforGeeks:** 100+ ejercicios resueltos
- **TutorialsPoint:** Tests de autoevaluación
- **StackOverflow:** Dudas específicas

---

## ⚠️ Errores Comunes a Evitar

### Top 5 Errores en Exámenes Pasados

1. **Confundir paginación con segmentación**
   - Paginación: tamaño FIJO
   - Segmentación: tamaño VARIABLE

2. **Calcular mal el Turnaround Time**
   - TT = Tiempo fin - Tiempo llegada (NO solo ráfaga)

3. **Olvidar context switch en Round Robin**
   - RR tiene overhead de cambio de contexto

4. **No diferenciar inodo de archivo**
   - Inodo: metadatos (permisos, fechas)
   - Archivo: datos reales

5. **Confundir prevención con detección de deadlock**
   - Prevención: eliminar condiciones
   - Detección: grafo de asignación

---

## 🎯 Checklist Pre-Examen

### 48 horas antes

- [ ] Repasé todas las presentaciones
- [ ] Resolví 5+ ejercicios de cada tema
- [ ] Creé resumen de 2 páginas
- [ ] Identifiqué 3 temas débiles
- [ ] Practiqué ejercicios cronometrados

### 24 horas antes

- [ ] Revisé mapas conceptuales
- [ ] Dormí 8 horas
- [ ] Repasé errores comunes
- [ ] Preparé materiales permitidos
- [ ] Llegué temprano al salón

---

## 💪 Motivación Final

### Recuerda

> "El éxito es la suma de pequeños esfuerzos repetidos día tras día"

**Has visto:**
- 15 clases de contenido
- 8 unidades temáticas
- 50+ conceptos fundamentales
- 100+ ejemplos prácticos

**¡Estás preparado/a!** 🚀

---

## 📝 Próxima Clase: Examen Final

### Formato del Examen

- **Duración:** 90 minutos
- **Preguntas:**
  - 10 selección múltiple (30%)
  - 3 ejercicios prácticos (50%)
  - 2 preguntas de análisis (20%)

### Temas con Mayor Peso

1. Planificación de CPU (25%)
2. Memoria Virtual (25%)
3. Sistemas de Archivos (20%)
4. Sincronización (15%)
5. E/S y Protección (15%)

### Materiales Permitidos

- ✅ Calculadora básica
- ✅ 1 hoja de resumen (ambos lados)
- ❌ Celular
- ❌ Laptop
- ❌ Notas adicionales

---

## 🙋 Espacio para Dudas Finales

### Preguntas Frecuentes

**P:** ¿Hay que memorizar todas las syscalls?
**R:** No, solo las principales (fork, exec, wait, read, write, open, close)

**P:** ¿Cálculos complejos en el examen?
**R:** No, matemáticas básicas (sumas, divisiones, potencias de 2)

**P:** ¿Preguntas de historia de SO?
**R:** Mínimas, enfoque en conceptos técnicos

---

## ✅ Cierre de Clase

### Resumen de Hoy

✅ Repasamos 8 unidades temáticas
✅ Resolvimos 3 ejercicios integradores
✅ Practicamos en parejas
✅ Identificamos errores comunes
✅ Definimos estrategia de estudio

### Acción Inmediata (Hoy)

1. Crear resumen personal de 2 páginas
2. Identificar 3 temas débiles
3. Formar grupo de estudio (3-4 personas)
4. Programar sesiones de repaso

---

## 🎯 Próxima Clase

### Clase 16: Examen Final

📅 **Fecha:** [Según cronograma]
⏰ **Hora:** [Horario habitual]
📍 **Lugar:** [Salón habitual]

**¡Mucho éxito en su preparación!** 🚀

---

## Referencias y Material Complementario

### Para profundizar

- Silberschatz, A. (2018). *Operating System Concepts*, 10th Ed.
- Tanenbaum, A. (2015). *Modern Operating Systems*, 4th Ed.
- [OSDev.org](https://wiki.osdev.org/) - Wiki de desarrollo de SO
- [Linux Kernel Archives](https://www.kernel.org/) - Código fuente

### Contacto

**Email:** [profesor@unaula.edu.co]
**Horario oficina:** [Horario]
**Plataforma:** [LMS del curso]

**¡Nos vemos en el examen final!** 💪

---

## 📚 Resumen Completo del Curso

### Unidad 1: Introducción y Procesos

#### ¿Qué es un Sistema Operativo?
```
┌─────────────────────────────────────────┐
│           APLICACIONES                   │
├─────────────────────────────────────────┤
│       SISTEMA OPERATIVO                  │
│   • Gestión de procesos                  │
│   • Gestión de memoria                   │
│   • Sistema de archivos                  │
│   • Gestión de E/S                       │
├─────────────────────────────────────────┤
│            HARDWARE                      │
└─────────────────────────────────────────┘
```

**Funciones principales:**
1. **Abstracción:** Oculta complejidad del hardware
2. **Gestión de recursos:** CPU, memoria, disco, E/S
3. **Interfaz:** GUI y CLI para interactuar
4. **Protección:** Aísla procesos entre sí

---

### Proceso vs Programa

| Aspecto | Programa | Proceso |
|---------|----------|---------|
| **Naturaleza** | Estático (archivo) | Dinámico (en ejecución) |
| **Ubicación** | Disco | Memoria RAM |
| **Recursos** | Ninguno | CPU, memoria, archivos |
| **Estado** | No tiene | Nuevo, Listo, Ejecutando, Bloqueado, Terminado |

```
Estados de un proceso:
          ┌─────────┐
          │  NUEVO  │
          └────┬────┘
               │ admitido
               ▼
          ┌─────────┐      dispatch      ┌─────────────┐
          │  LISTO  │ ─────────────────► │ EJECUTANDO  │
          └────┬────┘ ◄───────────────── └──────┬──────┘
               │       interrupción            │
               │                               │ E/S o evento
               │                               ▼
               │                        ┌─────────────┐
               └──────────────────────► │  BLOQUEADO  │
                    E/S completada      └─────────────┘
```

---

### PCB (Process Control Block)

```
┌────────────────────────────────────┐
│          PCB - Proceso 1234        │
├────────────────────────────────────┤
│ PID: 1234                          │
│ Estado: LISTO                      │
│ Program Counter: 0x00401000        │
│ Registros: [R1=5, R2=100, ...]     │
│ Límites memoria: 0x1000 - 0x9000   │
│ Archivos abiertos: [fd0, fd1, ...] │
│ Prioridad: 10                      │
│ Tiempo CPU usado: 523 ms           │
│ Puntero al padre: 1001             │
└────────────────────────────────────┘
```

---

### Unidad 2: Planificación de CPU

#### Algoritmos - Comparación Rápida

| Algoritmo | Tipo | Starvation | Ideal para |
|-----------|------|------------|------------|
| **FCFS** | No-preemptive | No | Simple, batch |
| **SJF** | Ambos | Sí | Mejor turnaround |
| **Prioridad** | Ambos | Sí | Sistemas interactivos |
| **Round Robin** | Preemptive | No | Time-sharing |

#### Fórmulas Clave

```
Turnaround Time = Tiempo_Finalización - Tiempo_Llegada
Waiting Time = Turnaround - Tiempo_Ráfaga (CPU)
Response Time = Primera_Ejecución - Tiempo_Llegada
```

---

### Ejercicio Resuelto: FCFS

**Datos:**
| Proceso | Llegada | Ráfaga |
|---------|---------|--------|
| P1 | 0 | 5 |
| P2 | 1 | 3 |
| P3 | 2 | 8 |

**Diagrama de Gantt:**
```
|  P1  |  P2  |    P3    |
0      5      8          16
```

**Cálculos:**
| Proceso | Fin | Turnaround | Waiting |
|---------|-----|------------|---------|
| P1 | 5 | 5-0=5 | 5-5=0 |
| P2 | 8 | 8-1=7 | 7-3=4 |
| P3 | 16 | 16-2=14 | 14-8=6 |

**Promedios:** TT=8.67, WT=3.33

---

### Ejercicio Resuelto: Round Robin (Q=2)

**Datos:** (mismos)
| Proceso | Llegada | Ráfaga |
|---------|---------|--------|
| P1 | 0 | 5 |
| P2 | 1 | 3 |
| P3 | 2 | 8 |

**Ejecución paso a paso:**
```
t=0-2:  P1 ejecuta (restante=3), cola=[P2,P3,P1]
t=2-4:  P2 ejecuta (restante=1), cola=[P3,P1,P2]
t=4-6:  P3 ejecuta (restante=6), cola=[P1,P2,P3]
t=6-8:  P1 ejecuta (restante=1), cola=[P2,P3,P1]
t=8-9:  P2 termina
t=9-11: P3 ejecuta (restante=4), cola=[P1,P3]
t=11-12: P1 termina
t=12-14: P3 ejecuta (restante=2)
t=14-16: P3 termina
```

---

### Unidad 3: Sincronización

#### Problema de la Sección Crítica

```c
// MAL - Race Condition
void depositar(int monto) {
    saldo = saldo + monto;  // No atómico!
}

// BIEN - Con mutex
pthread_mutex_t lock;

void depositar(int monto) {
    pthread_mutex_lock(&lock);
    saldo = saldo + monto;
    pthread_mutex_unlock(&lock);
}
```

#### Semáforos

```c
sem_t mutex;
sem_init(&mutex, 0, 1);  // Inicializar en 1

// Entrada a sección crítica
sem_wait(&mutex);  // P() - decrementa

// ... sección crítica ...

// Salida
sem_post(&mutex);  // V() - incrementa
```

---

### Condiciones de Deadlock (Coffman)

**Las 4 condiciones necesarias:**
1. **Exclusión mutua:** Recurso no compartible
2. **Retención y espera:** Proceso retiene mientras espera
3. **No apropiación:** No se puede quitar recurso por fuerza
4. **Espera circular:** A→B→C→A

```
Prevención: Romper AL MENOS UNA condición

Ejemplo de espera circular:
    P1 tiene R1, espera R2
          ↓
    P2 tiene R2, espera R1
          ↑───────────────┘
```

---

### Unidad 4: Gestión de Memoria

#### Paginación - Traducción de Direcciones

**Fórmulas:**
```
Número de página = Dirección_Lógica / Tamaño_Página
Offset = Dirección_Lógica % Tamaño_Página
Dirección_Física = (Marco × Tamaño_Página) + Offset
```

**Ejemplo:**
```
Dirección lógica: 8500
Tamaño página: 4096 bytes

Página = 8500 / 4096 = 2
Offset = 8500 % 4096 = 308

Si tabla de páginas dice: Página 2 → Marco 5
Dir. Física = 5 × 4096 + 308 = 20788
```

---

### Algoritmos de Reemplazo de Páginas

**FIFO:** Primera página que entró, primera que sale
**LRU:** Página menos usada recientemente sale
**Óptimo:** Página que se usará más tarde (teórico)

**Ejemplo FIFO (3 marcos):**
```
Secuencia: 1, 2, 3, 4, 1, 2, 5

| Paso | Página | M1 | M2 | M3 | Fault? |
|------|--------|----|----|----| -------|
| 1 | 1 | 1 |   |   | ✓ |
| 2 | 2 | 1 | 2 |   | ✓ |
| 3 | 3 | 1 | 2 | 3 | ✓ |
| 4 | 4 | 4 | 2 | 3 | ✓ (sale 1) |
| 5 | 1 | 4 | 1 | 3 | ✓ (sale 2) |
| 6 | 2 | 4 | 1 | 2 | ✓ (sale 3) |
| 7 | 5 | 5 | 1 | 2 | ✓ (sale 4) |

Total Page Faults: 7
```

---

### Unidad 5: Sistemas de Archivos

#### Estructura de Directorios

```
Linux:                          Windows:
/                               C:\
├── bin/                        ├── Windows\
├── etc/                        ├── Program Files\
├── home/                       ├── Users\
│   └── usuario/                │   └── Usuario\
│       ├── Documents/          │       ├── Documents\
│       └── Downloads/          │       └── Downloads\
└── var/                        └── ...
```

#### Inodos (ext4)

```
┌──────────────────────────────────┐
│ INODO #12345                     │
├──────────────────────────────────┤
│ Permisos: rw-r--r-- (644)        │
│ Propietario: UID 1000            │
│ Tamaño: 15360 bytes              │
│ Timestamps: ctime, mtime, atime  │
│ Punteros a bloques: [100,101,...]│
└──────────────────────────────────┘

Nota: El NOMBRE del archivo está en el directorio,
      no en el inodo.
```

---

### Comparación de Sistemas de Archivos

| Característica | FAT32 | NTFS | ext4 |
|----------------|-------|------|------|
| **Tamaño máx archivo** | 4 GB | 16 EB | 16 TB |
| **Journaling** | ❌ | ✅ | ✅ |
| **Permisos** | ❌ | ACL | Unix |
| **Cifrado** | ❌ | EFS | LUKS |
| **Uso típico** | USB | Windows | Linux |

---

### Unidad 6: Protección y Seguridad

#### Principio de Mínimo Privilegio

```
MAL:                           BIEN:
┌─────────────────┐           ┌─────────────────┐
│ Web Server      │           │ Web Server      │
│ Usuario: root   │           │ Usuario: www    │
│ Acceso: TODO    │           │ Acceso:         │
└─────────────────┘           │ - /var/www (RO) │
                              │ - /var/log (RW) │
Si es hackeado:               │ - Puerto 80     │
¡Control total!               └─────────────────┘
                              Si es hackeado:
                              Daño limitado
```

#### Permisos Unix

```bash
-rw-r--r-- 1 juan users 1024 Jan 31 archivo.txt
 │││ │││ │││
 │││ │││ └└└─ Otros: r-- (solo lectura)
 │││ └└└───── Grupo: r-- (solo lectura)
 └└└───────── Dueño: rw- (lectura y escritura)

chmod 755 archivo  # rwxr-xr-x
chmod 644 archivo  # rw-r--r--
```

---

## 📝 Preguntas de Práctica

### Pregunta 1: Procesos
¿Cuál es la diferencia entre modo usuario y modo kernel?

**Respuesta:**
- **Modo usuario:** Acceso limitado, no puede acceder hardware directo
- **Modo kernel:** Acceso total, ejecuta código privilegiado
- Transición mediante **syscalls** (interrupciones de software)

---

### Pregunta 2: Planificación
Un sistema usa Round Robin con Q=4. Si llegan P1(CPU=10) y P2(CPU=3) en t=0, ¿cuántos context switches hay?

**Respuesta:**
```
t=0-4:   P1 (restante=6)  | Switch 1
t=4-7:   P2 termina       | Switch 2
t=7-11:  P1 (restante=2)  | Switch 3 (aunque no hay otros)
t=11-13: P1 termina

Total: 3 context switches
```

---

### Pregunta 3: Memoria
¿Qué es thrashing y cómo se previene?

**Respuesta:**
- **Thrashing:** El sistema pasa más tiempo en page faults que ejecutando
- **Causa:** Demasiados procesos compiten por pocos marcos
- **Prevención:** 
  - Asegurar working set de cada proceso
  - Reducir grado de multiprogramación
  - Añadir más RAM

---

### Pregunta 4: Archivos
¿Qué ventaja tiene journaling?

**Respuesta:**
- **Journaling:** Registro de transacciones antes de hacerlas
- **Ventaja:** Recuperación rápida tras fallo (no fsck completo)
- **Proceso:**
  1. Escribir en journal
  2. Hacer cambio real
  3. Marcar como completado
- Si falla en 1-2: Se descarta la operación
- Si falla en 3: Se completa al reiniciar

---

## 📋 Checklist de Estudio

- [ ] Entiendo los estados de un proceso y transiciones
- [ ] Puedo calcular métricas con FCFS, SJF, RR
- [ ] Sé qué es una race condition y cómo evitarla
- [ ] Puedo traducir direcciones con paginación
- [ ] Entiendo la diferencia entre FAT32, NTFS, ext4
- [ ] Conozco las syscalls básicas (open, read, write, fork)
- [ ] Puedo explicar el teorema CAP
- [ ] Sé qué son y para qué sirven los semáforos
