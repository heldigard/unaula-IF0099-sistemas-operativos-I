---
marp: true
theme: default
paginate: true
header: 'IF0099 - Sistemas Operativos I | Unidad 5'
footer: 'UNAULA - Ingenieria Informatica - 2026-I'
---

# Clase 8: Memoria Secundaria y Discos

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

---

## Estructura, planificacion y rendimiento

**IF0099 - Sistemas Operativos I**
*4 Semestre - Ingenieria Informatica*

![Estructura de Disco Duro](../../../assets/infografias/clase-08-estructura-disco.png)

**En esta clase veremos:**
- Estructura fisica de HDD y SSD
- Tiempo de acceso y rendimiento
- Algoritmos de planificacion de disco
- RAID y almacenamiento moderno

---

## Objetivos de la Clase

Al finalizar esta clase, el estudiante sera capaz de:

1. **Describir** la estructura fisica de un disco
2. **Explicar** el tiempo de acceso y sus componentes
3. **Comparar** algoritmos de planificacion de discos
4. **Evaluar** estrategias de optimizacion y caching

**Duracion:** 90 minutos

---

## Agenda

1. Estructura de discos (15 min)
2. Tiempo de acceso y rendimiento (15 min)
3. Algoritmos de planificacion (25 min)
4. RAID y SSD (25 min)
5. Actividad practica (10 min)

---

## 1. Estructura de un Disco (HDD)

### Componentes principales

<div class="columns">
<div>

**Mecanicos:**
- **Platos:** superficies magneticas que giran (5400-15000 RPM)
- **Pistas:** circunferencias concentricas en cada plato
- **Sectores:** porciones de una pista (unidad minima, tipico 512B-4KB)
- **Cabezal:** lee y escribe datos (uno por superficie)
- **Cilindro:** conjunto de pistas alineadas en todos los platos

</div>
<div>

**Capacidades tipicas:**
- Disco de 1TB = ~2 billones de sectores
- Densidad: 100-1000 Gb/in²
- Latencia: 2-15 ms (HDD)
- SSD: 0.1-0.5 ms

**Organizacion logica:**
- Sector → Bloque → Cluster
- SO gestiona bloques, no sectores

</div>
</div>

---

## 1.1. Esquema deDireccionamientoFisico

```
Direcciondisco = Cilindro + Cabeza + Sector
 Ejemplo: (1024, 3, 7)
 Cilindro 1024, Cabezal 3, Sector 7
```

**CHS vs LBA:**
- **CHS:** Cilindro-Cabezal-Sector (antiguo, BIOS)
- **LBA:** Logical Block Addressing (moderno, lineal)

```
LBA simplifica la gestion:
SO ve bloques 0, 1, 2, 3, ...
El controlador traduce a CHS
```

---

## 2. Tiempo de Acceso

**Tiempo total = seek + latencia rotacional + transferencia**

| Componente | Descripcion |
| ----------- | ------------- |
| **Seek** | Mover el cabezal a la pista correcta |
| **Latencia** | Esperar que el sector gire hasta el cabezal |
| **Transferencia** | Leer o escribir datos |

**Ejemplo:** 8 ms (seek) + 4 ms (latencia) + 1 ms (transfer) = 13 ms

---

## 3. Algoritmos de Planificacion de Discos

### ¿Por que importa?

**El problema:** Las solicitudes de E/S llegan desordenadas
- Si atendemos en orden de llegada (FCFS), el cabezal se mueve mucho
- Mucho movimiento = mayor tiempo de espera = bajo rendimiento

**Solucion:** Reordenar solicitudes para minimizar movimiento del cabezal

---

## 3.1. Algoritmos Principales

<div class="columns">
<div>

**FCFS (First-Come, First-Served):**
- Atiende en orden de llegada
- Simple pero ineficiente
- Puede causar "oscilacion" del cabezal

**SSTF (Shortest Seek Time First):**
- Atiende la solicitud mas cercana
- Eficiente pero causa inanicion
- Solicitudes lejanas esperan mucho

</div>
<div>

**SCAN (Elevator):**
- Atiende en una direccion y luego regresa
- Justo, pero espera variable
- Similar a un ascensor

**C-SCAN:**
- Atiende en una direccion
- Regresa sin servir solicitudes
- Tiempo de espera uniforme

**LOOK / C-LOOK:**
- Como SCAN/C-SCAN
- Pero sin ir al extremo innecesario

</div>
</div>

---

## Ejemplo Visual (SCAN)

**Solicitudes:** 98, 183, 37, 122, 14, 124, 65, 67
**Cabezal inicia en:** 53

```
Movimiento (SCAN):
53 -> 65 -> 67 -> 98 -> 122 -> 124 -> 183 -> 199
(regresa) -> 37 -> 14
```

**Ventaja:** tiempo de espera mas uniforme que FCFS y SSTF

---

## Tabla Comparativa de Algoritmos

| Algoritmo | Ventaja | Desventaja | Uso recomendado |
|-----------|---------|------------|-----------------|
| **FCFS** | Simple | Alto movimiento | Sistemas simples |
| **SSTF** | Eficiente | Inanicion posible | Carga baja |
| **SCAN** | Justo | Espera variable | Uso general |
| **C-SCAN** | Uniforme | Regreso sin servicio | Servidores |
| **LOOK** | Eficiente | Mas complejo | Alta carga |
| **C-LOOK** | Muy eficiente | Mas complejo | Produccion |

---

## 4. RAID (Resumen)

### ¿Por que RAID?

**Problema:** Los discos fallan y son lentos
**Solucion:** RAID combina discos para:
- **Mejorar rendimiento** (RAID 0)
- **Añadir redundancia** (RAID 1, 5, 6, 10)
- **Ambos** (RAID 10)

---

## 4.1. Niveles RAID Comunes

<div class="columns">
<div>

**RAID 0 - Striping:**
- Datos divididos entre discos
- 2x velocidad (teoria)
- Sin redundancia
- Si falla 1 disco, se pierde todo

**RAID 1 - Mirroring:**
- Datos duplicados en 2+ discos
- Lectura 2x mas rapida
- 50% de capacidad util
- Sobrevive 1 fallo

**RAID 5 - Paridad:**
- Datos + paridad distribuida
- Minimo 3 discos
- Sobrevive 1 fallo
- Escritura mas lenta

</div>
<div>

**RAID 6 - Doble paridad:**
- Like RAID 5 pero 2 paridades
- Minimo 4 discos
- Sobrevive 2 fallos simultaneos
- Escritura aun mas lenta

**RAID 10 - Stripe of Mirrors:**
- RAID 0 + RAID 1
- Minimo 4 discos
- Rendimiento y redundancia
- 50% capacidad util

**RAID 50 / 60:**
- Combinaciones de niveles
- Para grandes arrays
- Mejor rendimiento

</div>
</div>

---

## 4.2. RAID en la Practica

| Uso | RAID recomendado | Por que |
|-----|------------------|---------|
| **Gaming PC** | RAID 0 o ninguno | Max velocidad |
| **Servidor web** | RAID 10 | Rendimiento + redundancia |
| **NAS hogar** | RAID 5 | Balance costo/capacidad |
| **Data center** | RAID 6 o 10 | Alta disponibilidad |

**Consideracion importante:** RAID NO es backup

---

## HDD vs SSD (Resumen)

| Caracteristica | HDD | SSD |
|----------------|-----|-----|
| **Latencia** | 5-15 ms | 0.1-0.2 ms |
| **IOPS** | 100-200 | 10k-100k |
| **Ruido** | Audible | Silencioso |
| **Resistencia** | Sensible a golpes | Mas resistente |
| **Costo/GB** | Bajo | Mayor |

**Regla practica:** SSD para sistema y apps, HDD para almacenamiento masivo.

---

## NVMe vs SATA SSD

### Diferencias clave

| Aspecto | SATA SSD | NVMe SSD |
|---------|----------|----------|
| **Interfaz** | SATA III (6 Gb/s) | PCIe 3.0/4.0 (32+ Gb/s) |
| **Colas** | 1 cola, 32 comandos | 65k colas, 64k comandos |
| **Latencia** | ~50 µs | ~10 µs |
| **IOPS** | 100k | 1M+ |
| **Ancho banda** | 560 MB/s | 3500-7000 MB/s |

---

## ¿Por que NVMe es mas rapido?

<div class="columns">
<div>

**Arquitectura:**
- Comunicacion directa con CPU via PCIe
- Menos capas de protocolo
- Comandos paralelos (múltiples colas)
- Menor overhead

**Ventajas practicas:**
- Boot en segundos
- Apps abren instantaneamente
- Mejor para workloads pesados

</div>
<div>

**Para servidores:**
- Mas I/O por segundo
- Menor latencia = DB mas rapidas
- Menor CPU utilizada para I/O

**Consideraciones:**
- Costo mayor que SATA
- Requiere slot M.2 o PCIe
- Compatible con几乎所有 motherboards modernas

</div>
</div>

---

## Optimizacion de Rendimiento

**Para HDD:**
- Evitar desorden de archivos (defrag)
- Reducir movimientos del cabezal (SCAN/LOOK)

**Para SSD:**
- Habilitar TRIM
- Evitar desfragmentacion
- Dejar espacio libre (over-provisioning)

---

## Actividad Practica (10 min)

### En parejas

**Linux:**
```bash
lsblk
sudo hdparm -t /dev/sda
```

**Windows (PowerShell):**
```powershell
Get-Disk
Get-PhysicalDisk
```

**Pregunta:** Que tipo de disco usa tu equipo y como afecta el rendimiento?

---

## Resumen de la Clase

| Concepto | Idea clave |
|----------|-----------|
| **Disco** | Pistas, sectores, cabezales |
| **Acceso** | Seek + latencia + transferencia |
| **Planificacion** | FCFS, SSTF, SCAN, C-SCAN |
| **RAID** | Redundancia y rendimiento |
| **SSD** | Menor latencia, mayor IOPS |

---

## Tarea

1. Comparar SSD vs HDD (3 diferencias tecnicas)
2. Explicar por que SCAN reduce el tiempo promedio
3. Investigar que RAID usa un data center moderno

---

## Proxima Clase

### Clase 9: Sistemas de Archivos

- Concepto de archivo y atributos
- Operaciones sobre archivos
- Estructura de directorios
- FAT, NTFS, ext4

**Nos vemos!**
