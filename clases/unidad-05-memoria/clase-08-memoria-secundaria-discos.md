---
marp: true
theme: default
paginate: true
header: 'IF0099 - Sistemas Operativos I | Unidad 5'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
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
# Clase 8: Memoria Secundaria y Discos

*(continuación...)*


<!--
IMÁGENES GENERADAS:
- clase-08-estructura-disco.png: Infografía sobre estructura de disco duro y algoritmos de planificación
-->

---
## Estructura, planificación y rendimiento

**IF0099 - Sistemas Operativos I**
*4° Semestre - Ingeniería Informática*

![Estructura de Disco Duro](../../assets/infografias/clase-08-estructura-disco.png)

---

## Objetivos de la Clase

Al finalizar esta clase, el estudiante será capaz de:

1. **Describir** la estructura física de un disco
2. **Explicar** el tiempo de acceso y sus componentes
3. **Comparar** algoritmos de planificación de discos
4. **Evaluar** estrategias de optimización y caching

**Duración:** 90 minutos

---

## Agenda

1. Estructura de discos (15 min)
2. Tiempo de acceso y rendimiento (15 min)
3. Algoritmos de planificación (30 min)
4. RAID y almacenamiento moderno (20 min)
5. Actividad práctica (10 min)

---

## 1. Estructura de un Disco

```
Platos ─► Pistas ─► Sectores

┌───────────────┐
│   PLATO 0     │
│ ┌───────────┐ │
│ │  PISTA 0  │ │
│ │  PISTA 1  │ │
│ │  PISTA 2  │ │
│ └───────────┘ │
└───────────────┘
```

- **Pista:** circunferencia concéntrica
- **Sector:** porción de una pista (unidad mínima)
- **Cabezal:** lee/escribe sobre la superficie
- **Cilindro:** conjunto de pistas alineadas entre platos

---

## 2. Tiempo de Acceso

**Tiempo total = seek + latencia + transferencia**

| Componente | Descripción |
| ----------- | ------------- |
| **Seek** | Mover cabezal a la pista correcta |
| **Latencia rotacional** | Esperar que el sector gire hasta el cabezal |
| **Transferencia** | Leer/escribir datos |

```
Ejemplo: 8ms (seek) + 4ms (latencia) + 1ms (transfer) = 13ms
```

---

## 3. Algoritmos de Planificación de Discos

### FCFS (First-Come, First-Served)
- Simple, pero puede ser ineficiente

### SSTF (Shortest Seek Time First)
- Minimiza el movimiento del cabezal
- Puede causar starvation

### SCAN (Elevator)
- Cabezal se mueve en una dirección y luego regresa

### C-SCAN
- Solo atiende en una dirección

---

## Ejemplo Visual (SCAN)

```
Solicitudes: 98, 183, 37, 122, 14, 124, 65, 67
Cabezal inicia en 53

Movimiento (SCAN): 53 → 65 → 67 → 98 → 122 → 124 → 183 → (regresa) → 37 → 14
```

**Ventaja:** tiempo de espera más uniforme

---

## 4. RAID y Almacenamiento Moderno

| Tipo | Descripción | Beneficio |
| ------ | ------------- | ----------- |
| **RAID 0** | Striping | Velocidad (sin redundancia) |
| **RAID 1** | Mirroring | Redundancia |
| **RAID 5** | Paridad distribuida | Balance rendimiento/seguridad |
| **RAID 10** | 0 + 1 | Rendimiento y redundancia |

**SSD:** sin partes mecánicas, menor latencia

---


---

## 💡 Conceptos Clave de Discos Duros

### Anatomía Detallada de un Disco

Un disco duro (HDD) es un dispositivo de almacenamiento magnético con componentes mecánicos:

```
┌─────────────────────────────────────────────────────────┐
│  COMPONENTES FÍSICOS DE UN HDD                          │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1. PLATOS (Platters)                                   │
│     - Material: aluminio o vidrio                       │
│     - Recubrimiento: óxido magnético                    │
│     - Típico: 2-5 platos por disco                      │
│                                                         │
│  2. CABEZALES (Read/Write Heads)                        │
│     - Flotan a 3-6 nanómetros de la superficie          │
│     - 1 cabezal por superficie (2 por plato)            │
│                                                         │
│  3. BRAZO ACTUADOR (Actuator Arm)                       │
│     - Mueve cabezales radialmente                       │
│     - Velocidad: 10-15ms típico                         │
│                                                         │
│  4. MOTOR DE HUSILLO (Spindle Motor)                    │
│     - Velocidad: 5400, 7200, 10000 RPM                  │
│     - Más RPM = menor latencia rotacional               │
└─────────────────────────────────────────────────────────┘
```

---

## 🔍 Cálculo Detallado del Tiempo de Acceso

### Fórmula Completa

```
T_acceso = T_seek + T_latencia + T_transferencia + T_controller
```

### Componentes Explicados

1. **Tiempo de Seek (búsqueda)**
   - Promedio: 8-12ms en HDDs modernos
   - Depende de la distancia entre pistas
   - Fórmula: `T_seek = a + b × √distancia`

2. **Latencia Rotacional**
   - Promedio: la mitad de una rotación completa
   - Fórmula: `T_latencia = (60 / RPM) / 2`
   - Ejemplo 7200 RPM: `(60 / 7200) / 2 = 4.17ms`

3. **Tiempo de Transferencia**
   - Depende del tamaño del bloque
   - Fórmula: `T_trans = (tamaño_bloque / tasa_transferencia)`
   - Ejemplo: `(4KB / 100MB/s) = 0.04ms`

### Ejemplo Completo

```python
# Disco: 7200 RPM, tasa 150MB/s, seek promedio 9ms
# Leer bloque de 8KB

T_seek = 9  # ms (promedio)
T_latencia = (60 / 7200) / 2 * 1000  # = 4.17 ms
T_transferencia = (8 / 1024 / 150) * 1000  # = 0.05 ms
T_controller = 0.1  # overhead del controlador

T_total = 9 + 4.17 + 0.05 + 0.1 = 13.32 ms
```

**Conclusión:** El seek y latencia dominan (>99% del tiempo)

---

## 📊 Algoritmos de Planificación - Análisis Comparativo

### Escenario de Ejemplo

Configuración:
- **Cola de solicitudes:** 98, 183, 37, 122, 14, 124, 65, 67
- **Posición inicial del cabezal:** 53
- **Rango de cilindros:** 0-199

### 1. FCFS (First-Come, First-Served)

**Secuencia:** 53 → 98 → 183 → 37 → 122 → 14 → 124 → 65 → 67

```
Movimiento total:
|98-53| + |183-98| + |37-183| + |122-37| + |14-122| + |124-14| + |65-124| + |67-65|
= 45 + 85 + 146 + 85 + 108 + 110 + 59 + 2
= 640 cilindros
```

**Ventajas:** Simple, justo (no inanición)
**Desventajas:** Muy ineficiente, movimiento errático

---

### 2. SSTF (Shortest Seek Time First)

**Secuencia:** 53 → 65 → 67 → 37 → 14 → 98 → 122 → 124 → 183

```
Movimiento total:
|65-53| + |67-65| + |37-67| + |14-37| + |98-14| + |122-98| + |124-122| + |183-124|
= 12 + 2 + 30 + 23 + 84 + 24 + 2 + 59
= 236 cilindros
```

**Ventajas:** Mejor rendimiento que FCFS
**Desventajas:** Puede causar inanición (starvation)

**Ejemplo de inanición:**
```
Si llegan constantemente solicitudes cerca del cabezal,
las solicitudes lejanas nunca se atienden.
```

---

### 3. SCAN (Algoritmo del Ascensor)

**Secuencia:** 53 → 65 → 67 → 98 → 122 → 124 → 183 → 199 (extremo) → 37 → 14

```
Movimiento total (hasta extremo):
|65-53| + |67-65| + |98-67| + |122-98| + |124-122| + |183-124| + |199-183|
+ |37-199| + |14-37|
= 12 + 2 + 31 + 24 + 2 + 59 + 16 + 162 + 23
= 331 cilindros
```

**Ventajas:** Sin inanición, predecible
**Desventajas:** Tiempo de espera variable

---

### 4. C-SCAN (Circular SCAN)

**Secuencia:** 53 → 65 → 67 → 98 → 122 → 124 → 183 → 199 → 0 (salto) → 14 → 37

```
Movimiento efectivo (sin contar salto circular):
= 146 + 14 + 23 = 183 cilindros
(El salto de 199 → 0 no cuenta como servicio)
```

**Ventajas:** Tiempo de espera más uniforme
**Desventajas:** Overhead del regreso

---

### 5. LOOK y C-LOOK

**Diferencia con SCAN:** No llegan hasta el extremo, solo hasta última solicitud.

**C-LOOK Secuencia:** 53 → 65 → 67 → 98 → 122 → 124 → 183 → (salta a 14) → 14 → 37

```
Movimiento: 130 + 23 = 153 cilindros (más eficiente)
```

---

## 📈 Tabla Comparativa de Algoritmos

| Algoritmo | Mov. Total | Ventaja | Desventaja | Uso Recomendado |
|-----------|------------|---------|------------|-----------------|
| **FCFS** | 640 | Simple | Ineficiente | Sistemas simples |
| **SSTF** | 236 | Rápido | Inanición | Carga baja |
| **SCAN** | 331 | Justo | Irregular | Uso general |
| **C-SCAN** | 183 | Uniforme | Overhead | Servidores |
| **LOOK** | 208 | Eficiente | Complejo | Alta carga |
| **C-LOOK** | 153 | Óptimo | Más complejo | Producción |

---

## 🚀 SSD vs HDD: Evolución del Almacenamiento

### Comparación Técnica

| Característica | HDD | SSD |
|----------------|-----|-----|
| **Tecnología** | Magnética, mecánica | Flash NAND, electrónica |
| **Latencia** | 10-15ms | 0.1-0.2ms (100× más rápido) |
| **IOPS** | 100-200 | 50,000-100,000 |
| **Velocidad seq.** | 100-200 MB/s | 500-7000 MB/s |
| **Durabilidad** | Frágil (golpes) | Resistente |
| **Vida útil** | 3-5 años | 5-10 años (por escrituras) |
| **Costo/GB** | $0.02 | $0.10 |
| **Ruido** | Audible | Silencioso |
| **Energía** | 6-7W | 2-3W |

### Arquitectura SSD

```
┌────────────────────────────────────────────┐
│  SSD (Solid State Drive)                   │
├────────────────────────────────────────────┤
│  Controlador SSD                           │
│  ├─ FTL (Flash Translation Layer)          │
│  ├─ Wear Leveling (distribuir escrituras)  │
│  ├─ Garbage Collection                     │
│  └─ ECC (Error Correction)                 │
│                                            │
│  Chips NAND Flash                          │
│  ├─ SLC (1 bit/celda) - más rápido        │
│  ├─ MLC (2 bits/celda) - balance           │
│  ├─ TLC (3 bits/celda) - más capacidad    │
│  └─ QLC (4 bits/celda) - más económico    │
│                                            │
│  Cache DRAM (opcional)                     │
│  └─ Acelera operaciones pequeñas           │
└────────────────────────────────────────────┘
```

---

## 💾 RAID: Redundancia y Rendimiento

### Niveles RAID Explicados

#### RAID 0 - Striping (División)

```
Datos: [A1][A2][A3][A4][A5][A6]

Disco 1: [A1][A3][A5]
Disco 2: [A2][A4][A6]

Ventajas:
- Velocidad 2× (lectura/escritura paralela)
- Capacidad total = suma de discos

Desventajas:
- SIN redundancia (1 disco falla → todo perdido)
- Fiabilidad: 1/n (empeora con más discos)
```

**Caso de uso:** Edición de video, scratch space

---

#### RAID 1 - Mirroring (Espejo)

```
Datos: [A1][A2][A3][A4]

Disco 1: [A1][A2][A3][A4]
Disco 2: [A1][A2][A3][A4] (copia exacta)

Ventajas:
- Tolerancia a fallo (1 disco puede fallar)
- Lectura 2× más rápida

Desventajas:
- Capacidad útil = 50%
- Escritura igual velocidad (ambos discos)
```

**Caso de uso:** Datos críticos, servidores

---

#### RAID 5 - Paridad Distribuida

```
Con 3 discos:

Bloque 1:  [A1] [A2] [P(A1,A2)]
Bloque 2:  [B1] [P(B1,B2)] [B2]
Bloque 3:  [P(C1,C2)] [C1] [C2]

P = XOR de los bloques de datos

Ventajas:
- Balance rendimiento/redundancia
- Capacidad útil = (n-1) discos
- Tolerancia: 1 disco puede fallar

Desventajas:
- Escritura lenta (cálculo paridad)
- Reconstrucción lenta tras fallo
```

**Caso de uso:** Servidores de archivos, NAS

---

## 🎯 Ejercicio Práctico 1: Cálculo de Tiempos

### Problema

Un disco duro tiene las siguientes características:
- 7200 RPM
- Seek time promedio: 9ms
- Tasa de transferencia: 180 MB/s
- Tamaño de sector: 512 bytes

**Pregunta:** ¿Cuánto tiempo toma leer 100 sectores secuenciales?

### Solución Paso a Paso

```python
# Datos
RPM = 7200
T_seek = 9  # ms
tasa = 180  # MB/s
tam_sector = 512  # bytes
num_sectores = 100

# Paso 1: Seek inicial
tiempo_seek = 9  # ms

# Paso 2: Latencia rotacional (solo inicial)
T_latencia = (60 / RPM) / 2 * 1000
T_latencia = (60 / 7200) / 2 * 1000 = 4.17  # ms

# Paso 3: Transferencia (todos los sectores son secuenciales)
tamaño_total = num_sectores * tam_sector / (1024 * 1024)  # MB
tamaño_total = 100 * 512 / (1024 * 1024) = 0.0488 MB

T_transferencia = (tamaño_total / tasa) * 1000
T_transferencia = (0.0488 / 180) * 1000 = 0.27 ms

# Tiempo total
T_total = tiempo_seek + T_latencia + T_transferencia
T_total = 9 + 4.17 + 0.27 = 13.44 ms
```

**Respuesta:** 13.44 ms

**Nota clave:** Acceso secuencial es MUY eficiente (1 seek para 100 sectores)

---

## 🎯 Ejercicio Práctico 2: Comparar Algoritmos

### Problema

Cola de solicitudes: **95, 180, 34, 119, 11, 123, 62, 64**
Posición inicial: **50**
Dirección inicial: **hacia arriba (→)**

**Calcular movimiento total para:**
1. FCFS
2. SSTF
3. SCAN
4. C-LOOK

### Solución

#### 1. FCFS

```
Secuencia: 50 → 95 → 180 → 34 → 119 → 11 → 123 → 62 → 64

Movimiento:
45 + 85 + 146 + 85 + 108 + 112 + 61 + 2 = 644 cilindros
```

#### 2. SSTF

```
Secuencia: 50 → 62 → 64 → 34 → 11 → 95 → 119 → 123 → 180

Movimiento:
12 + 2 + 30 + 23 + 84 + 24 + 4 + 57 = 236 cilindros
```

#### 3. SCAN (hasta extremo 199)

```
Secuencia: 50 → 62 → 64 → 95 → 119 → 123 → 180 → 199 → 34 → 11

Movimiento:
12 + 2 + 31 + 24 + 4 + 57 + 19 + 165 + 23 = 337 cilindros
```

#### 4. C-LOOK

```
Secuencia: 50 → 62 → 64 → 95 → 119 → 123 → 180 → (salta) → 11 → 34

Movimiento (sin contar salto):
12 + 2 + 31 + 24 + 4 + 57 + 169 + 23 = 322 cilindros
```

**Ganador:** SSTF (236), pero con riesgo de inanición

---

## 🏠 Tarea para Casa

### Investigación: NVMe vs SATA SSD

**Instrucciones:**
1. Investiga las diferencias entre NVMe y SATA (protocolos)
2. Compara velocidades típicas
3. Explica por qué NVMe es más rápido (arquitectura)
4. ¿Cuándo vale la pena NVMe sobre SATA SSD?

**Formato:** 1-2 páginas, entregar vía plataforma

**Fecha límite:** Próxima clase

---

## 📚 Referencias y Recursos

### Lecturas Recomendadas

- Silberschatz, Cap. 10: "Mass-Storage Structure"
- Tanenbaum, Cap. 5.4: "Disks"
- [How HDDs Work](https://www.youtube.com/watch?v=wteUW2sL7bc) - Video

### Herramientas para Explorar

**Linux:**
```bash
# Ver discos y particiones
lsblk

# Información detallada de disco
sudo hdparm -I /dev/sda

# Benchmark de disco
sudo hdparm -t /dev/sda
```

**Windows:**
```powershell
# Información de discos
Get-PhysicalDisk | Format-Table

# Fragmentación
Optimize-Volume -DriveLetter C -Analyze
```

---

## Actividad Práctica (10 min)

### En parejas:

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

**Pregunta:** ¿Qué tipo de disco usa tu equipo y cómo afecta el rendimiento?

---

## 💾 SSD vs HDD: Comparativa Técnica Profunda

### Tecnología Interna

| Aspecto | HDD (Mecánico) | SSD (Estado Sólido) |
|---------|----------------|---------------------|
| **Tecnología** | Discos magnéticos giratorios | Memoria NAND Flash |
| **Velocidad lectura** | 80-160 MB/s | 200-3500 MB/s |
| **Velocidad escritura** | 80-160 MB/s | 200-3000 MB/s |
| **Latencia** | 5-10 ms | 0.1 ms |
| **IOPS** | 100-200 | 10,000-100,000 |
| **Durabilidad** | Sensible a golpes | Resistente golpes |
| **Ruido** | Audible (motor) | Silencioso |
| **Consumo energía** | 6-7 W | 2-3 W |
| **Vida útil** | 3-5 años | 5-10 años |
| **Costo por GB** | $0.03-0.05 | $0.10-0.20 |

### 🎯 Cuándo Usar Cada Uno

**HDD:** Almacenamiento masivo, backups, archivos poco usados  
**SSD:** Sistema operativo, aplicaciones, bases de datos

---

## 🔬 Estructura Interna de un SSD

### Arquitectura NAND Flash

```
┌─────────────────────────────────────────────────────────┐
│                  CONTROLADOR SSD                        │
│  ┌────────────┬───────────────┬──────────────┐         │
│  │ Wear       │  Garbage      │   Cache      │         │
│  │ Leveling   │  Collection   │   DRAM       │         │
│  └────────────┴───────────────┴──────────────┘         │
├─────────────────────────────────────────────────────────┤
│                     BLOQUES NAND                        │
│  ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐    │
│  │Block│Block│Block│Block│Block│Block│Block│Block│    │
│  │  0  │  1  │  2  │  3  │  4  │  5  │  6  │  7  │    │
│  └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘    │
│         Cada bloque: 128-256 páginas                    │
│         Cada página: 4-16 KB                            │
└─────────────────────────────────────────────────────────┘
```

### Limitaciones de SSD
- **Write Amplification:** Reescrituras multiplican desgaste
- **TRIM necesario:** Para mantener rendimiento
- **Writes limitados:** ~3000-10000 ciclos P/E por celda

---

## 📊 Configuraciones RAID Avanzadas

### RAID 0 (Striping)

```
Datos: A B C D E F G H

Disco 1: [A][C][E][G]
Disco 2: [B][D][F][H]

✅ Velocidad: 2x
❌ Tolerancia fallas: 0 (cualquier disco falla = pérdida total)
```

### RAID 1 (Mirroring)

```
Disco 1: [A][B][C][D]
Disco 2: [A][B][C][D]  ← Copia exacta

✅ Tolerancia: 1 disco puede fallar
❌ Capacidad: 50% del total
```

### RAID 5 (Paridad Distribuida)

```
     Disco 1   Disco 2   Disco 3
      [A]       [B]      [Parity AB]
      [C]      [Parity CD] [D]
   [Parity EF]  [E]       [F]

✅ Balance: Velocidad + redundancia
✅ Capacidad: (n-1) discos
❌ Mínimo 3 discos
```

### RAID 10 (1+0)

```
      RAID 1          RAID 1
   ┌────┴────┐    ┌────┴────┐
Disco1  Disco2  Disco3  Disco4
  [A]    [A]     [B]     [B]
        └──────RAID 0──────┘

✅ Máxima velocidad + redundancia
❌ Costo: 50% capacidad
```

---

## 🔥 NVMe: El Futuro del Almacenamiento

### NVMe vs SATA

```
                SATA SSD          NVMe SSD
              ┌──────────┐      ┌──────────┐
Interfaz:     │   SATA   │      │   PCIe   │
              │  3.0/3.1 │      │ 3.0/4.0  │
              └──────────┘      └──────────┘
                   │                 │
Ancho banda:      600 MB/s        4000 MB/s
Latencia:         50 µs           25 µs
Colas:            32               65536
IOPS:             100K             1M+
```

### Ventajas NVMe
- ✅ **Protocolo optimizado** para flash
- ✅ **Conexión directa** a PCIe
- ✅ **Menor latencia** de software
- ✅ **Más colas paralelas** (65K vs 32)

---

## 💻 Comandos Prácticos de Diagnóstico

### Linux: Análisis de Disco

```bash
# Ver información de discos
lsblk
sudo fdisk -l

# Velocidad de lectura/escritura
sudo hdparm -tT /dev/sda

# Información SMART (salud del disco)
sudo smartctl -a /dev/sda

# I/O actual en tiempo real
sudo iotop

# Estadísticas de I/O
iostat -x 2

# Ver tipo de disco (HDD/SSD)
cat /sys/block/sda/queue/rotational
# 0 = SSD, 1 = HDD
```

### Windows: PowerShell

```powershell
# Información de discos
Get-PhysicalDisk | Format-Table FriendlyName, MediaType, Size

# Velocidad de transferencia
Get-PhysicalDisk | Get-StorageReliabilityCounter

# Optimización SSD (TRIM)
Optimize-Volume -DriveLetter C -Defrag

# Información SMART
Get-PhysicalDisk | Get-StorageReliabilityCounter | Select Wear
```

---

## 🎯 Optimización de Rendimiento de Disco

### Para HDD

1. **Desfragmentación regular**
   ```bash
   # Windows
   defrag C: /O
   ```

2. **Alinear particiones** (importante en RAID)
3. **Deshabilitar indexación** en volúmenes de datos
4. **Usar write-back cache** (con UPS)

### Para SSD

1. **Habilitar TRIM**
   ```bash
   # Linux
   sudo systemctl enable fstrim.timer
   
   # Windows (automático si soporta)
   fsutil behavior query DisableDeleteNotify
   ```

2. **NO desfragmentar** (desgasta innecesariamente)
3. **Alineación de 4K** en particiones
4. **Over-provisioning:** Dejar 10-20% sin particionar

---

## 📐 Cálculo de Throughput en RAID

### Ejemplo: RAID 5 con 4 discos

**Datos:**
- 4 discos de 1TB @ 150 MB/s cada uno
- 1 disco para paridad

**Lectura:**
```
Throughput = 3 × 150 MB/s = 450 MB/s
(lee de 3 discos en paralelo)
```

**Escritura:**
```
Throughput ≈ 150-200 MB/s
(bottleneck por cálculo de paridad)
```

**Capacidad:**
```
Total = 3 × 1TB = 3TB
(n-1 discos útiles)
```

---

## Resumen de la Clase

| Concepto | Idea clave |
| ---------- | ------------ |
| **Disco** | Pistas, sectores, cabezales |
| **Tiempo de acceso** | Seek + latencia + transferencia |
| **Planificación** | FCFS, SSTF, SCAN, C-SCAN |
| **RAID** | Redundancia y rendimiento |

---

## Tarea

1. Comparar SSD vs HDD (3 diferencias técnicas)
2. Explicar por qué SCAN reduce el tiempo promedio
3. Investigar qué RAID usa un data center moderno

---

## Próxima Clase

### Clase 11: Implementación de Sistemas de Archivos

- Estructuras internas
- Inodos y bloques
- Ejemplo ext4

**¡Nos vemos!**


---


## 🔄 Algoritmos de Planificación de Disco

### 1. FCFS (First-Come, First-Served)

**Concepto:**
- Atiende las solicitudes en el orden en que llegan
- Más simple pero puede ser ineficiente

**Ejemplo:**
Cola de solicitudes: 98, 183, 37, 122, 14, 124, 65, 67
Posición inicial del cabezal: 53

```
Orden de atención: 53 → 98 → 183 → 37 → 122 → 14 → 124 → 65 → 67
Movimiento total: |98-53| + |183-98| + |183-37| + ... = 640 cilindros
```

---

### 2. SSTF (Shortest Seek Time First)

**Concepto:**
- Atiende primero la solicitud más cercana
- Reduce movimiento promedio
- **Problema:** Inanición (starvation)

**Ejemplo con misma cola:**
```
53 → 65 → 67 → 37 → 14 → 98 → 122 → 124 → 183
Movimiento total: 236 cilindros (63% menos que FCFS)
```

**⚠️ Problema de inanición:**
Si llegan continuamente solicitudes cerca del cabezal, las lejanas nunca se atienden.

---

### 3. SCAN (Algoritmo del Ascensor)

**Concepto:**
- El cabezal se mueve en una dirección hasta el final
- Luego invierte y va al otro extremo
- Atiende solicitudes en el camino

**Ejemplo:**
Dirección inicial: hacia arriba (mayor numeración)
```
53 → 65 → 67 → 98 → 122 → 124 → 183 → 199(fin) → 37 → 14
Movimiento total: 336 cilindros
```

**Ventaja:** Evita inanición, tiempo de espera más predecible

---

### 4. C-SCAN (Circular SCAN)

**Concepto:**
- Como SCAN pero solo atiende en una dirección
- Al llegar al final, salta al inicio sin atender
- Distribuye más equitativamente los tiempos de espera

**Ejemplo:**
```
53 → 65 → 67 → 98 → 122 → 124 → 183 → 199 → 0 → 14 → 37
```

---

### 5. LOOK y C-LOOK

**Diferencia con SCAN:**
- No va hasta el extremo del disco
- Solo hasta la última solicitud en esa dirección

**Ejemplo C-LOOK:**
```
53 → 65 → 67 → 98 → 122 → 124 → 183 (última solicitud) → 14 → 37
Movimiento: 153 cilindros (mejor que C-SCAN)
```

---

### 📊 Comparación de Algoritmos

| Algoritmo | Movimiento (cilindros) | Ventajas | Desventajas |
|-----------|------------------------|----------|-------------|
| **FCFS** | 640 | Simple, justo | Ineficiente |
| **SSTF** | 236 | Eficiente | Inanición posible |
| **SCAN** | 336 | Evita inanición | Favorece cilindros medios |
| **C-SCAN** | 382 | Tiempos uniformes | Más movimiento |
| **C-LOOK** | 153 | Más eficiente | Complejidad moderada |

---

### 💡 Algoritmo Usado en Sistemas Modernos

**Linux:** Usa **Deadline I/O Scheduler** y **CFQ** (Completely Fair Queueing)
- Combina varios algoritmos
- Considera también prioridades de procesos
- Optimizado para SSDs (no solo HDD)

**Windows:** Usa **SSTF mejorado** con prevención de inanición

---


---


## 💻 Actividad Práctica: Simulación de Algoritmos

### Ejercicio 1: Calcular Movimientos

**Situación:**
- Disco con 200 cilindros (0-199)
- Posición inicial cabezal: 50
- Cola de solicitudes: 82, 170, 43, 140, 24, 16, 190

**Tareas:**
1. Calcular movimiento total para FCFS
2. Calcular movimiento total para SSTF
3. Calcular movimiento total para SCAN (dirección: creciente)
4. ¿Qué algoritmo es más eficiente para este caso?

---

### Ejercicio 2: Análisis de Inanición

**Escenario:**
Usando SSTF, el cabezal está en 100 y hay solicitudes en: 50, 120
Cada 5ms llegan nuevas solicitudes en posiciones aleatorias entre 90-110

**Pregunta:**
¿La solicitud en 50 sufriría inanición? ¿Por qué?

---
### Tiempo estimado: 45 minutos

Implementar el algoritmo SSTF en Python:

```python
def sstf(posicion_inicial, solicitudes):
    movimiento_total = 0
    posicion_actual = posicion_inicial
    solicitudes_restantes = solicitudes.copy()
    orden = []
    
    while solicitudes_restantes:
        # Encontrar la más cercana
        mas_cercana = min(solicitudes_restantes, 
                         key=lambda x: abs(x - posicion_actual))
        
        # Calcular movimiento
        movimiento = abs(mas_cercana - posicion_actual)
        movimiento_total += movimiento
        
        # Actualizar estado
        posicion_actual = mas_cercana
        orden.append(mas_cercana)
        solicitudes_restantes.remove(mas_cercana)
    
---
### Tiempo estimado: 45 minutos

*(continuación...)*

    return movimiento_total, orden

solicitudes = [82, 170, 43, 140, 24, 16, 190]
total, orden = sstf(50, solicitudes)
print(f"Movimiento total: {total}")
print(f"Orden de atención: {orden}")
```


---
