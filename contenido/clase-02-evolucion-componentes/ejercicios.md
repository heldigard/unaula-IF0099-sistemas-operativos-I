# Ejercicios Prácticos - Clase 2: Evolución y Componentes del SO

**IF0099 - Sistemas Operativos I**

---

## Ejercicio 1: Instalar WSL (Windows Subsystem for Linux)

**Objetivo:** Configurar entorno Linux en Windows para el curso
**Dificultad:** ⭐
**Tiempo estimado:** 20 minutos

### Enunciado

Instalar WSL 2 en Windows para tener un entorno Linux nativo.

### Instrucciones Paso a Paso

#### Opción A: Windows 11 (Recomendado)

- [ ] **Paso 1:** Abrir PowerShell como Administrador
  - Buscar "PowerShell" en inicio
  - Clic derecho → "Ejecutar como administrador"

- [ ] **Paso 2:** Ejecutar comando de instalación
  ```powershell
  wsl --install
  ```

- [ ] **Paso 3:** Reiniciar el computador cuando se solicite

- [ ] **Paso 4:** Abrir "Ubuntu" desde el menú de inicio
  - Se creará un usuario UNIX la primera vez
  - Elige un nombre de usuario y contraseña

- [ ] **Paso 5:** Actualizar paquetes
  ```bash
  sudo apt update && sudo apt upgrade -y
  ```

- [ ] **Paso 6:** Verificar instalación
  ```bash
  uname -a
  cat /etc/os-release
  ```

#### Opción B: Windows 10

- [ ] **Paso 1:** Habilitar WSL
  - Abrir "Activar o desactivar características de Windows"
  - Buscar "Subsistema de Windows para Linux"
  - Marcar y reiniciar

- [ ] **Paso 2:** Descargar e instalar WSL2 kernel update
  - Visitar: https://aka.ms/wsl2kernel
  - Ejecutar el descargado

- [ ] **Paso 3:** Establecer WSL 2 como default
  ```powershell
  wsl --set-default-version 2
  ```

- [ ] **Paso 4:** Instalar Ubuntu
  ```powershell
  wsl --install -d Ubuntu
  ```

### Verificación

**Criterio de éxito:**
- `bash` ejecuta comandos Linux
- `uname -a` muestra información de Linux
- `ls /` muestra directorios de Linux
- `sudo` funciona con contraseña configurada

---

## Ejercicio 2: Explorar Generaciones de SO

**Objetivo:** Investigar y comparar características de diferentes generaciones de SO
**Dificultad:** ⭐⭐
**Tiempo estimado:** 30 minutos

### Enunciado

Crear una tabla comparativa de las 5 generaciones de SO con investigación.

### Instrucciones Paso a Paso

- [ ] **Paso 1:** Crear archivo `generaciones_so.md`
  ```bash
  nano generaciones_so.md
  ```

- [ ] **Paso 2:** Investigar cada generación
  - Buscar información sobre ENIAC, batch processing, UNIX, Windows, Linux
  - Usar referencias del curso

- [ ] **Paso 3:** Completar tabla

| Generación | Período | SO Representativo | Innovación Clave | Problema Resuelto |
|-----------|---------|-------------------|------------------|------------------|
| 0 (Sin SO) | 1940s | ENIAC, UNIVAC I | N/A | Programación manual |
| 1 (Batch) | 1950s | GM-NAA I/O, OS/360 | Tarjetas perforadas, colas | Automatización |
| 2 (Multi) | 1960s | UNIX, OS/360 | Multiprogramación | CPU ociosa en E/S |
| 3 (Time-share) | 1970s | UNIX, VMS, CP/M | Time-sharing | Interactividad |
| 4 (PC) | 1980s | MS-DOS, Mac OS, Windows | GUI | Computación personal |
| 5 (Modernos) | 2000s+ | Linux, Windows 11, Android | Cloud, móviles, VMs | Escalabilidad |

- [ ] **Paso 4:** Agregar insights
  - ¿Qué generación tuvo mayor impacto social?
  - ¿Qué generación enabled la era de internet?
  - ¿Qué problemas de generaciones anteriores persisten hoy?

### Verificación

**Criterio de éxito:**
- Todas las generaciones descritas
- SO representativo identificado correctamente
- Problema resuelto explicado claramente

---

## Ejercicio 3: Explorar Componentes del SO

**Objetivo:** Identificar y examinar componentes del SO en tu sistema
**Dificultad:** ⭐
**Tiempo estimado:** 15 minutos

### Instrucciones Paso a Paso

- [ ] **Paso 1:** Identificar el kernel
  ```bash
  uname -r                    # Versión del kernel
  cat /proc/version          # Información detallada
  ```

- [ ] **Paso 2:** Identificar el shell
  ```bash
  echo $SHELL                 # Shell actual
  cat /etc/shells            # Shells disponibles
  ```

- [ ] **Paso 3:** Ver system calls en acción
  ```bash
  # Rastrear un comando simple
  strace -e trace=open,close,read ls /etc 2>&1 | head -20
  ```

- [ ] **Paso 4:** Explorar /proc
  ```bash
  ls /proc                    # Archivos "virtuales" del kernel
  cat /proc/cpuinfo | head -10
  cat /proc/meminfo | head -10
  ```

- [ ] **Paso 5:** Ver modo usuario vs kernel
  ```bash
  # Esto fallará en modo usuario (permiso denegado)
  cat /proc/kcore           # Lectura de memoria kernel

  # Esto funciona (información filtrada)
  cat /proc/$$/status        # Información de tu proceso
  ```

### Preguntas para Responder

1. **¿Qué versión del kernel estás usando?** _______
2. **¿Qué shell usas por defecto?** _______
3. **¿Cuántas system calls hace `ls /etc`?** Ejecuta `strace -c ls /etc`
4. **¿Por qué no puedes leer `/proc/kcore`?** Piensa sobre modos y permisos

---

## Ejercicio 4: Comparar Modo Usuario y Kernel

**Objetivo:** Entender diferencias entre modo usuario y modo kernel
**Dificultad:** ⭐⭐
**Tiempo estimado:** 20 minutos

### Instrucciones Paso a Paso

- [ ] **Paso 1:** Crear programa que intenta acceso directo
  ```c
  // kernel_access.c - Intenta acceder a modo kernel
  #include <stdio.h>

  int main() {
      printf("Intentando ejecutar instrucción privilegiada...\n");

      // Esto causará una violación de segmento
      // porque estamos en modo usuario (Ring 3)
      asm volatile("mov %%cr3, %%eax" : : "%eax");

      return 0;
  }
  ```

- [ ] **Paso 2:** Compilar y ejecutar
  ```bash
  gcc kernel_access.c -o kernel_access
  ./kernel_access
  ```

- [ ] **Paso 3:** Observar el resultado
  - **Salida esperada:** Segmentation fault (core dumped)
  - **Explicación:** La instrucción `mov cr3` está prohibida en modo usuario

- [ ] **Paso 4:** Verificar con strace
  ```bash
  strace ./kernel_access 2>&1 | grep -E "SIGSEGV|segfault"
  ```

- [ ] **Paso 5:** Comparar con system call válida
  ```c
  // user_mode.c - Usa system call correctamente
  #include <stdio.h>
  #include <unistd.h>

  int main() {
      pid_t pid = getpid();  // System call válida
      printf("Mi PID es: %d\n", pid);
      return 0;
  }
  ```

### Verificación

**Criterio de éxito:**
- Entiendes que instrucciones privilegiadas fallan en modo usuario
- Comprendes que system calls son la forma correcta de solicitar servicios del kernel
- Puedes explicar la diferencia entre acceso directo y mediated

---

## Ejercicio 5: Mini-Explorador de /proc

**Objetivo:** Crear un programa que muestre información del sistema usando `/proc`
**Dificultad:** ⭐⭐
**Tiempo estimado:** 25 minutos

### Enunciado

Escribe un programa que muestre:
1. Información del kernel (versión, hostname)
2. Información de CPU (modelo, cores)
3. Información de memoria (total, disponible)
4. Tiempo de actividad del sistema (uptime)

### Instrucciones Paso a Paso

- [ ] **Paso 1:** Crear `proc_explorer.c`

- [ ] **Paso 2:** Incluir librerías necesarias
  ```c
  #include <stdio.h>
  #include <stdlib.h>
  #include <sys/sysinfo.h>
  #include <sys/utsname.h>
  ```

- [ ] **Paso 3:** Leer información de kernel
  ```c
  struct utsname uts;
  if (uname(&uts) != -1) {
      printf("=== Información del Kernel ===\n");
      printf("SO: %s\n", uts.sysname);
      printf("Nodo: %s\n", uts.nodename);
      printf("Release: %s\n", uts.release);
      printf("Versión: %s\n", uts.version);
      printf("Arquitectura: %s\n\n", uts.machine);
  }
  ```

- [ ] **Paso 4:** Leer uptime
  ```c
  struct sysinfo info;
  if (sysinfo(&info) != -1) {
      printf("=== Tiempo de Actividad ===\n");
      printf("Uptime: %ld segundos\n", info.uptime);
      printf("Procesos creados desde boot: %d\n", info.procs);
      printf("Usuarios actuales: %d\n\n", info.users);
  }
  ```

- [ ] **Paso 5:** Leer información de CPU desde /proc
  ```c
  FILE *fp;

  fp = fopen("/proc/cpuinfo", "r");
  if (fp) {
      char line[256];
      printf("=== Información de CPU ===\n");
      while (fgets(line, sizeof(line), fp)) {
          if (strncmp(line, "model name", 10) == 0) {
              printf("%s", line);
              break;
          }
      }
      fclose(fp);
  }
  ```

- [ ] **Paso 6:** Leer memoria desde /proc
  ```c
  fp = fopen("/proc/meminfo", "r");
  if (fp) {
      char line[256];
      printf("\n=== Información de Memoria ===\n");
      for (int i = 0; i < 5 && fgets(line, sizeof(line), fp); i++) {
          printf("%s", line);
      }
      fclose(fp);
  }
  ```

- [ ] **Paso 7:** Compilar y ejecutar
  ```bash
  gcc proc_explorer.c -o proc_explorer
  ./proc_explorer
  ```

### Verificación

**Criterio de éxito:**
- Programa compila sin errores
- Muestra información correcta del kernel
- Lee archivos de /proc correctamente
- Formato de salida es legible

---

## Ejercicio 6: Investigar UNIX History

**Objetivo:** Investigar la historia de UNIX y su impacto
**Dificultad:** ⭐⭐
**Tiempo estimado:** 30 minutos

### Preguntas de Investigación

Responde estas preguntas usando recursos online (man pages, documentación, artículos):

1. **¿Quiénes crearon UNIX y en qué año?** _______
2. **¿Qué problema con MULTICS motivó la creación de UNIX?** _______
3. **¿Qué significa "todo es un archivo" en UNIX?** _______
4. **¿Qué es un pipe y cómo revolucionó la composición de comandos?** _______
5. **¿Cuál es la diferencia entre UNIX y Linux?** _______
6. **¿Qué distribución de Linux usas y qué derivación es?** _______

### Recursos Recomendados

- `man history` - Comando de historial de bash
- https://www.kernel.org/doc/html/latest/ - Documentación del kernel Linux
- https://www.gnu.org/software/bash/manual/ - Manual de bash
- https://linuxjourney.com/ - Tutorial interactivo

---

## Desafío Extra: Timeline Interactivo

**Objetivo:** Crear una visualización de la evolución de SO
**Dificultad:** ⭐⭐⭐
**Tiempo estimado:** 45 minutos

### Enunciado

Crear un script en bash que muestre una línea de tiempo interactiva de las generaciones de SO, permitiendo al usuario explorar cada una.

### Requisitos

- Menú interactivo para seleccionar generación
- Información detallada de cada generación
- Opción para salir

### Estructura Sugerida

```bash
#!/bin/bash

while true; do
    clear
    echo "=== Evolución de Sistemas Operativos ==="
    echo ""
    echo "1. Generación 0: Sin SO (1940-1950)"
    echo "2. Generación 1: Batch (1950-1965)"
    echo "3. Generación 2: Multiprogramación (1965-1980)"
    echo "4. Generación 3: Time-Sharing (1970-1990)"
    echo "5. Generación 4: PC (1980-2000)"
    echo "6. Generación 5: Modernos (2000-presente)"
    echo "0. Salir"
    echo ""
    read -p "Selecciona una generación: " opcion

    case $opcion in
        1) echo "Detalles de Generación 0..." ;;
        2) echo "Detalles de Generación 1..." ;;
        # ... completar casos
        0) echo "¡Hasta luego!"; break ;;
        *) echo "Opción inválida" ;;
    esac

    read -p "Presiona Enter para continuar..."
done
```

---

**Última actualización**: 2026-02-01
