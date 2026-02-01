---
marp: true
theme: default
paginate: true
header: 'IF0099 - Sistemas Operativos I | Unidad 8'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
---

# Clase 14: Programas, Aplicaciones e Interfaces
## System Calls, APIs y Comunicación con el Kernel

<style>
section {
  font-size: 20px;
  overflow: hidden;
}
img {
  max-width: 70% !important;
  max-height: 50vh !important;
  object-fit: contain !important;
  height: auto !important;
  display: block !important;
  margin: 0 auto !important;
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

## Objetivos de la Clase

Al finalizar esta clase, el estudiante será capaz de:

1. **Distinguir** entre llamadas al sistema (syscalls) y APIs de usuario
2. **Explicar** el flujo completo: Aplicación → Biblioteca → Kernel → Hardware
3. **Reconocer** las categorías de system calls en Linux
4. **Usar** herramientas como `strace` para analizar syscalls
5. **Comparar** system calls entre Linux y Windows
6. **Implementar** programas básicos usando syscalls directamente

**Duración:** 90 minutos

---

## Agenda

1. Interfaz usuario-sistema: La arquitectura de capas (15 min)
2. System Calls: La puerta al kernel (25 min)
3. APIs y bibliotecas estándar (15 min)
4. System Calls en Linux vs Windows (10 min)
5. Ejemplos prácticos y strace (20 min)
6. Ejercicio: Implementar micat (5 min)

---

## 1. Interfaz Usuario-Sistema

### La Arquitectura de Capas

```
┌─────────────────────────────────────────────────────────┐
│  NIVEL 4: APLICACIONES DEL USUARIO                      │
│  (Chrome, VS Code, Juegos, Tu programa)                 │
├─────────────────────────────────────────────────────────┤
│  NIVEL 3: BIBLIOTECAS ESTÁNDAR                          │
│  (libc, WinAPI, Python stdlib)                          │
│  → Proporcionan funciones de alto nivel                 │
├─────────────────────────────────────────────────────────┤
│  NIVEL 2: LLAMADAS AL SISTEMA (SYSCALLS)                │
│  → Interfaz controlada con el kernel                    │
├─────────────────────────────────────────────────────────┤
│  NIVEL 1: KERNEL DEL SISTEMA OPERATIVO                  │
│  → Gestión de procesos, memoria, archivos, E/S          │
├─────────────────────────────────────────────────────────┤
│  NIVEL 0: HARDWARE                                      │
│  (CPU, Memoria, Disco, Red)                             │
└─────────────────────────────────────────────────────────┘
```

---

### Flujo de una Operación

**Ejemplo: Abrir un archivo en Python**

```python
# Código de usuario (Nivel 4)
with open("datos.txt", "r") as f:
    contenido = f.read()
```

**¿Qué pasa internamente?**

```
1. Python open() → llama a C stdio
2. C fopen() → llama a syscall open()
3. Syscall open() → kernel verifica permisos
4. Kernel → solicita acceso al driver de disco
5. Driver → opera el hardware del disco
6. Resultado → vuelve por la cadena
```

> **Key insight:** Cada nivel agrega abstracción, pero las syscalls son el único camino al kernel.

---

## 2. System Calls: La Puerta al Kernel

### ¿Qué son las System Calls?

Las **llamadas al sistema** (syscalls) son la **única forma** en que un programa en modo usuario puede solicitar servicios privilegiados al kernel.

```
┌───────────────────────────────────┐
│      MODO USUARIO (Ring 3)        │
│                                   │
│  Aplicación                       │
│    ↓ (open, read, write...)       │
│  Biblioteca C (libc)              │
│    ↓ (syscall wrapper)            │
├───────────────────────────────────┤ ← TRAP/INT: Cambio de modo
│      MODO KERNEL (Ring 0)         │
│                                   │
│  Despachador de Syscalls          │
│    ↓ (tabla de syscalls)          │
│  Función del Kernel               │
│    ↓ (acceso a hardware)          │
│  Controladores (drivers)          │
│    ↓                              │
│  HARDWARE                         │
└───────────────────────────────────┘
```

---

### ¿Por qué dos modos de operación?

| Aspecto | Modo Usuario (Ring 3) | Modo Kernel (Ring 0) |
|---------|----------------------|---------------------|
| **Quién ejecuta** | Aplicaciones normales | SO y drivers |
| **Privilegios** | Limitados | Totales |
| **Acceso a hardware** | ❌ No directo | ✅ Directo |
| **Memoria accesible** | Solo la asignada | Toda |
| **Si hay error** | Muere el proceso | Crash del sistema |
| **Instrucciones** | ADD, MOV, JMP | + IN, OUT, HLT |

**La syscall es la "puerta controlada"** entre estos mundos.

---

### El Mecanismo Paso a Paso

**Ejemplo: `open("/tmp/test.txt", O_RDONLY)`**

<div style="display: flex; gap: 10px; font-size: 0.85em;">

<div style="flex: 1;">

**Paso 1: Preparación**
```c
// libc prepara parámetros
mov rax, 2        // syscall #2 = open
mov rdi, path     // "/tmp/test.txt"
mov rsi, O_RDONLY // flags
```

</div>

<div style="flex: 1;">

**Paso 2: Ejecutar syscall**
```asm
syscall           // ← CPU cambia a Ring 0
                  // Hardware guarda contexto
```

</div>

<div style="flex: 1;">

**Paso 3: Kernel ejecuta**
```c
sys_open() {
  1. Validar ruta
  2. Verificar permisos
  3. Asignar file descriptor
  4. Retornar fd
}
```

</div>

</div>

**Paso 4: Retorno**
```asm
// Kernel pone resultado en rax
// CPU vuelve a Ring 3
iret              // Continúa programa
```

> ⚠️ **Cambiar de modo cuesta ~100-1000 ciclos de CPU**

---

### Categorías de System Calls (Linux)

| Categoría | Ejemplos | Función |
|-----------|----------|---------|
| **Control de procesos** | `fork()`, `exec()`, `exit()`, `wait()` | Crear, terminar procesos |
| **Manejo de archivos** | `open()`, `read()`, `write()`, `close()` | Operaciones con archivos |
| **Gestión de memoria** | `mmap()`, `brk()`, `mprotect()` | Asignar/liberar memoria |
| **Gestión de dispositivos** | `ioctl()`, `read()`, `write()` | Control de hardware |
| **Información del sistema** | `getpid()`, `time()`, `uname()` | Datos del sistema |
| **Comunicación** | `pipe()`, `socket()`, `send()`, `recv()` | IPC y red |

---

### Tabla de System Calls Comunes

| Syscall | Número (x86-64) | Descripción | Ejemplo en C |
|---------|-----------------|-------------|--------------|
| `read` | 0 | Leer de file descriptor | `read(fd, buf, count)` |
| `write` | 1 | Escribir a file descriptor | `write(fd, "hola", 4)` |
| `open` | 2 | Abrir/crear archivo | `open("/file", O_RDONLY)` |
| `close` | 3 | Cerrar file descriptor | `close(fd)` |
| `stat` | 4 | Información de archivo | `stat("/file", &buf)` |
| `fork` | 57 | Crear proceso hijo | `fork()` |
| `execve` | 59 | Ejecutar programa | `execve("/bin/ls", ...)` |
| `exit` | 60 | Terminar proceso | `exit(0)` |
| `getpid` | 39 | Obtener PID | `getpid()` |
| `socket` | 41 | Crear socket de red | `socket(AF_INET, ...)` |

> **Nota:** Los números varían según arquitectura (x86-64 vs ARM).

---

## 3. APIs y Bibliotecas Estándar

### APIs vs System Calls

| Aspecto | System Calls | APIs (libc, etc.) |
|---------|--------------|-------------------|
| **Nivel** | Bajo (kernel) | Alto (usuario) |
| **Portabilidad** | Específico del SO | Portátil entre SO |
| **Usabilidad** | Complejo (ensamblador) | Simple (C/Python) |
| **Overhead** | Alto (cambio de modo) | Variable |
| **Funciones** | Primitivas básicas | Funciones compuestas |

**Ejemplo:** `printf()` vs `write()`
```c
// printf() - API de alto nivel
printf("Hola %s, tienes %d mensajes\n", nombre, count);
// → Formatea string, maneja buffers, luego llama write()

// write() - Syscall directo
write(1, "Hola\n", 5);  // fd=1 (stdout)
```

---

### La Biblioteca C (libc)

**Funciones de la libc:**
- **Wrapper de syscalls:** `open()`, `read()`, `write()`
- **Gestión de memoria:** `malloc()`, `free()`
- **Entrada/Salida:** `printf()`, `scanf()`, `fopen()`
- **Procesos:** `system()`, `popen()`
- **Strings:** `strcpy()`, `strcmp()`, `strlen()`

**Flujo de printf():**
```
printf("Hola")
  ↓
formatea string → buffer
  ↓
write(1, buffer, len)  // syscall real
  ↓
syscall instruction
  ↓
kernel escribe en terminal
```

---

## 4. System Calls: Linux vs Windows

### Diferencias Arquitectónicas

| Característica | Linux | Windows |
|----------------|-------|---------|
| **Estándar** | POSIX | Win32 API |
| **Syscalls** | Documentadas (~300) | No documentadas oficialmente |
| **Interfaz** | Directa (syscall) | A través de ntdll.dll |
| **Números** | Estables por arquitectura | Cambian entre versiones |

### Equivalencia de Operaciones

| Operación | Linux (POSIX) | Windows (Win32) |
|-----------|---------------|-----------------|
| Abrir archivo | `open()` | `CreateFile()` |
| Leer archivo | `read()` | `ReadFile()` |
| Escribir archivo | `write()` | `WriteFile()` |
| Crear proceso | `fork()` + `exec()` | `CreateProcess()` |
| Esperar proceso | `wait()` | `WaitForSingleObject()` |
| Mapear memoria | `mmap()` | `VirtualAlloc()` + `MapViewOfFile()` |
| Crear thread | `pthread_create()` | `CreateThread()` |

---

### Ejemplo Comparativo: Crear Proceso

**Linux:**
```c
pid_t pid = fork();     // Clonar proceso actual
if (pid == 0) {
    // Proceso hijo
    execl("/bin/ls", "ls", "-l", NULL);
} else {
    // Proceso padre
    wait(NULL);         // Esperar al hijo
}
```

**Windows:**
```c
STARTUPINFO si = {sizeof(si)};
PROCESS_INFORMATION pi;

CreateProcess(
    NULL,               // No module name
    "cmd /c dir",       // Command line
    NULL, NULL,         // Security attrs
    FALSE,              // Inherit handles
    0, NULL, NULL,      // Flags, env, dir
    &si, &pi             // Startup info, process info
);

WaitForSingleObject(pi.hProcess, INFINITE);
CloseHandle(pi.hProcess);
```

---

## 5. Ejemplos Prácticos y strace

### La Herramienta `strace`

**strace** intercepta y muestra todas las system calls que realiza un proceso.

**Uso básico:**
```bash
strace comando
strace -c comando      # Contar syscalls
strace -e open,read ls # Filtrar syscalls
strace -o salida.txt comando  # Guardar a archivo
```

---

### Ejemplo 1: Analizando `ls`

```bash
$ strace ls /tmp 2>&1 | head -20
```

**Salida:**
```
execve("/bin/ls", ["ls", "/tmp"], ...) = 0  # Ejecutar programa
brk(NULL)                               = 0x55a8f4b4a000  # Asignar memoria
openat(AT_FDCWD, "/tmp", O_RDONLY|O_DIRECTORY) = 3  # Abrir directorio
getdents64(3, /* 15 entries */, 32768)  = 480  # Leer entradas
write(1, "archivo1.txt  archivo2.txt\n", 28) = 28  # Escribir a stdout
close(3)                                = 0  # Cerrar fd
exit_group(0)                           = ?  # Terminar
```

**Interpretación:**
1. `execve`: Carga `/bin/ls`
2. `brk`: Reserva memoria heap
3. `openat`: Abre `/tmp` → fd=3
4. `getdents64`: Lee contenido del directorio
5. `write`: Escribe resultado a stdout (fd=1)
6. `close`: Cierra el directorio
7. `exit_group`: Termina el proceso

---

### Ejemplo 2: Contar Syscalls de Python vs C

**Programa en C:**
```c
#include <fcntl.h>
#include <unistd.h>

int main() {
    int fd = open("/tmp/test.txt", O_WRONLY|O_CREAT, 0644);
    write(fd, "Hola\n", 5);
    close(fd);
    return 0;
}
```

**Equivalente en Python:**
```python
with open("/tmp/test.txt", "w") as f:
    f.write("Hola\n")
```

**Comparación con strace:**
```bash
# Compilar y contar syscalls de C
gcc -o test_c test.c
strace -c ./test_c
# → ~15 syscalls

# Contar syscalls de Python
strace -c python3 test.py
# → ~500+ syscalls (import, inicialización, etc.)
```

> **Conclusión:** Python hace muchas más syscalls debido a la inicialización del intérprete.

---

### Ejemplo 3: Analizar un Programa con Error

```c
// bug.c - Intento de abrir archivo inexistente
int main() {
    int fd = open("/noexiste.txt", O_RDONLY);
    // Sin verificar error!
    write(fd, "hola", 4);  // fd = -1, ¡error!
    return 0;
}
```

```bash
$ strace ./bug 2>&1 | tail -10
openat(AT_FDCWD, "/noexiste.txt", O_RDONLY) = -1 ENOENT
  # ↑ Retorna -1, archivo no existe!
write(-1, "hola", 4) = -1 EBADF
  # ↑ Intenta escribir a fd inválido
exit_group(0) = ?
```

**Diagnóstico rápido con strace:** El archivo no existe (`ENOENT` = Error NO ENTry).

---

## 6. Ejercicio: Implementar `micat`

### Objetivo

Crear un programa que replique la funcionalidad básica de `cat` usando syscalls directamente.

### Código Base

```c
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    // Verificar argumentos
    if (argc != 2) {
        const char usage[] = "Uso: micat <archivo>\n";
        write(2, usage, sizeof(usage) - 1);  // stderr = fd 2
        return 1;
    }
    
    // Abrir archivo (syscall open)
    int fd = open(argv[1], O_RDONLY);
    if (fd == -1) {
        const char err[] = "Error: no se puede abrir el archivo\n";
        write(2, err, sizeof(err) - 1);
        return 1;
    }
    
    // Leer y escribir en chunks
    char buffer[4096];
    ssize_t bytes;
    
    while ((bytes = read(fd, buffer, sizeof(buffer))) > 0) {
        write(1, buffer, bytes);  // stdout = fd 1
    }
    
    // Cerrar archivo
    close(fd);
    return 0;
}
```

---

### Instrucciones

```bash
# 1. Guardar el código en micat.c
# 2. Compilar
gcc -o micat micat.c

# 3. Probar
./micat /etc/passwd
./micat micat.c  # ¡Se lee a sí mismo!

# 4. Analizar con strace
strace ./micat /etc/passwd

# 5. Contar syscalls
strace -c ./micat /etc/passwd

# 6. Comparar con cat real
strace -c cat /etc/passwd
```

**Preguntas de reflexión:**
1. ¿Cuántas syscalls hace tu implementación vs `cat` original?
2. ¿Qué hace `cat` adicional que tu programa no hace?
3. ¿Por qué usamos buffer de 4096 bytes?

---

## Resumen de la Clase

| Concepto | Descripción |
|----------|-------------|
| **System Call** | Interfaz controlada al kernel |
| **Modo Usuario** | Aplicaciones, acceso limitado (Ring 3) |
| **Modo Kernel** | SO, acceso total (Ring 0) |
| **API** | Abstracción de alto nivel sobre syscalls |
| **libc** | Biblioteca estándar de C, wrappers de syscalls |
| **strace** | Herramienta para observar syscalls |

### Syscalls más importantes:
- `open()`, `read()`, `write()`, `close()` - Archivos
- `fork()`, `exec()`, `wait()`, `exit()` - Procesos
- `mmap()`, `brk()` - Memoria
- `socket()`, `connect()`, `send()`, `recv()` - Red

---

## Próxima Clase

### Clase 15: Repaso Integral

- Mapa conceptual completo del curso
- Conexiones entre unidades
- Resolución de dudas
- Preparación para el examen final

**¡Nos vemos!**

---

## Recursos y Referencias

### Manuales y Documentación
```bash
man 2 open      # Syscalls: sección 2
man 3 printf    # Funciones de biblioteca: sección 3
man 2 syscalls  # Lista de syscalls de Linux
```

### Herramientas Útiles
- **strace:** Rastrear syscalls (Linux)
- **Process Monitor:** Equivalente en Windows (Sysinternals)
- **ltrace:** Rastrear llamadas a bibliotecas
- **gdb:** Debugger con capacidad de ver syscalls

### Para Profundizar
- **Libro:** "The Linux Programming Interface" - Michael Kerrisk
- **Libro:** "Advanced Programming in the UNIX Environment" - Stevens
- **Repositorio:** `strace` en GitHub (código fuente)
