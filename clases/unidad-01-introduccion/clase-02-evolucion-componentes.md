---
marp: true
theme: default
paginate: true
header: 'IF0099 - Sistemas Operativos I | Unidad 1'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
---

<!--
[2026-01-31] - Clase enriquecida con infografías

IMÁGENES GENERADAS:
- so-evolucion-timeline.png: Línea de tiempo de la evolución de SO
- so-componentes-arquitectura.png: Diagrama de arquitectura en capas (Hardware, Kernel, Servicios, Apps)
-->

# Clase 2: Evolución Histórica y Componentes del SO
## De las tarjetas perforadas a la nube

**IF0099 - Sistemas Operativos I**
*4° Semestre - Ingeniería Informática*

---

## Objetivos de la Clase

Al finalizar esta clase, el estudiante será capaz de:

1. **Describir** la evolución histórica de los sistemas operativos
2. **Identificar** las generaciones de sistemas operativos
3. **Explicar** los componentes principales de un SO
4. **Diferenciar** modo usuario vs modo kernel

**Duración:** 90 minutos

---

## Agenda

1. Generación 0: Sin SO (1940s) - 10 min
2. Primera a Cuarta Generación - 25 min
3. Componentes del SO moderno - 25 min
4. Modo Usuario vs Modo Kernel - 20 min
5. Actividad práctica - 10 min

---

## Línea de Tiempo de los SO

![Evolución de los Sistemas Operativos](../../assets/infografias/so-evolucion-timeline.png)

---

## Generación 0: Sin Sistema Operativo (1940-1950)

### Características
- **ENIAC, UNIVAC**: Primeras computadoras
- Programación con **cables y switches**
- **Una persona** = un programa = toda la máquina
- Sin concepto de "software de sistema"

```
┌─────────────────────────────────┐
│    PROGRAMADOR                  │
│         │                       │
│         ▼                       │
│  ┌─────────────┐               │
│  │  HARDWARE   │ (directo)     │
│  └─────────────┘               │
└─────────────────────────────────┘
```

**Problema:** Desperdicio de tiempo y recursos

---

## Primera Generación: Procesamiento por Lotes (1950-1965)

### Batch Processing

```
┌─────────────────────────────────────────┐
│ 1. Programador escribe código en papel  │
│              ↓                          │
│ 2. Operador perfora tarjetas            │
│              ↓                          │
│ 3. Tarjetas se acumulan en "lote"       │
│              ↓                          │
│ 4. Computador procesa todo el lote      │
│              ↓                          │
│ 5. Resultados en impresora (horas después)│
└─────────────────────────────────────────┘
```

### Primer SO: **GM-NAA I/O** (1956) - General Motors

---

## Segunda Generación: Multiprogramación (1965-1980)

### Múltiples programas en memoria

```
┌────────────────────────────────┐
│         MEMORIA RAM            │
├────────────────────────────────┤
│  Sistema Operativo             │
├────────────────────────────────┤
│  Programa A (esperando E/S)    │
├────────────────────────────────┤
│  Programa B (ejecutando)       │ ← CPU
├────────────────────────────────┤
│  Programa C (esperando E/S)    │
└────────────────────────────────┘
```

### Sistemas importantes
- **IBM OS/360** (1964)
- **MULTICS** (1969) - Precursor de UNIX

---

## Nacimiento de UNIX (1969)

### Ken Thompson y Dennis Ritchie - Bell Labs

```
      ┌─────────────────┐
      │    MULTICS      │ (muy complejo)
      │    (fallido)    │
      └────────┬────────┘
               │ Thompson y Ritchie
               │ simplifican
               ▼
      ┌─────────────────┐
      │     UNIX        │
      │ "Una cosa bien" │
      └─────────────────┘
```

### Innovaciones de UNIX:
- Escrito en **C** (portable)
- Filosofía: "Haz una cosa y hazla bien"
- Todo es un archivo
- Base de Linux, macOS, Android

---

## Tercera Generación: Tiempo Compartido (1970-1990)

### Time-Sharing: Múltiples usuarios simultáneos

```
Usuario 1 ──┐
            │
Usuario 2 ──┼──→ [SO Time-Sharing] ──→ [CPU]
            │         │
Usuario 3 ──┘    Reparte tiempo
                 en "tajadas"
```

### Sistemas importantes:
- **UNIX** (1969-presente)
- **VMS** (DEC)
- **CP/M** (microcomputadores)

---

## Cuarta Generación: Computadoras Personales (1980-2000)

### La era del PC

| Año | Sistema | Importancia |
|-----|---------|-------------|
| 1981 | MS-DOS | IBM PC |
| 1984 | Mac OS | Primera GUI comercial exitosa |
| 1985 | Windows 1.0 | Intento de GUI sobre DOS |
| 1991 | **Linux** | SO libre y abierto |
| 1995 | Windows 95 | GUI dominante |

> 💡 **Prompt para infografía:** "Crear línea de tiempo visual de sistemas operativos desde 1970 hasta 2000, mostrando UNIX, MS-DOS, Mac OS, Windows y Linux con sus logos y fechas clave"

---

## Quinta Generación: SO Modernos (2000-presente)

### Características actuales:
- **Multitarea real** (múltiples núcleos)
- **Conectividad** (redes, Internet)
- **Seguridad** (permisos, encriptación)
- **Virtualización** (VMs, contenedores)
- **Cloud computing** (SO en la nube)

### Sistemas actuales (2026):
- Windows 11
- macOS Sequoia
- Ubuntu 24.04 LTS
- Android 16
- iOS 19

---

## Componentes de un SO Moderno

![Arquitectura del Sistema Operativo](../../assets/infografias/so-componentes-arquitectura.png)

---

### Representación ASCII:
```
┌─────────────────────────────────────────────────┐
│                  APLICACIONES                   │
├─────────────────────────────────────────────────┤
│              UTILIDADES DEL SISTEMA             │
│    (Administrador archivos, Terminal, etc.)     │
├─────────────────────────────────────────────────┤
│                    SHELL                        │
│         (Intérprete de comandos / GUI)          │
├─────────────────────────────────────────────────┤
│            LLAMADAS AL SISTEMA (API)            │
├─────────────────────────────────────────────────┤
│                   KERNEL                        │
│  ┌──────────┬──────────┬──────────┬──────────┐ │
│  │ Gestor   │ Gestor   │ Sistema  │ Gestor   │ │
│  │ Procesos │ Memoria  │ Archivos │   E/S    │ │
│  └──────────┴──────────┴──────────┴──────────┘ │
├─────────────────────────────────────────────────┤
│                   HARDWARE                      │
└─────────────────────────────────────────────────┘
```

---

## El Kernel (Núcleo)

### El corazón del Sistema Operativo

```
         Aplicaciones
              │
              ▼
    ┌─────────────────┐
    │     KERNEL      │ ← Siempre en memoria
    │                 │ ← Código privilegiado
    │ - Planificador  │ ← Acceso a hardware
    │ - Memoria       │
    │ - Drivers       │
    │ - Sistema arch. │
    └─────────────────┘
              │
              ▼
         Hardware
```

### Tipos de Kernel:
- **Monolítico**: Linux, Windows
- **Microkernel**: Minix, QNX
- **Híbrido**: macOS (XNU), Windows NT

---

## El Shell

### Interfaz entre usuario y kernel

```
┌────────────────────────────────────────┐
│            USUARIO                     │
└───────────────┬────────────────────────┘
                │ escribe comando
                ▼
┌────────────────────────────────────────┐
│             SHELL                      │
│  $ ls -la /home                        │
│                                        │
│  - Interpreta el comando               │
│  - Llama al kernel                     │
│  - Muestra resultado                   │
└───────────────┬────────────────────────┘
                │ llamada al sistema
                ▼
┌────────────────────────────────────────┐
│            KERNEL                      │
└────────────────────────────────────────┘
```

### Shells populares: **bash**, zsh, PowerShell, fish

---

## Llamadas al Sistema (System Calls)

### La API del Sistema Operativo

```c
// Ejemplo: Abrir un archivo
int fd = open("/home/user/archivo.txt", O_RDONLY);

// El programa NO accede al disco directamente
// Pide al kernel que lo haga por él
```

### Categorías de system calls:

| Categoría | Ejemplos |
|-----------|----------|
| Procesos | fork(), exec(), exit(), wait() |
| Archivos | open(), read(), write(), close() |
| Dispositivos | ioctl(), read(), write() |
| Información | getpid(), time(), uname() |
| Comunicación | pipe(), socket(), send() |

---

## Modo Usuario vs Modo Kernel

### Dos niveles de privilegio

```
┌─────────────────────────────────────────────┐
│           MODO USUARIO (Ring 3)             │
│                                             │
│  - Aplicaciones normales                    │
│  - NO puede acceder hardware directamente   │
│  - Memoria limitada                         │
│  - Si falla, solo muere la aplicación       │
└──────────────────┬──────────────────────────┘
                   │ System Call
                   ▼
┌─────────────────────────────────────────────┐
│           MODO KERNEL (Ring 0)              │
│                                             │
│  - Acceso total al hardware                 │
│  - Toda la memoria accesible                │
│  - Código del SO y drivers                  │
│  - Si falla = CRASH del sistema             │
└─────────────────────────────────────────────┘
```

---

## ¿Por qué separar modos?

### Seguridad y estabilidad

**Sin separación:**
```
Programa malicioso → Accede a toda la memoria → DESASTRE
```

**Con separación:**
```
Programa malicioso → Pide al kernel → Kernel DENIEGA → Sistema seguro
```

### Ejemplo real:
- Un programa en modo usuario NO puede:
  - Apagar el computador directamente
  - Leer memoria de otro programa
  - Acceder al disco sin permiso

---

## Transición entre modos

```
┌─────────────────────────────────────────────────┐
│                MODO USUARIO                     │
│                                                 │
│   programa ejecuta: read(fd, buffer, 100)       │
│                         │                       │
└─────────────────────────┼───────────────────────┘
                          │ TRAP (interrupción)
                          ▼
┌─────────────────────────────────────────────────┐
│                MODO KERNEL                      │
│                                                 │
│   1. Verifica permisos                          │
│   2. Lee datos del disco                        │
│   3. Copia datos a buffer del usuario           │
│   4. Retorna al modo usuario                    │
│                         │                       │
└─────────────────────────┼───────────────────────┘
                          │ RETURN
                          ▼
┌─────────────────────────────────────────────────┐
│                MODO USUARIO                     │
│   programa continúa con datos en buffer         │
└─────────────────────────────────────────────────┘
```

---

## Actividad Práctica (10 min)

### En parejas, investiguen en su computador:

1. **Windows**: Abran PowerShell y ejecuten:
   ```powershell
   Get-ComputerInfo | Select-Object OsName, OsVersion
   ```

2. **Linux/Mac**: Abran Terminal y ejecuten:
   ```bash
   uname -a
   cat /etc/os-release  # Solo Linux
   ```

3. **Discutan**: ¿Qué información les da cada comando?

---

## Resumen de la Clase

| Generación | Época | Característica |
|------------|-------|----------------|
| 0 | 1940s | Sin SO |
| 1 | 1950s | Procesamiento por lotes |
| 2 | 1960s | Multiprogramación |
| 3 | 1970s | Tiempo compartido |
| 4 | 1980s | PCs y GUI |
| 5 | 2000s+ | Modernos, cloud, móviles |

### Componentes: Kernel + Shell + Utilidades + System Calls

---

## Tarea para próxima clase

### Preparación para laboratorio

1. **Descargar** VirtualBox: https://www.virtualbox.org/
2. **Descargar** Ubuntu 24.04 LTS ISO: https://ubuntu.com/download
3. **Leer** el manual del Laboratorio 1

**En la próxima clase:** Instalaremos Linux en máquina virtual

---

## Próxima Clase

### Clase 3: Concepto de Proceso

- ¿Qué es un proceso?
- Diferencia entre proceso y programa
- PCB (Process Control Block)
- Estados de un proceso

**¡Nos vemos!**
