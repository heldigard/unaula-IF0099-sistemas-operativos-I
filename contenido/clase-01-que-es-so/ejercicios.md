# Ejercicios Prácticos - Clase 1: ¿Qué es un Sistema Operativo?

**IF0099 - Sistemas Operativos I**

---

## Ejercicio 1: Tu Primer fork()

**Objetivo:** Crear tu primer proceso hijo usando `fork()`
**Dificultad:** ⭐
**Tiempo estimado:** 15 minutos

### Enunciado

Escribe un programa en C que:
1. Cree un proceso hijo usando `fork()`
2. El proceso padre debe imprimir "PADRE: Hola soy el padre"
3. El proceso hijo debe imprimir "HIJO: Hola soy el hijo"
4. Ambos deben imprimir su PID

### Instrucciones Paso a Paso

- [ ] **Paso 1:** Crear archivo `fork_basico.c`
  ```bash
  nano fork_basico.c
  # o usa tu editor favorito: vim, code, etc.
  ```

- [ ] **Paso 2:** Incluir las librerías necesarias
  ```c
  #include <stdio.h>
  #include <unistd.h>
  ```

- [ ] **Paso 3:** Escribir la función main
  ```c
  int main() {
      pid_t pid;

      pid = fork();

      if (pid == 0) {
          // Código del hijo
          printf("HIJO: Hola soy el hijo\n");
          printf("HIJO: Mi PID es %d\n", getpid());
      } else {
          // Código del padre
          printf("PADRE: Hola soy el padre\n");
          printf("PADRE: Mi PID es %d\n", getpid());
      }

      return 0;
  }
  ```

- [ ] **Paso 4:** Compilar el programa
  ```bash
  gcc fork_basico.c -o fork_basico
  ```

- [ ] **Paso 5:** Ejecutar y observar salida
  ```bash
  ./fork_basico
  ```

- [ ] **Paso 6:** Ejecutar múltiples veces
  ```bash
  for i in {1..5}; do ./fork_basico; done
  ```
  Observa: ¿El orden de salida es siempre el mismo? ¿Por qué?

### Verificación

**Criterio de éxito:**
- El programa compila sin errores
- Se ven ambos mensajes (PADRE e HIJO)
- Cada proceso imprime su PID correctamente

### Solución

<details>
<summary>Ver solución completa</summary>

```c
// fork_basico.c
#include <stdio.h>
#include <unistd.h>

int main() {
    pid_t pid;

    pid = fork();

    if (pid == 0) {
        // Proceso hijo
        printf("HIJO: Hola soy el hijo\n");
        printf("HIJO: Mi PID es %d\n", getpid());
        printf("HIJO: El PID de mi padre es %d\n", getppid());
    } else if (pid > 0) {
        // Proceso padre
        printf("PADRE: Hola soy el padre\n");
        printf("PADRE: Mi PID es %d\n", getpid());
        printf("PADRE: El PID de mi hijo es %d\n", pid);
    } else {
        // Error
        perror("Error en fork()");
        return 1;
    }

    return 0;
}
```

**Compilar y ejecutar:**
```bash
gcc fork_basico.c -o fork_basico
./fork_basico
```

</details>

---

## Ejercicio 2: Explorador de Procesos

**Objetivo:** Usar comandos de Linux para explorar procesos activos
**Dificultad:** ⭐
**Tiempo estimado:** 10 minutos

### Enunciado

Usa comandos de Linux para responder estas preguntas:
1. ¿Cuántos procesos están corriendo en tu sistema?
2. ¿Cuál es el PID del proceso init (PID 1)?
3. ¿Qué proceso consume más CPU?
4. ¿Qué proceso consume más memoria?

### Instrucciones Paso a Paso

- [ ] **Paso 1:** Contar todos los procesos
  ```bash
  ps aux | wc -l
  ```
  Anota el número: _______

- [ ] **Paso 2:** Ver el proceso init
  ```bash
  ps -p 1 -o pid,ppid,cmd
  ```
  Anota el nombre: _______

- [ ] **Paso 3:** Ver procesos ordenados por CPU
  ```bash
  ps aux --sort=-%cpu | head -10
  ```
  Anota el top 1: _______

- [ ] **Paso 4:** Ver procesos ordenados por memoria
  ```bash
  ps aux --sort=-%mem | head -10
  ```
  Anota el top 1: _______

- [ ] **Paso 5:** Ver tu proceso actual
  ```bash
  ps -p $$
  ```

- [ ] **Paso 6:** Ver procesos en árbol
  ```bash
  pstree -p | head -20
  ```

### Verificación

**Criterio de éxito:**
- Comandos ejecutados sin errores
- Respuestas anotadas correctamente
- Entiendes qué representa cada columna de `ps aux`

### Solución

<details>
<summary>Ver comandos y respuestas típicas</summary>

```bash
# 1. Contar procesos (resta 1 por el encabezado)
ps aux | wc -l
# Salida típica: ~200-300 procesos

# 2. Ver proceso init
ps -p 1 -o pid,ppid,cmd
# Salida típica: systemd o init (depende del SO)

# 3. Top por CPU
ps aux --sort=-%cpu | head -10
# Salida típica: Puede ser tu navegador, compilador, etc.

# 4. Top por memoria
ps aux --sort=-%mem | head -10
# Salida típica: Navegador web (Chrome/Firefox)
```

**Columnas de `ps aux`:**
- `USER`: Usuario dueño del proceso
- `PID`: Process ID (identificador único)
- `%CPU`: Porcentaje de uso de CPU
- `%MEM`: Porcentaje de memoria RAM usada
- `VSZ`: Tamaño virtual de memoria (KB)
- `RSS`: Memoria física real usada (KB)
- `TTY`: Terminal asociado
- `STAT`: Estado del proceso
- `START`: Hora de inicio
- `TIME`: Tiempo total de CPU usado
- `COMMAND`: Comando ejecutado

</details>

---

## Ejercicio 3: Multiproceso con wait()

**Objetivo:** Crear múltiples procesos y esperar su terminación
**Dificultad:** ⭐⭐
**Tiempo estimado:** 20 minutos

### Enunciado

Escribe un programa que:
1. Cree 3 procesos hijos
2. Cada hijo imprime un número (1, 2, 3) y espera 1 segundo
3. El padre espera a que todos los hijos terminen
4. El padre imprime "Todos los hijos terminaron"

### Instrucciones Paso a Paso

- [ ] **Paso 1:** Crear `multiproceso.c`

- [ ] **Paso 2:** Incluir librerías necesarias
  ```c
  #include <stdio.h>
  #include <stdlib.h>
  #include <unistd.h>
  #include <sys/wait.h>
  ```

- [ ] **Paso 3:** Crear 3 hijos en un loop
  ```c
  for (int i = 1; i <= 3; i++) {
      pid_t pid = fork();

      if (pid == 0) {
          // Código del hijo
          printf("Hijo %d: PID=%d\n", i, getpid());
          sleep(1);
          exit(0);  // Importante: salir del loop
      }
  }
  ```

- [ ] **Paso 4:** Esperar a los hijos
  ```c
  for (int i = 1; i <= 3; i++) {
      wait(NULL);
  }
  printf("Padre: Todos los hijos terminaron\n");
  ```

- [ ] **Paso 5:** Compilar y ejecutar
  ```bash
  gcc multiproceso.c -o multiproceso
  ./multiproceso
  ```

- [ ] **Paso 6:** Observar el orden de salida
  - Ejecuta varias veces
  - ¿El orden es siempre el mismo? ¿Por qué?

### Verificación

**Criterio de éxito:**
- Se crean exactamente 3 hijos
- Cada hijo imprime su número
- El padre espera correctamente
- El mensaje final aparece después de todos los hijos

### Solución

<details>
<summary>Ver solución completa</summary>

```c
// multiproceso.c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid;
    int num_hijos = 3;

    printf("Padre: PID=%d, creando %d hijos\n", getpid(), num_hijos);

    for (int i = 1; i <= num_hijos; i++) {
        pid = fork();

        if (pid == 0) {
            // Proceso hijo
            printf("  Hijo %d: PID=%d, padre PID=%d\n",
                   i, getpid(), getppid());
            sleep(1);
            printf("  Hijo %d: Terminando\n", i);
            exit(0);
        } else if (pid < 0) {
            perror("Error en fork()");
            return 1;
        }
    }

    // Proceso padre espera a todos
    for (int i = 1; i <= num_hijos; i++) {
        wait(NULL);
    }

    printf("Padre: Todos los %d hijos terminaron\n", num_hijos);

    return 0;
}
```

**Compilar y ejecutar:**
```bash
gcc multiproceso.c -o multiproceso
./multiproceso
```

**Nota:** El orden en que los hijos terminan puede variar debido al scheduling del SO.

</details>

---

## Ejercicio 4: Análisis de System Calls

**Objetivo:** Observar las system calls que hace un programa
**Dificultad:** ⭐⭐
**Tiempo estimado:** 15 minutos

### Enunciado

Usa `strace` para analizar qué system calls hacen diferentes comandos.

### Instrucciones Paso a Paso

- [ ] **Paso 1:** Instalar strace si no está disponible
  ```bash
  # En Debian/Ubuntu
  sudo apt-get install strace

  # En Fedora/RHEL
  sudo dnf install strace
  ```

- [ ] **Paso 2:** Rastrear `ls`
  ```bash
  strace ls -la 2>&1 | head -20
  ```
  Anota las primeras 5 system calls: _______

- [ ] **Paso 3:** Rastrear `cat`
  ```bash
  strace cat /etc/hostname 2>&1 | head -20
  ```

- [ ] **Paso 4:** Contar system calls por tipo
  ```bash
  strace -c ls
  ```
  ¿Cuál es la system call más frecuente? _______

- [ ] **Paso 5:** Rastrear solo system calls de archivos
  ```bash
  strace -e trace=open,close,read,write ls /etc 2>&1 | head -20
  ```

- [ ] **Paso 6:** Rastrear un proceso en ejecución
  ```bash
  # En una terminal, ejecuta:
  sleep 60

  # En otra terminal, encuentra el PID y rastrea:
  ps aux | grep sleep
  sudo strace -p [PID]
  ```

### Verificación

**Criterio de éxito:**
- `strace` funciona correctamente
- Puedes identificar system calls comunes
- Entiendes la diferencia entre `ls` y `cat` a nivel de system calls

### Solución

<details>
<summary>Ver análisis de system calls típico</summary>

**System calls comunes en `ls -la`:**
1. `execve()` - Ejecuta el comando ls
2. `brk()` - Asigna memoria
3. `access()` - Verifica permisos
4. `mmap()` - Mapea memoria
5. `open()` - Abre directorios
6. `getdents()` - Lee entradas de directorio
7. `write()` - Escribe salida

**Diferencias entre `ls` y `cat`:**
- `ls` usa `getdents()` para leer directorios
- `cat` usa `read()` para leer contenido de archivos
- Ambos usan `open()` y `close()`

**Salida de `strace -c ls`:**
```
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
 45.00    0.000123          12        10           1 open
  25.00    0.000068           8         8           mmap
  10.00    0.000027           9         3           read
...
```

</details>

---

## Ejercicio 5: Mini-Explorador de Archivos

**Objetivo:** Crear un programa que liste archivos como `ls`
**Dificultad:** ⭐⭐⭐
**Tiempo estimado:** 30 minutos

### Enunciado

Escribe un programa en C que:
1. Abra el directorio actual
2. Liste todos los archivos
3. Para cada archivo, muestre: nombre, tamaño, permisos
4. Use system calls directamente (no usar `system("ls")`)

### Instrucciones Paso a Paso

- [ ] **Paso 1:** Crear `mini_ls.c`

- [ ] **Paso 2:** Incluir librerías
  ```c
  #include <stdio.h>
  #include <dirent.h>
  #include <sys/stat.h>
  #include <sys/types.h>
  ```

- [ ] **Paso 3:** Abrir directorio
  ```c
  DIR *d;
  struct dirent *dir;
  struct stat file_stat;

  d = opendir(".");
  if (d) {
      // Leer entradas...
  }
  ```

- [ ] **Paso 4:** Leer cada entrada
  ```c
  while ((dir = readdir(d)) != NULL) {
      printf("%s\n", dir->d_name);
  }
  ```

- [ ] **Paso 5:** Obtener metadatos con `stat()`
  ```c
  stat(dir->d_name, &file_stat);
  printf("%s (%ld bytes)\n", dir->d_name, file_stat.st_size);
  ```

- [ ] **Paso 6:** Compilar y probar
  ```bash
  gcc mini_ls.c -o mini_ls
  ./mini_ls
  ```

### Verificación

**Criterio de éxito:**
- Lista todos los archivos del directorio
- Muestra tamaños correctamente
- Funciona con cualquier directorio

### Solución

<details>
<summary>Ver solución completa</summary>

```c
// mini_ls.c - Mini explorador de archivos
#include <stdio.h>
#include <dirent.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <pwd.h>
#include <grp.h>

void print_permissions(mode_t mode) {
    printf((mode & S_IRUSR) ? "r" : "-");
    printf((mode & S_IWUSR) ? "w" : "-");
    printf((mode & S_IXUSR) ? "x" : "-");
    printf((mode & S_IRGRP) ? "r" : "-");
    printf((mode & S_IWGRP) ? "w" : "-");
    printf((mode & S_IXGRP) ? "x" : "-");
    printf((mode & S_IROTH) ? "r" : "-");
    printf((mode & S_IWOTH) ? "w" : "-");
    printf((mode & S_IXOTH) ? "x" : "-");
}

int main() {
    DIR *d;
    struct dirent *dir;
    struct stat file_stat;
    struct passwd *pw;
    struct grp *gr;

    d = opendir(".");
    if (!d) {
        perror("opendir");
        return 1;
    }

    printf("Permisos    Usuario  Grupo    Tamaño    Nombre\n");
    printf("---------   ------   ------   -------   --------\n");

    while ((dir = readdir(d)) != NULL) {
        if (stat(dir->d_name, &file_stat) == 0) {
            print_permissions(file_stat.st_mode);

            pw = getpwuid(file_stat.st_uid);
            gr = getgrgid(file_stat.st_gid);

            printf("   %-8s %-8s %8ld   %s\n",
                   pw ? pw->pw_name : "unknown",
                   gr ? gr->gr_name : "unknown",
                   file_stat.st_size,
                   dir->d_name);
        }
    }

    closedir(d);
    return 0;
}
```

**Compilar y ejecutar:**
```bash
gcc mini_ls.c -o mini_ls
./mini_ls
```

**Salida típica:**
```
Permisos    Usuario  Grupo    Tamaño    Nombre
---------   ------   ------   -------   --------
rwxr-xr-x   user     user          512   .
rwxr-xr-x   user     user         4096   ..
rw-r--r--   user     user         2048   mini_ls.c
rwxr-xr-x   user     user        16856   mini_ls
```

</details>

---

## Desafío Extra: Pipe entre Procesos

**Objetivo:** Crear comunicación entre procesos usando pipes
**Dificultad:** ⭐⭐⭐⭐
**Tiempo estimado:** 45 minutos

### Enunciado

Crea un programa donde:
1. El padre crea un pipe
2. Crea un proceso hijo
3. El padre escribe un mensaje en el pipe
4. El hijo lee el mensaje del pipe
5. El hijo invierte el texto y lo devuelve

### Pista

Usa `pipe()`, `fork()`, `write()`, `read()`.

---

**Última actualización**: 2026-02-01
