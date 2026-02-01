---
marp: true
theme: default
paginate: true
header: 'IF0099 - Sistemas Operativos I | Unidad 8'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
---

# Clase 13: Sistemas Distribuidos

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

## Objetivos de la Clase

Al finalizar esta clase, el estudiante será capaz de:

1. **Definir** qué es un sistema distribuido
2. **Identificar** ventajas y desafíos principales
3. **Reconocer** modelos de comunicación y coordinación
4. **Relacionar** SO con servicios distribuidos

**Duración:** 90 minutos

---

## Agenda

1. Conceptos básicos (20 min)
2. Tipos de sistemas distribuidos (15 min)
3. Retos: sincronización, fallos, consistencia (25 min)
4. Casos reales (20 min)
5. Actividad (10 min)

---

## 1. ¿Qué es un Sistema Distribuido?

### Ejemplos cotidianos de sistemas distribuidos

**En tu día a día:**
- 🌐 **Google:** Miles de servidores trabajando juntos
- 📱 **WhatsApp:** Mensajes sincronizados en múltiples dispositivos
- 🎮 **Juegos online:** Jugadores conectados desde todo el mundo
- 💰 **Blockchain:** Bitcoin y criptomonedas
- 📧 **Email:** Servidores distribuidos globalmente

💡 **La nube (AWS, Azure, Google Cloud) son sistemas distribuidos masivos.**


> Conjunto de computadores independientes que se presentan como un solo sistema coherente.

```
Cliente ──► Nodo A ──► Nodo B
           │            │
           └──► Nodo C ─┘
```

Características:
- Concurrencia
- Falta de reloj global
- Fallos parciales

---

## 2. Tipos Comunes

| Tipo | Ejemplo |
| ------ | --------- |
| **Clúster** | HPC, procesamiento paralelo |
| **Cliente-Servidor** | Bases de datos, apps web |
| **P2P** | BitTorrent, blockchain |
| **Microservicios** | Arquitecturas modernas en cloud |

---

## 3. Retos Clave

### Consistencia vs Disponibilidad
- Teorema CAP: no se pueden maximizar ambas simultáneamente

### Fallos parciales
- Un nodo puede fallar sin caer todo el sistema

### Sincronización
- Locks distribuidos
- Elección de líder

---

## 4. Comunicación

| Modelo | Descripción |
| -------- | ------------- |
| **RPC** | Llamadas remotas como si fueran locales |
| **Mensajería** | Cola y eventos (Kafka, RabbitMQ) |
| **REST** | APIs HTTP |

---

## Casos Reales

- **Google File System / HDFS**: almacenamiento distribuido
- **Kubernetes**: orquestación de contenedores
- **CDN**: distribución global de contenido

---

## Actividad (10 min)

En parejas:
1. Dar un ejemplo de sistema distribuido en su vida diaria
2. Identificar 2 retos y 1 ventaja

---

## Resumen

| Concepto | Idea clave |
| ---------- | ------------ |
| **Distribuido** | Varios nodos = un solo sistema |
| **Retos** | Fallos parciales, consistencia, sincronización |
| **Modelos** | RPC, mensajería, REST |

---

## Próxima Clase

### Clase 14: Programas de Aplicación e Interfaces

- Llamadas al sistema
- APIs del SO
- Ejemplos en Linux/Windows

**¡Nos vemos!**


---
### 1. Kubernetes - Orquestación de Contenedores



**¿Qué es?**
Sistema distribuido para gestionar contenedores Docker en múltiples máquinas.

**Arquitectura:**
```
┌─────────────────────────────────────────┐
│          KUBERNETES CLUSTER             │
├─────────────────────────────────────────┤
│                                         │
│  ┌──────────────┐    ┌──────────────┐  │
│  │   Master     │    │    etcd      │  │
│  │   (Control   │◄──►│  (Registro   │  │
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
### 1. Kubernetes - Orquestación de Contenedores (Continuación)

**Componentes Principales del Cluster:**

- **Master Node (Control Plane):**
  - **API Server:** Punto de entrada para todas las operaciones
  - **Scheduler:** Decide en qué nodo ejecutar cada pod
  - **Controller Manager:** Mantiene el estado deseado del cluster
  - **etcd:** Base de datos distribuida con toda la configuración

- **Worker Nodes:**
  - **Kubelet:** Agente que ejecuta containers en cada nodo
  - **Kube-proxy:** Maneja networking y balanceo de carga
  - **Container Runtime:** Docker, containerd, etc.

**Características Distribuidas:**
- **Replicación:** Copia automática de pods en múltiples nodos
- **Balanceo de carga:** Distribuye tráfico entre réplicas
- **Auto-recuperación:** Si un nodo falla, mueve pods a otro nodo
- **Escalado horizontal:** Añade/quita nodos dinámicamente

---

### 2. Apache Cassandra - Base de Datos Distribuida

**Arquitectura sin Maestro:**
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

**Ejemplo de Escritura:**

```python
# Cliente escribe "usuario123" con RF=3 (Replication Factor)
cassandra.insert("usuarios", "usuario123", datos)

# Cassandra automáticamente:
# 1. Calcula hash(usuario123) = 0x8A3F...
# 2. Ubica en el anillo: Nodo B es responsable
# 3. Replica en Nodos C y D (siguientes en el anillo)
# 4. Escritura exitosa si 2 de 3 nodos confirman (Quorum)
```

---
### 3. Google File System (GFS) / HDFS

**Problema que resuelve:**
Almacenar archivos de **petabytes** en miles de máquinas comunes (no servidores caros).

**Arquitectura:**

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
### 3. Google File System (GFS) / HDFS (Continuación)

**Componentes del Sistema:**

- **Master (NameNode en HDFS):**
  - Almacena metadata: nombres de archivos, permisos, ubicación de chunks
  - NO almacena datos reales (solo metadatos)
  - Single point of failure (mitigado con Secondary Master)

- **Chunk Servers (DataNodes en HDFS):**
  - Almacenan los datos reales
  - Reportan su estado al Master periódicamente
  - Se comunican directamente con los clientes

**Tamaño de Chunks:**
- GFS: 64 MB (mucho más grande que bloques de filesystems tradicionales)
- HDFS: 128 MB (por defecto)
- ¿Por qué tan grandes? Reduce overhead de metadata

**Proceso de Lectura:**

1. Cliente: "Quiero leer `video.mp4` desde byte 1GB"
2. Master: "Los chunks están en Servers 2, 3, 4"
3. Cliente lee directamente de esos servidores (paralelo!)

**Replicación:**
Cada chunk (64 MB) se replica en 3 servidores diferentes.
Si uno falla, Master ordena replicar desde otro.

---
### 4. Netflix - CDN Distribuido

**Problema:** Entregar video HD a 200M usuarios simultáneos sin lag.

**Solución: Open Connect**

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
      │   Latinoamérica│
      └──────┬───────┘
             │ (si no está)
             ↓
      ┌──────────────┐
      │  Origen AWS  │  ← Servidor origen en Virginia
      │   EE.UU.     │
      └──────────────┘
```

---
### 4. Netflix - CDN Distribuido (Continuación)

**Arquitectura de Open Connect:**

**Jerarquía de Caches:**
1. **Edge Cache (Nivel 1):** Servidores en ciudades grandes
   - Ubicados en ISPs locales
   - 20-40 TB de almacenamiento
   - Atienden 90% del tráfico

2. **Regional Cache (Nivel 2):** Servidores regionales
   - Ubicados en puntos de intercambio de internet
   - 100+ TB de almacenamiento
   - Respaldan a los edge caches

3. **Origin Servers:** AWS Cloud
   - Almacén completo del catálogo
   - Codifican video en múltiples resoluciones/bitrates

**Algoritmo de Entrega:**
```
Usuario solicita película
    ↓
Verificar: ¿Está en Edge Cache?
    ↓ Sí → Entregar desde Edge (<50ms)
    ↓ No
Verificar: ¿Está en Regional Cache?
    ↓ Sí → Entregar desde Regional (<200ms)
    ↓ No
Obtener desde Origin + Cachear en Regional/Edge
```

**Optimizaciones:**
- **Pre-caching:** Películas populares se cargan en caches durante la noche
- **Smart routing:** DNS inteligente dirige al servidor más cercano
- **Adaptive streaming:** Calidad se ajusta según ancho de banda

**Métricas Reales:**
- **90% del tráfico** se sirve desde cache local
- **Latencia promedio:** <50 ms
- **Throughput:** 100 Gbps por servidor edge

---

### 5. WhatsApp - Sistema de Mensajería Distribuido

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
- **50M mensajes/segundo** en infraestructura distribuida

**Garantías:**
- **Entrega garantizada:** Aunque el receptor esté offline
- **Ordenamiento:** Mensajes llegan en orden enviado
- **Cifrado E2E:** Solo emisor y receptor descifran

---

### 📊 Comparación de Estrategias

| Sistema | Consistencia | Disponibilidad | Particionamiento |
|---------|--------------|----------------|------------------|
| **Kubernetes** | Fuerte (etcd) | Alta | Sí |
| **Cassandra** | Eventual | Muy alta | Sí |
| **GFS/HDFS** | Eventual | Alta | Sí |
| **Netflix CDN** | Eventual | Muy alta | Geográfico |
| **WhatsApp** | Fuerte | Alta | Por usuario |

---

### 💡 Teorema CAP en Práctica

**CAP:** Solo puedes garantizar 2 de 3 (Consistency, Availability, Partition tolerance)

**Elecciones:**
- **Cassandra:** AP (Disponibilidad + Particionamiento) → Eventual consistency
- **etcd (Kubernetes):** CP (Consistencia + Particionamiento) → Menor disponibilidad
- **DNS:** AP → Por eso a veces ves info desactualizada

---

## 💻 Actividad Práctica: Explorar Kubernetes Local

### Requisitos: Docker Desktop + Habilitar Kubernetes

```bash
# 1. Verificar que Kubernetes esté corriendo
kubectl version --short

# 2. Crear un deployment simple (3 réplicas)
kubectl create deployment hello --image=nginx --replicas=3

# 3. Ver los pods distribuidos
kubectl get pods -o wide
# Observa en qué nodos están

# 4. Exponer el servicio
kubectl expose deployment hello --port=80 --type=LoadBalancer

# 5. Simular falla: eliminar un pod
kubectl delete pod <nombre-de-un-pod>

# 6. Ver auto-recuperación
kubectl get pods -w  # (-w = watch en tiempo real)
# Kubernetes automáticamente crea un nuevo pod!

# 7. Escalar horizontalmente
kubectl scale deployment hello --replicas=5

# 8. Limpiar
kubectl delete deployment hello
kubectl delete service hello
```

### Preguntas de Reflexión:

1. ¿Qué pasó cuando eliminaste un pod?
2. ¿En cuánto tiempo se creó el reemplazo?
3. ¿Los pods están en el mismo nodo o distribuidos?
4. ¿Cómo garantiza Kubernetes alta disponibilidad?

### Tiempo estimado: 45 minutos

---
