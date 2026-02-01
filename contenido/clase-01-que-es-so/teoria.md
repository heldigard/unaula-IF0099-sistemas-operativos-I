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

El SO administra la RAM como un edificio de apartamentos.

> **¿Qué es RAM?** La **Random Access Memory** (Memoria de Acceso Aleatorio) es la memoria principal del computador. Es volátil (pierde datos sin energía) y muy rápida. El SO la asigna a los procesos para que ejecuten sus programas.

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

#### Explicación de Problemas Clave

**Fragmentación:** Ocurre cuando la memoria libre está dispersa en pequeños huecos no contiguos. Aunque haya suficiente memoria total, ningún hueco individual es lo bastante grande para un proceso nuevo.

- **Error común:** Creer que fragmentación = "memoria llena". ¡No es lo mismo! Puedes tener 100MB libres pero fragmentados en 10 bloques de 10MB, y un proceso que necesite 50MB no podrá cargarse.

**Thrashing:** El sistema pasa más tiempo swapping (moviendo datos entre RAM y disco) que ejecutando programas. Ocurre cuando hay demasiados procesos para la RAM disponible.

- **Señal:** El disco está 100% ocupado pero la CPU está ociosa
- **Causa típica:** Abrir demasiadas pestañas del navegador simultáneamente

**Memoria Virtual y Paginación:**

- **Memoria Virtual:** Técnica que permite al computador "engañar" a los programas haciéndoles creer que tienen más RAM de la que realmente existe. Usa espacio en disco como extensión de la RAM.

- **Paginación:** Divide la memoria en bloques de tamaño fijo llamados "páginas" (típicamente 4KB). El SO mueve páginas entre RAM y disco según se necesiten.

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

> **¿Qué es E/S?** **Entrada/Salida** (Input/Output, I/O) se refiere a toda comunicación entre el computador y el mundo exterior: teclado, mouse, monitor, disco, red, etc.

El SO controla dispositivos mediante **drivers** y técnicas de E/S:

#### Técnicas de E/S

| Técnica | Descripción | Eficiencia | Uso |
|---------|-------------|------------|-----|
| **Polling** | CPU pregunta repetidamente | ❌ Baja | Casi obsoleto |
| **Interrupciones** | Dispositivo avisa a CPU | ✅ Alta | Estándar |
| **DMA** | Memoria ↔ Dispositivo directo | ✅ Máxima | Discos, red |

#### DMA (Direct Memory Access) - Explicación Detallada

> **¿Qué es DMA?** El **Acceso Directo a Memoria** es un mecanismo que permite a los dispositivos transferir datos directamente hacia/desde la RAM sin intervenir a la CPU.

**Sin DMA:** La CPU debe controlar cada byte de transferencia, lo que la deja ocupada y no puede hacer otras tareas.

**Con DMA:** Un controlador especial llamado "controlador DMA" maneja la transferencia. La CPU solo:
1. Configura la transferencia (dirección origen, destino, cantidad)
2. Inicia el controlador DMA
3. Continúa con otras tareas
4. Recibe una interrupción cuando la transferencia termina

**Ejemplo:** Cuando copias un archivo de 1GB, el DMA mueve los datos entre disco y RAM mientras la CPU puede seguir respondiendo al mouse y teclado.

#### IPC (Inter-Process Communication)

> **¿Qué es IPC?** La **Comunicación entre Procesos** es el conjunto de mecanismos que permiten a los procesos intercambiar datos y sincronizarse.

**Mecanismos IPC comunes:**
- **Pipes:** Canales unidireccionales (ej: `ls | grep`)
- **Sockets:** Comunicación en red
- **Memoria compartida:** Zonas de memoria accesibles por múltiples procesos
- **Semáforos:** Sincronización (control de acceso a recursos compartidos)
- **Mensajes:** Colas de mensajes entre procesos

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

> **¿Por qué son necesarias?** Los programas de aplicación (modo usuario) NO pueden acceder directamente al hardware por razones de seguridad. Las system calls son la ÚNICA forma válida de solicitar servicios del kernel.

### Modos de Ejecución: Usuario vs Kernel

Los procesadores modernos tienen **anillos de protección** (protection rings):

| Modo | Anillo | Privilegios | ¿Qué puede hacer? | Ejemplo |
|------|-------|-------------|-------------------|---------|
| **Kernel** | Ring 0 | Máximo | Acceso total a hardware, toda la memoria, cualquier instrucción | El SO y drivers |
| **Usuario** | Ring 3 | Mínimo | Solo su propia memoria, instrucciones no privilegiadas | Chrome, VS Code, juegos |

**Analogía del edificio:**
- **Modo Usuario:** Piso público (puedes moverte libremente, pero no entrar a áreas restringidas)
- **Modo Kernel:** Sótano de seguridad (acceso total, incluido la bóveda)

**¿Por qué la separación?**
- **Seguridad:** Un programa malicioso no puede leer tus archivos directamente
- **Estabilidad:** Si un programa falla, NO crashea todo el sistema
- **Aislamiento:** Cada proceso está en su "sandbox" (arena aislada)

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

| Plataforma | Líder | Cuota de mercado (2025-2026) | Por qué |
|------------|-------|-----------------------------|---------|
| **Escritorio** | Windows | ~67-70% | Compatibilidad, Office, Gaming |
| **Servidores** | Linux | ~44-96% (web: 96%) | Gratis, estable, Docker/K8s, 92% VMs en cloud |
| **Móviles** | Android | ~71-73% | Código abierto, ecosistema |

**Nota:** Las cifras varían según la fuente (StatCounter, DemandSage, CommandLinux). Los datos presentados son los más recientes disponibles a inicios de 2026.

### Tendencias Importantes

**Desktop Linux en crecimiento:**
- Linux desktop alcanzó **4.7%** global en 2025 (70% de aumento desde 2022)
- En Estados Unidos alcanzó **5.38%** en 2025
- Proyecciones para 2026 sugieren que podría alcanzar **6%**

**Servidores:**
- Linux domina el 96% de servidores web
- **92%** de las máquinas virtuales en plataformas cloud (AWS, Google Cloud, Azure) corren Linux
- Windows Server mantienen fuerte presencia en entornos empresariales tradicionales (~4-11% en web)

**Móviles:**
- Android: 71-73% global, pero iOS domina en ingresos (50%+ de ingresos del mercado)
- Juntos, Android e iOS controlan más del **99%** del mercado móvil

**Insight:** Cada SO domina donde resuelve mejor un problema específico. Linux gana donde la tecnología importa (servidores, desarrolladores); Windows gana en facilidad de uso y compatibilidad.

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
