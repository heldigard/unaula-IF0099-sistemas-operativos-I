---
marp: true
theme: default
paginate: true
header: 'IF0099 - Sistemas Operativos I | Unidad 8'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
---

# Clase 14: Programas, Aplicaciones e Interfaces

<style>
section {
  font-size: 24px;
}
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

<!--
IMÁGENES GENERADAS:
- clase-14-llamadas-sistema.png: Arquitectura de llamadas al sistema y APIs
-->


**IF0099 - Sistemas Operativos I**
*4° Semestre - Ingeniería Informática*
---

## Objetivos

Al finalizar esta clase, el estudiante será capaz de:

1. **Distinguir** entre llamadas al sistema y APIs de usuario
2. **Reconocer** interfaces típicas del SO
3. **Usar** llamadas básicas (archivos y procesos)
4. **Explicar** el flujo app → kernel

**Duración:** 90 minutos

---

## Agenda

1. Interfaz usuario-sistema (15 min)
2. Llamadas al sistema (25 min)
3. APIs y bibliotecas (15 min)
4. Ejemplos Linux/Windows (25 min)
5. Actividad (10 min)

---

## 1. Interfaz Usuario-Sistema

```
Aplicación
   │  (API)
Biblioteca estándar
   │  (syscall)
Kernel
   │
Hardware
```

- **Syscall:** entrada controlada al kernel
- **API:** funciones de alto nivel (libc, WinAPI)

---

## 2. Llamadas al Sistema (Linux)

| Categoría | Ejemplos |
| ---------- | ---------- |
| **Procesos** | fork, exec, wait |
| **Archivos** | open, read, write, close |
| **Memoria** | mmap, brk |
| **E/S** | ioctl |

```c
int fd = open("datos.txt", O_RDONLY);
read(fd, buffer, 100);
close(fd);
```

---

## 3. APIs de Usuario

- **libc**: capa estándar en Unix
- **WinAPI**: CreateProcess, ReadFile, WriteFile

**Idea:** Las APIs esconden detalles de syscalls

---

## 4. Ejemplos Prácticos

### Linux: contar líneas
```bash
wc -l archivo.txt
```

### Windows PowerShell:
```powershell
Get-Content archivo.txt | Measure-Object -Line
```

---

## Actividad (10 min)

En parejas:
1. Escribir un programa en C que abra un archivo y muestre su tamaño
2. Investigar qué syscall usa `ls` para listar directorios

---

## Resumen

| Concepto | Idea clave |
| ---------- | ------------ |
| **Syscall** | Puerta de entrada al kernel |
| **API** | Abstracción de alto nivel |
| **Interfaz** | App → Biblioteca → Kernel |

---

## Próxima Clase

### Clase 15: Repaso Integral

- Conceptos clave del curso
- Resolución de dudas
- Preparación examen final

**¡Nos vemos!**


---


## 🔧 System Calls: La Interfaz con el Kernel

### ¿Qué son las System Calls?

Las **llamadas al sistema** (syscalls) son la única forma en que un programa puede pedirle al kernel que haga algo privilegiado.

```
┌───────────────────────────────────┐
│      MODO USUARIO                 │
│                                   │
│  Aplicación                       │
│    ↓ (open, read, write...)       │
│  Biblioteca C (libc)              │
│    ↓ (syscall wrapper)            │
├───────────────────────────────────┤ ← CPU cambia a Modo Kernel
│      MODO KERNEL                  │
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
#### ¿Qué pasa internamente?


```c

int main() {
    // 1. Llamada a open() en modo usuario
    int fd = open("/tmp/test.txt", O_RDONLY);
    
    if (fd == -1) {
        perror("Error abriendo archivo");
        return 1;
    }
    
    printf("Archivo abierto con descriptor: %d\n", fd);
    close(fd);
    return 0;
}
```


**Paso 1:** `open()` en libc prepara parámetros
```c
// libc traduce a syscall #2 (en x86-64)
syscall(__NR_open, "/tmp/test.txt", O_RDONLY, 0);
```

---
#### ¿Qué pasa internamente?

*(continuación...)*

**Paso 2:** Instrucción especial de CPU
```asm
mov rax, 2              ; Número de syscall (open = 2)
mov rdi, path           ; Parámetro 1: ruta del archivo
mov rsi, O_RDONLY       ; Parámetro 2: flags
syscall                 ; ← CPU cambia a modo kernel
```

**Paso 3:** Kernel ejecuta `sys_open()`
```c
// En el kernel de Linux:
asmlinkage long sys_open(const char __user *filename, 
                         int flags, umode_t mode)
{
    // 1. Validar ruta (¿existe?, ¿permisos?)
    // 2. Buscar inodo en filesystem
    // 3. Crear entrada en tabla de archivos abiertos
    // 4. Asignar file descriptor (fd)
    // 5. Retornar fd al programa
}
```

---
#### ¿Qué pasa internamente?

*(continuación...)*

**Paso 4:** Retorno a modo usuario
```c
// El valor de retorno está en rax
// libc retorna ese valor como int
return fd;  // Ej: 3 (0,1,2 están reservados para stdin/out/err)
```

---

### 📋 Syscalls Comunes en Linux

| Syscall | Número | Descripción | Ejemplo en C |
|---------|--------|-------------|--------------|
| `read` | 0 | Leer de fd | `read(fd, buf, count)` |
| `write` | 1 | Escribir a fd | `write(fd, "hola", 4)` |
| `open` | 2 | Abrir archivo | `open("/file", O_RDONLY)` |
| `close` | 3 | Cerrar fd | `close(fd)` |
| `stat` | 4 | Info de archivo | `stat("/file", &statbuf)` |
| `fork` | 57 | Crear proceso | `fork()` |
| `execve` | 59 | Ejecutar programa | `execve("/bin/ls", ...)` |
| `exit` | 60 | Terminar proceso | `exit(0)` |
| `getpid` | 39 | Obtener PID | `getpid()` |
| `socket` | 41 | Crear socket | `socket(AF_INET, ...)` |

**Nota:** Los números varían según arquitectura (x86-64 vs ARM).

---

### 🛠️ Herramienta `strace`: Espiar Syscalls

**strace** muestra todas las syscalls que hace un programa.

#### Ejemplo 1: `ls`

```bash
strace ls /tmp 2>&1 | head -20
```

**Salida:**
```
execve("/bin/ls", ["ls", "/tmp"], ...) = 0
brk(NULL)                               = 0x55a8f4b4a000
openat(AT_FDCWD, "/tmp", O_RDONLY|O_DIRECTORY) = 3
getdents64(3, /* 15 entries */, 32768) = 480
write(1, "archivo1.txt  archivo2.txt\n", 28) = 28
close(3)                                = 0
exit_group(0)                           = ?
```

**Interpretación:**
1. `execve`: Ejecuta `/bin/ls`
2. `openat`: Abre directorio `/tmp` (fd=3)
3. `getdents64`: Lee entradas del directorio
4. `write`: Escribe a stdout (fd=1)
5. `close`: Cierra fd 3
6. `exit_group`: Termina proceso

---

#### Ejemplo 2: Programa Propio

```bash
# Compilar programa
gcc -o test test.c

# Ejecutar con strace
strace ./test
```

**Ejercicio:** Escribe un programa que:
1. Abra un archivo
2. Lea 10 bytes
3. Escriba en otro archivo
4. Cierre ambos

Luego ejecuta con `strace` y cuenta cuántas syscalls hace.

---

### 🪟 System Calls en Windows

Windows usa **Native API** (ntdll.dll), no POSIX.

| Linux Syscall | Windows Native API | Descripción |
|---------------|-------------------|-------------|
| `open()` | `NtCreateFile()` | Abrir archivo |
| `read()` | `NtReadFile()` | Leer |
| `write()` | `NtWriteFile()` | Escribir |
| `fork()` | ❌ (no existe) | Usar `CreateProcess()` |
| `getpid()` | `NtGetCurrentProcessId()` | Obtener PID |

**Herramienta equivalente a strace:** **Process Monitor** (de Sysinternals)

---

## Ejemplo en C usando Syscalls Directamente

```c
#include <fcntl.h>
#include <unistd.h>

int main() {
    // Sin printf - usamos write directo
    const char msg[] = "Hola desde syscalls\n";
    
    // 1. Escribir a stdout (fd=1)
    write(1, msg, sizeof(msg) - 1);
    
    // 2. Crear y escribir archivo
    int fd = open("/tmp/syscall_test.txt", 
                  O_WRONLY | O_CREAT | O_TRUNC, 
                  0644);
    
    if (fd != -1) {
        write(fd, msg, sizeof(msg) - 1);
        close(fd);
    }
    
    return 0;
}
```

```bash
gcc -o syscall_test syscall_test.c
strace -c ./syscall_test
cat /tmp/syscall_test.txt
```

---

## Comparación: Python vs C

### Python (alto nivel)

```python
with open("/tmp/test.txt", "w") as f:
    f.write("Hola\n")
```

**Pregunta:** ¿Cuántas syscalls hace Python vs el programa en C?

```bash
strace -c python3 -c "open('/tmp/test.txt','w').write('Hola\n')"
strace -c ./syscall_test
```

**Análisis:** Python hace muchas más syscalls (imports, inicialización, etc.).

---

## 📝 Ejercicio: Implementar `micat`

### Tiempo estimado: 30 minutos

Implementa un programa que replique `cat` usando syscalls directamente:

```c
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        const char usage[] = "Uso: micat <archivo>\n";
        write(2, usage, sizeof(usage) - 1);  // stderr
        return 1;
    }
    
    int fd = open(argv[1], O_RDONLY);
    if (fd == -1) {
        const char err[] = "Error: archivo no existe\n";
        write(2, err, sizeof(err) - 1);
        return 1;
    }
    
    char buffer[4096];
    ssize_t bytes;
    
    while ((bytes = read(fd, buffer, sizeof(buffer))) > 0) {
        write(1, buffer, bytes);  // stdout
    }
    
    close(fd);
    return 0;
}
```

**Compilar y probar:**
```bash
gcc -o micat micat.c
./micat /etc/passwd
strace ./micat /etc/passwd
```


---
