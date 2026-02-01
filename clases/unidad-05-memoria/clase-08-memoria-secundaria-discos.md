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

![Estructura de Disco Duro](../../assets/infografias/clase-08-estructura-disco.png)

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

- **Platos:** superficies magneticas que giran
- **Pistas:** circunferencias concentricas en cada plato
- **Sectores:** porciones de una pista (unidad minima)
- **Cabezal:** lee y escribe datos
- **Cilindro:** conjunto de pistas alineadas en todos los platos

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

- **FCFS:** atiende en orden de llegada, simple pero ineficiente
- **SSTF:** atiende la solicitud mas cercana, puede causar inanicion
- **SCAN (Elevator):** atiende en una direccion y luego regresa
- **C-SCAN:** atiende en una direccion y regresa sin servir
- **LOOK / C-LOOK:** como SCAN pero sin ir al extremo

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

| Nivel | Idea | Ventaja | Riesgo |
|------|------|---------|--------|
| **RAID 0** | Striping | Velocidad | Sin redundancia |
| **RAID 1** | Mirroring | Redundancia | 50% capacidad |
| **RAID 5** | Paridad distribuida | Balance | Escritura mas lenta |
| **RAID 10** | 0 + 1 | Rendimiento y redundancia | Costoso |

**Idea clave:** RAID combina discos para mejorar rendimiento o tolerancia a fallos.

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

| Aspecto | SATA SSD | NVMe SSD |
|---------|----------|----------|
| **Interfaz** | SATA | PCIe |
| **Colas** | 32 | 65k |
| **Latencia** | Mayor | Menor |
| **IOPS** | 100k | 1M+ |

**Por que es mas rapido?**
- Menos capas de protocolo
- Mas paralelismo en colas
- Mayor ancho de banda PCIe

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
