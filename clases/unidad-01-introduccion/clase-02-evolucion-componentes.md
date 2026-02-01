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

## Objetivos de la Clase

Al finalizar esta clase, el estudiante será capaz de:

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">

<div style="padding: 15px; background: #dbeafe; border-radius: 10px;">

### 📚 Histórico
| Objetivo | Habilidad |
|----------|-----------|
| **Describir** evolución histórica | Comprensión temporal |
| **Identificar** generaciones de SO | Análisis de épocas |
| **Relacionar** contexto con diseño | Síntesis |

</div>

<div style="padding: 15px; background: #d1fae5; border-radius: 10px;">

### 🏗️ Técnico
| Objetivo | Habilidad |
|----------|-----------|
| **Explicar** componentes principales | Análisis estructural |
| **Diferenciar** modo usuario vs kernel | Comparación crítica |
| **Reconocer** system calls clave | Identificación |

</div>

</div>

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

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">

<div>

### 📚 Valor de la Historia

Entender la historia nos ayuda a:

| Beneficio | Explicación |
|-----------|-------------|
| **Comprender diseño actual** | Las decisiones del pasado moldean el presente |
| **Aprender de errores** | No repetir fracasos históricos |
| **Anticipar tendencias** | Patrones se repiten |
| **Valorar complejidad** | Lo que damos por sentido tomó décadas |

### 🎯 Motivación Clave

> "Aquellos que no pueden recordar el pasado están condenados a repetirlo."
> — George Santayana

**En SO:** Cada generación resolvió problemas específicos de su época.

</div>

<div>

### 📊 Hitos Clave en la Evolución

| Período | Avance | Problema Resuelto |
|---------|---------|-------------------|
| **1940s** | Sin SO | Programación con cables |
| **1950s** | Batch | Automatizar trabajos |
| **1960s** | Multiprogramación | CPU ociosa en E/S |
| **1970s** | Time-sharing | Usuarios interactivos |
| **1980s** | GUI PC | Computación masiva |
| **2000s+** | Cloud/VM | Escalabilidad |

```
1940      1960      1980      2000      2020
  │         │         │         │         │
  ▼         ▼         ▼         ▼         ▼
Sin SO  →  Batch  →  Multi   →   PC    → Cloud
                    prog           GUI      VMs
```

**Insight:** Cada década trajo un paradigma nuevo impulsado por hardware más poderoso.

</div>

</div>

---

## Generación 0: Sin Sistema Operativo (1940-1950)

### La era de los "gigantes" computacionales

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">

<div>

### 🔌 Características

| Aspecto | Descripción |
|---------|-------------|
| **Hardware** | ENIAC (1945), UNIVAC I (1951) |
| **Tamaño** | Ocupaban habitaciones completas |
| **Programación** | Cables y switches físicos |
| **Uso** | Cálculos balísticos, censos |
| **Costo** | Millones de dólares |

```
    ┌──────────────────────────────┐
    │                              │
    │    🏭 ENIAC (1945)           │
    │    30 toneladas              │
    │    17,468 válvulas            │
    │    174 kW de potencia         │
    │                              │
    │   [Programador cableando]     │
    │         │                    │
    │         ▼                    │
    │    ┌─────────────┐            │
    │    │  SWITCHES    │           │
    │    │  CABLES      │           │
    │    └─────────────┘            │
    └──────────────────────────────┘
```

### ⚠️ Problemas

- **Tiempo perdido** reconectando cables
- **Errores humanos** frecuentes
- **Un programa** = toda la máquina
- **Sin concepto** de "software de sistema"

</div>

<div>

### 💡 Insight Histórico

> "Programar la ENIAC era como reconectar una central telefónica
> cada vez que querías hacer una llamada."

### 📊 Comparación

| Métrica | 1940s | Hoy |
|---------|-------|-----|
| Peso | 30 toneladas | Gramos |
| Energía | 174 kW | 5-15 W |
| Velocidad | ~5,000 ops/s | ~100,000 M ops/s |
| Costo | ~$500,000 | ~$500 |

### 🎯 ¿Por qué estudiarnos?

- **Origen de conceptos:** todavía usamos herencia de esta época
- **Contexto:** entender por qué los SO surgieron como respuesta a estos problemas
- **Agradecimiento:** valorar lo fácil que es programar hoy

</div>

</div>

<div style="text-align: center; margin-top: 20px; padding: 15px; background: #fef3c7; border-radius: 10px;">

**💡 Lección:** La necesidad es la madre de la invención. Estos problemas extremos impulsaron la creación de los primeros sistemas operativos.

</div>

---

## Primera Generación: Procesamiento por Lotes (1950-1965)

### Batch Processing: Automatizando el flujo

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">

<div>

### 📦 El flujo del batch

```
PROGRAMADOR           OPERADOR           COMPUTADORA
    │                    │                    │
    │ Escribe            │ Perfora            │
    │ en papel           │ tarjetas           │
    ▼                    ▼                    ▼
┌────────┐          ┌────────┐          ┌────────┐
│ CÓDIGO  │          │TARJETAS│          │  LOTE  │
│ FUENTE │          │PERFORADAS│         │ACUMU-  │
└────────┘          └────────┘          │ LADO   │
                                        └───┬────┘
                                            │
                       (horas después)      ▼
                                            │
                                        ┌────────┐
                                        │SALIDA  │
                                        │IMPRESA │
                                        └────────┘
```

### 🎯 Ventajas del Sistema de Lotes

| Aspecto | Sin Sistema | Con Batch |
|---------|-------------|-----------|
| **Preparación** | Manual | Automatizada |
| **Throughput** | 1 trabajo/hora | Varios/hora |
| **Eficiencia** | CPU ociosa mucho | CPU casi siempre ocupada |
| **Errores** | Frecuentes | Detectados antes |

### ⚙️ Primer SO: GM-NAA I/O (1956)

- **Creado por:** General Motors e IBM
- **Innovación:** Primer SO de producción real
- **Función:** Automatizar procesamiento de nómina de GM
- **Impacto:** Probó que los SO valían la inversión

</div>

<div>

### 🏭 Secuencia de un Job Batch

```
┌────────────────────────────────────────┐
│ 1. PROGRAMADOR                           │
│    Escribe código en FORTRAN/COBOL      │
└────────────┬───────────────────────────┘
             │ Tarjetas perforadas
             ▼
┌────────────────────────────────────────┐
│ 2. OPERADOR                            │
│    Prepara tarjetas y tarjetas          │
│    Incluye: código + datos + control    │
└────────────┬───────────────────────────┘
             │ Se acumulan en lote
             ▼
┌────────────────────────────────────────┐
│ 3. LECTOR DE TARJETAS                  │
│    Lee tarjetas a alta velocidad        │
└────────────┬───────────────────────────┘
             │ Datos en memoria
             ▼
┌────────────────────────────────────────┐
│ 4. COMPUTADORA PROCESA                │
│    Ejecuta secuencialmente             │
│    Uno tras otro                       │
└────────────┬───────────────────────────┘
             │ Resultados listos
             ▼
┌────────────────────────────────────────┐
│ 5. IMPRESORA                           │
│    Salida en papel (horas después)     │
└────────────────────────────────────────┘
```

### 📊 Limitaciones

| Problema | Explicación |
|----------|-------------|
| **Sin interactividad** | No puedes corregir errores en tiempo real |
| **Turnaround largo** | Horas o días para resultados |
| **Sin debugging** | Casi imposible encontrar bugs |
| **Ineficiente** | CPU espera E/S del siguiente job |

</div>

</div>

<div style="text-align: center; margin-top: 20px; padding: 15px; background: #dbeafe; border-radius: 10px;">

**💡 Evolución clave:** El concepto de "cola de trabajos" (job queue) nació aquí y todavía lo usamos hoy (printers, batch jobs).

</div>

---

## Segunda Generación: Multiprogramación (1965-1980)

### 🎯 El problema: CPU esperando E/S

```
SIN MULTIPROGRAMACIÓN        CON MULTIPROGRAMACIÓN
┌──────────────────┐         ┌──────────────────┐
│ CPU: 10% ocupada │         │ CPU: 95% ocupada  │
│ E/S: 90% tiempo  │         │ E/S: 5% tiempo   │
└──────────────────┘         └──────────────────┘

Porque cuando un programa      Ahora CPU NO espera:
lee del disco, CPU ociosa     - Mientras A lee, B corre
porque no hay otro programa    - Mientras B escribe, C corre
que ejecutar.
```

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">

<div>

### 💾 Memoria con Múltiples Programas

```
┌────────────────────────────────┐
│         MEMORIA RAM            │
├────────────────────────────────┤
│  Sistema Operativo             │
├────────────────────────────────┤
│  Programa A                     │ ← esperando E/S
│  (en espera de disco)           │
├────────────────────────────────┤
│  Programa B  ◀─────► CPU        │ ← ejecutando ahora
│  (usa CPU activamente)          │
├────────────────────────────────┤
│  Programa C                     │ ← esperando E/S
│  (en espera de red)             │
└────────────────────────────────┘

La CPU cambia de programa cuando
uno hace E/S. A = B = C = A = B ...
```

### 🚀 Innovación Clave

| Aspecto | Antes | Después |
|---------|-------|---------|
| **Uso de CPU** | ~10-20% | ~80-95% |
| **Throughput** | 1 job/hora | 3-5 jobs/hora |
| **Eficiencia** | Muy baja | Muy alta |
| **Costo** | Alto por job | Bajo por job |

</div>

<div>

### 🏭 Sistemas Importantes

#### IBM OS/360 (1964)
- **Primer SO de "propósito general"**
- **Familia de SOs** para diferentes hardware
- **Conceptos introducidos:**
  - Job control language (JCL)
  - Spooling (Simultaneous Peripheral Operations On-Line)
  - Multiprogramación real

```
OS/360 fue el proyecto de software más
grande de la época: 5,000 personas-año
```

#### MULTICS (1969)
- **Proyecto conjunto:** Bell Labs, MIT, GE
- **Objetivo:** SO "universal" para todas las necesidades
- **Resultado:** Demasiado complejo, proyecto cancelado
- **Legado:** Ideas que inspiraron UNIX

```
MULTICS era "todo para todos":
- Muy potente
- Muy complejo
- Muy caro
- Falló por sobre-ingeniería
```

### 💡 Insight

> "La perfección se alcanza no cuando no hay nada más que añadir,
> sino cuando no hay nada más que quitar."
> — Antoine de Saint-Exupéry

**MULTICS añadió de todo. UNIX eliminó hasta lo esencial.**

</div>

</div>

<div style="text-align: center; margin-top: 20px; padding: 15px; background: #d1fae5; border-radius: 10px;">

**💡 Evolución clave:** Multiprogramación = El kernel cambia de programa activo cada milisegundo, maximizando uso de CPU.

</div>

---

## Nacimiento de UNIX (1969)

### 📖 La historia de cómo un proyecto fallido creó el SO más influyente

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">

<div>

### 🔬 El contexto: MULTICS

```
┌─────────────────────────────────────┐
│           MULTICS (1964-1969)        │
│                                     │
│  Objetivo: SO "perfecto" universal   │
│  Problema: Demasiado complejo        │
│  Resultado: Proyecto cancelado      │
│                                     │
│  Bell Labs se retira del proyecto   │
└─────────────────────────────────────┘
           │ Ken Thompson, Dennis Ritchie
           │ decepcionados, deciden
           │ crear su propio SO minimalista
           ▼
┌─────────────────────────────────────┐
│           UNIX (1969)               │
│                                     │
│  Filosofía: "Haz una cosa bien"     │
│  Simple, elegante, poderoso          │
└─────────────────────────────────────┘
```

### 🎯 Los Creadores

| Persona | Rol | Contribución |
|---------|-----|-------------|
| **Ken Thompson** | Arquitecto principal | Diseñó UNIX, escribió B |
| **Dennis Ritchie** | Creador de C | Inventó C, reescribió UNIX |
| **Douglas McIlroy** | Filosofía | "Pipes", filosofía UNIX |
| **Brian Kernighan** | Documentación | Explicó UNIX al mundo |

</div>

<div>

### 💡 Innovaciones Revolucionarias

#### 1. Escrito en C (Portabilidad)
```
ANTES (SO en ensamblador):
┌──────────────────┐
│ SO IBM 360       │ → Solo corre en IBM 360
│ (ensamblador)    │
└──────────────────┘

DESPUÉS (UNIX en C):
┌──────────────────┐        ┌──────────────┐
│ UNIX en C        │   ──►  │ PDP-11       │
└──────────────────┘        │ VAX          │
                            │ x86          │
                            │ ARM          │
                            └──────────────┘

UN SO corre en CUALQUIER hardware
con solo recompilar.
```

#### 2. Filosofía "Haz una cosa y hazla bien"

| Programa | Función | Combinar |
|----------|---------|----------|
| `ls` | Listar archivos | `ls \| grep .txt` |
| `grep` | Buscar texto | `cat file \| grep error` |
| `cat` | Mostrar archivo | `cat file \| wc -l` |
| `wc` | Contar líneas | `ls \| wc -l` |

**Pequeñas herramientas que se combinan = Poder infinito**

#### 3. "Todo es un archivo"

```
/archivo/disco
/dispositivo/teclado
/socket/red
/todo/es/un/archivo
```

Abstracción elegante y uniforme.

#### 4. Herencia que define el mundo actual

```
UNIX (1969)
   │
   ├───→ Linux (1991) → Servidores, Android, IoT
   ├───→ BSD → macOS, iOS
   ├───→ Minix → Educación
   └───→ Plan 9 → Inspiración para Go
```

**El 99% de internet corre descendientes de UNIX.**

</div>

</div>

<div style="text-align: center; margin-top: 20px; padding: 15px; background: #fef3c7; border-radius: 10px;">

**🎯 Lección:** A veces, un fracaso (MULTICS) conduce a un éxito aún mayor (UNIX). La simplicidad gana.

</div>

---

## Tercera Generación: Tiempo Compartido (1970-1990)

### ⏱️ Time-Sharing: Interactividad para múltiples usuarios

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">

<div>

### 💡 El concepto: "Tajadas" de tiempo

```
CPU de 1 segundo se divide en "tajadas":

┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
│100ms│100ms│100ms│100ms│100ms│100ms│100ms│100ms│100ms│
└──┬──┴──┬──┴──┬──┴──┬──┴──┬──┴──┬──┴──┬──┴──┬──┘
   │   │   │   │   │   │   │   │   │
   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼
Usuario Usuario Usuario Usuario Usuario Usuario Usuario
  1      2      3      4      5      6      7      8

Cada usuario tiene la ILLUSIÓN de
exclusividad, pero comparten la CPU.
```

### 🎯 Problema Resuelto

| Antes (Batch) | Después (Time-Sharing) |
|---------------|----------------------|
| Horas de espera | Respuesta inmediata |
| Sin interactividad | Interactivo |
| Un usuario a la vez | Decenas de usuarios |
| Debugging difícil | Debugging en tiempo real |

### ⚙️ Cómo funciona

```
1. Usuario presiona tecla
   ↓
2. SO guarda contexto del programa actual
   ↓
3. SO carga programa del usuario
   ↓
4. Usuario tiene CPU por su "tajada"
   ↓
5. SO interrumpe y cambia a siguiente usuario
   ↓
6. (Repetir muy rápido)

Todo esto ocurre en milisegundos.
```

</div>

<div>

### 🏛️ Sistemas Importantes

#### UNIX (1969-presente) - El estándar

```
Características innovadoras:
- Time-sharing real
- Jerarquía de archivos
- Permisos de usuario
- Shell programable
- Todo es un archivo
- Escrito en C (portable)
```

| Año | Versión | Innovación |
|-----|---------|-------------|
| 1969 | UNIX v1 | Primer sistema time-sharing |
| 1971 | UNIX v4 | Pipes (comunicación entre procesos) |
| 1973 | UNIX v5 | Primera versión portátil |
| 1977 | BSD | Berkeley sockets (red) |
| 1983 | System V | IPC System V, semáforos |

#### VMS (1978) - Virtual Memory System

```
DEC VAX/VMS fue el SO más influyente
de los años 80 en entornos académicos
y de ingeniería.

Características:
- Clustering (varios computadores como uno)
- Sistema de archivos robusto
- DDCMP (protocolo de red)
- Impacto: Influenció Windows NT
```

#### CP/M (1974) - Microprocesadores

```
Gary Kildall crea CP/M para microprocesadores
Intel 8080.

Características:
- SO simple para 8-bit
- API consistente
- Se convirtió en estándar de facto
- Base para MS-DOS

Impacto: Popularizó computación personal
```

### 📊 Comparativa de Sistemas de los 70s

| Sistema | Hardware | Usuarios | Uso principal |
|---------|----------|----------|----------------|
| UNIX | PDP-11, VAX | ~50-100 | Academia, investigación |
| VMS | VAX | ~100 | Empresas, ingeniería |
| CP/M | 8080, Z80 | 1 | Oficina, juegos tempranos |
| DOS | 8086 | 1 | Jogos, ofimática |

</div>

</div>

<div style="text-align: center; margin-top: 20px; padding: 15px; background: #dbeafe; border-radius: 10px;">

**💡 Evolución clave:** Time-sharing + Terminales remotas = Primera forma de "computación en la nube" (mainframes con terminales tontas).

</div>

---

## Cuarta Generación: Computadoras Personales (1980-2000)

### 🏠 La revolución del PC: Computación para todos

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">

<div>

### 📊 Línea de tiempo del PC

```
1975          1981          1984          1991          1995
 │             │             │             │             │
 ▼             ▼             ▼             ▼             ▼
Altair        IBM PC         Mac           Linux         Win 95
8800          (MS-DOS)       (GUI)         (Open)        (GUI masivo)
```

### 🎯 Sistemas que Definieron una Época

| Año | Sistema | Importancia Histórica |
|-----|---------|----------------------|
| **1981** | **MS-DOS** | IBM PC, dominio empresarial |
| **1984** | **Mac OS** | Primera GUI comercial exitosa |
| **1985** | Windows 1.0 | Intento de GUI sobre DOS |
| **1991** | **Linux** | SO libre y abierto |
| **1995** | **Windows 95** | GUI dominante en hogares |
| **1998** | **Windows 98** | Internet integrado |

### 💡 La Guerra de los SO

```
┌─────────────┐                    ┌─────────────┐
│   DOS       │                    │   Mac OS    │
│   $ prompt  │                    │   🖼️  GUI   │
│   c:\>       │                    │   Mouse      │
│             │                    │   Iconos     │
└─────────────┘                    └─────────────┘
     │                                   │
     │     1991: Linux nace           │
     │     1995: Win 95 une GUI       │
     │           │                    │
     ▼           ▼                    ▼
┌─────────────────────────────────────────┐
│  El gana: GUI + Compatibilidad        │
│  (Microsoft)                          │
│                                         │
│  Los perdedores:                       │
│  - Mac: Cerrado, hardware caro          │
│  - Linux: Técnico, sin GUI             │
└─────────────────────────────────────────┘
```

### 🚀 Transformación Social

| Antes (1980) | Después (2000) |
|---------------|----------------|
| Computadoras = empresas | Computadoras = hogares |
| Programadores = expertos | Cualquiera programa |
| Internet = académicos | Internet = todos |
| Costo = $5,000+ | Costo = $500 |

</div>

<div>

### 🎮 El impacto en la cultura popular

#### Gaming
```
1980: Pac-Man, Space Invaders (Arcades)
1990: Doom, SimCity (PC games)
2000+: MMORPG, Esports (Jugar en red)

La GUI hizo los PCs "amigables" para juegos.
```

#### Oficina
```
1985: Excel, WordPerfect (Productivity apps)
1990: Microsoft Office (Dominio absoluto)
2000: Google Docs (Computación en nube)

La PC se volvió indispensable para negocios.
```

#### Educación
```
1980s: Logo, BASIC (Aprender a programar)
1990s: CD-ROMs enciclopedias (Información digital)
2000s: Internet (Aprendizaje en línea)

La PC democratizó el conocimiento.
```

### 📈 Números de la Revolución del PC

| Métrica | 1981 | 1990 | 2000 | 2010 |
|---------|------|------|------|------|
| PCs vendidos/año | ~0.2M | ~10M | ~140M | ~350M |
| Penetración hogares | <1% | ~20% | ~60% | ~80% |
| Costo promedio | $3,000 | $1,500 | $800 | $500 |

### 💡 Insight

> "La computadora personal más importante es la que
> tienen las personas que no saben que la necesitan."
> — Steve Jobs, 1985

**Windows 95 fue el momento en que la computación se volvió mainstream.**

</div>

</div>

<div style="text-align: center; margin-top: 20px; padding: 15px; background: #f0f9ff; border-radius: 10px;">

**💡 Evolución clave:** El PC + GUI = Democratización de la computación. Ya no necesitabas ser ingeniero para usar un computador.

</div>

---

## Quinta Generación: SO Modernos (2000-presente)

### 🌐 La era de la conectividad total y la computación ubicua

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">

<div>

### ⚡ Características Definitorias

| Característica | Descripción | Ejemplo |
|----------------|-------------|---------|
| **Multitarea real** | Múltiples núcleos, múltiples CPUs | Tu PC hace 100 cosas a la vez |
| **Conectividad total** | Redes, Internet, 5G | Todo siempre conectado |
| **Seguridad avanzada** | Encriptación, permisos granulares | FaceID, HTTPS, sandbox |
| **Virtualización** | VMs, contenedores | Docker, KVM, Hyper-V |
| **Cloud native** | Servicios on-demand | AWS, Azure, GCP |
| **Computación móvil** | Smartphones = computadores potentes | Tu celular es más rápido que PCs de 2010 |
| **Edge computing** | Procesamiento en el borde | IoT, sensores, CDN |

### 📱 El cambio de paradigma: Desktop → Cloud → Edge

```
2000s: Desktop Computing
┌─────────────────────────────┐
│  Todo corre LOCALMENTE         │
│  - Office instalado            │
│  - Archivos en disco duro     │
│  - Aplicaciones .exe          │
└─────────────────────────────┘

2010s: Cloud Computing
┌─────────────────────────────┐
│  Todo en la NUBE              │
│  - Google Docs               │
│  - Netflix streaming          │
│  - Dropbox                   │
│  - Microsoft 365             │
└─────────────────────────────┘

2020s: Edge Computing
┌─────────────────────────────┐
│  Procesamiento DISTRIBUIDO    │
│  - CDNs                     │
│  - IoT gateways             │
│  - Edge functions          │
└─────────────────────────────┘
```

### 🔮 Tendencias emergentes (2026+)

| Tendencia | Explicación | Impacto |
|----------|-------------|---------|
| **AI-native OS** | SO optimizados para ML chips | Windows Copilot, Apple Intelligence |
| **Container-first** | Microservicios + contenedores | Kubernetes everywhere |
| **Real-time OS** | Latencia ultrabaja | Automotrización, VR/AR |
| **Energy-aware** | Optimización de batería | Chips ARM en servidores |

</div>

<div>

### 🖥️ Ejemplos Actuales por Categoría

#### Desktop
```
Windows 11 (2021+)
├── Interfaz híbrida (Start Menu)
├── WSL 2 (Linux integrado)
├── Teams integrado
└── Microsoft Store

macOS (versiones anuales)
├── macOS Sequoia, Ventura, Sonoma...
├── ARM64 (Apple Silicon)
├── Continuidad iOS/macOS
└── Optimizado para creativos

Linux Desktop
├── Ubuntu LTS (soporte 5 años)
├── Fedora (bleeding edge)
├── Pop!_OS (usabilidad)
└── Mint (fácil para migrantes)
```

#### Móvil
```
Android (Google)
├── 71% market share
├── Fragmentación (skins: Samsung, Xiaomi)
├── Google Play Services
└── Base de 24,000+ modelos

iOS (Apple)
├── 28% market share
├── Ecosistema cerrado
├── App Store curado
└── Base de ~10 modelos
```

#### Servidor
```
Distribuciones empresariales:
├── RHEL (Red Hat, soporte pagado)
├── Ubuntu LTS (Canonical, free/pagado)
├── Debian (comunidad, estable)
└── SUSE (Enterprise, europeo)

SO Cloud:
├── Amazon Linux (optimizado para AWS)
├── Azure Linux (optimizado para Azure)
└── Google COS (optimizado para GCP)
```

### 💡 Insights

> "La computación más importante es la que ni ves ni piensas.
> Está en data centers procesando tus búsquedas, transacciones y
> streams de video las 24/7."

**El SO moderno es invisible: está en la nube, en tu celular, en tu smartwatch.**

</div>

</div>

<div style="text-align: center; margin-top: 20px; padding: 15px; background: #d1fae5; border-radius: 10px;">

**💡 Evolución clave:** Ya no hay "el" SO dominante. Hay múltiples SOs para diferentes usos, y todos coexisten en un ecosistema conectado.

</div>

---

## Componentes de un SO Moderno

### Capas de Abstracción: El modelo de cebolla

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">

<div>

#### 🧅 ¿Por qué "capas"?

Cada capa **oculta la complejidad** de la inferior:

```
┌─────────────────────────────────────────────────┐
│                  APLICACIONES                   │ ← Usuario interactúa aquí
├─────────────────────────────────────────────────┤
│              UTILIDADES DEL SISTEMA             │
│    (Administrador archivos, Terminal, etc.)     │
├─────────────────────────────────────────────────┤
│                    SHELL                        │
│         (Intérprete de comandos / GUI)          │
├─────────────────────────────────────────────────┤
│            LLAMADAS AL SISTEMA (API)            │ ← La frontera crucial
├─────────────────────────────────────────────────┤
│                   KERNEL                        │
│  ┌──────────┬──────────┬──────────┬──────────┐ │
│  │ Gestor   │ Gestor   │ Sistema  │ Gestor   │ │
│  │ Procesos │ Memoria  │ Archivos │   E/S    │ │
│  └──────────┴──────────┴──────────┴──────────┘ │
├─────────────────────────────────────────────────┤
│                   HARDWARE                      │ ← Componentes físicos
└─────────────────────────────────────────────────┘
```

</div>

<div>

#### 📋 Responsabilidades por Capa

| Capa | Responsabilidad | Ejemplos |
|------|-----------------|----------|
| **Aplicaciones** | Funcionalidad para usuario | Chrome, VS Code, juegos |
| **Utilidades** | Herramientas del sistema | FileManager, TaskManager |
| **Shell** | Puente usuario-kernel | bash, PowerShell, Explorador |
| **System Calls** | API oficial del SO | open(), read(), fork() |
| **Kernel** | Gestión de recursos | CPU, RAM, disco, red |
| **Hardware** | Componentes físicos | CPU, RAM, SSD, GPU |

#### 💡 Insight: La transición clave

> **Las system calls son la ÚNICA forma válida**
> **de que un programa acceda a servicios del kernel.**

```
Aplicación ──✖──> Hardware directo
              │
              └──> System Call ──> Kernel ──> Hardware
```

**Sin system calls:** Caos, inseguridad, crashes
**Con system calls:** Orden, seguridad, estabilidad

</div>

</div>

---

## El Kernel (Núcleo)

### El corazón del Sistema Operativo

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">

<div>

#### 💓 Por qué es el "corazón"

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

#### 🎯 Responsabilidades Principales

| Componente | Función |
|-----------|---------|
| **Planificador** | Decide qué proceso ejecuta |
| **Gestor de memoria** | Asigna RAM a procesos |
| **Sistema de archivos** | Organiza datos en disco |
| **Drivers E/S** | Habla con hardware |
| **Gestor de procesos** | Crea, destruye procesos |

</div>

<div>

#### 🏗️ Tipos de Kernel

| Tipo | Estructura | Ventajas | Ejemplos |
|------|------------|----------|----------|
| **Monolítico** | Todo en un espacio | Rápido, directo | Linux, DOS |
| **Microkernel** | Mínimo en kernel | Seguro, flexible | Minix, QNX, seL4 |
| **Híbrido** | Mezcla de ambos | Balance | macOS, Windows NT |
| **Exokernel** | Mínimo absoluto | Flexibilidad total | Investigación |

#### ⚖️ Comparativa

```
MONOLÍTICO                    MICROKERNEL
┌─────────────┐              ┌──────────┐
│   KERNEL    │              │  Kernel  │
│             │              │  mínimo  │
│ Todo junto  │              └─────┬────┘
│             │                    │
│ - Rápido    │              ┌──────▼──────┐
│ - Complejo  │              │   Servicios │
│ - Crash total│             │   en user   │
└─────────────┘              └─────────────┘
```

> **Nota:** Linux es monolítico con módulos cargables → "lo mejor de ambos mundos"

</div>

</div>

---

## El Shell

### Interfaz entre usuario y kernel

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">

<div>

#### 🔄 El flujo de trabajo

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

#### 🎭 Dos tipos de Shell

| Tipo | Descripción | Ejemplos |
|------|-------------|----------|
| **CLI** | Comandos de texto | bash, zsh, PowerShell |
| **GUI** | Interfaz gráfica | Explorador Windows, Finder |

</div>

<div>

#### 🐚 Shells CLI populares

| Shell | Características | Uso típico |
|-------|----------------|------------|
| **bash** | Estándar POSIX, omnipresente | Linux, macOS (antes) |
| **zsh** | Autocompletado avanzado, themes | macOS default |
| **PowerShell** | Orientado a objetos, .NET | Windows admin |
| **fish** | Autocompletado inteligente, UX-friendly | Principiantes |

#### 💻 GUI como Shell

```
EXPLORADOR WINDOWS = Shell gráfico

Click carpeta → Explorador interpreta
                → Llama a kernel
                → Muestra contenido

Lo MISMO que bash, pero con clics
en lugar de comandos de texto.
```

> **El shell NO es el kernel.**
> Es un programa CORRIENDO en modo usuario
> que SOLICITA servicios al kernel.

</div>

</div>

---

## Llamadas al Sistema (System Calls)

### La API del Sistema Operativo

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px;">

<div>

#### 🔌 Por qué son necesarias

```c
// Ejemplo: Abrir un archivo
int fd = open("/home/user/archivo.txt", O_RDONLY);

// El programa NO accede al disco directamente
// Pide al kernel que lo haga por él
```

```
┌─────────────┐                    ┌─────────────┐
│  PROGRAMA   │                    │   HARDWARE  │
│             │                    │             │
│ "Quiero     │────✖────directo──→│  (DISCO)    │
│  leer disco"│                    │             │
└──────┬──────┘                    └─────────────┘
       │
       │ System Call
       ▼
┌─────────────┐
│   KERNEL    │ ← Verifica permisos
│             │ ← Accede a hardware
│ "Autorizado"│ ← Devuelve datos
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  PROGRAMA   │ ← Recibe datos
│   (datos)   │
└─────────────┘
```

</div>

<div>

#### 📂 Categorías de System Calls

| Categoría | Propósito | Ejemplos |
|-----------|-----------|----------|
| **Procesos** | Crear/destruir procesos | fork(), exec(), exit(), wait() |
| **Archivos** | Manipular archivos | open(), read(), write(), close() |
| **Dispositivos** | Acceder a hardware | ioctl(), read(), write() |
| **Información** | Obtener datos del sistema | getpid(), time(), uname() |
| **Comunicación** | Enviar/recibir datos | pipe(), socket(), send() |
| **Memoria** | Gestión de memoria | mmap(), brk(), sbrk() |

#### 🎯 Ejemplo real: `ls -la`

```
$ ls -la /home

bash ejecuta:
1. getuid() → Verificar permisos
2. opendir("/home") → Abrir directorio
3. readdir() → Leer entrada
4. stat() → Obtener metadatos
5. printf() → Mostrar en pantalla
6. closedir() → Cerrar directorio

¡6 system calls para un simple ls!
```

</div>

</div>

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
### En parejas, preparen su entorno de trabajo

**Para estudiantes con Windows:**
Los comandos de Linux del curso NO funcionan directamente en Windows.
Tienen dos opciones para practicar:

**Opción 1: WSL (Recomendada)** - Linux dentro de Windows
1. Abran PowerShell como administrador
2. Ejecuten: `wsl --install`
3. Reinicien el computador
4. Abran "Ubuntu" desde el menú de inicio

**Opción 2: Máquina Virtual**
1. Instalen VirtualBox: https://www.virtualbox.org/
2. Descarguen Ubuntu LTS ISO: https://ubuntu.com/download
3. Sigan el tutorial del Laboratorio 1 para crear la VM

**En este curso usaremos Linux (Ubuntu)**

---

## Actividad Práctica
### En Windows (PowerShell) - Comandos nativos

```powershell
# Ver información del sistema operativo
Get-ComputerInfo | Select-Object CsName, WindowsVersion, OsArchitecture

# Ver procesos (top 10 por uso de CPU)
Get-Process | Select-Object -First 10 Name, CPU, PM | Sort-Object CPU -Descending

# Ver memoria disponible
systeminfo | findstr /C:"Total Physical Memory" /C:"Available Physical Memory"
```

---

## Actividad Práctica
### En Linux/Ubuntu (Terminal) - Lo que usaremos en el curso

Abren Terminal (en WSL o VM) y ejecuten:

```bash
# Ver información del sistema
uname -a                # Información del kernel
cat /etc/os-release     # Distribución Linux

# Ver procesos (top 10)
ps aux | head -11       # Incluye encabezado

# Ver memoria
free -h                 # Muestra memoria RAM y swap
```

---

## Actividad Práctica
### Discusión en parejas

1. **Expliquen** qué información aporta cada comando
2. **Comparen** resultados entre Windows y Linux
3. **Conclusión breve**: ¿Qué datos del SO te parecen más relevantes?

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
