---
marp: true
theme: default
paginate: true
header: 'IF0099 - Sistemas Operativos I | Unidad 8'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
---

# Clase 13: Sistemas Distribuidos
## Arquitecturas, Retos y Casos Reales

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

## Objetivos de la Clase

Al finalizar esta clase, el estudiante será capaz de:

1. **Definir** qué es un sistema distribuido y sus características fundamentales
2. **Identificar** ventajas y desafíos de los sistemas distribuidos
3. **Clasificar** los tipos de sistemas distribuidos según su arquitectura
4. **Explicar** el teorema CAP y sus implicaciones prácticas
5. **Reconocer** modelos de comunicación y coordinación distribuida
6. **Analizar** casos reales de sistemas distribuidos modernos

**Duración:** 90 minutos

---

## Agenda

1. Conceptos básicos de sistemas distribuidos (15 min)
2. Características y tipos de sistemas distribuidos (15 min)
3. Retos: sincronización, fallos, consistencia (20 min)
4. Modelos de comunicación (10 min)
5. Casos reales: Kubernetes, Cassandra, GFS, Netflix (25 min)
6. Actividad práctica (5 min)

---

## 1. ¿Qué es un Sistema Distribuido?

### Definición Formal

> Un **sistema distribuido** es un conjunto de computadores independientes que se presentan al usuario como un único sistema coherente.

---

### Ejemplos Cotidianos de Sistemas Distribuidos

**En tu día a día (sin que lo notes):**

| Servicio | ¿Qué hace distribuido? | Nodos involucrados |
|----------|------------------------|-------------------|
| 🌐 **Google** | Búsqueda en milisegundos | Miles de servidores globales |
| 📱 **WhatsApp** | Mensajes sincronizados | Servidores en múltiples regiones |
| 🎮 **Juegos online** | Jugadores conectados | Clientes + servidores de juego |
| 💰 **Bitcoin** | Transacciones verificadas | Miles de nodos blockchain |
| 📧 **Email** | Correo global | Servidores SMTP/IMAP distribuidos |

💡 **La nube (AWS, Azure, Google Cloud) son sistemas distribuidos masivos.**

---

### Características Fundamentales

```
┌─────────────────────────────────────────────────────────────┐
│           CARACTERÍSTICAS DE SISTEMAS DISTRIBUIDOS          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  🔹 CONCURRENCIA           🔹 FALTA DE RELOJ GLOBAL        │
│     Múltiples actividades      No hay "hora exacta" única   │
│     simultáneas en diferentes  Cada nodo tiene su reloj     │
│     nodos                                                     │
│                                                             │
│  🔹 FALLOS PARCIALES       🔹 TRANSPARENCIA                │
│     Un nodo puede fallar       Se ve como un solo sistema   │
│     sin afectar todo           El usuario no ve la          │
│                                complejidad distribuida      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Tipos de Sistemas Distribuidos

### Clasificación por Arquitectura

<div style="display: flex; gap: 15px; font-size: 0.9em;">

<div style="flex: 1;">

### 🖥️ **Cliente-Servidor**
- Servidores centralizados
- Clientes solicitan servicios
- **Ejemplos:** Web, Bases de datos
- **Ventaja:** Simple de gestionar
- **Desventaja:** Punto único de fallo

</div>

<div style="flex: 1;">

### 🔄 **Peer-to-Peer (P2P)**
- Todos los nodos son iguales
- Sin servidor central
- **Ejemplos:** BitTorrent, Blockchain
- **Ventaja:** Escalabilidad
- **Desventaja:** Coordinación compleja

</div>

<div style="flex: 1;">

### ☁️ **Clúster/Grid**
- Nodos dedicados al cómputo
- Alta disponibilidad
- **Ejemplos:** HPC, Kubernetes
- **Ventaja:** Alto rendimiento
- **Desventaja:** Costo de infraestructura

</div>

</div>

---

## 3. Retos de los Sistemas Distribuidos

### El Teorema CAP

> **CAP:** Consistency (Consistencia) - Availability (Disponibilidad) - Partition Tolerance (Tolerancia a particiones)

**Principio fundamental:** En un sistema distribuido, solo puedes garantizar **2 de las 3** propiedades simultáneamente.

```
                    CAP
                   / | \
                  /  |  \
                 /   |   \
           Consistency  Partition
                 \   |   /
                  \  |  /
                   \ | /
                 Availability
```

---

### Elecciones de Diseño CAP

| Sistema | Elige | Significado | Ejemplo |
|---------|-------|-------------|---------|
| **CP** | Consistencia + Particionamiento | Datos consistentes, pero puede no estar disponible | etcd (Kubernetes), HBase |
| **AP** | Disponibilidad + Particionamiento | Siempre responde, pero datos pueden ser inconsistentes | Cassandra, DynamoDB |
| **CA** | Consistencia + Disponibilidad | Solo en sistemas NO distribuidos | Bases de datos tradicionales (MySQL single-node) |

**En la práctica:** Todos los sistemas distribuidos deben soportar particiones (redes fallan), así que la elección real es entre **CP** o **AP**.

---

### Otros Retos Importantes

<div style="display: flex; gap: 15px; font-size: 0.85em;">

<div style="flex: 1;">

#### ⚠️ **Fallos Parciales**
- Un nodo falla, otros continúan
- Difícil de detectar (¿lento o caído?)
- Requiere mecanismos de heartbeat

#### 🔒 **Consenso Distribuido**
- ¿Cómo ponernos de acuerdo?
- Algoritmos: Raft, Paxos
- Elección de líder

</div>

<div style="flex: 1;">

#### 🕐 **Sincronización**
- No hay reloj global exacto
- Eventos pueden llegar desordenados
- Relojes lógicos (Lamport timestamps)

#### 📊 **Consistencia de Datos**
- Réplicas pueden divergir
- Modelos: eventual, fuerte, causal
- Compromiso consistencia vs rendimiento

</div>

</div>

---

## 4. Modelos de Comunicación

### Mecanismos de Comunicación entre Nodos

| Modelo | Descripción | Caso de Uso | Ejemplo Tecnología |
|--------|-------------|-------------|-------------------|
| **RPC** | Llamada a función remota como si fuera local | Servicios internos | gRPC, Thrift |
| **Mensajería** | Colas de mensajes asíncronas | Procesamiento por lotes | Kafka, RabbitMQ |
| **REST** | HTTP + JSON/XML | APIs públicas | API REST |
| **Streaming** | Flujo continuo de datos | Tiempo real | WebSocket, Flink |

---

### Comparación: Síncrono vs Asíncrono

<div style="display: flex; gap: 20px;">

<div style="flex: 1;">

#### 🔄 **Síncrono (RPC)**
```
Cliente ──request──► Servidor
   │◄────response────┘
   │
   ▼
Espera bloqueada
```
- **Ventaja:** Simple de razonar
- **Desventaja:** Acoplamiento temporal

</div>

<div style="flex: 1;">

#### 📨 **Asíncrono (Mensajes)**
```
Productor ──msg──► Cola ──msg──► Consumidor
     │                            │
     └────► Continúa              └──► Procesa cuando puede
```
- **Ventaja:** Desacoplamiento, resiliencia
- **Desventaja:** Complejidad de manejo

</div>

</div>

---

## 5. Casos Reales de Sistemas Distribuidos

### 5.1 Kubernetes - Orquestación de Contenedores

**¿Qué es?**
Sistema distribuido para gestionar contenedores Docker en múltiples máquinas.

```
┌─────────────────────────────────────────┐
│          KUBERNETES CLUSTER             │
├─────────────────────────────────────────┤
│                                         │
│  ┌──────────────┐    ┌──────────────┐  │
│  │   Master     │◄──►│    etcd      │  │
│  │   (Control   │    │  (Registro   │  │
│  │    Plane)    │    │ Distribuido) │  │
│  └──────┬───────┘    └──────────────┘  │
│         │                               │
│    ┌────┴────┬────────┬────────┐       │
│    │         │        │        │       │
│  ┌─▼──┐   ┌─▼──┐  ┌─▼──┐  ┌─▼──┐     │
│  │Node│   │Node│  │Node│  │Node│     │
│  │  1 │   │  2 │  │  3 │  │  4 │     │
│  └────┘   └────┘  └────┘  └────┘     │
│                                         │
└─────────────────────────────────────────┘
```

---

### Componentes de Kubernetes

<div style="display: flex; gap: 15px; font-size: 0.85em;">

<div style="flex: 1;">

#### **Master Node (Control Plane)**
- **API Server:** Punto de entrada para todas las operaciones
- **Scheduler:** Decide en qué nodo ejecutar cada pod
- **Controller Manager:** Mantiene el estado deseado
- **etcd:** Base de datos distribuida de configuración

</div>

<div style="flex: 1;">

#### **Worker Nodes**
- **Kubelet:** Agente que ejecuta containers en cada nodo
- **Kube-proxy:** Maneja networking y balanceo
- **Container Runtime:** Docker, containerd

</div>

</div>

**Características Distribuidas:**
- ✅ **Replicación:** Copia automática de pods en múltiples nodos
- ✅ **Auto-recuperación:** Si un nodo falla, mueve pods a otro
- ✅ **Escalado horizontal:** Añade/quita nodos dinámicamente

---

### 5.2 Apache Cassandra - Base de Datos Distribuida

**Arquitectura sin Maestro (Masterless):**

```
         Nodo A
         /    \
       /        \
    Nodo B ─── Nodo C
       \        /
        \      /
         Nodo D
```

**Características:**
- **Sin single point of failure:** Todos los nodos son iguales
- **Replicación configurable:** Datos en N nodos (ej: N=3)
- **Consistencia eventual:** Escribe en algunos, lee de algunos
- **Particionamiento:** Hash ring divide datos entre nodos

---

### Cassandra: Ejemplo de Escritura

```python
# Cliente escribe "usuario123" con RF=3 (Replication Factor)
cassandra.insert("usuarios", "usuario123", datos)

# Cassandra automáticamente:
# 1. Calcula hash(usuario123) = 0x8A3F...
# 2. Ubica en el anillo: Nodo B es responsable
# 3. Replica en Nodos C y D (siguientes en el anillo)
# 4. Escritura exitosa si 2 de 3 nodos confirman (Quorum)
```

**Elección CAP:** Cassandra elige **AP** (Disponibilidad + Particionamiento)
→ Eventual consistency para máxima disponibilidad

---

### 5.3 Google File System (GFS) / HDFS

**Problema que resuelve:**
Almacenar archivos de **petabytes** en miles de máquinas comunes.

```
┌────────────────────────────────────────┐
│           GFS MASTER                   │
│  • Almacena metadata (nombres, etc)   │
│  • Coordina operaciones                │
└────────┬───────────────────────────────┘
         │
    ┌────┴────┬────────┬────────┐
    │         │        │        │
┌───▼───┐ ┌──▼───┐ ┌──▼───┐ ┌──▼───┐
│Chunk  │ │Chunk │ │Chunk │ │Chunk │
│Server │ │Server│ │Server│ │Server│
│   1   │ │  2   │ │  3   │ │  4   │
└───────┘ └──────┘ └──────┘ └──────┘
  Datos    Datos    Datos    Datos
```

---

### GFS/HDFS: Detalles Técnicos

**Componentes:**

| Componente | Función | En HDFS |
|------------|---------|---------|
| **Master** | Metadatos, coordina operaciones | NameNode |
| **Chunk Servers** | Almacenan datos reales | DataNodes |

**Tamaño de Chunks:**
- GFS: 64 MB (más grande que bloques tradicionales)
- HDFS: 128 MB (por defecto)
- **¿Por qué tan grandes?** Reduce overhead de metadata

**Replicación:**
Cada chunk se replica en 3 servidores diferentes. Si uno falla, Master ordena replicar desde otro.

---

### 5.4 Netflix - CDN Distribuido

**Problema:** Entregar video HD a 200M usuarios simultáneos sin lag.

**Solución: Open Connect (CDN propio)**

```
        Usuario en Medellín
              │
              ↓
      ┌──────────────┐
      │   CDN Cache  │  ← Servidor en Medellín (local)
      │   Colombia   │     Tiene películas populares
      └──────┬───────┘
             │ (si no está)
             ↓
      ┌──────────────┐
      │  CDN Regional│  ← Servidor en Miami
      │ Latinoamérica│
      └──────┬───────┘
             │ (si no está)
             ↓
      ┌──────────────┐
      │  Origen AWS  │  ← Servidor origen en Virginia
      │   EE.UU.     │
      └──────────────┘
```

---

### Netflix: Jerarquía de Caches

| Nivel | Ubicación | Almacenamiento | Tráfico |
|-------|-----------|----------------|---------|
| **Edge Cache** | Ciudades grandes (ISP local) | 20-40 TB | 90% |
| **Regional Cache** | Puntos de intercambio | 100+ TB | 9% |
| **Origin (AWS)** | Virginia | Todo el catálogo | 1% |

**Optimizaciones:**
- **Pre-caching:** Películas populares se cargan durante la noche
- **Smart routing:** DNS inteligente dirige al servidor más cercano
- **Adaptive streaming:** Calidad se ajusta según ancho de banda

**Métricas:**
- Latencia promedio: **<50 ms**
- Throughput: **100 Gbps** por servidor edge

---

### 5.5 WhatsApp - Sistema de Mensajería

**Arquitectura (Simplificada):**

```
Usuario A (Colombia)             Usuario B (Japón)
      │                                │
      ↓                                ↓
┌──────────┐                    ┌──────────┐
│ Servidor │                    │ Servidor │
│ Colombia │────Sincronización──│  Japón   │
└──────────┘                    └──────────┘
      │                                │
      └────────► Ejabberd ◄────────────┘
              (Protocolo XMPP)
```

**Tecnología:**
- **Erlang:** Lenguaje diseñado para sistemas distribuidos
- **Actor model:** Cada conversación es un proceso ligero
- **Capacidad:** 50M mensajes/segundo

**Garantías:**
- ✅ Entrega garantizada (aunque receptor esté offline)
- ✅ Ordenamiento de mensajes
- ✅ Cifrado end-to-end

---

## Comparación de Estrategias

| Sistema | Tipo | CAP | Caso de Uso Principal |
|---------|------|-----|----------------------|
| **Kubernetes** | Orquestación | CP (etcd) | Gestión de containers |
| **Cassandra** | Base de datos | AP | Escrituras masivas, alta disponibilidad |
| **GFS/HDFS** | Almacenamiento | CP | Big Data, procesamiento batch |
| **Netflix CDN** | Distribución de contenido | AP | Streaming de video |
| **WhatsApp** | Mensajería | CP | Comunicación en tiempo real |

---

## Actividad Práctica (10 min)

### En parejas, respondan:

1. **Identificar:** Dar un ejemplo de sistema distribuido en su vida diaria (diferente a los vistos en clase)

2. **Analizar:** Para ese sistema, identificar:
   - ¿Cuál es el problema que resuelve la distribución?
   - ¿Qué tipo de arquitectura tiene?
   - ¿Qué retos enfrenta (consistencia, disponibilidad, particiones)?

3. **Discutir:** ¿Por qué creen que WhatsApp eligió CP en lugar de AP?

---

## Resumen de la Clase

| Concepto | Idea Clave |
|----------|------------|
| **Sistema Distribuido** | Múltiples nodos = un solo sistema |
| **CAP** | Solo 2 de 3: Consistencia, Disponibilidad, Particiones |
| **Tipos** | Cliente-Servidor, P2P, Clúster |
| **Comunicación** | RPC, Mensajería, REST |
| **Retos** | Fallos parciales, consistencia, sincronización |

### Sistemas Analizados:
- **Kubernetes:** Orquestación de containers
- **Cassandra:** Base de datos AP
- **GFS/HDFS:** Almacenamiento masivo
- **Netflix:** CDN para streaming
- **WhatsApp:** Mensajería CP

---

## Próxima Clase

### Clase 14: Programas de Aplicación e Interfaces

- Llamadas al sistema en profundidad
- APIs del SO
- System calls en Linux vs Windows
- Ejemplos prácticos con strace

**¡Nos vemos!**

---

## Recursos Adicionales

### Para profundizar:
- **Libro:** "Designing Data-Intensive Applications" - Martin Kleppmann
- **Paper:** "The Google File System" - Sanjay Ghemawat et al.
- **Curso:** MIT 6.824 - Distributed Systems

### Herramientas para experimentar:
- **Minikube:** Kubernetes local en tu laptop
- **Docker Swarm:** Alternativa ligera a Kubernetes
- **Consul:** Service discovery y configuración distribuida
