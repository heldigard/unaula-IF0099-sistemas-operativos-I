---
marp: true
theme: default
paginate: true
header: 'IF0099 - Sistemas Operativos I | Unidad 6'
footer: 'UNAULA - Ingeniería Informática - 2026-I'

  section {
    font-size: 24px;
  }

---
<style>
img {
  max-width: 65% !important;
  max-height: 45vh !important;
  object-fit: contain !important;
  height: auto !important;
}
section {
  font-size: 24px;
}
</style>


<!--
IMÁGENES GENERADAS:
- clase-09-sistemas-archivos.png: Comparación de sistemas de archivos FAT32, NTFS y ext4
-->

# Clase 9: Sistemas de Archivos
## Organización, Directorios y Sistemas de Archivos Modernos

**IF0099 - Sistemas Operativos I**
*4° Semestre - Ingeniería Informática*

![Comparación de Sistemas de Archivos](../../assets/infografias/clase-09-sistemas-archivos.png)

---

## Objetivos de la Clase

Al finalizar esta clase, el estudiante será capaz de:

1. **Definir** qué es un archivo y sus atributos
2. **Describir** las operaciones sobre archivos
3. **Explicar** diferentes estructuras de directorios
4. **Comparar** sistemas de archivos: FAT32, NTFS, ext4

**Duración:** 90 minutos

---

## ¿Qué es un Archivo?

### Definición

> Un **archivo** es una colección de información relacionada,
> identificada por un nombre, almacenada en memoria secundaria.

```
Desde el punto de vista del usuario:
┌──────────────────────────────────────────┐
│  informe.docx                            │
│  ├── Nombre: informe.docx                │
│  ├── Tipo: Documento Word                │
│  ├── Tamaño: 2.5 MB                      │
│  ├── Ubicación: C:\Documentos\           │
│  └── Modificado: 2026-02-15 14:30        │
└──────────────────────────────────────────┘

Desde el punto de vista del SO:
┌──────────────────────────────────────────┐
│  Secuencia de bloques en disco           │
│  Bloques: 100, 101, 250, 251, 252, ...   │
└──────────────────────────────────────────┘
```

---

## Atributos de un Archivo

```
┌─────────────────────────────────────────────────────────────┐
│                    METADATOS DEL ARCHIVO                    │
├─────────────────────────────────────────────────────────────┤
│  Nombre         │ identificador legible para humanos        │
│  Identificador  │ número único en el sistema de archivos    │
│  Tipo           │ .txt, .exe, .jpg, etc.                    │
│  Ubicación      │ puntero a bloques en disco                │
│  Tamaño         │ bytes / bloques                           │
│  Protección     │ permisos (rwx)                            │
│  Hora/Fecha     │ creación, modificación, acceso            │
│  Propietario    │ UID/GID (Linux) o SID (Windows)           │
└─────────────────────────────────────────────────────────────┘
```

---

## Operaciones sobre Archivos

### Operaciones básicas del SO

| Operación | Descripción | System Call (Linux) |
|-----------|-------------|---------------------|
| **Crear** | Asignar espacio, crear entrada en directorio | `creat()`, `open()` |
| **Abrir** | Cargar metadatos en memoria | `open()` |
| **Leer** | Copiar datos a buffer del proceso | `read()` |
| **Escribir** | Copiar datos del buffer al disco | `write()` |
| **Posicionar** | Mover puntero de lectura/escritura | `lseek()` |
| **Cerrar** | Liberar estructuras en memoria | `close()` |
| **Eliminar** | Liberar bloques, eliminar entrada | `unlink()` |

---

## Ejemplo en C

```c
#include <fcntl.h>
#include <unistd.h>

int main() {
    // Crear y abrir archivo
    int fd = open("datos.txt", O_CREAT | O_WRONLY, 0644);
    
    // Escribir
    char *texto = "Hola Mundo\n";
    write(fd, texto, 11);
    
    // Posicionar al inicio
    lseek(fd, 0, SEEK_SET);
    
    // Cerrar
    close(fd);
    
    return 0;
}
```

---

## Estructura de Directorios

### Directorio: archivo especial que contiene lista de archivos

```
DIRECTORIO = Lista de entradas
┌─────────────────────────────────────────┐
│  Entrada 1: nombre → metadatos/inode    │
│  Entrada 2: nombre → metadatos/inode    │
│  Entrada 3: nombre → metadatos/inode    │
│  ...                                    │
└─────────────────────────────────────────┘
```

### Tipos de estructuras de directorios:
1. Nivel único
2. Dos niveles
3. Árbol
4. Grafo acíclico
5. Grafo general

---

## Directorio de Un Nivel

```
┌──────────────────────────────────────────────────────┐
│                   DIRECTORIO ÚNICO                   │
├──────────────────────────────────────────────────────┤
│  cat.exe │ bo.txt │ a.txt │ test.txt │ data.txt │...│
└──────────────────────────────────────────────────────┘

✅ Simple
❌ Todos los archivos deben tener nombres únicos
❌ No hay organización
❌ No hay privacidad entre usuarios
```

**Usado en:** Primeros sistemas operativos (CP/M)

---

## Directorio de Dos Niveles

```
                    DIRECTORIO MAESTRO
                ┌─────────┬─────────┬─────────┐
                │ Usuario1│ Usuario2│ Usuario3│
                └────┬────┴────┬────┴────┬────┘
                     │         │         │
         ┌───────────┘         │         └───────────┐
         ▼                     ▼                     ▼
    ┌─────────┐          ┌─────────┐          ┌─────────┐
    │cat.exe  │          │a.txt    │          │data.txt │
    │bo.txt   │          │b.txt    │          │prog.exe │
    └─────────┘          └─────────┘          └─────────┘
     Usuario1              Usuario2              Usuario3
```

✅ Cada usuario tiene su espacio
✅ Pueden repetirse nombres entre usuarios
❌ No permite subdirectorios

---

## Directorio de Árbol (Jerárquico)

```
                         / (raíz)
                          │
          ┌───────────────┼───────────────┐
          ▼               ▼               ▼
        /home           /etc           /var
          │               │               │
    ┌─────┼─────┐         │         ┌─────┴─────┐
    ▼     ▼     ▼         ▼         ▼           ▼
  juan  maria  pedro   passwd     log         cache
    │     │                        │
    ▼     └──┐                     ▼
 docs       |                   syslog
    │    Desktop
    ▼       │
 tesis.pdf foto.jpg
```

**Rutas:**
- Absoluta: `/home/juan/docs/tesis.pdf`
- Relativa: `docs/tesis.pdf` (desde `/home/juan`)

---

## Grafo Acíclico (Links/Accesos Directos)

### Permite compartir archivos entre directorios

```
        /home/juan/docs              /home/maria/shared
              │                              │
              ▼                              ▼
         proyecto.pdf ◄──────────────── proyecto.pdf
              │                          (enlace)
              ▼
        DATOS REALES

Linux: ln -s /home/juan/docs/proyecto.pdf /home/maria/shared/
Windows: Acceso directo (shortcut)
```

**Tipos de enlaces:**
- **Hard link:** Mismo inodo, mismo archivo
- **Soft link (simbólico):** Archivo que apunta a ruta

---

## Sistemas de Archivos Comunes

| Sistema | SO | Tamaño máx. archivo | Tamaño máx. partición |
|---------|-----|---------------------|----------------------|
| **FAT32** | Windows/Linux | 4 GB | 2 TB |
| **NTFS** | Windows | 16 EB | 256 TB |
| **ext4** | Linux | 16 TB | 1 EB |
| **APFS** | macOS | 8 EB | 8 EB |

---

## FAT32 (File Allocation Table)

```
           FAT (Tabla de Asignación)        Área de Datos
        ┌───┬───┬───┬───┬───┬───┬───┐    ┌───────────────┐
Entrada:│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │    │   Bloque 2    │
        ├───┼───┼───┼───┼───┼───┼───┤    │   (inicio)    │
Valor:  │ - │ - │ 3 │ 5 │EOF│ 4 │ - │    ├───────────────┤
        └───┴───┴───┴───┴───┴───┴───┘    │   Bloque 3    │
              │   │   │   │               ├───────────────┤
              │   └───│───│──────────┐    │   Bloque 4    │
              │       │   │          │    ├───────────────┤
              └───────│───│────────┐ │    │   Bloque 5    │
                      │   │        │ │    └───────────────┘
                      │   │        │ │
Archivo: Inicio=2 → 2→3→5→4→EOF    ▼ ▼
                                  Orden: 2→3→5→4
```

✅ Simple, compatible con todo
❌ Límite 4GB por archivo
❌ Sin permisos, sin journaling

---

## NTFS (New Technology File System)

```
                NTFS ESTRUCTURA
┌────────────────────────────────────────────────────────┐
│  MFT (Master File Table)                               │
│  ┌──────────────────────────────────────────────────┐  │
│  │ Registro 0: $MFT (tabla misma)                   │  │
│  │ Registro 1: $MFTMirr (copia de seguridad)        │  │
│  │ Registro 2: $LogFile (journaling)                │  │
│  │ Registro 3: $Volume (info del volumen)           │  │
│  │ ...                                              │  │
│  │ Registro N: archivo del usuario                  │  │
│  └──────────────────────────────────────────────────┘  │
│                                                        │
│  Cada registro MFT: 1KB                                │
│  Contiene: Atributos, permisos ACL, timestamps, datos  │
└────────────────────────────────────────────────────────┘
```

✅ Journaling (recuperación de errores)
✅ Permisos ACL granulares
✅ Compresión y cifrado (EFS)

---

## ext4 (Fourth Extended Filesystem)

```
                EXT4 ESTRUCTURA
┌─────────────────────────────────────────────────────────┐
│  Superbloque │ Tabla de inodos │ Bloques de datos      │
├──────────────┴─────────────────┴────────────────────────┤
│                                                         │
│  INODO (128 bytes):                                     │
│  ┌───────────────────────────────────────────────┐     │
│  │ Modo (permisos) │ UID │ GID │ Tamaño │ Tiempo │     │
│  │ Punteros a bloques (12 directos + indirectos) │     │
│  └───────────────────────────────────────────────┘     │
│                                                         │
│  El nombre NO está en el inodo (está en directorio)     │
└─────────────────────────────────────────────────────────┘
```

✅ Journaling
✅ Extents (bloques contiguos)
✅ Alocación retardada

---

## Journaling: Protección contra Fallos

```
SIN JOURNALING:                    CON JOURNALING:
┌────────────────────┐             ┌────────────────────┐
│ 1. Escribir datos  │             │ 1. Escribir en log │
│ 2. Actualizar FAT  │             │ 2. Escribir datos  │
│ 3. Actualizar dir  │             │ 3. Actualizar FAT  │
└────────────────────┘             │ 4. Actualizar dir  │
                                   │ 5. Marcar completo │
Si falla en paso 2:                └────────────────────┘
¡Inconsistencia!
                                   Si falla en cualquier paso:
                                   El log permite recuperar
```

**Tipos de journaling:**
- **Metadata only:** Solo cambios de estructura (ext4 default)
- **Full:** Datos y metadata (más lento, más seguro)

---

## Comparación Visual

```
                 FAT32         NTFS          ext4
             ┌─────────────┬─────────────┬─────────────┐
Journaling   │     ❌      │     ✅      │     ✅      │
             ├─────────────┼─────────────┼─────────────┤
Permisos     │     ❌      │  ACL ✅     │  Unix ✅    │
             ├─────────────┼─────────────┼─────────────┤
Tamaño máx   │     4GB     │   16 EB     │    16 TB    │
archivo      │             │             │             │
             ├─────────────┼─────────────┼─────────────┤
Compresión   │     ❌      │     ✅      │   ext. ✅   │
             ├─────────────┼─────────────┼─────────────┤
Cifrado      │     ❌      │  EFS ✅     │ ext./LUKS   │
             └─────────────┴─────────────┴─────────────┘
```

---

## Montaje de Sistemas de Archivos

### Linux: Un árbol único con múltiples dispositivos

```
                    / (raíz - /dev/sda1 ext4)
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
     /home         /mnt          /boot
    (sda2)         │            (sda3)
      │            │
      ▼            ▼
   ext4      /mnt/usb ← montaje de USB (FAT32)
             /mnt/cd  ← montaje de CD (ISO9660)

Comando: mount /dev/sdb1 /mnt/usb
```

---

## Actividad Práctica (10 min)

### En parejas:

1. En terminal Linux (o WSL):
```bash
# Ver sistemas de archivos montados
df -Th

# Ver inodo de un archivo
ls -li archivo.txt

# Crear enlace simbólico
ln -s /ruta/original enlace

# Ver contenido de directorio (detallado)
ls -la /
```

2. **Responder:** ¿Cuántos sistemas de archivos hay montados? ¿Qué tipos son?

---

## Resumen de la Clase

| Concepto | Descripción |
|----------|-------------|
| **Archivo** | Unidad lógica de almacenamiento con nombre |
| **Directorio** | Archivo especial que contiene lista de archivos |
| **FAT32** | Simple, compatible, límite 4GB |
| **NTFS** | Windows moderno, journaling, ACL |
| **ext4** | Linux, journaling, extents |
| **Journaling** | Log de operaciones para recuperación |
| **Montaje** | Conectar sistema de archivos al árbol |

---

## Para la Próxima Clase

### Clase 9: Gestión de E/S y Protección

- Dispositivos de E/S
- Controladores (drivers)
- DMA (Direct Memory Access)
- Protección y seguridad básica

**¡Nos vemos!**
