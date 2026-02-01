# Teoría Expandida - Clase 2: Evolución y Componentes del SO

**IF0099 - Sistemas Operativos I**

---

## 1. Evolución Histórica de los SO

### Generación 0: Sin SO (1940-1950)

**Contexto:** Los primeros computadores (ENIAC, UNIVAC I) no tenían sistema operativo.

**Características:**
- **Programación:** Cables y switches físicos
- **Ejecución:** Un programa a la vez
- **Tamaño:** Ocupaban habitaciones completas (30 toneladas)
- **Costo:** Millones de dólares
- **Eficiencia:** CPU ociosa la mayor parte del tiempo

**Problemas clave:**
- Tiempo perdido reconectando cables para cada programa
- Errores humanos frecuentes
- Sin concepto de "software" como lo conocemos

---

### Primera Generación: Procesamiento por Lotes (1950-1965)

**Innovación:** Batch processing - automatizar el flujo de trabajos.

**Características:**
- **Tarjetas perforadas** como medio de entrada
- **Jobs encolados** para procesamiento secuencial
- **Operadores humanos** preparaban los lotes
- **Horas de turnaround** para resultados

**Sistemas importantes:**
- **GM-NAA I/O (1956):** Primer SO de producción (General Motors + IBM)
- **IBM OS/360 (1964):** Familia de SOs para diferentes hardware

**Problemas resueltos:**
- Automatización de preparación de trabajos
- Mejor uso de CPU (aún limitado)
- Detección de errores antes de ejecutar

**Limitaciones:**
- Sin interactividad (no se puede corregir en tiempo real)
- CPU espera E/S del siguiente job
- Debugging casi imposible

---

### Segunda Generación: Multiprogramación (1965-1980)

**Innovación clave:** Múltiples programas en RAM simultáneamente.

```
Sin Multiprogramación:        Con Multiprogramación:
CPU ejecuta A                 CPU ejecuta A
A hace E/S                    A hace E/S → CPU ejecuta B
CPU ociosa                    B hace E/S → CPU ejecuta C
                               C hace E/S → CPU vuelve a A
```

**Sistemas importantes:**
- **IBM OS/360 (1964):** Primer SO de "propósito general". Introdujo conceptos clave:
  - **Spooling:** Simultaneous Peripheral Operations On-Line - Permite que el SO prepare E/S de un job mientras se ejecuta otro
  - **JCL (Job Control Language):** Lenguaje de control para describir jobs al sistema
  - **Multiprogramación real:** Varios programas en RAM simultáneamente

> **¿Qué es Spooling?** El spooling permite que trabajos de E/S (como imprimir) se encolen para procesarse en segundo plano, sin que la CPU espere. Por ejemplo, múltiples usuarios pueden enviar documentos a imprimir simultáneamente; el SO los encola y los imprime uno por uno en segundo plano.

> **¿Qué es JCL?** El Job Control Language es un lenguaje especial que usan los operadores para describir los trabajos al sistema operativo. Por ejemplo: `//JOB NAME=REPORT,CLASS=A,MSG=SYSPRINT` le dice al sistema cómo procesar un trabajo.

- **MULTICS (1969):** Proyecto conjunto de Bell Labs, MIT y GE para crear un SO "universal". Falló por sobre-ingeniería (demasiado complejo, caro).
- **UNIX (1969):** Respuesta minimalista de Ken Thompson y Dennis Ritchie (de Bell Labs) al fracaso de MULTICS

**Innovaciones de UNIX:**
- **Escrito en C:** Primer SO portable (no ensamblador)
- **"Haz una cosa y hazla bien":** Pequeñas herramientas combinables
- **"Todo es un archivo":** Abstracción uniforme
- **Pipes:** Comunicación entre procesos (`ls | grep .txt`)

**Impacto de UNIX:**
```
UNIX (1969)
   ├─── Linux (1991) → Servidores, Android, IoT
   ├─── BSD → macOS, iOS
   ├─── Minix → Educación
   └─── Plan 9 → Go, 9P
```

---

### Tercera Generación: Tiempo Compartido (1970-1990)

**Innovación:** Time-sharing - múltiples usuarios interactivos simultáneos.

> **¿Qué es Time-Sharing?** El **tiempo compartido** es una técnica que permite a múltiples usuarios acceder simultáneamente a un computador. La CPU cambia rápidamente entre usuarios, dando a cada uno una "tajada" de tiempo (generalmente milisegundos). Los usuarios tienen la ilusión de uso exclusivo, aunque en realidad comparten la CPU.

**Concepto:** CPU dividida en "tajadas" de tiempo (quantum):
```
1 segundo = 100ms usuario 1 + 100ms usuario 2 + 100ms usuario 3 + ...
```

**Diferencia clave con multiprogramación:**
- **Multiprogramación:** Varios programas se alternan, pero uno puede esperar E/S
- **Time-sharing:** Varios **usuarios** interactivos se alternan, cada uno con su terminal

**Sistemas importantes:**
- **UNIX v4 (1973):** Introdujo pipes
- **BSD (1977):** Sockets (red)
- **VMS (1978):** Virtual Memory System en DEC VAX
  > **¿Qué es VMS?** El **Virtual Memory System** fue un SO innovador para computadores VAX de Digital Equipment Corporation. Introdujo el **clustering** (varios computadores actuando como uno) y un sistema de archivos muy robusto. VMS influyó fuertemente en Windows NT (diseñado por ex-ingenieros de DEC).

- **CP/M (1974):** SO para microprocesadores 8-bit de Intel y Zilog. Creado por Gary Kildall, se convirtió en el estándar para computadoras tempranas y fue la base de MS-DOS.

**Problemas resueltos:**
- Interactividad en tiempo real
- Múltiples usuarios simultáneos
- Debugging interactivo
- Respuesta inmediata

---

### Cuarta Generación: PCs y GUI (1980-2000)

**Hitos clave:**
| Año | Sistema | Impacto |
|-----|---------|---------|
| 1981 | MS-DOS | IBM PC, dominio empresarial |
| 1984 | Mac OS | Primera GUI comercial exitosa |
| 1991 | Linux | SO libre y abierto |
| 1995 | Windows 95 | GUI dominante en hogares |

**Transformación social:**
- Computadoras pasaron de empresas → hogares
- Programación pasó de expertos → cualquiera
- Costo: $5,000+ → $500

**La guerra de los SO:**
- **DOS:** Líder técnico, pero complejo
- **Mac:** GUI innovadora, pero hardware caro
- **Windows 95:** Unió GUI + compatibilidad → ganador masivo

---

### Quinta Generación: SO Modernos (2000-presente)

**Características:**
- **Multitarea real:** Múltiples núcleos, múltiples CPUs
- **Conectividad total:** Internet, redes 5G
- **Virtualización:** VMs, contenedores (Docker, KVM)
- **Cloud native:** Servicios on-demand (AWS, Azure, GCP)
- **Computación móvil:** Smartphones potentes

**Tendencias 2026+:**
- **AI-native OS:** Windows Copilot, Apple Intelligence
- **Container-first:** Kubernetes everywhere
- **Real-time OS:** Latencia ultrabaja (automotrización, VR/AR)
- **Edge computing:** Procesamiento distribuido

---

## 2. Componentes de un SO Moderno

### Modelo en Capas

```
┌─────────────────────────────────────────┐
│            APLICACIONES                 │ ← Usuario interactúa aquí
├─────────────────────────────────────────┤
│         UTILIDADES DEL SISTEMA          │
├─────────────────────────────────────────┤
│              SHELL                        │
│         (Intérprete de comandos/GUI)      │
├─────────────────────────────────────────┤
│         LLAMADAS AL SISTEMA (API)       │ ← Frontera crucial
├─────────────────────────────────────────┤
│              KERNEL                       │
│  ┌────────┬────────┬────────┬────────┐ │
│  │Procesos│Memoria │Archivos│  E/S   │ │
│  └────────┴────────┴────────┴────────┘ │
├─────────────────────────────────────────┤
│             HARDWARE                      │
└─────────────────────────────────────────┘
```

### El Kernel (Núcleo)

**Responsabilidades:**
- **Planificador:** Decide qué proceso ejecuta
- **Gestor de memoria:** Asigna RAM a procesos
- **Sistema de archivos:** Organiza datos en disco
- **Drivers E/S:** Habla con hardware
- **Gestor de procesos:** Crea, destruye procesos

**Tipos de kernel:**
| Tipo | Ventajas | Desventajas | Ejemplos |
|------|----------|-------------|----------|
| Monolítico | Rápido, directo | Complejo, crash total | Linux, DOS |
| Microkernel | Seguro, flexible | Lento (IPC) | Minix, QNX |
| Híbrido | Balance | Complejo | macOS, Windows NT |

### El Shell

**Dos tipos:**
1. **CLI:** Comandos de texto (bash, zsh, PowerShell)
2. **GUI:** Interfaz gráfica (Explorador Windows, Finder)

**Importante:** El shell NO es el kernel. Es un programa en modo usuario que solicita servicios al kernel.

---

## 3. Modo Usuario vs Modo Kernel

### Protection Rings (Anillos de Protección)

```
Ring 0: MODO KERNEL (Kernel, drivers, acceso total)
Ring 1: (Reservado)
Ring 2: (Reservado)
Ring 3: MODO USUARIO (Aplicaciones, acceso restringido)
```

### Diferencias Clave

| Aspecto | Modo Usuario (Ring 3) | Modo Kernel (Ring 0) |
|---------|----------------------|---------------------|
| **Aplicaciones** | Chrome, VS Code, juegos | Kernel, drivers |
| **Acceso hardware** | ❌ Solo vía system calls | ✅ Acceso directo |
| **Memoria** | Solo su espacio | Toda la memoria |
| **Si falla** | Solo la aplicación muere | Crash del sistema |
| **Instrucciones prohibidas** | IN, OUT, CLI, STI, HLT | Todas permitidas |

### Transición entre Modos

**System call flow:**
```
Usuario (Ring 3)
  → syscall/int 0x80 (TRAP)
    → Kernel (Ring 0)
      → Verifica permisos
      → Ejecuta operación
      → IRET (return)
    → Usuario (Ring 3)
```

---

## Conceptos Clave

| Concepto | Definición |
|----------|------------|
| **Batch processing** | Procesamiento automático de trabajos encolados |
| **Spooling** | Simultaneous Peripheral Operations On-Line - E/S en segundo plano |
| **JCL** | Job Control Language - Lenguaje para describir jobs |
| **Multiprogramación** | Múltiples programas en RAM simultáneamente |
| **Time-sharing** | Usuarios interactivos comparten CPU mediante tajadas de tiempo |
| **Virtual Memory (VMS)** | SO innovador con clustering y robustez (influyó Windows NT) |
| **Kernel** | Núcleo del SO, corre en modo privilegiado |
| **Shell** | Intérprete de comandos, puente usuario-kernel |
| **System call** | Puente controlada entre usuario y kernel |
| **Protection rings** | Niveles de privilegio del procesador (0-3) |
| **Mode transition** | Cambio de modo usuario → kernel (TRAP/IRET) |

> **Error común a evitar:** Confundir multiprogramación con time-sharing.
> - **Multiprogramación** = varios programas simultáneos (uno puede estar esperando)
> - **Time-sharing** = varios **usuarios** simultáneos (todos interactivos)

---

**Última actualización**: 2026-02-01
