---
marp: true
theme: default
paginate: true
header: 'IF0099 - Sistemas Operativos I | Unidad 4'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
---

# Clase 5: Sección Crítica y Semáforos
## Sección Crítica, Semáforos y Mutex

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
- clase-05-seccion-critica.png: Diagrama del problema de sección crítica
- clase-05-semaforos.png: Visualización de semáforos y operaciones wait/signal
- clase-05-semaforos-mutex.png: Comparación visual entre semáforos y mutex
-->


**IF0099 - Sistemas Operativos I**
*4° Semestre - Ingeniería Informática*

---

## Objetivos de la Clase

Al finalizar esta clase, el estudiante será capaz de:

1. **Identificar** condiciones de carrera en programas concurrentes
2. **Explicar** el problema de la sección crítica y sus requisitos
3. **Describir** mecanismos de hardware para sincronización (TAS, CAS)
4. **Implementar** soluciones usando semáforos y mutex
5. **Explicar** el concepto de monitores y variables de condición
6. **Resolver** problemas clásicos: productor-consumidor, filósofos
7. **Identificar** y prevenir deadlocks

**Duración:** 90 minutos

---

## El Problema de la Concurrencia

### Cuando dos procesos acceden al mismo recurso

```c
// Proceso A                    // Proceso B
saldo = leer_cuenta();          saldo = leer_cuenta();
saldo = saldo + 100;            saldo = saldo - 50;
escribir_cuenta(saldo);         escribir_cuenta(saldo);
```

**Saldo inicial: $1000**

### ¿Qué puede pasar?
- Esperado: $1000 + $100 - $50 = **$1050**
- Posible: $1100 o $950 (¡ERROR!)

---

## Condición de Carrera (Race Condition)

```
Tiempo    Proceso A              Memoria          Proceso B
──────────────────────────────────────────────────────────────
  t1      lee saldo (1000)      [saldo=1000]
  t2                            [saldo=1000]     lee saldo (1000)
  t3      suma 100 (local=1100)
  t4                                             resta 50 (local=950)
  t5      escribe 1100          [saldo=1100]
  t6                            [saldo=950]      escribe 950
──────────────────────────────────────────────────────────────
                                 RESULTADO: $950 (¡perdimos $100!)
```

### Definición:
**Race condition**: El resultado depende del orden de ejecución (no determinístico)

---

## La Sección Crítica

### Código que accede a recursos compartidos

![Sección Crítica](../../assets/infografias/clase-05-seccion-critica.png)

### Idea clave
- **Sección crítica**: fragmento donde se **lee/modifica** un recurso compartido
- **Riesgo**: si dos procesos entran a la vez, el estado puede quedar inconsistente
- **Solución**: garantizar **exclusión mutua** (solo uno a la vez)

---

### Representación ASCII del problema
```
┌────────────────────────────────────────────────────────┐
│                     PROCESO                            │
├────────────────────────────────────────────────────────┤
│   Código normal (no crítico)                           │
├────────────────────────────────────────────────────────┤
│   ┌──────────────────────────────────────────────┐    │
│   │         SECCIÓN CRÍTICA                      │    │
│   │   - Accede a variable compartida             │    │
│   │   - Modifica recurso común                   │    │
│   │   - Solo UN proceso a la vez                 │    │
│   └──────────────────────────────────────────────┘    │
├────────────────────────────────────────────────────────┤
│   Código normal (no crítico)                           │
└────────────────────────────────────────────────────────┘
```

---

## Requisitos de la Solución

### Una buena solución debe garantizar

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">

<div>

#### ✅ Los 3 requisitos

| Requisito | Descripción |
|-----------|-------------|
| **Exclusión mutua** | Solo un proceso en la sección crítica |
| **Progreso** | Si nadie está en SC, alguien puede entrar |
| **Espera limitada** | Un proceso no debe esperar infinitamente |

#### 📝 Estructura general

```c
while (true) {
    ENTRADA_SECCION_CRITICA();   // Solicitar permiso

    // ... sección crítica ...

    SALIDA_SECCION_CRITICA();    // Liberar permiso

    // ... resto del código ...
}
```

</div>

<div>

#### 🎯 ¿Por qué son necesarios?

**Exclusión Mutua**
```
Sin ella:
Proceso A: saldo = 1000 + 100
Proceso B: saldo = 1000 - 50
Resultado: saldo inconsistente
```

**Progreso**
```
Sin progreso:
Si un proceso fuera de SC impide
que otros entren, nadie avanza.
```

**Espera Limitada**
```
Sin ella:
Un proceso puede esperar
indefinidamente (inanición).
```

#### 💡 Soluciones
- **Hardware**: TAS, CAS (instrucciones atómicas)
- **Software**: Semáforos, Mutex, Monitores
- **Lenguaje**: Java synchronized, C# lock

</div>

</div>

---

## Intento 1: Variable de turno

```c
int turno = 0;  // Variable compartida

// Proceso 0                    // Proceso 1
while (turno != 0);            while (turno != 1);
// sección crítica             // sección crítica
turno = 1;                     turno = 0;
```

### ¿Funciona?
- ✅ Exclusión mutua: Sí
- ❌ Progreso: No (alternancia estricta)

Si P0 no quiere entrar, P1 no puede entrar dos veces seguidas.

---

## Intento 2: Flags (Peterson's Algorithm)

```c
int flag[2] = {false, false};
int turno;

// Proceso i (i = 0 o 1, j = 1-i)
void entrar(int i) {
    int j = 1 - i;
    flag[i] = true;       // Quiero entrar
    turno = j;            // Doy prioridad al otro
    while (flag[j] && turno == j);  // Espero si es necesario
}

void salir(int i) {
    flag[i] = false;      // Ya no quiero estar
}
```

### ¿Funciona?
✅ Cumple los 3 requisitos (para 2 procesos)
❌ Solo funciona para 2 procesos
❌ Requiere busy waiting (espera activa)

---

## 4. Hardware de Sincronización

### Instrucciones Atómicas del Procesador

> El hardware proporciona operaciones atómicas (indivisibles) para sincronización

#### Test-and-Set (TAS)
```c
// Ejecuta atómicamente (no interrumpible)
boolean test_and_set(boolean *target) {
    boolean valor = *target;
    *target = true;
    return valor;
}
```

**Uso para exclusión mutua:**
```c
boolean lock = false;  // Variable compartida

// Entrada a sección crítica
while (test_and_set(&lock));  // Espera activa hasta obtener lock

// ========= SECCIÓN CRÍTICA =========

// Salida de sección crítica
lock = false;
```

---

## Compare-and-Swap (CAS)

### Operación atómica más flexible
```c
// Ejecuta atómicamente
int compare_and_swap(int *valor, int esperado, int nuevo) {
    int temp = *valor;
    if (*valor == esperado)
        *valor = nuevo;
    return temp;
}
```

**Uso para exclusión mutua:**
```c
int lock = 0;  // 0 = libre, 1 = ocupado

// Entrada
while (compare_and_swap(&lock, 0, 1) != 0);
    // Si lock era 0, lo pone en 1 y sale del while
    // Si lock era 1, sigue en el while

// ========= SECCIÓN CRÍTICA =========

// Salida
lock = 0;
```

**Usado en:** Java, C++11 (atomic), Linux kernel

---

## Busy Waiting vs Bloqueo

| Enfoque | Qué hace | Ventaja | Desventaja |
|---------|----------|---------|------------|
| **Espera activa (spin)** | El proceso gira en un while | Muy rápido si la espera es corta | Consume CPU inútilmente |
| **Bloqueo** | El proceso duerme y espera señal | Ahorra CPU | Mayor latencia por despertar |

> **Regla práctica:** spin para secciones muy cortas, bloqueo para esperas largas.

---

## Lista Enlazada Libre de Bloqueos (Lock-Free)

### Usando CAS para estructuras de datos concurrentes
```
┌──────────┐    ┌──────────┐    ┌──────────┐
│  Nodo A  │───►│  Nodo B  │───►│  Nodo C  │───► NULL
└──────────┘    └──────────┘    └──────────┘
```

```c
// Insertar nodo nuevo después de A
// PASO 1: Guardar referencias actuales
nuevo->siguiente = A->siguiente;  // Apunta a B

// PASO 2: Intentar actualizar A->siguiente con CAS
if (CAS(&A->siguiente, B, nuevo) == B) {
    // Éxito: A->siguiente ahora apunta a nuevo
} else {
    // Fallo: otro hilo modificó A->siguiente
    // Reintentar desde PASO 1
}
```

---

## 5. Monitores

### Concepto de Monitor (Hoare, 1974)

> Un **monitor** es una construcción del lenguaje de programación que encapsula:
> - Variables compartidas
> - Procedimientos que operan sobre esas variables
> - Sincronización implícita

```
┌─────────────────────────────────────────┐
│              MONITOR                    │
│  ┌─────────────────────────────────┐    │
│  │  Variables privadas             │    │
│  │  (solo accesibles dentro)       │    │
│  └─────────────────────────────────┘    │
│                                          │
│  ┌─────────────────────────────────┐    │
│  │  Procedimiento op1()            │    │
│  │    ... operaciones ...          │    │
│  └─────────────────────────────────┘    │
│  ┌─────────────────────────────────┐    │
│  │  Procedimiento op2()            │    │
│  │    ... operaciones ...          │    │
│  └─────────────────────────────────┘    │
│                                          │
│  ⚡ Solo UN proceso puede ejecutar       │
│     un procedimiento del monitor         │
│     a la vez (exclusión mutua implícita) │
└─────────────────────────────────────────┘
```

---

## Variables de Condición

### Dentro de un monitor: sincronización condicional

```
monitor BufferLimitado {
    // Variables del monitor
    item buffer[N];
    int count = 0;
    
    // Variables de condición
    condition no_lleno;    // Esperar si buffer lleno
    condition no_vacio;    // Esperar si buffer vacío
    
    procedure insertar(item x) {
        if (count == N)
            no_lleno.wait;     // Duerme si lleno
        buffer[in] = x;
        count++;
        no_vacio.signal;       // Despierta a consumidor
    }
    
    procedure remover() {
        if (count == 0)
            no_vacio.wait;     // Duerme si vacío
        item = buffer[out];
        count--;
        no_lleno.signal;       // Despierta a productor
        return item;
    }
}
```

---

## Monitores en Java

### Cada objeto tiene un monitor implícito
```java
public class CuentaBancaria {
    private double saldo = 0;
    
    // 'synchronized' = monitor
    public synchronized void depositar(double monto) {
        saldo += monto;
    }
    
    public synchronized void retirar(double monto) {
        saldo -= monto;
    }
    
    // Uso de variables de condición
    public synchronized void retirarSeguro(double monto) 
            throws InterruptedException {
        while (saldo < monto) {
            wait();  // Espera en la variable de condición
        }
        saldo -= monto;
    }
    
    public synchronized void depositarNotificar(double monto) {
        saldo += monto;
        notifyAll();  // Despierta a los que esperan
    }
}
```

---

## Semáforos vs Mutex vs Monitores

| Característica | Semáforo | Mutex | Monitor |
|----------------|----------|-------|---------|
| **Nivel** | Sistema operativo | Biblioteca/Lenguaje | Lenguaje (alto nivel) |
| **Valor** | 0, 1, 2, ... | 0 o 1 | Implícito (lock implícito) |
| **Exclusión mutua** | ✅ | ✅ | ✅ (automática) |
| **Sincronización condicional** | ✅ (con semáforos adicionales) | ❌ | ✅ (variables de condición) |
| **Errores comunes** | Olvidar signal/wait | Olvidar unlock | Menos probable |
| **Ejemplos** | `sem_t` (C), `Semaphore` (Java) | `pthread_mutex`, `std::mutex` | Java `synchronized`, C# `lock` |

---

## Semáforos vs Mutex

### Comparación de mecanismos de sincronización

![Semáforos vs Mutex](../../assets/infografias/clase-05-semaforos-mutex.png)

### Diferencias rápidas
- **Mutex**: exclusión mutua estricta (0/1)
- **Semáforo**: contador de recursos (0..N)
- **Uso típico**: mutex para proteger una sección crítica, semáforo para recursos múltiples

---

## Semáforos

### Inventados por Dijkstra (1965)

![Semáforos](../../assets/infografias/clase-05-semaforos.png)

### Qué resuelven
- Controlan **quién entra** a una sección crítica o a un recurso
- Permiten **sincronizar** productor-consumidor, lectores-escritores, etc.

---

Un **semáforo** es una variable entera con dos operaciones atómicas:

```
┌─────────────────────────────────────────────────────────┐
│  wait(S)  o  P(S)  o  down(S)                          │
│  ─────────────────────────────────────────             │
│  if (S > 0)                                            │
│      S = S - 1;                                        │
│  else                                                  │
│      bloquear proceso;                                 │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│  signal(S)  o  V(S)  o  up(S)                          │
│  ─────────────────────────────────────────             │
│  if (hay procesos esperando)                           │
│      despertar uno;                                    │
│  else                                                  │
│      S = S + 1;                                        │
└─────────────────────────────────────────────────────────┘
```

---

## Tipos de Semáforos

### Semáforo Binario (Mutex)
- Valores: 0 o 1
- Usado para exclusión mutua

```c
semaphore mutex = 1;

// Proceso
wait(mutex);
// sección crítica
signal(mutex);
```

### Semáforo Contador
- Valores: 0, 1, 2, 3, ...
- Usado para controlar acceso a N recursos

```c
semaphore recursos = 5;  // 5 recursos disponibles
```

---

## Ejemplo: Exclusión Mutua con Semáforo

```c
#include <semaphore.h>

sem_t mutex;
int saldo = 1000;  // Variable compartida

void depositar(int monto) {
    sem_wait(&mutex);       // Entrada a SC
    saldo = saldo + monto;  // Sección crítica
    sem_post(&mutex);       // Salida de SC
}

void retirar(int monto) {
    sem_wait(&mutex);       // Entrada a SC
    saldo = saldo - monto;  // Sección crítica
    sem_post(&mutex);       // Salida de SC
}

int main() {
    sem_init(&mutex, 0, 1);  // Inicializar en 1
    // ... crear threads que llaman depositar/retirar ...
}
```

---

## Problema del Productor-Consumidor

### Buffer limitado compartido

```
                    BUFFER (tamaño N)
                 ┌───┬───┬───┬───┬───┐
PRODUCTOR ────→  │ X │ X │ X │   │   │ ────→ CONSUMIDOR
                 └───┴───┴───┴───┴───┘
                   0   1   2   3   4

Productor: Genera items y los pone en el buffer
Consumidor: Saca items del buffer y los usa

Problemas:
- Productor no puede poner si buffer lleno
- Consumidor no puede sacar si buffer vacío
- No pueden acceder al buffer simultáneamente
```

---

## Solución con Semáforos

```c
#define N 5  // Tamaño del buffer

sem_t mutex;     // Exclusión mutua para el buffer
sem_t empty;     // Espacios vacíos disponibles
sem_t full;      // Items disponibles

void productor() {
    while (true) {
        item = producir();
        
        sem_wait(&empty);    // Esperar espacio vacío
        sem_wait(&mutex);    // Entrar a SC
        
        buffer[in] = item;   // Poner item
        in = (in + 1) % N;
        
        sem_post(&mutex);    // Salir de SC
        sem_post(&full);     // Avisar que hay item
    }
}
```

---

## Solución: Código del Consumidor

```c
void consumidor() {
    while (true) {
        sem_wait(&full);     // Esperar item disponible
        sem_wait(&mutex);    // Entrar a SC
        
        item = buffer[out];  // Sacar item
        out = (out + 1) % N;
        
        sem_post(&mutex);    // Salir de SC
        sem_post(&empty);    // Avisar que hay espacio
        
        consumir(item);
    }
}

int main() {
    sem_init(&mutex, 0, 1);
    sem_init(&empty, 0, N);  // N espacios vacíos
    sem_init(&full, 0, 0);   // 0 items inicialmente
    // crear threads...
}
```

---

## Mutex en POSIX Threads

### pthread_mutex (más simple que semáforos)

```c
#include <pthread.h>

pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
int contador = 0;

void* incrementar(void* arg) {
    for (int i = 0; i < 1000000; i++) {
        pthread_mutex_lock(&lock);    // Adquirir lock
        contador++;                    // Sección crítica
        pthread_mutex_unlock(&lock);  // Liberar lock
    }
    return NULL;
}

int main() {
    pthread_t t1, t2;
    pthread_create(&t1, NULL, incrementar, NULL);
    pthread_create(&t2, NULL, incrementar, NULL);
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    printf("Contador: %d\n", contador);  // Siempre 2000000
}
```

---

## Deadlock (Interbloqueo)

### Cuando los procesos se bloquean mutuamente

```
Proceso A:                      Proceso B:
wait(sem1);  ← tiene sem1       wait(sem2);  ← tiene sem2
wait(sem2);  ← espera sem2      wait(sem1);  ← espera sem1
...                             ...
```

```
        ┌───────────────────────────────┐
        │                               │
        ▼                               │
   ┌─────────┐   espera    ┌─────────┐ │
   │    A    │ ──────────→ │    B    │ │
   │ (sem1)  │             │ (sem2)  │ │
   └─────────┘ ←────────── └─────────┘ │
                  espera               │
        │                               │
        └───────────────────────────────┘
                 ¡DEADLOCK!
```

---

## Condiciones para Deadlock

### Las 4 condiciones de Coffman (todas necesarias):

1. **Exclusión mutua**: Recursos no compartibles
2. **Retención y espera**: Proceso retiene recursos mientras espera otros
3. **No apropiación**: No se pueden quitar recursos por la fuerza
4. **Espera circular**: A espera a B, B espera a C, C espera a A

### Prevención: Romper al menos una condición

---

## Estrategias frente a Deadlocks

| Estrategia | Idea | Ejemplo |
|------------|------|---------|
| **Prevención** | Evitar que se cumpla alguna condición | Orden fijo de recursos |
| **Evitación** | Analizar si un estado es seguro | Algoritmo del banquero |
| **Detección** | Permitir deadlock y detectarlo | Grafo de espera |
| **Recuperación** | Romper el ciclo | Terminar/rollback procesos |

---

## Actividad Práctica (10 min)

### En parejas:

1. Identifiquen la sección crítica en este código:

```c
void transferir(Cuenta* origen, Cuenta* destino, int monto) {
    origen->saldo -= monto;
    destino->saldo += monto;
}
```

2. Agreguen semáforos/mutex para hacerlo thread-safe

3. ¿Puede haber deadlock si dos procesos hacen transferencias entre las mismas cuentas en direcciones opuestas?

---

## Resumen de la Clase

| Concepto | Descripción |
| ---------- | ------------- |
| **Race condition** | Resultado depende del orden de ejecución |
| **Sección crítica** | Código que accede a recursos compartidos |
| **Hardware sync** | TAS, CAS - instrucciones atómicas del procesador |
| **Monitor** | Construcción del lenguaje con sincronización implícita |
| **Semáforo** | Variable con wait/signal para sincronización |
| **Mutex** | Semáforo binario para exclusión mutua |
| **Deadlock** | Procesos bloqueados esperándose mutuamente |
| **Prevención** | Romper al menos una condición de Coffman |

---

## Evaluación (15% - Eval 2)

### Laboratorio + Sustentación: Semana 7

1. Implementar productor-consumidor en C con pthreads
2. Demostrar que funciona correctamente
3. Explicar cada semáforo y su propósito
4. **Sustentación oral** (5 min por pareja)

**Trabajo en parejas**

---

## Próxima Clase

### Clase 6: Gestión de Memoria

- Conceptos de memoria principal
- Direcciones lógicas vs físicas
- Partición de memoria
- Fragmentación

**¡Nos vemos!**
