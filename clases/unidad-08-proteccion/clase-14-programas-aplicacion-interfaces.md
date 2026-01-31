---
marp: true
theme: default
paginate: true
| header: 'IF0099 - Sistemas Operativos I | Unidad 8' |
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
| Get-Content archivo.txt | Measure-Object -Line |
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
