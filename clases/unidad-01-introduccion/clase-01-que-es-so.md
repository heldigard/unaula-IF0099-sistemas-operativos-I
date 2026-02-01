---
marp: true
theme: default
paginate: true
header: 'IF0099 - Sistemas Operativos I | Unidad 1'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
---

<style>
img {
  max-width: 70% !important;
  max-height: 45vh !important;
  object-fit: contain !important;
  height: auto !important;
  display: block !important;
  margin: 0 auto !important;
}
section {
  font-size: 18px;
  overflow: hidden;
}
section h1 { font-size: 1.7em; }
section h2 { font-size: 1.3em; }
section h3 { font-size: 1.1em; }
section ul, section ol { font-size: 0.85em; margin-left: 0.5em; }
section li { margin-bottom: 0.2em; }
section pre { font-size: 0.65em; max-height: 55vh; overflow-y: auto; }
section code { font-size: 0.8em; }
section p { margin: 0.3em 0; }
section table {
  width: 100%;
  max-width: 100%;
  font-size: 0.8em;
  border-collapse: collapse;
  margin: 0.3em auto;
}
section th {
  background-color: #1e40af;
  color: white;
  padding: 0.3em 0.5em;
  text-align: left;
  font-size: 0.85em;
}
section td {
  padding: 0.3em 0.5em;
  border: 1px solid #ddd;
  vertical-align: top;
  font-size: 0.8em;
}
section tbody tr:nth-child(even) { background-color: #f8f9fa; }
section tbody tr:hover { background-color: #e9ecef; }
section { padding: 1em 2em; box-sizing: border-box; }
</style>

# Clase 1: ¿Qué es un Sistema Operativo?

## *El corazón invisible de tu computador*

**IF0099 - Sistemas Operativos I**
*4° Semestre - Ingeniería Informática*

---

## Objetivos de la Clase

Al finalizar, serás capaz de:

| Objetivo | Habilidad |
|----------|-----------|
| 🎯 **Definir** qué es un SO | Concepto |
| 🔍 **Identificar** funciones principales | Análisis |
| 🏗️ **Comparar** arquitecturas | Evaluación |
| ⚙️ **Explicar** system calls | Comprensión |
| 🔗 **Relacionar** hardware-SO-aplicaciones | Síntesis |

**Duración:** 90 minutos

---

## Agenda del Día

```
┌─────────────────────────────────────────────────┐
│ 1️⃣  ¿Qué es un SO?              (15 min)       │
│ 2️⃣  Funciones principales         (20 min)       │
│ 3️⃣  Arquitecturas                 (15 min)       │
│ 4️⃣  Servicios y System Calls      (15 min)       │
│ 5️⃣  SO como interfaz              (10 min)       │
│ 6️⃣  Sistemas actuales             (10 min)       │
│ 7️⃣  Actividad práctica            (5 min)        │
└─────────────────────────────────────────────────┘
```

---

## 1. ¿Qué es un Sistema Operativo?

### Definición

> **Software intermediario** entre el **usuario** y el **hardware**

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 30px;">

<div>

```
┌─────────────────────┐
│   👤 USUARIO        │
│   Aplicaciones      │
│                     │
│   ▼ ▼ ▼            │
├─────────────────────┤
│   🖥️  SISTEMA       │
│   OPERATIVO         │
│                     │
│   ▼ ▼ ▼            │
├─────────────────────┤
│   ⚡ HARDWARE       │
│   CPU, RAM, Disco   │
└─────────────────────┘
```

**El SO abstrae la complejidad del hardware**

</div>

<div>

### Función Principal
- **Abstracción:** Oculta detalles de hardware
- **Interfaz:** Provee API estandarizada
- **Gestor:** Administra recursos limitados
- **Protector:** Aísla procesos entre sí

</div>

</div>

---

## ¿Por qué necesitamos un SO?

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">

<div style="text-align: center;">

### ❌ Sin Sistema Operativo

```
┌─────────────────────────────┐
│  Programa 1 │ Programa 2   │
│      ↓      │      ↓        │
│    HARWARE ←────────┘       │
│      ↓                      │
│   ¡COLISIÓN!               │
└─────────────────────────────┘
```

- Cada programa accede al hardware directamente
- Programadores deben conocer cada dispositivo
- Solo un programa a la vez
- Sin protección entre programas

</div>

<div style="text-align: center;">

### ✅ Con Sistema Operativo

```
┌─────────────────────────────┐
│  P1  │  P2  │  P3         │
│   ↓   ↓   ↓                │
│  ┌─────────────────┐       │
│  │   SISTEMA       │       │
│  │   OPERATIVO     │       │
│  └─────────────────┘       │
│           ↓                │
│        HARWARE             │
└─────────────────────────────┘
```

- Interfaz uniforme para todos
- Multiprogramación eficiente
- Memoria protegida
- Hardware abstracto

</div>

</div>

<div style="text-align: center; margin-top: 20px; font-size: 0.9em;">

**El SO transforma el hardware crudo en una plataforma usable y programable**

</div>

---

## Analogía: El Hotel 🏨

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px;">

<div style="text-align: center;">

### 🏨 El Hotel

```
    ┌─────────────┐
    │ HUESPEDES  │ ← Clientes
    │   Mario    │    Ana
    │    Carlos  │
    └──────┬──────┘
           │
    ┌──────▼──────┐
    │  GERENTE 🎯 │ ← Asigna
    │   Hotel     │    habitaciones
    └──────┬──────┘
           │
    ┌──────▼──────┐
    │🛏️ HABITACIONES│ ← Recursos
    │ 101  102    │    limitados
    │ 103  ...   │
    └─────────────┘
```

</div>

<div style="text-align: center;">

### 💻 El Computador

```
    ┌─────────────┐
    │APLICACIONES │ ← Chrome,
    │  Spotify   │    VS Code
    │   Discord  │
    └──────┬──────┘
           │
    ┌──────▼──────┐
    │SO 🖥️       │ ← Asigna
    │  Linux/Win  │    recursos
    └──────┬──────┘
           │
    ┌──────▼──────┐
    │💾 RAM 16GB  │ ← Recursos
    │ CPU 8 núcleos│    limitados
    │ Disco 1TB  │
    └─────────────┘
```

</div>

</div>

<div style="text-align: center; margin-top: 20px;">

**Sin el gerente, los huéspedes pelearían por las habitaciones. Sin el SO, los programas pelearían por la RAM.**

</div>

---

## El Hotel: ¿Qué hace el gerente?

| Hotel | Computador |
|-------|------------|
| Asignar habitaciones | Asignar memoria |
| Mantener registro de huéspedes | Sistema de archivos |
| Evitar conflictos | Sincronización de procesos |
| Seguridad (llaves) | Permisos y protección |
| Mantenimiento | Drivers y E/S |

---

## 2. Funciones Principales del SO

### Las 4 funciones fundamentales

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 25px; margin-top: 20px;">

<div style="text-align: center; padding: 15px; border: 2px solid #3b82f6; border-radius: 10px;">

#### 📊 Gestión de Procesos

- Crear y destruir procesos
- Planificar CPU (scheduling)
- Sincronizar y comunicar procesos
- Manejar deadlocks

**Ejemplo:** Ejecutar Chrome + Spotify a la vez

</div>

<div style="text-align: center; padding: 15px; border: 2px solid #10b981; border-radius: 10px;">

#### 💾 Gestión de Memoria

- Asignar memoria a procesos
- Proteger memoria entre procesos
- Implementar memoria virtual
- Paginación y segmentación

**Ejemplo:** 16GB RAM compartida por 20 programas

</div>

<div style="text-align: center; padding: 15px; border: 2px solid #f59e0b; border-radius: 10px;">

#### 📁 Gestión de Archivos

- Crear, leer, escribir archivos
- Organizar en directorios
- Manejar permisos y acceso
- Backups y recuperación

**Ejemplo:** Sistema de archivos jerárquico

</div>

<div style="text-align: center; padding: 15px; border: 2px solid #ef4444; border-radius: 10px;">

#### 🔌 Gestión de E/S

- Controlar dispositivos
- Buffering y caching
- Manejar interrupciones
- Drivers de dispositivos

**Ejemplo:** Teclado, mouse, disco, red

</div>

</div>

---

## 2.1 Gestión de Procesos

### Programa vs Proceso

| Programa | Proceso |
|----------|---------|
| Archivo en disco | Instancia en memoria |
| Pasivo (no hace nada) | Activo (ejecutándose) |
| `chrome.exe` | Chrome con 5 pestañas |
| Solo ocupa disco | Usa RAM + CPU + archivos |

```
RECETA  📜  →  COCINANDO  🍳
(programa)      (proceso)
```

---

## El Ciclo de Vida de un Proceso

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">

<div>

```
    ┌─────┐
    │📝 NUEVO│
    └──┬──┘
       │ creado
       ▼
    ┌─────┐  ready    ┌─────┐
    │🏃LISTO├────────→│🎯EJEC│
    └──┬──┘           │UTANDO│
       │               └──┬──┘
       │ running         │
       │                 │ I/O
       │        waiting  ▼
       │             ┌─────┐
       └─────────────│⏸️BLOQ│  exit
  scheduler            │UEADO├──→ ✅TERMINADO
                     └─────┘
```

</div>

<div>

### Estados del Proceso

| Estado | Significado | Ejemplo |
|--------|-------------|---------|
| **NUEVO** | Se está creando | `fork()` en C |
| **LISTO** | Espera CPU | En cola de ready |
| **EJECUTANDO** | Usa CPU ahora | Proceso actual |
| **BLOQUEADO** | Espera I/O | Leyendo archivo |
| **TERMINADO** | Fin ejecución | `exit()` llamado |

### Transiciones Clave

- **LISTO → EJECUTANDO:** scheduler elige proceso
- **EJECUTANDO → LISTO:** quantum expiró (preemptivo)
- **EJECUTANDO → BLOQUEADO:** espera I/O
- **BLOQUEADO → LISTO:** I/O completó

</div>

</div>

<div style="text-align: center; margin-top: 15px; font-size: 0.85em;">

**El scheduler decide QUÉ proceso corre. Las interrupciones deciden CUÁNDO cambiar.**

</div>

---

## 2.2 Gestión de Memoria

### La RAM como edificio de apartamentos

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">

<div>

```
┌─────────────────────────────┐
│   🏢 EDIFICIO RAM (16 GB)   │
├──────────┬──────────┬───────┤
│ Apart. 0 │ Apart. 1 │  ...  │
│  SO 2GB  │ Chrome   │       │
│   🔴     │   🟡     │       │
├──────────┼──────────┼───────┤
│ Apart. 3 │ Apart. 4 │ Apart.│
│ Spotify  │ VS Code  │ Libre │
│   🟢     │   🟠     │  ⚪  │
└──────────┴──────────┴───────┘
```

**Cada apartamento = proceso aislado**

</div>

<div>

### Funciones del Gestor de Memoria

| Función | ¿Qué hace? | Ejemplo |
|---------|-----------|---------|
| **Asignar** | Dar RAM a procesos | Chrome pide 500MB |
| **Liberar** | Recuperar RAM | Cerrar Firefox |
| **Proteger** | Aislar procesos | Chrome NO lee Spotify |
| **Virtual** | Usar disco como RAM | Swap en disco SSD |
| **Compartir** | Mismo código en RAM | Librerías compartidas |

### Problemas Clave

- **Fragmentación:** Huecos entre procesos
- **Thrashing:** swapping excesivo
- **Fugas:** Memoria no liberada

</div>

</div>

---

## 2.3 Gestión de Archivos

### El SO como bibliotecario digital

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">

<div>

```
        📁 / (raíz)
         │
    ┌────┼────┬────┬────┐
    │    │    │    │    │
  📁home 📁usr 📁etc 📁var 📁tmp
    │
  📁usuario
    │
  ┌─┴─┬────────────┐
  │   │             │
📁docs 📁downloads 📁code
  │
 📄notes.txt
 📄report.pdf
```

### Operaciones del Sistema de Archivos

| Operación | Descripción | System Call |
|-----------|-------------|-------------|
| **Crear** | Nuevo archivo | `creat()` |
| **Leer** | Obtener datos | `read()` |
| **Escribir** | Guardar datos | `write()` |
| **Eliminar** | Borrar archivo | `unlink()` |
| **Mover** | Cambiar ubicación | `rename()` |

</div>

<div>

### Funciones del Gestor de Archivos

- **Organización:** Directorios jerárquicos
- **Nombres:** Rutas absolutas y relativas
- **Permisos:** Lectura, escritura, ejecución
- **Metadatos:** Tamaño, fecha, dueño
- **Acceso:** Secuencial o aleatorio

### Estructura vs Contenido

```
📦 archivo.txt = [metadatos + datos]

METADATOS                     DATOS
┌─────────────────┐         ┌─────────────┐
│ tipo: regular   │         │ "Hola       │
│ tamaño: 1024    │ ────▶   │  Mundo..."   │
│ permisos: rw-  │         │             │
│ dueño: usuario  │         │ (bytes en   │
│ fecha: hoy     │         │  disco)     │
└─────────────────┘         └─────────────┘
```

**El separa QUÉ es el archivo de DÓNDE están los datos**

</div>

</div>

---

## 2.4 Gestión de E/S

### Dispositivos de entrada/salida

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">

<div>

```
    APLICACION
        ↓
┌───────────────────────┐
│  CAPA DE ABSTRACCIÓN  │  ← APIs uniformes
├───────────────────────┤
│   SUBSISTEMA E/S      │
├───────────────────────┤
│    DRIVERS 📝         │  ← Hablan con hw
├───────────────────────┤
│   CONTROLADOR         │  ← Hardware real
└───────────────────────┘
        ↓
    DISPOSITIVO
```

### Tipos de Dispositivos

| Entrada ⬇️ | Salida ⬆️ | Ambos ↕️ |
|------------|-----------|----------|
| ⌨️ Teclado | 🖥️ Monitor | 💾 Disco duro |
| 🖱️ Mouse | 🖨️ Impresora | 🔌 USB |
| 🎤 Micrófono | 🔊 Altavoces | 🌐 Tarjeta red |
| 📷 Cámara web | 👞 Auriculares | 📱 Móviles |

</div>

<div>

### Técnicas de E/S

#### 1. Polling (Sondeo)
- CPU pregunta repetidamente
- Ineficiente, desperdicia ciclos

#### 2. Interrupciones
- Dispositivo avisa a CPU
- Más eficiente, estándar actual

#### 3. DMA (Direct Memory Access)
- Dispositivo ↔ Memoria directa
- Sin intervención de CPU
- Para transferencias grandes

### Ejemplo: Leer un archivo

```
Programa → read() → SO → Driver → Disco
                      ↓
                 (interrupción)
                      ↓
SO → "¡Datos listos!" → Programa
```

**El SO es el traductor entre software y hardware**

</div>

</div>

---

## 3. Arquitecturas del SO

### ¿Cómo organizar un SO complejo?

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px;">

<div style="text-align: center; padding: 15px; border: 3px solid #3b82f6; border-radius: 10px;">

### 🏛️ Monolítico

```
┌─────────────────┐
│   TODOS LOS     │
│   SERVICIOS     │
│   JUNTOS        │
├─────────────────┤
│   KERNEL UNICO  │
├─────────────────┤
│   HARDWARE      │
└─────────────────┘
```

**Linux, MS-DOS**

✅ Rápido (sin overhead)
❌ Difícil de mantener
❌ Un fallo = crash total

</div>

<div style="text-align: center; padding: 15px; border: 3px solid #10b981; border-radius: 10px;">

### 🧱 Capas

```
┌─────────────────┐
│   Nivel 5       │
├─────────────────┤
│   Nivel 4       │
├─────────────────┤
│   Nivel 3       │
├─────────────────┤
│   Nivel 2       │
├─────────────────┤
│   Nivel 1       │
├─────────────────┤
│   Nivel 0       │
└─────────────────┘
```

**THE, VMS**

✅ Modular
✅ Más seguro
❌ Overhead por capas
❌ Más lento

</div>

<div style="text-align: center; padding: 15px; border: 3px solid #f59e0b; border-radius: 10px;">

### 🧩 Microkernel

```
┌─────┐ ┌─────┐ ┌─────┐
│Files│ │Mem  │ │Proc │
└──┬──┘ └──┬──┘ └──┬──┘
   │       │       │
   └───┬───┴───┬───┘
       │       │
   ┌───▼───────▼───┐
   │  MICROKERNEL  │
   │  (mínimo)     │
   └───┬───────────┘
       │
   HARDWARE
```

**MINIX, QNX**

✅ Más seguro
✅ Flexible
❌ Más lento
❌ Complejo

</div>

</div>

---

## Microkernel: El enfoque minimalista

### ¿Por qué mover servicios fuera del kernel?

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">

<div>

```
┌─────────────────────────────────────┐
│  📁 Servidor Archivos (user space)  │
│         │                           │
│         │ IPC                       │
│         ↓                           │
│  🔄 Servidor Procesos (user space)  │
│         │                           │
│         │ IPC                       │
│         ↓                           │
│  ┌─────────────────────────────┐   │
│  │   MICROKERNEL (kernel)      │   │
│  │   - IPC                     │   │
│  │   - Scheduling básico       │   │
│  │   - Memoria básica          │   │
│  └───────────┬─────────────────┘   │
│              │                      │
│         HARDWARE                   │
└─────────────────────────────────────┘
```

**Solo lo esencial en kernel mode**

</div>

<div>

### Ventajas del Microkernel

| Aspecto | Beneficio |
|---------|-----------|
| **Seguridad** | Menos código en kernel = menos fallos |
| **Extensibilidad** | Agregar servicios sin recompilar kernel |
| **Mantenibilidad** | Fallos en user space NO crashean el sistema |
| **Portabilidad** | Kernel pequeño es más portable |

### Desventajas

| Aspecto | Problema |
|---------|----------|
| **Rendimiento** | IPC entre servicios es costoso |
| **Complejidad** | Difícil de diseñar correctamente |
| **Overhead** | Cambios de contexto adicionales |

**Ejemplo real:** Minix 3 (usado en educación) y QNX (usado en sistemas críticos como autos)

</div>

</div>

---

## Comparación de Arquitecturas

### ¿Cuál elegir? Depende del objetivo

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px;">

<div style="text-align: center;">

### 🏛️ Monolítico

| Criterio | Calificación |
|----------|--------------|
| **Rendimiento** | ⭐⭐⭐⭐⭐ |
| **Seguridad** | ⭐⭐ |
| **Mantenibilidad** | ⭐⭐ |
| **Complejidad** | Baja |
| **Uso ideal** | Escritorio, servidores |

**Ejemplos:**
- Linux (más popular)
- MS-DOS (histórico)
- Unix BSD

</div>

<div style="text-align: center;">

### 🧱 Capas

| Criterio | Calificación |
|----------|--------------|
| **Rendimiento** | ⭐⭐⭐ |
| **Seguridad** | ⭐⭐⭐⭐ |
| **Mantenibilidad** | ⭐⭐⭐⭐ |
| **Complejidad** | Media |
| **Uso ideal** | Sistemas académicos |

**Ejemplos:**
- THE (histórico)
- VAX/VMS
- Windows (híbrido)

</div>

<div style="text-align: center;">

### 🧩 Microkernel

| Criterio | Calificación |
|----------|--------------|
| **Rendimiento** | ⭐⭐ |
| **Seguridad** | ⭐⭐⭐⭐⭐ |
| **Mantenibilidad** | ⭐⭐⭐⭐⭐ |
| **Complejidad** | Alta |
| **Uso ideal** | Sistemas críticos |

**Ejemplos:**
- MINIX 3 (educación)
- QNX (automotriz)
- GNU Hurd (experimental)

</div>

</div>

<div style="text-align: center; margin-top: 20px; padding: 15px; background: #f0f9ff; border-radius: 10px;">

**Insight:** Linux es técnicamente monolítico pero usa módulos cargables, obteniendo lo mejor de ambos mundos.

</div>

---

## 4. System Calls (Llamadas al Sistema)

### La puerta entre usuario y kernel

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">

<div>

```
USUARIO          KERNEL
    │                │
    │ printf("hola")  │
    ▼                │
┌─────────┐          │
│ libc    │          │
│ write() │          │
└────┬────┘          │
     │               │
     │ syscall       │
     ▼               │
┌─────────┐          │
│  TRAP   │─────────►│
│ (cambio │          │
│  modo)  │          │
         ───────────►│
                    ▼
         ◄──────────│
     │              │ sys_write()
     ▼              │
┌─────────┐         │
│ libc    │         │
└────┬────┘         │
     │              │
     ▼              │
   printf()         │
    │              │
    ▼              │
  Usuario         │
```

**TRAP = Transición segura de modo usuario → kernel**

</div>

<div>

### ¿Por qué System Calls?

| Razón | Explicación |
|--------|-------------|
| **Protección** | Hardware no debe ser accesible directamente |
| **Abstracción** | No necesitas saber cómo funciona el disco |
| **Seguridad** | El SO valida cada operación |
| **Portabilidad** | Mismo código en diferentes hardware |

### Flujo Complejo

1. **Programa** llama función en libc
2. **libc** prepara parámetros
3. **TRAP** cambia a modo kernel
4. **Kernel** valida permisos
5. **Kernel** ejecuta operación
6. **RET** retorna resultado
7. **Programa** continúa

**Todo esto en microsegundos, millones de veces por segundo**

</div>

</div>

---

## System Calls: Categorías

### Tipos de operaciones que el kernel puede hacer

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">

<div>

#### 🔄 Control de Procesos

| System Call | Propósito |
|-------------|-----------|
| `fork()` | Crear proceso hijo |
| `exec()` | Reemplazar programa |
| `wait()` | Esperar hijo |
| `exit()` | Terminar proceso |
| `kill()` | Enviar señal |

**Ejemplo:** Cuando ejecutas `ls`, bash hace fork() + exec()

</div>

<div>

#### 📁 Manipulación de Archivos

| System Call | Propósito |
|-------------|-----------|
| `open()` | Abrir archivo |
| `read()` | Leer datos |
| `write()` | Escribir datos |
| `close()` | Cerrar archivo |
| `lseek()` | Mover posición |

**Ejemplo:** `cat archivo.txt` hace open() + read() + write()

</div>

<div>

#### 🔌 Control de Dispositivos

| System Call | Propósito |
|-------------|-----------|
| `ioctl()` | Control específico |
| `mmap()` | Mapear memoria |
| `read()` | Leer de dispositivo |
| `write()` | Escribir a dispositivo |

**Ejemplo:** Configurar velocidad de puerto serie

</div>

<div>

#### 📊 Información del Sistema

| System Call | Propósito |
|-------------|-----------|
| `getpid()` | ID del proceso |
| `getuid()` | ID del usuario |
| `time()` | Hora actual |
| `gettimeofday()` | Hora precisa |

**Ejemplo:** `ps` usa getpid() para listar procesos

</div>

</div>

<div style="text-align: center; margin-top: 20px; padding: 15px; background: #fef3c7; border-radius: 10px;">

**💡 Las system calls son la API del kernel. Todo lo que hace un programa pasa por ellas.**

</div>

---

## 5. El SO como Interfaz

### Dos formas de interactuar con el computador

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px;">

<div style="text-align: center;">

### 🖼️ GUI (Interfaz Gráfica)

```
┌──────────────────────────────────┐
│  [📁] [📝] [⚙️]         [🔊] [🔋] │
├──────────────────────────────────┤
│                                  │
│     Iconos de programas          │
│     📁  📄  🌐  📮                │
│                                  │
│     Ventanas, menúes             │
│     Botones, cuadros             │
│                                  │
└──────────────────────────────────┘
```

#### Características

| Ventaja | Desventaja |
|---------|------------|
| ✅ Fácil de usar | ❌ Usa más recursos |
| ✅ Intuitivo | ❌ Difícil de automatizar |
| ✅ Visual | ❌ Menos potente |

**Ejemplos:** Windows, macOS GNOME, KDE

</div>

<div style="text-align: center;">

### ⌨️ CLI (Interfaz de Comandos)

```
usuario@so:~$ ls -la
drwxr-xr-x  5 usuario  512 Jan 28 10:30 .
drwxr-xr-x  3 root     256 Jan 27 09:00 ..
-rw-r--r--  1 usuario 1024 Jan 28 10:30 datos.txt
-rwxr-xr-x  1 usuario  8192 Jan 27 12:00 script.sh

usuario@so:~$ cat datos.txt | grep error > log.txt

usuario@so:~$
```

#### Características

| Ventaja | Desventaja |
|---------|------------|
| ✅ Muy potente | ❌ Curva de aprendizaje |
| ✅ Automatizable | ❌ Memorizar comandos |
| ✅ Usa pocos recursos | ❌ No es visual |

**Ejemplos:** bash, zsh, PowerShell, cmd

</div>

</div>

<div style="text-align: center; margin-top: 20px; padding: 15px; background: #ecfdf5; border-radius: 10px;">

**💡 Los administradores de sistemas prefieren CLI. Los usuarios caseros prefieren GUI. Ambas usan el mismo kernel.**

</div>

---

## GUI vs CLI: Comparación Detallada

### ¿Cuál usar y cuándo?

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px;">

<div>

### 👥 Uso Cotidiano

| Aspecto | 🏆 Ganador |
|---------|-----------|
| Navegar web | GUI |
| Ver videos | GUI |
| Ofimática | GUI |
| Juegos | GUI |
| Edición fotos | GUI |

**La GUI es mejor para tareas visuales e interactivas**

</div>

<div>

### 🔧 Desarrollo y Administración

| Aspecto | 🏆 Ganador |
|---------|-----------|
| Servidores | CLI |
| Scripting | CLI |
| Automatización | CLI |
| Debug remoto | CLI |
| Batch processing | CLI |

**La CLI es mejor para automatización y administración**

</div>

<div>

### 📊 Comparativa Numérica

| Métrica | GUI | CLI |
|---------|-----|-----|
| Uso RAM | ~500MB | ~5MB |
| Tiempo startup | ~10s | ~0.1s |
| Potencia | 60% | 100% |
| Facilidad inicio | 95% | 20% |
| Automatizable | 10% | 100% |

**CLI = eficiencia máxima, GUI = accesibilidad máxima**

</div>

</div>

<div style="text-align: center; margin-top: 20px; padding: 15px; background: #eff6ff; border-radius: 10px;">

**💡 Insight:** La mayoría de servidores Linux NO tienen GUI instalada. ¿Por qué? Los servidores se administran remotamente vía SSH (CLI).

</div>

---

## 6. Sistemas Operativos Actuales (2026)

### El panorama de los sistemas operativos por plataforma

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px;">

<div style="text-align: center; padding: 15px; border: 3px solid #3b82f6; border-radius: 10px;">

### 💻 Escritorio

```
Windows ████████████████  70%
macOS   ████████████  16%
Linux   ████   4%
Otros   ████   10%
```

#### Windows (Microsoft)
- **Líder absoluto** en escritorio corporativo
- Office, SAP, Adobe → ecosistema completo
- **Hardware兼容:** funciona con cualquier PC
- Gaming → DirectX

#### macOS (Apple)
- **Favorito** de creativos (video, música, diseño)
- Ecosistema Apple integrado (iPhone, iPad, Watch)
- Desarrollo iOS requiere Mac

#### Linux (Escritorio)
- Minoría pero creciendo
- Favorito de desarrolladores
- Distribuciones: Ubuntu, Mint, Fedora

</div>

<div style="text-align: center; padding: 15px; border: 3px solid #10b981; border-radius: 10px;">

### 🖥️ Servidores

```
Linux ████████████████████████████████  96%
Windows ████   4%
Otros   █   1%
```

#### Linux (El rey indiscutible)
- **96% de servidores web** (Netcraft, 2026)
- **100% de supercomputadoras** (Top 500)
- Gratis, estable, uptime de años
- Docker, Kubernetes → stack cloud native

#### Windows Server
- 4% en empresas Microsoft
- Active Directory, Exchange, SharePoint

**¿Por qué Linux domina servidores?**
- Gratis (sin licenciamiento)
- Sin GUI ahorra RAM
- Scripting potente (bash)
- Seguridad por diseño

</div>

<div style="text-align: center; padding: 15px; border: 3px solid #f59e0b; border-radius: 10px;">

### 📱 Móviles

```
Android ████████████████████████████████  71%
iOS     ████████████████████████  28%
Otros   █   1%
```

#### Android (Google)
- **71% del mercado móvil mundial**
- Código abierto (proyecto AOSP)
- Ecosistema fragmentado (Samsung, Xiaomi, etc.)

#### iOS (Apple)
- **28% del mercado** pero **50% de ingresos**
- Exclusivo hardware Apple
- Usuarios con mayor gasto promedio

**Insight:** En móvil, Android domina en unidades, iOS domina en ganancias.

</div>

</div>

---

## ¿Por qué cada SO domina su nicho?

### Análisis de las fortalezas competitivas

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px;">

<div>

### 👔 Windows en Escritorio

```
┌──────────────────────────┐
│  FACTORES DE ÉXITO       │
├──────────────────────────┤
│ ✅ Compatible con todo   │
│ ✅ Office indispensable   │
│ ✅ Soporte mundial        │
│ ✅ Familiaridad           │
│ ✅ Gaming (DirectX 12)    │
│ ✅ Hardware variado       │
└──────────────────────────┘
```

#### Efecto de Red
- **Desarrolladores** → Windows por mercado
- **Usuarios** → Windows por software
- **Empresas** → Windows por compatibilidad

**Círculo virtuoso:** más usuarios → más software → más usuarios

</div>

<div>

### 🐧 Linux en Servidores

```
┌──────────────────────────┐
│  FACTORES DE ÉXITO       │
├──────────────────────────┤
│ ✅ Gratis (sin licencia)  │
│ ✅ Estabilidad extrema    │
│ ✅ Scripting superior     │
│ ✅ Seguridad por diseño   │
│ ✅ Comunidad activa       │
│ ✅ Cloud-native stack     │
└──────────────────────────┘
```

#### Dominio Absoluto
- **Internet corre Linux:** Google, Facebook, Amazon
- **Supercomputadoras:** 100% Top 500
- **IoT y Edge:** Raspberry Pi, routers

**Sin Linux, internet NO funcionaría.**

</div>

<div>

### 🍎 macOS en Creativos

```
┌──────────────────────────┐
│  FACTORES DE ÉXITO       │
├──────────────────────────┤
│ ✅ Hardware premium       │
│ ✅ Software creativo      │
│ ✅ Ecosistema integrado   │
│ ✅ Experiencia usuario    │
│ ✅ Desarrollo iOS         │
│ ✅ Unix underneath       │
└──────────────────────────┘
```

#### Nicho Premium
- **Video profesional:** Final Cut Pro
- **Diseño gráfico:** Adobe Suite optimizado
- **Música:** Logic Pro
- **Desarrollo móvil:** Xcode requerido

**Diseño → Mac. Oficina → Windows. Servidores → Linux.**

</div>

</div>

<div style="text-align: center; margin-top: 20px; padding: 15px; background: #f0f9ff; border-radius: 10px;">

**🎯 Lección:** No existe "el mejor" SO. Cada uno domina donde resuelve mejor un problema específico.

</div>

---

## 7. Actividad Práctica

### Explorando tu Sistema Operativo (5 min)

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">

<div>

### En parejas, investiguen:

#### 🪟 Windows
| Tarea | Comando/Acción |
|-------|-----------------|
| **Ver procesos** | `Ctrl+Shift+Esc` → Task Manager |
| **Ver memoria** | Pestaña "Rendimiento" |
| **Ver archivos abiertos** | `Ctrl+Shift+Esc` → Pestaña "Detalles" |
| **Terminal** | `Windows + X` → Windows PowerShell |

#### 🐧 Linux / macOS
| Tarea | Comando/Acción |
|-------|-----------------|
| **Ver procesos** | `top` o `htop` |
| **Ver memoria** | `free -h` (Linux) o `vm_stat` (macOS) |
| **Ver archivos abiertos** | `lsof` |
| **Terminal** | `Ctrl+Alt+T` o buscar "Terminal" |

</div>

<div>

### Preguntas para discutir:

1. **¿Cuántos procesos** están corriendo?
   - ¿Por qué hay tantos que no reconoces?

2. **¿Cuánta memoria** está en uso?
   - ¿Qué pasa si se llena?

3. **¿Qué proceso** consume más CPU?
   - ¿Es esperado o sospechoso?

4. **¿Por qué Linux** domina servidores?
   - Basado en lo que observaste

### 🎯 Objetivo
Conectar la teoría con la realidad: **tu computador está ejecutando cientos de procesos simultáneamente**, coordinados por el SO.

</div>

</div>

<div style="text-align: center; margin-top: 20px; padding: 15px; background: #fef3c7; border-radius: 10px;">

**💡 Compartan sus descubrimientos con la clase. ¿Algo les sorprendió?**

</div>

---

## Resumen

| Concepto | Clave |
|----------|-------|
| **SO** = Intermediario usuario ↔ hardware |
| **4 funciones**: Procesos, Memoria, Archivos, E/S |
| **Arquitecturas**: Monolítico, Capas, Microkernel |
| **System call** = Puerta al kernel |
| **Interfaces**: GUI (fácil) vs CLI (potente) |

---

## Próxima Clase

### Clase 2: Evolución y Componentes del SO

- 📜 Historia de los SO
- 🏗️ Componentes: Kernel, Shell, Utilidades
- 🔐 Modos: Usuario vs Kernel

**¡Nos vemos!**
