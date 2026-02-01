---
marp: true
theme: default
paginate: true
header: 'IF0099 - Sistemas Operativos I | Unidad 6'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
---

# Clase 11: Implementación de Sistemas de Archivos

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
## Inodos, bloques y estructuras internas

**IF0099 - Sistemas Operativos I**
*4° Semestre - Ingeniería Informática*

![Estructura Interna FS - Inodos](../../assets/infografias/clase-11-inodos.png)

---

## Objetivos de la Clase

Al finalizar esta clase, el estudiante será capaz de:

1. **Explicar** la estructura interna de un sistema de archivos
2. **Describir** el rol de inodos, directorios y bloques
3. **Analizar** la asignación de espacio (contigua, enlazada, indexada)
4. **Relacionar** el diseño con el rendimiento

**Duración:** 90 minutos

---

## Agenda

1. Estructuras de un FS (20 min)
2. Inodos y metadatos (20 min)
3. Asignación de espacio (25 min)
4. Caso ext4 (15 min)
5. Actividad práctica (10 min)

---

## 1. Estructura Interna del FS

```
┌──────────────────────────────────────┐
│ Superblock                           │
├──────────────────────────────────────┤
│ Bitmaps (bloques / inodos libres)    │
├──────────────────────────────────────┤
│ Tabla de Inodos                      │
├──────────────────────────────────────┤
│ Bloques de Datos                     │
└──────────────────────────────────────┘
```

- **Superblock:** tamaño, FS, estado, conteos
- **Bitmaps:** qué está libre/ocupado
- **Inodos:** metadatos de archivos
- **Datos:** contenido real

---

## 2. ¿Qué es un Inodo?

```
INODO:
- Permisos (rwx)
- Propietario / grupo
- Tamaño
- Timestamps (atime, mtime, ctime)
- Punteros a bloques de datos
```

**Regla clave:** El nombre del archivo está en el directorio, no en el inodo.

**Veremos detalles avanzados de inodos más adelante...**

---

## Directorios como Tablas

```
Directorio:
+----------------------+---------+
|  | Nombre | Inodo |  |
+----------------------+---------+
| documento.txt | 1052 |
| foto.jpg | 2048 |
| proyecto/ | 3021 |
+----------------------+---------+
```

- Directorio = archivo especial
- Mapea nombre → inodo

---

## 3. Asignación de Espacio

### Contigua
- Rápida, pero difícil de expandir

### Enlazada
- Fácil crecer, acceso lento

### Indexada
- Acceso directo, usa bloques índice

```
[Inodo] -> [Bloque índice] -> [Bloques de datos]
```

---

## 4. Ejemplo ext4 (Linux)

- **Journaling** para consistencia
- **Extents** para reducir fragmentación
- **Bloques** típicos: 4KB

**Ventaja:** rápido y confiable en servidores

---

## Resumen de la Clase (Parte 1)

| Concepto | Idea clave |
| ---------- | ------------ |
| **Superblock** | Información global del FS |
| **Inodo** | Metadatos y punteros a datos |
| **Directorio** | Tabla nombre → inodo |
| **Asignación** | Contigua, enlazada, indexada |
| **ext4** | Journaling y extents |

---

## Transición a Detalles Avanzados

### A continuación: Profundización en Inodos

Explicaremos en detalle:
- Estructura completa de un inodo
- Punteros directos e indirectos
- Hard links vs symbolic links
- Exploración práctica con comandos Linux

---

## 5. Detalles Avanzados de Inodos

### Estructura Completa de un Inodo



Un **inodo** (index node) es una estructura de datos que contiene metadatos sobre un archivo, **excepto su nombre y datos reales**.

```
┌─────────────────────────────────┐
│         INODO #12345            │
├─────────────────────────────────┤
│ Tipo: Archivo regular           │
│ Permisos: -rw-r--r-- (644)      │
│ Propietario: UID 1000           │
│ Grupo: GID 1000                 │
│ Tamaño: 4,096 bytes             │
│ Fecha creación: 2026-01-31      │
│ Fecha modificación: 2026-01-31  │
│ Último acceso: 2026-01-31       │
│ Links: 1                        │
│ Bloques usados: 8               │
│ ┌─────────────────────────────┐ │
│ │  PUNTEROS A BLOQUES:        │ │
│ │  • Directos (12): → Bloques │ │
│ │  • Indirecto simple: → Tabla│ │
│ │  • Indirecto doble: → Tabla │ │
│ │  • Indirecto triple: → Tabla│ │
│ └─────────────────────────────┘ │
└─────────────────────────────────┘
```

---

## 📦 Punteros de Inodo en Detalle

#### 1. Punteros Directos (12)

Apuntan directamente a bloques de datos.

```
Inodo
 │
 ├─→ Bloque 1001  [4KB de datos]
 ├─→ Bloque 1002  [4KB de datos]
 ├─→ Bloque 1003  [4KB de datos]
 ...
 └─→ Bloque 1012  [4KB de datos]

Capacidad: 12 × 4KB = 48 KB
```

**Uso:** Archivos pequeños (< 48 KB) se acceden directamente, muy rápido.

---

#### 2. Puntero Indirecto Simple

Apunta a un bloque que contiene punteros a bloques de datos.

```
Inodo
 │
 └─→ Bloque Indirecto (1024 punteros)
      ├─→ Bloque 2001  [4KB]
      ├─→ Bloque 2002  [4KB]
      ...
      └─→ Bloque 3024  [4KB]

Capacidad adicional: 1024 × 4KB = 4 MB
Total hasta aquí: 48 KB + 4 MB = 4.048 MB
```

---

#### 3. Puntero Indirecto Doble

Apunta a un bloque con punteros a bloques de punteros.

```
Inodo
 │
 └─→ Bloque Indirecto Doble
      ├─→ Bloque Indirecto 1 (1024 punteros)
      │    ├─→ Bloque datos
      │    ├─→ Bloque datos
      │    ...
      │    └─→ Bloque datos (1024 bloques)
      │
      ├─→ Bloque Indirecto 2 (1024 punteros)
      ...
      └─→ Bloque Indirecto 1024

Capacidad: 1024 × 1024 × 4KB = 4 GB
```

---

#### 4. Puntero Indirecto Triple

Para archivos MUY grandes (>4 GB).

```
Capacidad: 1024³ × 4KB = 4 TB
```

**Total máximo teórico:** 48 KB + 4 MB + 4 GB + 4 TB ≈ **4 TB por archivo**

---

### 🔍 Ver Inodos en Linux

#### Listar Inodos

```bash
# Ver número de inodo de archivos
ls -i

# Salida ejemplo:
# 12345 documento.txt
# 67890 foto.jpg
```

#### Ver Detalles de Inodo

```bash
stat documento.txt
```

**Salida:**
```
  File: documento.txt
  Size: 4096          Blocks: 8          IO Block: 4096   regular file
Device: 802h/2050d    Inode: 12345       Links: 1
Access: (0644/-rw-r--r--)  Uid: ( 1000/ usuario)   Gid: ( 1000/ usuario)
Access: 2026-01-31 10:00:00.000000000 -0500
Modify: 2026-01-31 10:00:00.000000000 -0500
Change: 2026-01-31 10:00:00.000000000 -0500
 Birth: -
```

---

### 🛠️ Comando `debugfs` - Exploración Avanzada

**Requiere permisos root**

```bash
# Entrar en modo debug del filesystem
sudo debugfs /dev/sda1

# Comandos útiles:
debugfs> stat <12345>          # Ver inodo 12345 en detalle
debugfs> ls -l                 # Listar con inodos
debugfs> blocks <12345>        # Ver bloques usados por inodo
debugfs> imap documento.txt    # Encontrar inodo de archivo
```

---

### 📊 Tabla Comparativa: Nombre vs Inodo

| Aspecto | Nombre del Archivo | Inodo |
|---------|-------------------|-------|
| **Ubicación** | En directorio | En tabla de inodos |
| **Contiene** | Cadena de texto + ptr a inodo | Metadatos + punteros a bloques |
| **Puede cambiar** | Sí (con `mv`) | No (es un número fijo) |
| **Hard links** | Múltiples nombres | Un solo inodo |
| **Tamaño** | Variable (hasta 255 chars) | Fijo (128 o 256 bytes) |

---

### 🔗 Hard Links vs Symbolic Links

#### Hard Link
```bash
ln archivo.txt hardlink.txt
```

```
Directorio:
  "archivo.txt"    → Inodo 12345
  "hardlink.txt"   → Inodo 12345  (mismo inodo!)

Inodo 12345:
  Links: 2  ← Contador aumenta
```

**Eliminación:**
Solo se borra el archivo cuando Links = 0

---

#### Symbolic Link (Soft Link)
```bash
ln -s archivo.txt symlink.txt
```

```
Directorio:
  "archivo.txt"  → Inodo 12345
  "symlink.txt"  → Inodo 67890  (inodo diferente!)

Inodo 67890 (tipo: enlace simbólico):
  Datos: "ruta/a/archivo.txt"  ← Contiene ruta como texto
```

**Si se borra `archivo.txt`:**
El symlink queda "roto" (broken link)

---

## 💻 Actividad Práctica: Explorando Inodos

### Ejercicio 1: Observar Inodos

```bash
# 1. Crear archivo de prueba
echo "Hola mundo" > test.txt

# 2. Ver su inodo
ls -i test.txt
# Anota el número: __________

# 3. Ver detalles completos
stat test.txt

# 4. Crear hard link
ln test.txt test_hardlink.txt

# 5. Verificar que tienen el mismo inodo
ls -i test*.txt

# 6. Ver contador de links
stat test.txt | grep Links
# Debe mostrar: Links: 2
```

---

### Ejercicio 2: Hard Link vs Soft Link

```bash
# 1. Crear archivo original
echo "Contenido original" > original.txt

# 2. Crear hard link y soft link
ln original.txt hard.txt
ln -s original.txt soft.txt

# 3. Ver inodos (¿cuáles son iguales?)
ls -i original.txt hard.txt soft.txt

# 4. Eliminar el original
rm original.txt

# 5. Intentar leer ambos links
cat hard.txt      # ¿Funciona?
cat soft.txt      # ¿Funciona?

# 6. Explica: ¿Por qué uno funciona y otro no?
```

---

### Ejercicio 3: Límite de Inodos

```bash
# Ver total de inodos en el filesystem
df -i

# Salida ejemplo:
# Filesystem      Inodes  IUsed   IFree IUse% Mounted on
# /dev/sda1      6000000 500000 5500000    9% /

# Pregunta: ¿Qué pasa si IUse% llega a 100%,
#           aunque haya espacio en disco?
```

**Respuesta:** No se pueden crear más archivos, aunque haya espacio libre. Cada archivo necesita un inodo.

---

### Tiempo estimado: 30 minutos

---

## Resumen de la Clase (Parte 2)

| Concepto | Idea clave |
| ---------- | ------------ |
| **Punteros directos** | 12 bloques directos (~48 KB) |
| **Indirecto simple** | 1024 bloques (~4 MB adicionales) |
| **Indirecto doble** | 1024² bloques (~4 GB adicionales) |
| **Indirecto triple** | 1024³ bloques (~4 TB adicionales) |
| **Hard link** | Mismo inodo, contador de links |
| **Symbolic link** | Nuevo inodo, contiene ruta como texto |

---

## Próxima Clase

### Clase 12: Protección y Seguridad

- Diferencia entre protección y seguridad
- Dominios de protección y matriz de acceso
- Control de acceso en Linux (UGO, SUID, SGID)
- Control de acceso en Windows (ACL)
- Amenazas comunes y mecanismos de defensa

**¡Nos vemos!**
