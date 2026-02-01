# Referencias - Clase 2: Evolución y Componentes del SO

**IF0099 - Sistemas Operativos I**

---

## Bibliografía Histórica

### Libros Fundamentales

1. **Ritchie, Dennis M.; Thompson, Ken.** "The UNIX Time-Sharing System".
   - *Bell System Technical Journal*, 1978.
   - **Importancia:** Paper fundacional que describe UNIX
   - **Relevancia:** Base de Linux, macOS, y casi todos los SO modernos

2. **Tanenbaum, Andrew S.** *Modern Operating Systems*. 5th Edition.
   - Pearson, 2024.
   - **Capítulo 1:** Introduction - Historia y evolución
   - **Capítulo 2:** OS Structure - Componentes y arquitectura

3. **Silberschatz, Abraham; Galvin, Peter B.; Gagne, Greg.** *Operating System Concepts*.
   - 10th Edition, Wiley, 2018.
   - **Part 1:** Overview - Historia y conceptos básicos

4. **Salus, Peter H.** *A Quarter Century of UNIX*.
   - *UNIX Review*, 1994.
   - **Importancia:** Recopila historias de los creadores de UNIX

### Artículos y Papers Clásicos

| Paper | Autor | Año | Importancia |
|-------|-------|-----|-------------|
| "The UNIX Time-Sharing System" | Ritchie, Thompson | 1978 | Base de UNIX |
| "Structure of the THE-Multiprogramming System" | Dijkstra | 1968 | Arquitectura por capas |
| "On the Design of UNIX for Large-Scale Applications" | Ritchie | 1974 | Portabilidad y C |

---

## Recursos Online

### Documentación Histórica

| Recurso | URL | Descripción |
|---------|-----|-------------|
| **UNIX History** | https://www.bell-labs.com/usr/dmr/www/ | Archivos históricos de Dennis Ritchie |
| **The UNIX Heritage Society** | https://www.tuhs.org/ | Preserva SO históricos |
| **Computer History Museum** | https://computerhistory.org/ | Fotos y artefactos históricos |

### Documentación Técnica

| Recurso | URL | Descripción |
|---------|-----|-------------|
| **Linux Kernel Docs** | https://www.kernel.org/doc/html/latest/ | Documentación oficial del kernel |
| **Bash Manual** | https://www.gnu.org/software/bash/manual/ | Manual completo de bash |
| **POSIX Specification** | https://pubs.opengroup.org/onlinepubs/9699919799/ | Estándar IEEE 1003.1 |

### Tutoriales y Guías

| Recurso | URL | Descripción |
|---------|-----|-------------|
| **Beej's Guide to Unix IPC** | https://beej.us/guide/bgipc/ | Guía de procesos, pipes, signals |
| **Linux Journey** | https://linuxjourney.com/ | Tutorial interactivo de Linux |
| **OverTheWire: Bandit** | https://overthewire.org/wargames/bandit/ | Juego para aprender seguridad Linux |
| **Linux From Scratch** | https://www.linuxfromscratch.org/ | Construir Linux desde cero |

---

## Videos y Cursos

### Cursos Universitarios

| Curso | Plataforma | Duración | Nivel |
|-------|-----------|----------|-------|
| **CS162: Operating Systems** | UC Berkeley (YouTube) | ~40 horas | Avanzado |
| **OSTEP: Operating Systems: Three Easy Pieces** | Remzi Arpaci-Dusseau | Libro + videos | Intermedio |
| **XV6: a simple Unix teaching OS** | MIT | ~10 horas | Principiante |

### Canales de YouTube

| Canal | Enfoque | URL |
|-------|--------|-----|
| **Systems with Gautham** | Explicaciones de SO | https://youtube.com/@systemswithgautham |
| **Low Level Learning** | Programación de bajo nivel | https://youtube.com/@LowLevelLearning |
| **Corey Schafer** | Tutoriales técnicos | https://youtube.com/@coreyschafer |

---

## Referencias de System Calls

### POSIX System Calls

| Categoría | System Calls | Man Page |
|-----------|-------------|----------|
| **Procesos** | `fork()`, `exec()`, `wait()`, `exit()` | `man 2 fork` |
| **Archivos** | `open()`, `read()`, `write()`, `close()` | `man 2 open` |
| **Directorios** | `mkdir()`, `rmdir()`, `opendir()`, `readdir()` | `man 2 opendir` |
| **Información** | `getpid()`, `getuid()`, `uname()` | `man 2 uname` |

### Ver Man Pages en Tu Sistema

```bash
# Ver man page de una system call específica
man 2 fork

# Buscar man pages por palabra clave
man -k process

# Listar todas las secciones de system calls
apropos process
```

---

## Comandos de Referencia Rápida

### Información del Sistema

```bash
uname -a                 # Información del kernel y hardware
hostname                 # Nombre del host
whoami                   # Usuario actual
id                       # UID, GID y grupos
uptime                   # Tiempo de actividad del sistema
```

### Información de Hardware

```bash
lscpu                     # Información detallada de CPU
lsblk                     # Dispositivos de bloque
lsusb                     # Dispositivos USB
lspci                     # Dispositivos PCI
free -h                   # Uso de memoria
df -h                     # Espacio en disco
```

### Procesos

```bash
ps aux                    # Todos los procesos
top                      # Procesos en tiempo real
htop                     # Versión mejorada de top
pstree                   # Árbol de procesos
pgrep nombre              # Buscar proceso por nombre
```

### Archivos y Directorios

```bash
pwd                       # Directorio actual
ls -la                    # Listar detallado
find /path -name "*.txt"  # Buscar archivos
du -sh /path             # Tamaño de directorio
file archivo              # Tipo de archivo
stat archivo             # Metadatos completos
```

---

## Estándares Importantes

### POSIX (IEEE 1003.1)

- **Qué es:** Estándar para compatibilidad entre sistemas tipo Unix
- **Por qué importa:** Tu código compilado en Linux funciona en macOS, *BSD, etc.
- **System calls POSIX:** `fork()`, `open()`, `read()`, `write()`, `socket()`, etc.

### Filesystem Hierarchy Standard (FHS)

- **Qué es:** Estándar que define estructura de directorios Linux
- **Directorios clave:**
  - `/bin`: Comandos esenciales
  - `/etc`: Configuración del sistema
  - `/home`: Directorios de usuarios
  - `/proc`: Sistema de archivos virtual
  - `/var`: Datos variables (logs, spool)

### System V vs BSD

| Aspecto | System V | BSD |
|--------|---------|-----|
| **Origen** | AT&T Bell Labs | UC Berkeley |
| **IPC** | Msg queues, semáforos compartidos | Sockets, pipes |
| **PS** | `ps -elf` | `ps aux` |
| **Startup** | System V init scripts | BSD init scripts |
| **Influencia** | Solaris, AIX, Linux | macOS, FreeBSD |

---

## Para Profundizar

### Libros Recomendados

1. **"The Art of Unix Programming"** - Eric Raymond
   - Filosofía UNIX y cultura hacker

2. **"The Design of the UNIX Operating System"** - Maurice Bach
   - Diseño interno del sistema

3. **"Linux Kernel Development"** - Robert Love
   - Desarrollo del kernel Linux

4. **"UNIX and Linux System Administration Handbook"** - Nemeth et al.
   - Administración práctica de sistemas

### Comunidades

- **Reddit:** r/linux, r/operatingsystems, r/unix
- **Stack Overflow:** Etiquetas: linux, kernel, operating-system
- **Lists:** LKML (Linux Kernel Mailing List)

---

## Cronología Resumida

```
1940s: ENIAC - Primer computador electrónico general-purpose
1950s: GM-NAA I/O - Primer SO de producción
1964: OS/360 - Familia de SOs de propósito general
1969: UNIX - Sistema minimalista escrito en C
1970s: UNIX v4, v5, v6 - Pipes, portabilidad
1977: BSD - Sockets TCP/IP
1981: MS-DOS 1.0 - SO para IBM PC
1984: Mac OS - Primera GUI comercial exitosa
1991: Linux v0.01 - Primer kernel de Linux
1995: Windows 95 - GUI masiva en hogares
2000s: Cloud computing, virtualización
2010s: Contenedores, IoT, edge computing
2020s: AI-native OS, energy-aware computing
```

---

**Última actualización**: 2026-02-01
