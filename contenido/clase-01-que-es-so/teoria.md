# Teoría Expandida - Clase 1: ¿Qué es un Sistema Operativo?

**IF0099 - Sistemas Operativos I**

---

## 1. ¿Qué es un Sistema Operativo?

### Definición Formal

Un **Sistema Operativo (SO)** es el software fundamental que gestiona los recursos de hardware y provee servicios para los programas de aplicación. Actúa como intermediario entre el usuario/aplicaciones y el hardware del computador.

```
┌─────────────────────────────────────────────────────────┐
│                    CAPA DE APLICACIÓN                   │
│  (Navegadores, Juegos, Procesadores de texto, etc.)    │
├─────────────────────────────────────────────────────────┤
│                  SISTEMA OPERATIVO                      │
│  (Gestiona recursos, provee servicios, protección)     │
├─────────────────────────────────────────────────────────┤
│                      HARDWARE                           │
│  (CPU, RAM, Disco, Red, Dispositivos E/S)             │
└─────────────────────────────────────────────────────────┘
```

### ¿Por qué es importante?

El SO es esencial porque:

1. **Abstrae la complejidad del hardware**: Los programadores no necesitan conocer los detalles de cómo funciona cada dispositivo
2. **Maximiza el uso de recursos**: Permite que múltiples programas compartan CPU, RAM y otros recursos
3. **Protege el sistema**: Aísla procesos entre sí, evitando que un programa malicioso o con errores afecte a otros
4. **Provee una interfaz uniforme**: El mismo código funciona en diferentes hardware

### Analogía del Gerente de Hotel

Un SO es como el gerente de un hotel:

| Hotel | Computador |
|-------|------------|
| Huéspedes | Procesos/Programas |
| Habitaciones | Memoria RAM |
| Gerente | Sistema Operativo |
| Recepcionista | Scheduler |
| Personal de limpieza | Gestor de memoria |
| Seguridad | Protección de procesos |

**Sin el gerente**, los huéspedes pelearían por las habitaciones. **Sin el SO**, los programas pelearían por la RAM.

---

## 2. Funciones Principales del SO

### 2.1 Gestión de Procesos

Un **proceso** es un programa en ejecución. El SO es responsable de:

- **Creación y destrucción**: `fork()` crea procesos, `exit()` los termina
- **Scheduling (Planificación)**: Decide qué proceso ejecuta en cada momento
- **Sincronización**: Coordinación entre procesos que comparten recursos
- **Comunicación (IPC)**: Mecanismos para que procesos se intercambien datos

#### Estados de un Proceso

```
    NUEVO → LISTO → EJECUTANDO → BLOQUEADO → TERMINADO
              ↑         ↓            ↓
              └─────────┴────────────┘
              (scheduler/Interrupciones)
```

| Estado | Descripción | Ejemplo |
|--------|-------------|---------|
| **NUEVO** | Proceso being creado | `fork()` llamado |
| **LISTO** | Esperando por CPU | En cola de ready |
| **EJECUTANDO** | Usando CPU ahora | Instrucciones ejecutándose |
| **BLOQUEADO** | Esperando I/O | Leyendo del disco |
| **TERMINADO** | Ejecución completada | `exit()` llamado |

### 2.2 Gestión de Memoria

El SO administra la RAM como un edificio de apartamentos:

- **Asignación**: Dar memoria a procesos cuando la necesitan
- **Liberación**: Recuperar memoria cuando procesos terminan
- **Protección**: Evitar que un proceso acceda a memoria de otro
- **Memoria Virtual**: Usar disco como extensión de RAM (swap/paging)

#### Problemas Clave

| Problema | Descripción | Solución |
|----------|-------------|----------|
| **Fragmentación** | Huecos entre bloques de memoria | Compacción, paginación |
| **Thrashing** | Excesivo swapping, CPU inactiva | Aumentar RAM, ajustar parámetros |
| **Fugas de memoria** | Memoria no liberada | Herramientas de detección |

### 2.3 Gestión de Archivos

El SO organiza datos en **sistemas de archivos jerárquicos**:

```
/ (raíz)
├── home/
│   └── usuario/
│       ├── documentos/
│       └── imágenes/
├── usr/
│   └── bin/
├── etc/
└── var/
```

#### Operaciones Básicas (System Calls)

| Operación | System Call | Descripción |
|-----------|-------------|-------------|
| Crear | `creat()` | Crea nuevo archivo |
| Leer | `read()` | Lee bytes del archivo |
| Escribir | `write()` | Escribe bytes al archivo |
| Abrir | `open()` | Abre archivo existente |
| Cerrar | `close()` | Cierra archivo abierto |
| Eliminar | `unlink()` | Borra archivo |

### 2.4 Gestión de E/S (Entrada/Salida)

El SO controla dispositivos mediante **drivers** y técnicas de E/S:

#### Técnicas de E/S

| Técnica | Descripción | Eficiencia | Uso |
|---------|-------------|------------|-----|
| **Polling** | CPU pregunta repetidamente | ❌ Baja | Casi obsoleto |
| **Interrupciones** | Dispositivo avisa a CPU | ✅ Alta | Estándar |
| **DMA** | Memoria ↔ Dispositivo directo | ✅ Máxima | Discos, red |

---

## 3. Arquitecturas del Sistema Operativo

### 3.1 Monolítico

Todos los servicios del SO corren en **modo kernel**:

```
┌─────────────────────────────────┐
│   Todas las funciones del SO    │
│   (Gestión archivos, procesos,   │
│    memoria, E/S, etc.)          │
├─────────────────────────────────┤
│         KERNEL ÚNICO            │
├─────────────────────────────────┤
│          HARDWARE               │
└─────────────────────────────────┘
```

**Ventajas:**
- ✅ Rápido (sin overhead de comunicación)
- ✅ Simple de implementar

**Desventajas:**
- ❌ Difícil de mantener
- ❌ Un fallo = crash del sistema
- ❌ Complejo de depurar

**Ejemplos:** Linux, MS-DOS, Unix BSD

### 3.2 Capas (Layered)

El SO está organizado en **capas jerárquicas**:

```
┌─────────────────────────────────┐
│       Nivel 5: Aplicaciones     │
├─────────────────────────────────┤
│   Nivel 4: Utilidades           │
├─────────────────────────────────┤
│  Nivel 3: Gestión de recursos   │
├─────────────────────────────────┤
│   Nivel 2: Núcleo del SO        │
├─────────────────────────────────┤
│    Nivel 1: Hardware            │
├─────────────────────────────────┤
│      Nivel 0: Físico            │
└─────────────────────────────────┘
```

**Ventajas:**
- ✅ Modular y más fácil de mantener
- ✅ Más seguro (capas aíslan funciones)

**Desventajas:**
- ❌ Overhead por capas
- ❌ Más lento que monolítico

**Ejemplos:** THE, VMS, Windows (híbrido)

### 3.3 Microkernel

Solo lo **esencial** corre en modo kernel; el resto corre en **espacio de usuario**:

```
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│Servidor      │  │Servidor      │  │Servidor      │
│Archivos      │  │Procesos      │  │Memoria       │
│(user space)  │  │(user space)  │  │(user space)  │
└──────┬───────┘  └──────┬───────┘  └──────┬───────┘
      │                 │                 │
      │      IPC        │                 │
      └────────┬────────┴─────────────────┘
               │
        ┌──────▼──────────┐
        │  MICROKERNEL    │
        │  (modo kernel)  │
        │  - IPC          │
        │  - Scheduling   │
        │  - Memoria básica│
        └──────┬──────────┘
               │
           HARDWARE
```

**Ventajas:**
- ✅ Más seguro (menos código en kernel)
- ✅ Flexible (agregar servicios sin recompilar)
- ✅ Más mantenible (fallos en user space no crashean sistema)

**Desventajas:**
- ❌ Más lento (IPC entre servicios)
- ❌ Complejo de diseñar

**Ejemplos:** MINIX 3, QNX, GNU Hurd

---

## 4. System Calls (Llamadas al Sistema)

### ¿Qué son las System Calls?

Las **system calls** son la **puerta de entrada** al kernel. Son funciones que permiten a los programas solicitar servicios del SO que requieren privilegios especiales.

### Flujo de una System Call

```
Usuario                    Kernel
  │                          │
  │ printf("hola")           │
  ▼                          │
┌─────────┐                 │
│ libc    │                 │
│ write() │                 │
└────┬────┘                 │
     │                      │
     │ syscall (TRAP)        │
     ▼                      │
┌─────────┐ ──────────────► │
│  TRAP   │  Cambio modo    │
│ (cambio │  usuario→kernel │
│  modo)  │                 │
         ─────────────────► │
                             ▼
                    ┌──────────────┐
                    │ sys_write()  │
                    │ - Valida     │
                    │ - Ejecuta    │
                    │ - Retorna    │
                    └──────────────┘
                             │
         ◄──────────────────┘
     │                        │
     ▼                        │
┌─────────┐                   │
│ libc    │                   │
└────┬────┘                   │
     │                        │
     ▼                        │
  printf()                     │
     │                        │
     ▼                        │
  Usuario                      │
```

### Categorías de System Calls

| Categoría | Ejemplos | Propósito |
|-----------|----------|-----------|
| **Control de procesos** | `fork()`, `exec()`, `wait()`, `exit()` | Crear/destruir procesos |
| **Manipulación archivos** | `open()`, `read()`, `write()`, `close()` | Operaciones I/O |
| **Gestión directorios** | `mkdir()`, `rmdir()`, `chdir()` | Navegar sistema archivos |
| **Comunicaciones** | `socket()`, `bind()`, `listen()`, `accept()` | Comunicación en red |
| **Información sistema** | `getpid()`, `getuid()`, `time()` | Obtener datos del sistema |

---

## 5. El SO como Interfaz

### GUI vs CLI

| Aspecto | GUI (Gráfica) | CLI (Comandos) |
|---------|---------------|----------------|
| **Facilidad de uso** | ✅ Muy fácil | ❌ Curva de aprendizaje |
| **Potencia** | ⚠️ Limitada | ✅ Completa |
| **Automatización** | ❌ Difícil | ✅ Fácil (scripts) |
| **Recursos** | 💾 ~500MB RAM | 💾 ~5MB RAM |
| **Uso ideal** | Usuarios caseros | Administradores, desarrolladores |

**Ejemplos:**
- **GUI:** Windows Explorer, macOS Finder, GNOME Nautilus
- **CLI:** bash, zsh, PowerShell, cmd

---

## 6. Sistemas Operativos Actuales (2026)

### Por Plataforma

| Plataforma | Líder | Cuota de mercado | Por qué |
|------------|-------|------------------|---------|
| **Escritorio** | Windows | 70% | Compatibilidad, Office, Gaming |
| **Servidores** | Linux | 96% | Gratis, estable, Docker/K8s |
| **Móviles** | Android | 71% | Código abierto, ecosistema |

**Insight:** Cada SO domina donde resuelve mejor un problema específico.

---

## Conceptos Clave

| Concepto | Definición |
|----------|------------|
| **Sistema Operativo** | Software intermediario entre usuario y hardware |
| **Proceso** | Programa en ejecución con sus recursos |
| **System Call** | Puerta controlada al kernel |
| **Kernel** | Núcleo del SO, corre en modo privilegiado |
| **Arquitectura** | Cómo se organiza el SO internamente |
| **GUI** | Interfaz gráfica de usuario |
| **CLI** | Interfaz de línea de comandos |

---

**Última actualización**: 2026-02-01
