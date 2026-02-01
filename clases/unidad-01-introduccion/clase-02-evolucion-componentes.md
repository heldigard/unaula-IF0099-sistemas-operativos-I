---
marp: true
theme: default
paginate: true
header: 'IF0099 - Sistemas Operativos I | Unidad 1'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
---

# Clase 2: Evolución y Componentes del SO
## De las tarjetas perforadas a la nube

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
[2026-01-31] - Clase enriquecida con infografías

IMÁGENES GENERADAS:
- so-evolucion-timeline.png: Línea de tiempo de la evolución de SO
- so-componentes-arquitectura.png: Diagrama de arquitectura en capas (Hardware, Kernel, Servicios, Apps)
-->

---

**IF0099 - Sistemas Operativos I**
*4° Semestre - Ingeniería Informática*

---

## Objetivos de la Clase

Al finalizar esta clase, el estudiante será capaz de:

1. **Describir** la evolución histórica de los sistemas operativos
2. **Identificar** las generaciones de sistemas operativos
3. **Explicar** los componentes principales de un SO
4. **Diferenciar** modo usuario vs modo kernel

**Duración:** 90 minutos

---

## Agenda

1. Generación 0: Sin SO (1940s) - 10 min
2. Primera a Cuarta Generación - 25 min
3. Componentes del SO moderno - 25 min
4. Modo Usuario vs Modo Kernel - 20 min
5. Actividad práctica - 10 min

---

## Línea de Tiempo de los SO


### ¿Por qué estudiar la evolución?

Entender la historia nos ayuda a:
- 📚 Comprender decisiones de diseño actuales
- 🔍 Aprender de errores pasados
- 🚀 Anticipar tendencias futuras
- 💡 Valorar la complejidad actual

**Cada generación resolvió problemas específicos de su época.**


![Evolución de los Sistemas Operativos](../../assets/infografias/so-evolucion-timeline.png)

### Hitos Clave en la Evolución

| Período | Avance Tecnológico | Problema Resuelto |
|---------|-------------------|-------------------|
| **1940s** | Sin SO | Programación manual con cables |
| **1950s** | Batch processing | Automatizar secuencia de trabajos |
| **1960s** | Multiprogramación | CPU ociosa durante E/S |
| **1970s** | Time-sharing | Múltiples usuarios interactivos |
| **1980s** | GUI personal | Computación accesible para todos |
| **2000s+** | Virtualización/cloud | Escalabilidad y servicios on-demand |

---

## Generación 0: Sin Sistema Operativo (1940-1950)

### Características
- **ENIAC, UNIVAC**: Primeras computadoras
- Programación con **cables y switches**
- **Una persona** = un programa = toda la máquina
- Sin concepto de "software de sistema"

```
┌─────────────────────────────────┐
│    PROGRAMADOR                  │
│         │                       │
│         ▼                       │
│  ┌─────────────┐               │
│  │  HARDWARE   │ (directo)     │
│  └─────────────┘               │
└─────────────────────────────────┘
```

**Problema:** Desperdicio de tiempo y recursos

---

## Primera Generación: Procesamiento por Lotes (1950-1965)

### Batch Processing

```
┌─────────────────────────────────────────┐
│ 1. Programador escribe código en papel  │
│              ↓                          │
│ 2. Operador perfora tarjetas            │
│              ↓                          │
│ 3. Tarjetas se acumulan en "lote"       │
│              ↓                          │
│ 4. Computador procesa todo el lote      │
│              ↓                          │
│ 5. Resultados en impresora (horas después)│
└─────────────────────────────────────────┘
```

### Primer SO: **GM-NAA I/O** (1956) - General Motors

---

## Segunda Generación: Multiprogramación (1965-1980)

### Múltiples programas en memoria

```
┌────────────────────────────────┐
│         MEMORIA RAM            │
├────────────────────────────────┤
│  Sistema Operativo             │
├────────────────────────────────┤
│  Programa A (esperando E/S)    │
├────────────────────────────────┤
│  Programa B (ejecutando)       │ ← CPU
├────────────────────────────────┤
│  Programa C (esperando E/S)    │
└────────────────────────────────┘
```

### Sistemas importantes
- **IBM OS/360** (1964)
- **MULTICS** (1969) - Precursor de UNIX

---

## Nacimiento de UNIX (1969)

### Ken Thompson y Dennis Ritchie - Bell Labs

```
      ┌─────────────────┐
      │    MULTICS      │ (muy complejo)
      │    (fallido)    │
      └────────┬────────┘
               │ Thompson y Ritchie
               │ simplifican
               ▼
      ┌─────────────────┐
      │     UNIX        │
      │ "Una cosa bien" │
      └─────────────────┘
```

### Innovaciones de UNIX:
- Escrito en **C** (portable)
- Filosofía: "Haz una cosa y hazla bien"
- Todo es un archivo
- Base de Linux, macOS, Android

---

## Tercera Generación: Tiempo Compartido (1970-1990)

### Time-Sharing: Múltiples usuarios simultáneos

```
Usuario 1 ──┐
            │
Usuario 2 ──┼──→ [SO Time-Sharing] ──→ [CPU]
            │         │
Usuario 3 ──┘    Reparte tiempo
                 en "tajadas"
```

### Sistemas importantes:
- **UNIX** (1969-presente)
- **VMS** (DEC)
- **CP/M** (microcomputadores)

---

## Cuarta Generación: Computadoras Personales (1980-2000)

### La era del PC

| Año | Sistema | Importancia |
| ----- | --------- | ------------- |
| 1981 | MS-DOS | IBM PC |
| 1984 | Mac OS | Primera GUI comercial exitosa |
| 1985 | Windows 1.0 | Intento de GUI sobre DOS |
| 1991 | **Linux** | SO libre y abierto |
| 1995 | Windows 95 | GUI dominante |

**Impacto histórico:** Esta generación democrató el acceso a la computación, llevando los computadores de las grandes empresas a los hogares.

---

## Quinta Generación: SO Modernos (2000-presente)

### Características actuales:
- **Multitarea real** (múltiples núcleos)
- **Conectividad** (redes, Internet)
- **Seguridad** (permisos, encriptación)
- **Virtualización** (VMs, contenedores)
- **Cloud computing** (SO en la nube)

### Sistemas actuales (2026):
- Windows 11
- macOS Sequoia
- Ubuntu 24.04 LTS
- Android 16
- iOS 19

---

## Componentes de un SO Moderno

![Arquitectura del Sistema Operativo](../../assets/infografias/so-componentes-arquitectura.png)

### Capas de Abstracción

Cada capa oculta la complejidad de la inferior:
- **Aplicaciones** → No conocen el hardware específico
- **Shell** → Interpreta comandos sin saber del kernel
- **Kernel** → Gestiona recursos sin exponer detalles físicos
- **Hardware** → Componentes físicos reales

---

### Representación ASCII:
```
┌─────────────────────────────────────────────────┐
│                  APLICACIONES                   │
├─────────────────────────────────────────────────┤
│              UTILIDADES DEL SISTEMA             │
│    (Administrador archivos, Terminal, etc.)     │
├─────────────────────────────────────────────────┤
│                    SHELL                        │
│         (Intérprete de comandos / GUI)          │
├─────────────────────────────────────────────────┤
│            LLAMADAS AL SISTEMA (API)            │
├─────────────────────────────────────────────────┤
│                   KERNEL                        │
│  ┌──────────┬──────────┬──────────┬──────────┐ │
│  │ Gestor   │ Gestor   │ Sistema  │ Gestor   │ │
│  │ Procesos │ Memoria  │ Archivos │   E/S    │ │
│  └──────────┴──────────┴──────────┴──────────┘ │
├─────────────────────────────────────────────────┤
│                   HARDWARE                      │
└─────────────────────────────────────────────────┘
```

---

## El Kernel (Núcleo)

### El corazón del Sistema Operativo

```
         Aplicaciones
              │
              ▼
    ┌─────────────────┐
    │     KERNEL      │ ← Siempre en memoria
    │                 │ ← Código privilegiado
    │ - Planificador  │ ← Acceso a hardware
    │ - Memoria       │
    │ - Drivers       │
    │ - Sistema arch. │
    └─────────────────┘
              │
              ▼
         Hardware
```

### Tipos de Kernel y sus Características

| Tipo | Estructura | Ventajas | Ejemplos |
|------|------------|----------|----------|
| **Monolítico** | Todo en un solo espacio de memoria | Rápido, comunicación directa | Linux, Windows clásico |
| **Microkernel** | Mínimo en kernel, servicios en usuario | Seguro, mantenible | Minix, QNX, seL4 |
| **Híbrido** | Kernel monolítico + características microkernel | Balance rendimiento/seguridad | macOS (XNU), Windows NT |
| **Exokernel** | Mínimo, bibliotecas de usuario controlan recursos | Máxima flexibilidad | MIT Exokernel (investigación) |

> **Nota:** Linux es monolítico pero soporta módulos cargables, lo que le da cierta flexibilidad de microkernel.

---

## El Shell

### Interfaz entre usuario y kernel

```
┌────────────────────────────────────────┐
│            USUARIO                     │
└───────────────┬────────────────────────┘
                │ escribe comando
                ▼
┌────────────────────────────────────────┐
│             SHELL                      │
│  $ ls -la /home                        │
│                                        │
│  - Interpreta el comando               │
│  - Llama al kernel                     │
│  - Muestra resultado                   │
└───────────────┬────────────────────────┘
                │ llamada al sistema
                ▼
┌────────────────────────────────────────┐
│            KERNEL                      │
└────────────────────────────────────────┘
```

### Shells populares: **bash**, zsh, PowerShell, fish

---

## Llamadas al Sistema (System Calls)

### La API del Sistema Operativo

```c
// Ejemplo: Abrir un archivo
int fd = open("/home/user/archivo.txt", O_RDONLY);

// El programa NO accede al disco directamente
// Pide al kernel que lo haga por él
```

### Categorías de system calls:

| Categoría | Ejemplos |
| ----------- | ---------- |
| Procesos | fork(), exec(), exit(), wait() |
| Archivos | open(), read(), write(), close() |
| Dispositivos | ioctl(), read(), write() |
| Información | getpid(), time(), uname() |
| Comunicación | pipe(), socket(), send() |

---

## Modo Usuario vs Modo Kernel

### Los "Anillos" de Protección (Protection Rings)

Los procesadores modernos implementan **4 niveles de privilegio** (0-3), aunque la mayoría de SO solo usan 2:

```
┌─────────────────────────────────────────────────────┐
│  Ring 0  │  MODO KERNEL  │  Kernel, drivers         │
│          │  (Máximo)     │  Acceso total            │
├─────────────────────────────────────────────────────┤
│  Ring 1  │  (No usado)   │  Reservado               │
├─────────────────────────────────────────────────────┤
│  Ring 2  │  (No usado)   │  Reservado               │
├─────────────────────────────────────────────────────┤
│  Ring 3  │  MODO USUARIO │  Aplicaciones normales   │
│          │  (Mínimo)     │  Acceso restringido      │
└─────────────────────────────────────────────────────┘
```

> **¿Por qué solo 2 rings?** Simplifica el diseño del SO. OS/2 y antiguos Windows usaban Ring 2 para drivers.

---

## Comparación: Modo Usuario vs Modo Kernel

<div style="display: flex; gap: 15px;">

<div style="flex: 1;">

### 🔵 MODO USUARIO (Ring 3)
- **Aplicaciones normales** (Chrome, VS Code, juegos)
- **NO puede acceder hardware directamente**
- **Memoria aislada** (solo su espacio asignado)
- **Instrucciones prohibidas**: IN, OUT, CLI, HLT
- **Si falla**: Solo muere la aplicación
- **Ejemplo**: `printf()` → solicita servicio al kernel

</div>

<div style="flex: 1;">

### 🔴 MODO KERNEL (Ring 0)
- **Código del SO y drivers**
- **Acceso total al hardware**
- **Toda la memoria accesible**
- **Puede ejecutar cualquier instrucción**
- **Si falla**: CRASH/BSoD/Pánico del kernel
- **Ejemplo**: `sys_write()` → escribe directo en hardware

</div>

</div>

---

## Tabla de Instrucciones Permitidas

| Instrucción | Descripción | Ring 3 | Ring 0 |
|-------------|-------------|--------|--------|
| `MOV` | Mover datos | ✅ | ✅ |
| `ADD` | Sumar | ✅ | ✅ |
| `JMP` | Saltar | ✅ | ✅ |
| `IN` / `OUT` | Acceso a puertos E/S | ❌ | ✅ |
| `CLI` / `STI` | Des/habilitar interrupciones | ❌ | ✅ |
| `HLT` | Detener CPU | ❌ | ✅ |
| `LGDT` | Cargar tabla de descriptores | ❌ | ✅ |
| `MOV CR3` | Cambiar page tables | ❌ | ✅ |

> **Resultado en Ring 3:** Si un programa intenta ejecutar `IN` o `HLT`, la CPU genera una **excepción de protección general** (General Protection Fault) y el SO termina el proceso.

---

## ¿Por qué separar modos?

### Seguridad y estabilidad

**Sin separación:**
```
Programa malicioso → Accede a toda la memoria → DESASTRE
```

**Con separación:**
```
Programa malicioso → Pide al kernel → Kernel DENIEGA → Sistema seguro
```

### Ejemplo real:
- Un programa en modo usuario NO puede:
  - Apagar el computador directamente
  - Leer memoria de otro programa
  - Acceder al disco sin permiso

---

## Transición entre Modos: El Mecanismo

```
┌─────────────────────────────────────────────────┐
│                MODO USUARIO (Ring 3)            │
│                                                 │
│   programa ejecuta: read(fd, buffer, 100)       │
│                         │                       │
│   [Instrucción syscall/int 0x80]                │
└─────────────────────────┼───────────────────────┘
                          │ TRAP (Interrupción)
                          ▼
┌─────────────────────────────────────────────────┐
│                MODO KERNEL (Ring 0)             │
│                                                 │
│   1. Guardar contexto (registros)               │
│   2. Verificar permisos del fd                  │
│   3. Validar dirección de buffer                │
│   4. Ejecutar lectura física del disco          │
│   5. Copiar datos a espacio de usuario          │
│   6. Restaurar contexto                         │
│                         │                       │
└─────────────────────────┼───────────────────────┘
                          │ IRET (Return)
                          ▼
┌─────────────────────────────────────────────────┐
│                MODO USUARIO (Ring 3)            │
│   programa continúa con datos en buffer         │
└─────────────────────────────────────────────────┘
```

---

## Tipos de Transiciones al Kernel

| Tipo | Causa | Propósito | Frecuencia |
|------|-------|-----------|------------|
| **System Call** | Programa solicita servicio | E/S, procesos, memoria | Miles/segundo |
| **Interrupción** | Hardware necesita atención | Timer, teclado, disco | Miles/segundo |
| **Excepción** | Error en programa | Page fault, división por cero | Variable |
| **Trap** | Debug/breakpoint | Debugging | Baja |

---

## Analogía: La Transición como un Edificio de Seguridad

```
PISO 3 (PÚBLICO)          PISO 0 (SEGURIDAD MÁXIMA)
────────────────          ─────────────────────────
   Visitante                    Bóveda del banco
      │                              │
      │ "Quiero acceder a mi caja"   │
      ▼                              ▼
   Recepción ←────────────────→   Gerente de seguridad
      │                              │
      │ "Espere, verifico"           │ "Verificar identidad"
      │                              │ "Verificar permisos"
      │                              │ "Ejecutar acceso"
      ▼                              ▼
   Esperando ←────────────────→   Acceso concedido
      │                              │
      │ "Aquí tiene su contenido"    │ "Retornar resultado"
      ▼                              ▼
   Visitante satisfecho         Bóveda segura
```

> **Principio clave:** El visitante (modo usuario) **nunca entra** a la bóveda; solo recibe el resultado de la operación solicitada.
---
## Actividad Práctica (10 min)
### En parejas, investiguen en su computador:

> **⚠️ IMPORTANTE - Para estudiantes con Windows:**
> Los comandos de Linux que usaremos en este curso NO funcionan directamente en Windows.
> Tienes **dos opciones** para practicar:
> 
> **Opción 1: WSL (Recomendada)** - Linux dentro de Windows
> 1. Abre PowerShell como administrador
> 2. Ejecuta: `wsl --install`
> 3. Reinicia el computador
> 4. Una vez instalado, abre "Ubuntu" desde el menú de inicio
> 
> **Opción 2: Máquina Virtual**
> 1. Instala VirtualBox: https://www.virtualbox.org/
> 2. Descarga Ubuntu 24.04 ISO: https://ubuntu.com/download
> 3. Sigue el tutorial del Laboratorio 1 para crear la VM
>
> **En este curso usaremos exclusivamente Linux (Ubuntu)**
### En Windows (PowerShell) - Comandos nativos:

```powershell
# Ver información del sistema operativo
Get-ComputerInfo | Select-Object CsName, WindowsVersion, OsArchitecture

# Ver procesos (top 10 por uso de CPU)
Get-Process | Select-Object -First 10 Name, CPU, PM | Sort-Object CPU -Descending

# Ver memoria disponible
systeminfo | findstr /C:"Total Physical Memory" /C:"Available Physical Memory"
```

### En Linux/Ubuntu (Terminal) - Lo que usaremos en el curso:

Abre Terminal (en WSL o VM) y ejecuta:

```bash
# Ver información del sistema
uname -a                # Información del kernel
cat /etc/os-release     # Distribución Linux

# Ver procesos (top 10)
ps aux | head -11       # Incluye encabezado

# Ver memoria
free -h                 # Muestra memoria RAM y swap
```

3. **Discutan**: ¿Qué información les da cada comando?

---

## Resumen de la Clase

| Generación | Época | Característica |
| ------------ | ------- | ---------------- |
| 0 | 1940s | Sin SO |
| 1 | 1950s | Procesamiento por lotes |
| 2 | 1960s | Multiprogramación |
| 3 | 1970s | Tiempo compartido |
| 4 | 1980s | PCs y GUI |
| 5 | 2000s+ | Modernos, cloud, móviles |

### Componentes: Kernel + Shell + Utilidades + System Calls

---

## Tarea para próxima clase

### Preparación para laboratorio

1. **Descargar** VirtualBox: https://www.virtualbox.org/
2. **Descargar** Ubuntu 24.04 LTS ISO: https://ubuntu.com/download
3. **Leer** el manual del Laboratorio 1

**En la próxima clase:** Instalaremos Linux en máquina virtual

---

## Próxima Clase

### Clase 3: Concepto de Proceso

- ¿Qué es un proceso?
- Diferencia entre proceso y programa
- PCB (Process Control Block)
- Estados de un proceso

**¡Nos vemos!**
