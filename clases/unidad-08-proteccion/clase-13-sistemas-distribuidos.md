---
marp: true
theme: default
paginate: true
header: 'IF0099 - Sistemas Operativos I | Unidad 8'
footer: 'UNAULA - Ingeniería Informática - 2026-I'

  section {
    font-size: 24px;
  }

---
<style>
img {
  max-width: 65% !important;
  max-height: 45vh !important;
  object-fit: contain !important;
  height: auto !important;
}
section {
  font-size: 24px;
}
</style>


<!--
IMÁGENES GENERADAS:
- clase-13-sistemas-distribuidos.png: Arquitectura de sistemas distribuidos y teorema CAP
-->

# Clase 13: Sistemas Distribuidos
## Conceptos, ventajas y desafíos

**IF0099 - Sistemas Operativos I**
*4° Semestre - Ingeniería Informática*

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
|------|---------|
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
|--------|-------------|
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
|----------|------------|
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
