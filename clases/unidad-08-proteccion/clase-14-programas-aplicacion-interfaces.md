---
marp: true
theme: default
paginate: true
header: 'IF0099 - Sistemas Operativos I | Unidad 8'
footer: 'UNAULA - Ingeniería Informática - 2026-I'

  section {
    font-size: 24px;
  }

---
<style>
img {
  max-width: 70% !important;
  max-height: 50vh !important;
  object-fit: contain !important;
  height: auto !important;
}
section {
  font-size: 24px;
}
</style>


<!--
IMÁGENES GENERADAS:
- clase-14-llamadas-sistema.png: Arquitectura de llamadas al sistema y APIs
-->

# Clase 14: Programas de Aplicación e Interfaces
## APIs del sistema operativo y llamadas al sistema

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
|----------|----------|
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
|----------|------------|
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
