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

```
┌─────────────────────────────────────────┐
│                                         │
│   👤 USUARIO / APLICACIONES             │
│                                         │
│   ═══════════════════════════════════   │
│                                         │
│   🖥️  SISTEMA OPERATIVO                 │
│                                         │
│   ═══════════════════════════════════   │
│                                         │
│   ⚡ HARDWARE (CPU, RAM, Disco)         │
│                                         │
└─────────────────────────────────────────┘
```

![Capas del Sistema](../../assets/infografias/so-capas-sistema.png)

---

## ¿Por qué necesitamos un SO?

| Sin SO | Con SO |
|--------|--------|
| Cada programa maneja el hardware | El SO maneja todo |
| Muy complejo para programadores | Interfaz simple |
| No se pueden ejecutar varios programas | Multiprogramación |
| Sin protección entre programas | Memoria protegida |

**El SO hace que el hardware sea usable**

---

## Analogía: El Hotel 🏨

```
┌──────────────────────────────────────────────────┐
│                                                  │
│   🏨 HUESPEDES     ↔     💻 APLICACIONES         │
│      (clientes)              (programas)         │
│                                                  │
│   🎯 GERENTE        ↔     🖥️  SISTEMA OPERATIVO  │
│   (asigna habitaciones)    (asigna recursos)     │
│                                                  │
│   🛏️ HABITACIONES  ↔     💾 MEMORIA RAM          │
│   (recursos limitados)     (espacio limitado)    │
│                                                  │
└──────────────────────────────────────────────────┘
```

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

![Funciones del SO](../../assets/infografias/so-funciones-principales.png)

<div style="display: flex; gap: 20px; margin-top: 20px;">
<div style="flex: 1; text-align: center;">📊 Gestión de Procesos</div>
<div style="flex: 1; text-align: center;">💾 Gestión de Memoria</div>
<div style="flex: 1; text-align: center;">📁 Gestión de Archivos</div>
<div style="flex: 1; text-align: center;">🔌 Gestión de E/S</div>
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

```
    📝 CREADO
        │
        ▼
    🏃 LISTO ──→ 🎯 EJECUTANDO
        │          │
        │          ▼
        │      ⏸️ BLOQUEADO
        │          │
        └──────────┴──→ ✅ TERMINADO
```

**El SO gestiona:** crear, suspender, reanudar, sincronizar, comunicar

---

## 2.2 Gestión de Memoria

### La RAM como edificio

```
┌─────────────────────────────────────┐
│     🏢 EDIFICIO RAM (16 GB)          │
├─────────┬─────────┬─────────┬───────┤
│ SO 2GB  │ Chrome  │ Spotify │ Libre │
│ 🔴      │ 🟡      │ 🟢      │ ⚪    │
└─────────┴─────────┴─────────┴───────┘
```

| Función | Descripción |
|---------|-------------|
| **Asignar** | Dar memoria a procesos |
| **Liberar** | Recuperar memoria |
| **Proteger** | Chrome no lee Spotify |
| **Virtual** | Swap: disco como RAM |

---

## 2.3 Gestión de Archivos

### Sistema jerárquico

```
📁 C:\ o / (raíz)
├── 📁 Windows/ o /bin
├── 📁 Program Files/
├── 📁 Users/
│   └── 📁 estudiante/
│       ├── 📁 Documentos/
│       ├── 📁 Descargas/
│       └── 📁 Escritorio/
└── 📁 ...
```

**El SO es el bibliotecario:** sabe dónde está todo

---

## 2.4 Gestión de E/S

### Dispositivos de entrada/salida

| Entrada ⬇️ | Salida ⬆️ | Ambos ↕️ |
|------------|-----------|----------|
| ⌨️ Teclado | 🖥️ Monitor | 💾 Disco |
| 🖱️ Mouse | 🖨️ Impresora | 🔌 USB |
| 🎤 Mic | 🔊 Altavoz | 🌐 Red |

**El SO usa drivers** para "hablar" con cada dispositivo

---

## 3. Arquitecturas del SO

### Tipos de estructura

```
┌─────────────────────────────────────────────────┐
│          MONOLÍTICO               CAPAS         │
│      (Linux, MS-DOS)        (THE, VAX/VMS)     │
│                                                 │
│    ┌─────────┐              ┌─────────┐        │
│    │  TODO   │              │ Nivel 5 │        │
│    │ JUNTO   │              │   ...   │        │
│    │         │              │ Nivel 0 │        │
│    └─────────┘              └─────────┘        │
│                                                 │
│      Rápido              Seguro, Modular       │
│      Difícil mantener    Lento (overhead)       │
└─────────────────────────────────────────────────┘
```

---

## Microkernel: El enfoque minimalista

```
┌──────────────────────────────────────────┐
│                                          │
│  📁 Archivos  📊 Memoria  🔄 Procesos   │
│    (user)       (user)      (user)       │
│         │           │           │         │
│         └───────────┼───────────┘         │
│                     │                     │
│              ┌──────┴──────┐             │
│              │  MICROKERNEL│             │
│              │   (mínimo)  │             │
│              └──────┬──────┘             │
│                     │                     │
│                  HARDWARE                │
└──────────────────────────────────────────┘
```

**Solo en kernel:** IPC, scheduling básico, memoria básica

---

## Comparación de Arquitecturas

| | Monolítico | Capas | Microkernel |
|---|-----------|-------|-------------|
| **Rendimiento** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **Seguridad** | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Mantenibilidad** | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Ejemplos** | Linux, DOS | THE, VMS | MINIX, QNX |

---

## 4. System Calls (Llamadas al Sistema)

### La puerta entre usuario y kernel

```
┌─────────────────────────────────────────────┐
│  👤 USUARIO               🔧 KERNEL          │
│                                              │
│  printf("Hola")                              │
│      │                                       │
│      ▼                                       │
│  libc: write()                              │
│      │                                       │
│      ▼                                       │
│  ┌─────────┐          ┌─────────────────┐  │
│  │  TRAP   │ ────────► │ sys_write()     │  │
│  │ (syscall)│          │ en kernel       │  │
│  └─────────┘          └─────────────────┘  │
│                              │              │
│                              ▼              │
│                         🖴 DRIVER DISCO    │
└─────────────────────────────────────────────┘
```

---

## System Calls: Categorías

| Categoría | Ejemplos | Qué hace |
|-----------|----------|----------|
| **Procesos** | `fork()`, `exec()`, `exit()` | Crear/terminar |
| **Archivos** | `open()`, `read()`, `write()` | Manipular archivos |
| **Dispositivos** | `ioctl()`, `read()` | Controlar hardware |
| **Info** | `getpid()`, `time()` | Obtener datos |
| **Comms** | `pipe()`, `socket()` | IPC y red |

---

## 5. El SO como Interfaz

### Dos formas de interactuar

```
       👤 USUARIO
          │
     ┌────┴────┐
     │         │
     ▼         ▼
┌─────────┐ ┌─────────┐
│   GUI   │ │   CLI   │
│ Gráfica │ │Comandos │
└─────────┘ └─────────┘
 Windows    bash/PowerShell
 macOS      Terminal
 GNOME      zsh
```

---

## GUI vs CLI

| Aspecto | GUI | CLI |
|---------|-----|-----|
| Facilidad | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| Potencia | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Automatización | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| Recursos | Alto | Bajo |
| Servidores | Raro | **Estándar** |

---

## 6. Sistemas Operativos Actuales

### Dominio por plataforma

```
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│   ESCRITORIO     │ │    SERVIDORES    │ │     MÓVILES      │
│   Windows 70%    │ │    Linux 96%     │ │   Android 71%    │
│   macOS   16%    │ │    Windows 4%    │ │   iOS     28%    │
│   Linux    4%    │ │                  │ │                  │
└─────────────────┘ └─────────────────┘ └─────────────────┘
```

**Insight:** Linux domina servidores pero no escritorios. ¿Por qué?

---

## ¿Por qué cada SO domina su nicho?

### Windows: 👔 Escritorio corporativo
- Office, SAP, Adobe
- Soporte global
- Familiar para usuarios

### Linux: 🖥️ Servidores
- Gratis y estable
- Uptime de años
- 96% de servidores web

### macOS: 🎨 Creativos
- Video, música, diseño
- Desarrollo iOS
- Ecosistema Apple

---

## 7. Actividad Práctica

### En parejas, investiguen:

| Tarea | Instrucciones |
|-------|---------------|
| **1️⃣ Ver procesos** | `Ctrl+Shift+Esc` (Windows) o `top` (Linux) |
| **2️⃣ Ver memoria** | Pestaña "Rendimiento" o `free -h` |
| **3️⃣ Discutir** | ¿Por qué Linux en servidores? |

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
