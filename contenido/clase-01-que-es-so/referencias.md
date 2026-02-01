# Referencias - Clase 1: ¿Qué es un Sistema Operativo?

**IF0099 - Sistemas Operativos I**

---

## Fuentes de Datos Estadísticos (2026)

Las siguientes fuentes fueron consultadas para validar las estadísticas de mercado de sistemas operativos presentadas en esta clase:

### Desktop Operating System Market Share
- [StatCounter - Desktop OS Market Share Worldwide](https://gs.statcounter.com/os-market-share/desktop/worldwide)
- [CommandLinux - Linux Desktop Market Share Yearly Trends](https://commandlinux.com/statistics/linux-desktop-market-share-yearly-trends/)
- [Accio - 2025 Operating System Market Share Trends](https://www.accio.com/business/operating-system-market-share-trend)
- [PCMag - Linux Just Hit a Big Milestone in the Desktop OS Race](https://www.pcmag.com/news/linux-just-hit-a-big-milestone-in-the-desktop-os-race)

### Server Operating System Market Share
- [CommandLinux - Linux Server Market Share (2026)](https://commandlinux.com/statistics/linux-server-market-share/)
- [W3Techs - Linux vs Windows Usage Statistics](https://w3techs.com/technologies/comparison/os-linux,os-windows)
- [FactMR - Server Operating System Market](https://www.factmr.com/report/server-operating-system-market)

### Mobile Operating System Market Share
- [StatCounter - Mobile OS Market Share Worldwide](https://gs.statcounter.com/os-market-share/mobile/worldwide)
- [DemandSage - iPhone vs Android Users Market Share Statistics (2026)](https://www.demandsage.com/iphone-vs-android-users/)
- [CommandLinux - Android Global Market Share Statistics 2026](https://commandlinux.com/android/android-global-market-share-statistics/)
- [AppVertices - Android vs iOS Market Share 2025](https://appvertices.io/android-vs-ios-market-share-2025/)

**Nota:** Los datos presentados en el material reflejan cifras acumuladas de 2025 y proyecciones para 2026. Las variaciones entre fuentes son normales debido a diferencias en metodología de medición.

---

## Bibliografía

### Libros de Texto Recomendados

1. **Tanenbaum, Andrew S.** *Modern Operating Systems*. 5th Edition.
   - Pearson, 2024.
   - **Capítulo 1:** Introduction - Definición y conceptos básicos de SO
   - **Capítulo 2:** Processes and Threads - Gestión de procesos
   - **Relevancia:** Texto fundamental, muy claro y didáctico

2. **Silberschatz, Abraham; Galvin, Peter B.; Gagne, Greg.** *Operating System Concepts*.
   - 10th Edition, Wiley, 2018.
   - Conocido como el "dinosaurio" por su portada
   - **Capítulo 1:** Introduction
   - **Capítulo 3:** Processes
   - **Relevancia:** Referencia clásica en cursos de SO

3. **Stallings, William.** *Operating Systems: Internals and Design Principles*.
   - 9th Edition, Pearson, 2022.
   - **Capítulo 1:** Computer System Overview
   - **Capítulo 2:** Operating System Overview
   - **Relevancia:** Buen balance entre teoría y práctica

4. **Love, Robert.** *Linux Kernel Development*.
   - 3rd Edition, Addison-Wesley, 2010.
   - **Relevancia:** Para entender cómo funciona Linux específicamente

### Artículos y Papers Clásicos

1. **Dijkstra, E. W.** "Structure of the THE-Multiprogramming System".
   - *Communications of the ACM*, 1968.
   - **Relevancia:** Introduce el concepto de arquitectura por capas

2. **Ritchie, D. M.; Thompson, K.** "The UNIX Time-Sharing System".
   - *Bell System Technical Journal*, 1978.
   - **Relevancia:** Paper fundacional de UNIX, base de Linux y macOS

3. **Wulf, W. A.; Cohen, E.** "Hydra: The Kernel of a Multiprocessor Operating System".
   - *Communications of the ACM*, 1971.
   - **Relevancia:** Introduce conceptos de microkernel

---

## Recursos Online

### Documentación Oficial

| Recurso | URL | Descripción |
|---------|-----|-------------|
| **Linux man pages** | https://man7.org/linux/man-pages/ | Documentación completa de system calls Linux |
| **POSIX Specification** | https://pubs.opengroup.org/onlinepubs/9699919799/ | Estándar IEEE 1003.1 (POSIX) |
| **GNU C Library** | https://www.gnu.org/software/libc/manual/ | Documentación de glibc (wrapper de system calls) |
| **Linux Kernel Docs** | https://www.kernel.org/doc/html/latest/ | Documentación interna del kernel Linux |

### Tutoriales y Guías

| Recurso | URL | Descripción |
|---------|-----|-------------|
| **Beej's Guide to Unix IPC** | https://beej.us/guide/bgipc/ | Guía excelente sobre IPC, forks, pipes |
| **The Linux Programming Interface** | https://linuxprogrammingblog.com/ | Basado en el libro de Michael Kerrisk |
| **Linux Journey** | https://linuxjourney.com/ | Tutorial interactivo de comandos Linux |
| **OverTheWire: Bandit** | https://overthewire.org/wargames/bandit/ | Juego para aprender seguridad Linux |

### Videos y Cursos

| Recurso | URL | Descripción |
|---------|-----|-------------|
| **CS162: Operating Systems** (UC Berkeley) | https://archive.org/details/ucberkeley-webcast-PL-XXvCtBDoUdWMxsN3GiL60eKXbC9pJQA | Curso completo de SO |
| **OSTEP: Operating Systems: Three Easy Pieces** | https://www.youtube.com/playlist?list=PLHx89CvnPLkDhXjjYmMp8qbGQi5Y52Lx | Videos del libro OSTEP |
| **Systems with Gautham** | https://www.youtube.com/@systemswithgautham | Canal de YouTube sobre sistemas |

---

## Herramientas

### Para Linux

| Herramienta | Propósito | Instalación |
|-------------|-----------|-------------|
| `strace` | Rastrear system calls | `sudo apt install strace` |
| `ltrace` | Rastrear llamadas a librerías | `sudo apt install ltrace` |
| `lsof` | Listar archivos abiertos | `sudo apt install lsof` |
| `htop` | Monitor de procesos interactivo | `sudo apt install htop` |
| `iotop` | Monitor de I/O | `sudo apt install iotop` |
| `perf` | Analizador de rendimiento | `sudo apt install linux-tools-common` |

### Para Windows

| Herramienta | Propósito | URL |
|-------------|-----------|-----|
| **Process Explorer** | Monitor de procesos | https://learn.microsoft.com/sysinternals |
| **Process Monitor** | Monitor de sistema de archivos/registro | https://learn.microsoft.com/sysinternals |
| **WSL (Windows Subsystem for Linux)** | Ejecutar Linux en Windows | https://learn.microsoft.com/wsl |

---

## Comandos Útiles de Referencia

### Gestión de Procesos

```bash
# Ver todos los procesos
ps aux

# Ver proceso específico
ps -p 1234

# Matar proceso
kill 1234
kill -9 1234  # forzado

# Ver procesos en tiempo real
top
htop  # más amigable
```

### Gestión de Memoria

```bash
# Ver uso de memoria
free -h

# Ver detalles de memoria
cat /proc/meminfo

# Ver mapa de memoria de proceso
cat /proc/1234/maps
```

### Sistema de Archivos

```bash
# Ver espacio en disco
df -h

# Ver tamaño de directorio
du -sh /path/to/dir

# Encontrar archivos grandes
find / -size +100M 2>/dev/null
```

### Debugging

```bash
# Rastrear system calls
strace ./programa

# Rastrear proceso en ejecución
strace -p 1234

# Ver archivos abiertos
lsof -p 1234

# Depurador
gdb ./programa
```

---

## Estándares Importantes

### POSIX (Portable Operating System Interface)

- **Qué es:** Estándar IEEE para compatibilidad entre sistemas operativos
- **Por qué importa:** Tu código C compilado en Linux funcionará en macOS, BSD, etc.
- **System calls POSIX:** `fork()`, `open()`, `read()`, `write()`, `socket()`, etc.

### Filesystem Hierarchy Standard (FHS)

- **Qué es:** Estándar que define la estructura de directorios en sistemas tipo Unix
- **Directorios clave:**
  - `/bin`: Comandos esenciales
  - `/etc`: Configuración del sistema
  - `/home`: Directorios de usuarios
  - `/proc`: Sistema de archivos virtual con info del kernel
  - `/var**: Datos variables (logs, spool)

---

## Práctica Recomendada

### Para Dominar System Calls en C

1. **Escribir código todos los días**
   - Comienza con `fork()`, `wait()`, `exit()`
   - Continúa con `open()`, `read()`, `write()`, `close()`
   - Avanza a `pipe()`, `dup2()`, `socket()`

2. **Leer man pages**
   ```bash
  man 2 fork    # System call fork
  man 2 open    # System call open
  man 2 read    # System call read
  ```

3. **Usar strace para aprender**
   ```bash
  strace ls -la
  strace cat archivo.txt
  ```

4. **Compilar con advertencias máximas**
   ```bash
  gcc -Wall -Wextra -pedantic programa.c -o programa
  ```

5. **Usar valgrind para detectar errores**
   ```bash
  valgrind --leak-check=full ./programa
  ```

---

## Comunidades y Foros

### Para Preguntas

- **Stack Overflow** (tag: c, linux, system-calls)
- **Reddit:** r/linux, r/operatingsystems, r/C_Programming
- **Unix & Linux Stack Exchange** (https://unix.stackexchange.com/)
- **Lists del kernel Linux** (para avanzados)

### Para Mantenerse Actualizado

- **LWN.net** (Linux Weekly News) - https://lwn.net/
- **Phoronix** - https://www.phoronix.com/
- **Kernel Newbies** - https://kernelnewbies.org/

---

**Última actualización**: 2026-02-01
