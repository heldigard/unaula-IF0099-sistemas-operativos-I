---
marp: true
theme: default
paginate: true
header: 'IF0099 - Sistemas Operativos I | Unidad 7'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
---

<!--
IMÁGENES GENERADAS:
- clase-10-dma.png: Infografía sobre DMA y gestión de E/S
-->

# Clase 10: Gestión de Entrada/Salida
## Dispositivos, Controladores y DMA

**IF0099 - Sistemas Operativos I**
*4° Semestre - Ingeniería Informática*

![DMA - Acceso Directo a Memoria](../../assets/infografias/clase-10-dma.png)

---

## Objetivos de la Clase

Al finalizar esta clase, el estudiante será capaz de:

1. **Clasificar** los dispositivos de E/S
2. **Explicar** el rol de los controladores (drivers)
3. **Describir** las técnicas de E/S: polling, interrupciones, DMA
4. **Analizar** el subsistema de E/S del kernel

**Duración:** 90 minutos

---

## Diversidad de Dispositivos de E/S

```
┌─────────────────────────────────────────────────────────────┐
│                  DISPOSITIVOS DE E/S                        │
├─────────────────────────────────────────────────────────────┤
│  BLOQUE              │  CARÁCTER              │  RED        │
│  (almacenamiento)    │  (stream)              │             │
├──────────────────────┼────────────────────────┼─────────────┤
│  • Disco duro (HDD)  │  • Teclado             │  • Ethernet │
│  • SSD               │  • Mouse               │  • WiFi     │
│  • USB flash         │  • Terminal            │  • Bluetooth│
│  • CD/DVD            │  • Impresora           │             │
│                      │  • Puerto serial       │             │
└──────────────────────┴────────────────────────┴─────────────┘
```

**Diferencia clave:**
- **Bloque:** Acceso aleatorio, transferencia en bloques (512B, 4KB)
- **Carácter:** Acceso secuencial, transferencia byte a byte

---

## Arquitectura de E/S

```
┌─────────────────────────────────────────────────────────────┐
│                    APLICACIÓN                               │
│                   (read/write)                              │
├─────────────────────────────────────────────────────────────┤
│                  SISTEMA DE ARCHIVOS                        │
│                (ext4, NTFS, FAT32)                          │
├─────────────────────────────────────────────────────────────┤
│                 SUBSISTEMA DE E/S                           │
│           (buffering, caching, scheduling)                  │
├─────────────────────────────────────────────────────────────┤
│                 DEVICE DRIVERS                              │
│         (código específico del dispositivo)                 │
├─────────────────────────────────────────────────────────────┤
│              CONTROLADORES HARDWARE                         │
│                (chip en el dispositivo)                     │
├─────────────────────────────────────────────────────────────┤
│                   DISPOSITIVO                               │
│                 (disco, teclado, etc.)                      │
└─────────────────────────────────────────────────────────────┘
```

---

## Controlador de Hardware vs Driver

```
             CONTROLADOR HARDWARE           DRIVER (SOFTWARE)
          ┌─────────────────────┐       ┌─────────────────────┐
          │    Chip/Circuito    │       │   Código en kernel  │
          │    en dispositivo   │       │   del SO            │
          ├─────────────────────┤       ├─────────────────────┤
          │  • Registros        │       │  • Lee/escribe      │
          │  • Buffer interno   │       │    registros        │
          │  • Señales elect.   │       │  • Maneja IRQ       │
          │                     │       │  • Traduce comandos │
          └──────────┬──────────┘       └──────────┬──────────┘
                     │                             │
                     └──────────┬──────────────────┘
                                │
                                ▼
                       COMUNICACIÓN
                     (puerto I/O o MMIO)
```

---

## Comunicación CPU-Dispositivo

### Puertos de E/S (Port-Mapped I/O)

```
CPU usa instrucciones especiales: IN, OUT
Espacio de direcciones separado

IN AL, 0x60    ; Lee del puerto 0x60 (teclado)
OUT 0x60, AL   ; Escribe al puerto 0x60
```

### Memory-Mapped I/O (MMIO)

```
Registros del dispositivo mapeados a memoria
Se acceden como si fueran RAM

// Escribir al dispositivo
*(volatile uint32_t*)0xFFFF0000 = valor;

// Leer del dispositivo
dato = *(volatile uint32_t*)0xFFFF0000;
```

---

## Técnicas de E/S

### 1. Polling (Encuesta)

```c
// CPU pregunta constantemente si hay datos
while (1) {
    if (dispositivo_listo()) {
        dato = leer_dispositivo();
        procesar(dato);
    }
    // CPU ocupada esperando!
}
```

```
CPU     ──●──●──●──●──●──●──●──●──●──●──●──●──●──●──●
          P  P  P  P  P  P  D  P  P  P  P  P  P  P  P
          o  o  o  o  o  o  a  o  o  o  o  o  o  o  o
          l  l  l  l  l  l  t  l  l  l  l  l  l  l  l
          l  l  l  l  l  l  o  l  l  l  l  l  l  l  l

❌ Desperdicio de ciclos de CPU
✅ Simple de implementar
```

---

## Técnicas de E/S (cont.)

### 2. Interrupciones

```
1. Proceso solicita E/S
2. SO inicia operación en dispositivo
3. SO pone proceso en espera
4. CPU ejecuta otros procesos
5. Dispositivo genera INTERRUPCIÓN cuando termina
6. SO atiende interrupción
7. SO despierta al proceso original
```

```
CPU    ──●──●──●──●──●──────────────────●──●──●──●──
        P1 P1 P2 P2 P2                  P1 P1 P1 P1
                        │ proceso 1 esperando │
                        └────────────────────-┘
                                ↑
                            IRQ del disco
```

✅ CPU no desperdicia ciclos
✅ Mejor uso de recursos

---

## Interrupciones: Flujo Detallado

```
   CPU                         DISPOSITIVO
    │                              │
    │──────① solicita E/S ────────→│
    │                              │
    │   ejecuta otros procesos     │ trabajando...
    │                              │
    │←──② IRQ (interrupción)───────│ ¡listo!
    │                              │
    ├── ③ Guarda contexto actual   │
    │                              │
    ├── ④ Ejecuta ISR (handler)    │
    │      (lee datos, marca listo)│
    │                              │
    ├── ⑤ Restaura contexto        │
    │                              │
    │   continúa proceso original  │
```

**ISR** = Interrupt Service Routine

---

## Técnicas de E/S (cont.)

### 3. DMA (Direct Memory Access)

```
Sin DMA:                          Con DMA:
CPU lee dato del disco            Controlador DMA
CPU escribe dato en RAM           transfiere bloques
CPU lee dato del disco            directamente
CPU escribe dato en RAM           disco → RAM
... (miles de veces)              CPU hace otras cosas

     DISCO                             DISCO
       │                                 │
       ▼                                 │
     [CPU]──→ RAM                    DMA ──────→ RAM
  ↑        ↑                             │
  │        │                             ▼
  └────────┘                         [CPU] IRQ al final
  Involucra CPU                      CPU libre!
  en cada byte
```

---

## DMA: Flujo de Operación

```
┌─────────────────────────────────────────────────────────────┐
│  1. CPU programa el controlador DMA:                        │
│     - Dirección fuente (disco)                              │
│     - Dirección destino (RAM)                               │
│     - Cantidad de bytes                                     │
│     - Dirección de transferencia                            │
│                                                             │
│  2. DMA toma control del bus                                │
│     (cycle stealing o burst mode)                           │
│                                                             │
│  3. Controlador DMA transfiere datos                        │
│     Disco → Controlador DMA → RAM                           │
│                                                             │
│  4. DMA genera interrupción cuando termina                  │
│                                                             │
│  5. CPU procesa los datos ya en memoria                     │
└─────────────────────────────────────────────────────────────┘
```

---

## Comparación de Técnicas

| Aspecto | Polling | Interrupciones | DMA |
|---------|---------|----------------|-----|
| **Uso de CPU** | Alto (espera activa) | Bajo | Muy bajo |
| **Complejidad** | Simple | Media | Alta |
| **Latencia** | Baja | Media | Baja |
| **Ideal para** | Dispositivos rápidos | Dispositivos lentos | Transferencias grandes |
| **Hardware extra** | No | Controlador IRQ | Controlador DMA |

---

## Subsistema de E/S del Kernel

### Servicios proporcionados

```
┌─────────────────────────────────────────────────────────────┐
│                 SUBSISTEMA DE E/S                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  BUFFERING          CACHING           SPOOLING              │
│  ┌─────────┐        ┌─────────┐       ┌─────────┐          │
│  │ Buffer  │        │ Cache   │       │  Cola   │          │
│  │ temporal│        │ copia   │       │ de      │          │
│  │ para    │        │ para    │       │ trabajos│          │
│  │ vel.    │        │ acceso  │       │ (print) │          │
│  │ diferent│        │ rápido  │       │         │          │
│  └─────────┘        └─────────┘       └─────────┘          │
│                                                             │
│  SCHEDULING DE E/S          RESERVACIÓN DE DISPOSITIVOS     │
│  (ej: algoritmos de disco)  (acceso exclusivo)              │
└─────────────────────────────────────────────────────────────┘
```

---

## Buffering

### Por qué es necesario

```
Productor (disco) velocidad: 100 MB/s
Consumidor (red) velocidad: 10 MB/s

Sin buffer:                    Con buffer:
┌──────┐    ┌──────┐          ┌──────┐  ┌────────┐  ┌──────┐
│Disco │───→│ Red  │          │Disco │→ │ Buffer │→ │ Red  │
│100MB/s    │10MB/s│          │100MB/s  │ (RAM)  │  │10MB/s│
└──────┘    └──────┘          └──────┘  └────────┘  └──────┘
                               
Disco espera a red!            Disco llena buffer,
                               red consume a su ritmo
```

**Double buffering:** Dos buffers alternados para E/S continua

---

## Caching

### Cache de disco (Page Cache en Linux)

```
LECTURA:
┌──────────────────────────────────────────────────────────┐
│  1. Aplicación pide leer bloque 1000                     │
│  2. SO busca en page cache (RAM)                         │
│     ├── Si está (cache hit) → devuelve inmediatamente    │
│     └── Si no está (cache miss):                         │
│         a. Lee del disco                                 │
│         b. Guarda copia en cache                         │
│         c. Devuelve a la aplicación                      │
└──────────────────────────────────────────────────────────┘

ESCRITURA (write-back):
┌──────────────────────────────────────────────────────────┐
│  1. Aplicación escribe datos                             │
│  2. SO escribe en cache (marca como "dirty")             │
│  3. Luego (async), SO escribe al disco                   │
│     - Al cerrar archivo                                  │
│     - Periódicamente (pdflush/bdflush)                   │
│     - sync/fsync fuerza escritura                        │
└──────────────────────────────────────────────────────────┘
```

---

## Spooling (Print Spooler)

```
              Aplicaciones
                │  │  │
                ▼  ▼  ▼
           ┌───────────────┐
           │    SPOOLER    │
           │ ┌───────────┐ │
           │ │  Cola de  │ │
           │ │  trabajos │ │
           │ │  ┌─────┐  │ │
           │ │  │Job 1│  │ │
           │ │  │Job 2│  │ │
           │ │  │Job 3│  │ │
           │ │  └─────┘  │ │
           │ └───────────┘ │
           └───────┬───────┘
                   │
                   ▼
             ┌──────────┐
             │IMPRESORA │
             │(exclusiva)│
             └──────────┘
```

✅ Múltiples usuarios pueden "imprimir" simultáneamente
✅ Cola gestionada con prioridades

---

## Planificación de Disco

### Problema: Minimizar tiempo de búsqueda

```
Solicitudes de cilindros: 98, 183, 37, 122, 14, 124, 65, 67
Cabezal en: 53
Cilindros: 0-199

FCFS (First Come First Served):
53 → 98 → 183 → 37 → 122 → 14 → 124 → 65 → 67
Movimiento total: 45+85+146+85+108+110+59+2 = 640 cilindros

SSTF (Shortest Seek Time First):
53 → 65 → 67 → 37 → 14 → 98 → 122 → 124 → 183
Movimiento total: 12+2+30+23+84+24+2+59 = 236 cilindros

SCAN (Elevador):
53 → 37 → 14 → 0 → 65 → 67 → 98 → 122 → 124 → 183
Movimiento total: 236 cilindros (pero más justo)
```

---

## Algoritmo SCAN (Elevador)

```
Cilindros: 0 ─────────────────────────────────────── 199
                                                      
SCAN: Cabeza se mueve en una dirección hasta el final,
      luego invierte.

     ↓ inicio (53)
     │
 0 ──┼─14──37────53──65─67───98────122─124─────183── 199
     │  ↑   ↑          ↑  ↑    ↑      ↑   ↑      ↑
     └──1───2──────────3──4────5──────6───7──────8
     
Orden de servicio: 37, 14, 0 (borde), 65, 67, 98, 122, 124, 183

Como un elevador: sube hasta arriba, luego baja
```

---

## Actividad Práctica (10 min)

### En parejas:

**Dado:**
- Cola de cilindros: 95, 180, 34, 119, 11, 123, 62, 64
- Cabezal inicialmente en: 50
- Rango de cilindros: 0-199

**Calcular movimiento total de cabezal para:**
1. FCFS
2. SSTF
3. SCAN (dirección inicial: hacia 0)

---

## Comandos para Explorar E/S en Linux

```bash
# Ver dispositivos de bloque
lsblk

# Ver información de discos
sudo fdisk -l

# Estadísticas de E/S
iostat -x 1

# Ver interrupciones
cat /proc/interrupts

# Ver dispositivos PCI
lspci

# Ver módulos (drivers) cargados
lsmod

# Ver buffer cache
free -h
```

---

## Resumen de la Clase

| Concepto | Descripción |
|----------|-------------|
| **Dispositivo bloque** | Acceso aleatorio, bloques (disco) |
| **Dispositivo carácter** | Acceso secuencial, bytes (teclado) |
| **Polling** | CPU pregunta constantemente |
| **Interrupciones** | Dispositivo avisa cuando está listo |
| **DMA** | Transferencia directa disco→RAM |
| **Buffering** | Compatibilizar velocidades |
| **Caching** | Copia en RAM para acceso rápido |

---

## Próxima Clase

### Clase 10: Protección y Seguridad

- Dominios de protección
- Matriz de acceso
- Control de acceso en Linux/Windows
- Amenazas y mecanismos de defensa

**¡Nos vemos!**
