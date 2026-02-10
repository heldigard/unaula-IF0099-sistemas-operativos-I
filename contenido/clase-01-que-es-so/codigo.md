# Código y Laboratorios - Clase 1: ¿Qué es un Sistema Operativo?

**IF0099 - Sistemas Operativos I**

---

## System Calls en C

### Ejemplo 1: Crear un Proceso con fork()

```c
// fork_example.c - Demostración de fork()
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
    pid_t pid;

    printf("ANTES del fork() - Solo un proceso\n");

    // fork() crea un proceso idéntico (hijo)
    pid = fork();

    if (pid == 0) {
        // Código del proceso HIJO
        printf("HIJO: Mi PID es %d\n", getpid());
        printf("HIJO: El PID de mi padre es %d\n", getppid());
    } else if (pid > 0) {
        // Código del proceso PADRE
        printf("PADRE: Mi PID es %d\n", getpid());
        printf("PADRE: El PID de mi hijo es %d\n", pid);
    } else {
        // Error en fork()
        perror("Error en fork()");
        return 1;
    }

    printf("FIN: Ambos procesos ejecutan esto\n");
    return 0;
}
```

**Compilar:** `gcc fork_example.c -o fork_example`
**Ejecutar:** `./fork_example`

**Salida esperada:**
```
ANTES del fork() - Solo un proceso
PADRE: Mi PID es 1234
PADRE: El PID de mi hijo es 1235
FIN: Ambos procesos ejecutan esto
HIJO: Mi PID es 1235
HIJO: El PID de mi padre es 1234
FIN: Ambos procesos ejecutan esto
```

### Ejemplo 2: Ver Información del Sistema

```c
// sysinfo_example.c - Obtener información del sistema
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
    printf("=== Información del Sistema ===\n");
    printf("PID de este proceso: %d\n", getpid());
    printf("PID del proceso padre: %d\n", getppid());
    printf("UID del usuario: %d\n", getuid());
    printf("GID del grupo: %d\n", getgid());

    return 0;
}
```

**Compilar:** `gcc sysinfo_example.c -o sysinfo_example`
**Ejecutar:** `./sysinfo_example`

### Ejemplo 3: Leer un Archivo (System Calls)

```c
// read_file.c - Lectura de archivo con system calls
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>

#define BUFFER_SIZE 1024

int main(int argc, char *argv[]) {
    int fd;
    char buffer[BUFFER_SIZE];
    ssize_t bytes_read;

    if (argc != 2) {
        fprintf(stderr, "Uso: %s <archivo>\n", argv[0]);
        return 1;
    }

    // Abrir archivo (system call: open)
    fd = open(argv[1], O_RDONLY);
    if (fd == -1) {
        perror("Error al abrir archivo");
        return 1;
    }

    // Leer archivo (system call: read)
    while ((bytes_read = read(fd, buffer, BUFFER_SIZE - 1)) > 0) {
        buffer[bytes_read] = '\0';
        printf("%s", buffer);
    }

    if (bytes_read == -1) {
        perror("Error al leer archivo");
    }

    // Cerrar archivo (system call: close)
    close(fd);

    return 0;
}
```

**Compilar:** `gcc read_file.c -o read_file`
**Ejecutar:** `./read_file /etc/hostname`

---

## Errores Comunes en C

### Tabla de Errores Frecuentes

| Error | Causa | Solución |
|-------|-------|----------|
| **Segmentation fault** | Acceso a memoria inválida | Verificar punteros, límites de arreglos |
| **Bus error** | Alineación de memoria incorrecta | Usar tipos correctos de datos |
| **implicit declaration** | Falta include | Agregar `#include` correspondiente |
| **undefined reference** | Falta linker library | Agregar `-l` (ej: `-lpthread`) |

### Debugging con gdb

```bash
# Compilar con símbolos de depuración
gcc -g programa.c -o programa

# Iniciar gdb
gdb ./programa

# Comandos útiles de gdb
(gdb) run           # Ejecutar programa
(gdb) bt            # Backtrace (ver pila de llamadas)
(gdb) print var     # Imprimir valor de variable
(gdb) break main    # Punto de ruptura en main
(gdb) next          # Ejecutar siguiente línea
(gdb) step          # Paso a paso (entra en funciones)
(gdb) continue      # Continuar ejecución
(gdb) quit          # Salir de gdb
```

---

## Laboratorios Linux

### Lab 1: Explorar Procesos

#### Objetivo
Entender cómo el SO gestiona procesos activos.

#### Comandos

```bash
# Ver todos los procesos
ps aux

# Ver procesos en tiempo real
top

# Ver procesos en formato árbol
pstree

# Ver información de un proceso específico
ps -p 1 -o pid,ppid,cmd

# Ver archivos abiertos por un proceso
lsof -p $$

# Ver mapa de memoria del proceso actual
cat /proc/self/maps
```

**Salida esperada de `ps aux`:**
```
USER   PID %CPU %MEM    VSZ   RSS TTY   STAT START  TIME COMMAND
root     1  0.0  0.1  21500  3400 ?      Ss   10:00  0:01 /sbin/init
user   1234  0.5  1.2 345000 45000 ?      Sl   10:01  0:05 /usr/lib/firefox/firefox
```

### Lab 2: Explorar Memoria

#### Objetivo
Entender cómo el SO gestiona la memoria RAM.

#### Comandos

```bash
# Ver uso de memoria
free -h

# Ver memoria en detalle
cat /proc/meminfo

# Ver uso de memoria por proceso
ps aux --sort=-%mem | head -10

# Ver dispositivos de bloque (discos)
lsblk

# Ver uso de disco
df -h

# Ver estadísticas de E/S
iostat -x 1 5
```

**Salida esperada de `free -h`:**
```
              total        used        free      shared  buff/cache   available
Mem:           15Gi       4.5Gi       6.2Gi       512Mi       5.3Gi       9.8Gi
Swap:         2.0Gi          0B       2.0Gi
```

### Lab 3: Explorar Sistema de Archivos

#### Objetivo
Entender la estructura jerárquica del sistema de archivos.

#### Comandos

```bash
# Ver directorio actual
pwd

# Listar archivos (detallado)
ls -la

# Ver árbol de directorios
tree -L 2

# Ver espacio en disco
du -sh ~/

# Ver inodos (metadatos)
ls -li

# Ver tipo de archivo
file *

# Encontrar archivos
find /etc -name "*.conf" 2>/dev/null

# Ver permisos en formato octal
stat -c "%A %n %a" *
```

### Lab 4: System Calls en Vivo

#### Objetivo
Observar system calls que hace un programa.

#### Comandos

```bash
# Rastrear system calls de un programa
strace ls -la

# Rastrear system calls de un proceso en ejecución
strace -p 1234

# Ver network system calls
strace -e trace=network curl https://example.com

# Contar system calls por tipo
strace -c ls
```

**Salida de `strace ls -la`:**
```
execve("/usr/bin/ls", ["ls", "-la"], 0x7ffeb...) = 0
brk(NULL)                               = 0x55555000
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f1234000
open("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
...
```

---

## Debugging Básico

### Técnicas de Depuración

#### 1. Usar assert()

```c
#include <assert.h>
#include <stdio.h>

int main() {
    int x = 5;

    // Verificación que debe ser verdadera
    assert(x > 0);

    printf("x = %d\n", x);

    return 0;
}
```

Si `assert` falla, el programa termina con mensaje de error.

#### 2. Agregar printf de depuración

```c
#define DEBUG 1

#if DEBUG
    #define DBG_PRINT(fmt, args...) printf("DEBUG: " fmt, ##args)
#else
    #define DBG_PRINT(fmt, args...)
#endif

int main() {
    int x = 5;
    DBG_PRINT("Valor de x: %d\n", x);
    return 0;
}
```

#### 3. Verificar valores de retorno

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fp = fopen("archivo.txt", "r");

    // SIEMPRE verificar retorno
    if (fp == NULL) {
        perror("Error al abrir archivo");
        return EXIT_FAILURE;
    }

    // Usar archivo...
    fclose(fp);
    return EXIT_SUCCESS;
}
```

---

## Scripts Útiles

### Script: Monitorear Uso de Recursos

```bash
#!/bin/bash
# monitor.sh - Monitorea recursos del sistema

while true; do
    clear
    echo "=== $(date) ==="
    echo ""
    echo "CPU:"
    top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1"%"}'
    echo ""
    echo "Memoria:"
    free -h | grep Mem
    echo ""
    echo "Procesos top:"
    ps aux --sort=-%cpu | head -6
    echo ""
    sleep 5
done
```

**Uso:**
```bash
chmod +x monitor.sh
./monitor.sh
```

### Script: Contar Procesos por Usuario

```bash
#!/bin/bash
# count_procs.sh - Cuenta procesos por usuario

echo "=== Procesos por usuario ==="
ps aux | awk '{NR>1} {count[$1]++} END {for (user in count) print user, count[user]}' | sort -k2 -nr
```

---

**Última actualización**: 2026-02-01
