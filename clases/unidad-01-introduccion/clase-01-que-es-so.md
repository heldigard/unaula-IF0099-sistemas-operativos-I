---
marp: true
theme: default
paginate: true
header: 'IF0099 - Sistemas Operativos I | Unidad 1'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
style: |
  img {
    max-width: 85%;
    max-height: 60vh;
    object-fit: contain;
  }
  section {
    font-size: 24px;
  }
---

<!--
[2026-01-31] - Clase enriquecida con infografías

CAMBIOS REALIZADOS:
- Se añadieron 3 infografías educativas
- Se mejoraron las visualizaciones de conceptos clave

IMÁGENES GENERADAS:
- so-capas-sistema.png: Diagrama de capas (Aplicaciones, SO, Hardware)
- so-funciones-principales.png: Las 4 funciones del SO
- so-analogia-hotel.png: Analogía del hotel para explicar el SO
-->

# Clase 1: ¿Qué es un Sistema Operativo?
## Definición, Funciones y Propósito

**IF0099 - Sistemas Operativos I**
*4° Semestre - Ingeniería Informática*

---

## Objetivos de la Clase

Al finalizar esta clase, el estudiante será capaz de:

1. **Definir** qué es un sistema operativo y su propósito
2. **Identificar** las funciones principales de un SO
3. **Comprender** la relación entre hardware, SO y aplicaciones
4. **Reconocer** los SO más utilizados en la actualidad

**Duración:** 90 minutos

---

## Agenda

1. ¿Qué es un Sistema Operativo? (20 min)
2. Funciones principales del SO (25 min)
3. El SO como interfaz y administrador (20 min)
4. Sistemas Operativos actuales (15 min)
5. Actividad práctica (10 min)

---

## 1. ¿Qué es un Sistema Operativo?

### Definición Formal

> Un **Sistema Operativo (SO)** es el software que actúa como intermediario entre el usuario y el hardware del computador, gestionando los recursos y proporcionando servicios a las aplicaciones.

![Capas del Sistema](../../assets/infografias/so-capas-sistema.png)

---

## Analogía del SO

### El SO como el "Gerente de un Hotel"

![Analogía del Hotel](../../assets/infografias/so-analogia-hotel.png)

---

## 2. Funciones Principales del SO

### Las 4 funciones fundamentales

![Funciones del SO](../../assets/infografias/so-funciones-principales.png)

---

## 2.1 Gestión de Procesos

### ¿Qué es un proceso?
Un **proceso** es un programa en ejecución.

### El SO debe:
- **Crear** y **terminar** procesos
- **Suspender** y **reanudar** procesos
- **Sincronizar** procesos
- **Comunicar** procesos entre sí

### Ejemplo en Windows
```
Ctrl + Shift + Esc → Administrador de Tareas
```

---

## 2.2 Gestión de Memoria

### El SO administra la RAM

```
┌─────────────────────────────────────┐
│           MEMORIA RAM               │
├─────────┬─────────┬─────────┬───────┤
│ Sistema │ Chrome  │ Spotify │ Libre │
│ Operat. │ (500MB) │ (200MB) │(2.3GB)│
│ (1GB)   │         │         │       │
└─────────┴─────────┴─────────┴───────┘
```

### Funciones:
- Asignar memoria a procesos
- Liberar memoria cuando termina un proceso
- Proteger la memoria de un proceso de otros
- Implementar memoria virtual (swap)

---

## 2.3 Gestión de Archivos

### Sistema de archivos jerárquico

```
C:\ (o /)
├── Windows/ (o /bin)
├── Program Files/
├── Users/
│   └── estudiante/
│       ├── Documentos/
│       ├── Descargas/
│       └── Escritorio/
└── ...
```

### Funciones:
- Crear, eliminar, renombrar archivos
- Organizar en directorios
- Controlar permisos de acceso
- Gestionar espacio en disco

---

## 2.4 Gestión de Entrada/Salida

### Dispositivos de E/S

| Entrada | Salida | Ambos |
|---------|--------|-------|
| Teclado | Monitor | Disco duro |
| Mouse | Impresora | USB |
| Micrófono | Parlantes | Red |
| Cámara | - | Pantalla táctil |

### El SO:
- Proporciona **drivers** para cada dispositivo
- **Abstrae** las diferencias de hardware
- Maneja **interrupciones** de dispositivos

---

## 3. El SO como Interfaz

### Dos tipos de interfaz

```
┌───────────────────────────────────────────────┐
│                 USUARIO                        │
└───────────────────┬───────────────────────────┘
          ┌─────────┴─────────┐
          ▼                   ▼
    ┌───────────┐       ┌───────────┐
    │    GUI    │       │    CLI    │
    │ (Gráfica) │       │ (Comandos)│
    └───────────┘       └───────────┘
    - Windows           - cmd, PowerShell
    - macOS Finder      - Bash, Zsh
    - GNOME, KDE        - Terminal
```

---

## GUI vs CLI

| Aspecto | GUI | CLI |
|---------|-----|-----|
| Facilidad | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| Potencia | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Automatización | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| Recursos | Alto consumo | Bajo consumo |
| Servidores | Poco usado | **Estándar** |

### En este curso usaremos ambas, pero enfatizaremos CLI (Linux)

---

## 4. Sistemas Operativos Actuales (2026)

### Escritorio/Laptop
| SO | Cuota de mercado |
|----|------------------|
| Windows 11 | ~70% |
| macOS | ~16% |
| Linux | ~4% |
| Chrome OS | ~10% |

### Servidores
| SO | Uso |
|----|-----|
| **Linux** | ~96% de servidores web |
| Windows Server | ~4% |

---

## Familias de Sistemas Operativos

```
                    ┌─────────────┐
                    │   UNIX      │
                    │   (1969)    │
                    └──────┬──────┘
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
      ┌────────┐      ┌────────┐      ┌────────┐
      │ BSD    │      │ Linux  │      │ macOS  │
      │        │      │ (1991) │      │        │
      └────────┘      └───┬────┘      └────────┘
                    ┌─────┼─────┐
                    ▼     ▼     ▼
                 Ubuntu Fedora Android
```

```
      ┌─────────────┐
      │  MS-DOS     │
      │  (1981)     │
      └──────┬──────┘
             ▼
      ┌─────────────┐
      │  Windows    │
      │ (1985-hoy)  │
      └─────────────┘
```

---

## ¿Por qué Linux en este curso?

### Razones pedagógicas:
1. **Código abierto**: Podemos ver cómo funciona internamente
2. **Línea de comandos**: Entendemos mejor los conceptos
3. **Dominante en servidores**: Habilidad laboral esencial
4. **Gratuito**: Sin costo de licencias
5. **Seguro**: Ideal para aprender sin riesgos

### Usaremos: **Ubuntu 24.04 LTS**

---

## Actividad Práctica (10 min)

### En parejas, respondan:

1. **Identifiquen** 3 procesos que estén ejecutándose ahora en su computador
   - Windows: `Ctrl + Shift + Esc`
   - Mac: `Cmd + Space` → "Monitor de Actividad"

2. **Investiguen**: ¿Cuánta RAM tiene su computador y cuánta está en uso?

3. **Discutan**: ¿Por qué creen que Linux domina en servidores pero Windows en escritorios?

---

## Resumen de la Clase

| Concepto | Descripción |
|----------|-------------|
| **Sistema Operativo** | Software intermediario entre usuario y hardware |
| **Funciones** | Gestión de procesos, memoria, archivos y E/S |
| **Interfaz** | GUI (gráfica) y CLI (comandos) |
| **Kernel** | Núcleo del SO, gestiona recursos |

---

## Tarea para la próxima clase

### Investigación individual (entregar vía plataforma)

1. **Investiga** la historia de un SO (Windows, Linux, o macOS)
2. **Escribe** un párrafo de 150 palabras sobre:
   - Año de creación
   - Creador(es)
   - Versiones importantes
   - Un dato curioso

**Fecha de entrega:** Próxima clase

---

## Bibliografía

- Silberschatz, A. (2018). *Operating System Concepts*. 10th Ed.
- Tanenbaum, A. (2015). *Modern Operating Systems*. 4th Ed.
- Stallings, W. (2018). *Operating Systems: Internals and Design Principles*

### Recursos en línea
- [OSDev Wiki](https://wiki.osdev.org/)
- [Linux Journey](https://linuxjourney.com/)

---

## Próxima Clase

### Clase 2: Evolución y Componentes del SO

- Historia de los sistemas operativos
- Generaciones de SO
- Componentes: Kernel, Shell, Utilidades
- Modos de operación: Usuario vs Kernel

**¡Nos vemos!**
