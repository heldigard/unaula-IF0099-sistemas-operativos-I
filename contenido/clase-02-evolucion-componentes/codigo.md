# Código y Laboratorios - Clase 2: Evolución y Componentes del SO

**IF0099 - Sistemas Operativos I**

---

## System Calls de Información del Sistema

### Ejemplo 1: Obtener Información del Sistema

```c
// sysinfo.c - Obtener información del sistema
#include <stdio.h>
#include <unistd.h>
#include <sys/utsname.h>

int main() {
    char hostname[256];
    struct utsname uts;

    // Obtener nombre del host
    if (gethostname(hostname, sizeof(hostname)) == 0) {
        printf("Nombre del host: %s\n", hostname);
    }

    // Obtener información del sistema
    if (uname(&uts) == 0) {
        printf("Nombre del SO: %s\n", uts.sysname);
        printf("Nodo/hostname: %s\n", uts.nodename);
        printf("Versión: %s\n", uts.version);
        printf("Release: %s\n", uts.release);
        printf("Arquitectura: %s\n", uts.machine);
    }

    // Información del proceso
    printf("\n--- Información del Proceso ---\n");
    printf("PID: %d\n", getpid());
    printf("PID del padre: %d\n", getppid());
    printf("UID del usuario: %d\n", getuid());
    printf("GID del grupo: %d\n", getgid());

    return 0;
}
```

**Compilar:** `gcc sysinfo.c -o sysinfo`
**Ejecutar:** `./sysinfo`

### Ejemplo 2: Ver Límites del Sistema

```c
// syslimits.c - Ver límites del sistema
#include <stdio.h>
#include <unistd.h>
#include <limits.h>

void print_limit(const char *name, long value) {
    printf("%-30s: %ld\n", name, value);
}

int main() {
    printf("=== Límites del Sistema ===\n\n");

    // Límites de procesos
    print_limit("PID máximo", _POSIX_PID_MAX);
    print_limit("Hijos máximos", _POSIX_CHILD_MAX);
    print_limit("Archivos abiertos máx", _POSIX_OPEN_MAX);

    // Límites de nombres
    print_limit("Longitud hostname", HOST_NAME_MAX);
    print_limit("Longitud nombre login", LOGIN_NAME_MAX);

    // Límites de paths
    print_limit("Longitud path", PATH_MAX);

    return 0;
}
```

**Compilar:** `gcc syslimits.c -o syslimits`
**Ejecutar:** `./syslimits`

---

## Laboratorios Linux

### Lab 1: Explorar Información del Sistema

#### Objetivo
Familiarizarse con comandos para obtener información del sistema y procesos.

#### Comandos Básicos

```bash
# Información del kernel y hardware
uname -a                    # Información completa del sistema
uname -r                    # Versión del kernel
uname -m                    # Arquitectura (x86_64, arm64, etc.)

# Información de la distribución
cat /etc/os-release        # Distribución y versión
lsb_release -a              # Información LSB (si disponible)

# Información de hardware
cat /proc/cpuinfo | head -20 # Información de CPU
lscpu                      # Información detallada de CPU
lsusb                      # Dispositivos USB conectados
lspci                      # Dispositivos PCI
```

**Salida esperada de `uname -a`:**
```
Linux hostname 5.15.0-generic #42-Ubuntu SMP Fri Jan 20 14:00:00 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
```

### Lab 2: Comparar Shells Diferentes

#### Objetivo
Explorar diferencias entre shells y sus características.

#### Shells Disponibles

```bash
# Ver shells instalados
cat /etc/shells

# Probar diferentes shells (si están instalados)
bash   # Bourne Again Shell (estándar)
zsh    # Z Shell (macOS default, características avanzadas)
fish   # Friendly Interactive Shell (user-friendly)
dash   # Debian Almquist Shell (minimalista)
```

#### Características de Cada Shell

| Shell | Autocompletado | Scripting | Usabilidad | Startup |
|-------|----------------|-----------|-------------|---------|
| **bash** | Bueno | Excelente | Media | Rápido |
| **zsh** | Excelente | Bueno | Alta | Medio |
| **fish** | Excelente | Limitado | Muy alta | Rápido |
| **dash** | Bajo | Bueno | Baja | Muy rápido |

#### Experimentar con Diferentes Shells

```bash
# Entrar a zsh temporalmente
zsh
# Autocompletado con tab funciona diferente
# Presiona tab para ver comandos disponibles
exit

# Entrar a fish temporalmente
fish
# Autocompletado predictivo
# Sintaxis diferente de bash
exit

# Volver a bash
bash
```

### Lab 3: Ver Componentes del SO en /proc

#### Objetivo
Explorar el sistema de archivos `/proc` que expone información del kernel.

#### Estructura de /proc

```bash
# Listar contenido de /proc
ls /proc | head -20

# Información del kernel
cat /proc/version
cat /proc/cmdline         # Línea de comandos del kernel

# Información de CPU
cat /proc/cpuinfo | grep "model name" | head -1
cat /proc/cpuinfo | grep "cpu cores"

# Información de memoria
cat /proc/meminfo | head -10

# Ver estadísticas de interrupciones
cat /proc/interrupts | head -20

# Ver devices de bloque
cat /proc/partitions

# Ver filesystems montados
cat /proc/mounts | head -10
```

#### Archivos Importantes en /proc

| Archivo | Contenido |
|---------|----------|
| `/proc/[PID]/cmdline` | Línea de comandos del proceso |
| `/proc/[PID]/environ` | Variables de entorno |
| `/proc/[PID]/fd` | Archivos abiertos (file descriptors) |
| `/proc/[PID]/maps` | Mapa de memoria del proceso |
| `/proc/[PID]/status` | Estado completo del proceso |

```bash
# Ver información del proceso actual (PID = $$)
echo "Mi PID es: $$"
cat /proc/$$/status
cat /proc/$$/cmdline | tr '\0' ' '; echo
cat /proc/$$/environ | tr '\0' '\n' | head -5
```

### Lab 4: Explorar System Calls con strace

#### Objetivo
Observar las system calls que hacen diferentes comandos.

#### Rastrear Comandos Simples

```bash
# Rastrear 'ls' - ver system calls de archivos
strace ls /etc 2>&1 | head -30

# Rastrear 'cat' - ver lectura de archivos
strace cat /etc/hostname 2>&1 | head -20

# Contar system calls por tipo
strace -c ls /etc
```

#### Filtrar System Calls Específicas

```bash
# Solo system calls de archivos
strace -e trace=file ls /etc 2>&1 | head -20

# Solo system calls de procesos
strace -e trace=process ls 2>&1 | head -15

# Solo system calls de red (requiere conexión)
strace -e trace=network curl https://example.com 2>&1 | head -20
```

#### Comparar Dos Comandos

```bash
# Comparar 'ls' vs 'find'
echo "=== ls ==="
strace -c ls /etc 2>&1 | head -10

echo "=== find ==="
strace -c find /etc -name "*.conf" 2>&1 | head -10
```

### Lab 5: Modo Usuario vs Modo Kernel

#### Objetivo
Entender la transición entre modos usuario y kernel.

#### Observar Cambios de Contexto

```bash
# Instalar herramienta para ver cambios de contexto
sudo apt-get install perf  # Si no está instalado

# Ver cambios de contexto de un proceso
perf stat sleep 5

# Ver system calls de un programa simple
strace -T sleep 1 2>&1 | grep -E "rt_sigreturn|exit_group"
```

#### Experimento: Privilegios Insuficientes

```bash
# Intentar leer archivo sin permisos (modo usuario)
cat /etc/shadow  # Operación denegada

# Con sudo (escalada a modo kernel temporalmente)
sudo cat /etc/shadow | head -3  # Funciona
```

---

## Debugging Avanzado

### Ver Errores con errno

```c
// errno_example.c - Usar errno para depuración
#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <fcntl.h>

int main() {
    FILE *fp;

    // Intentar abrir archivo que no existe
    fp = fopen("/archivo/inexistente.txt", "r");

    if (fp == NULL) {
        // errno contiene el número de error
        // strerror() convierte errno a mensaje legible
        // perror() imprime el mensaje automáticamente
        perror("Error al abrir archivo");

        // Alternativa manual:
        printf("Error manual: %s (errno=%d)\n",
               strerror(errno), errno);

        return 1;
    }

    fclose(fp);
    return 0;
}
```

**Compilar:** `gcc errno_example.c -o errno_example`
**Ejecutar:** `./errno_example`

**Salida esperada:**
```
Error al abrir archivo: No such file or directory (errno=2)
Error manual: No such file or directory (errno=2)
```

### Códigos de Error Comunes

| errno | Código | Significado |
|-------|-------|------------|
| 1 | EPERM | Operación no permitida |
| 2 | ENOENT | Archivo o directorio no existe |
| 13 | EACCES | Permiso denegado |
| 21 | EISDIR | Es un directorio, no archivo |
| 22 | EINVAL | Argumento inválido |

---

## Scripts Útiles

### Script: Comparar Dos Shells

```bash
#!/bin/bash
# compare_shells.sh - Compara características de shells

echo "=== Comparación de Shells ==="
echo ""

for shell in bash zsh fish; do
    if command -v $shell >/dev/null 2>&1; then
        echo "--- $shell ---"
        echo "Path: $(which $shell)"
        echo "Versión: $($shell --version | head -1)"

        # Probar una operación simple
        time $shell -c "echo 'Hola desde $shell'" >/dev/null 2>&1
        echo ""
    fi
done
```

### Script: Monitorear Cambios en /proc

```bash
#!/bin/bash
# monitor_proc.sh - Monitorea cambios en /proc/PID

if [ -z "$1" ]; then
    echo "Uso: $0 <PID>"
    exit 1
fi

PID=$1
INTERVALO=2

echo "Monitoreando proceso $PID cada ${INTERVALO}s..."
echo "Presiona Ctrl+C para detener"
echo ""

while true; do
    clear
    echo "=== Proceso $PID - $(date) ==="
    echo ""

    echo "--- Estado ---"
    cat /proc/$PID/status 2>/dev/null | grep -E "State|Threads|VmSize|VmRSS" || echo "Proceso no existe"

    echo ""
    echo "--- CPU (último segundo) ---"
    cat /proc/$PID/stat 2>/dev/null | awk '{print "utime: " $14 " stime: " $15}' || echo "No disponible"

    echo ""
    echo "--- Archivos abiertos ---"
    ls -la /proc/$PID/fd 2>/dev/null | head -10 || echo "No disponible"

    sleep $INTERVALO
done
```

**Uso:**
```bash
chmod +x monitor_proc.sh
./monitor_proc.sh $$
```

---

**Última actualización**: 2026-02-01
