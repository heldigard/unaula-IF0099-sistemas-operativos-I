# EVALUACIONES ACTUALES - IF0099 Sistemas Operativos I

## Estado Actual de Evaluaciones

| Eval | % | Resultado de Aprendizaje | Tipo Actual | Tipo Concertado | Fecha Actual | Estado |
|------|---|-------------------------|-------------|-----------------|--------------|--------|
| E1 | 15% | Identifica la estructura y los tipos de los sistemas operativos | Taller | Taller | 25/02/2026 | ✅ OK |
| E2 | 15% | Gestiona los procesos que se llevan a cabo en los sistemas operativos | Informe | Informe | 11/03/2026 | ✅ OK |
| E3 | 20% | Administra la memoria, E/S, archivos, comunicación, sincronización | Examen | Examen | 25/03/2026 | ✅ OK |
| E4 | 15% | Evalúa la seguridad de los sistemas operativos | Reporte | Reporte | 22/04/2026 | ✅ OK |
| E5 | 15% | Comprende conceptos fundamentales: archivos, procesos, hilos, memoria, comunicación | Informe | Informe | 06/05/2026 | ✅ OK |
| E6 | 20% | Estudia las interfaces que ofrece el SO al usuario y programas de aplicación | Examen | Examen | 27/05/2026 | ✅ OK |

---

## Detalle de Cada Evaluación

### E1 - Estructura y Tipos de SO (15%)

**Tipo actual:** Taller  
**Tipo concertado:** Taller ✅  
**Fecha propuesta:** 25 de febrero de 2026  
**Resultado de aprendizaje:** Identifica la estructura y los tipos de los sistemas operativos

**Contenido evaluado:**
- Definición y funciones del SO
- Tipos de SO (monolítico, microkernel, híbrido)
- Estructura del SO (kernel, shell, utilidades)
- Evolución histórica de los SO
- Comparación Linux vs Windows vs macOS

**Formato de evaluación teórico-práctico:**
- **Teoría (40%):** Comparación de arquitecturas, funciones del SO, línea de tiempo histórica
- **Práctica (60%):** Exploración de kernel Linux (uname, /proc, lsmod), exploración Windows (systeminfo, Get-Process), comparación de shells

**Entregables:**
- Documento PDF con análisis comparativo
- PowerPoint de sustentación
- Capturas de pantalla de comandos ejecutados
- Scripts de shell básicos

---

### E2 - Gestión de Procesos (15%)

**Tipo actual:** Informe ✅
**Tipo concertado:** Informe ✅  
**Fecha propuesta:** 11 de marzo de 2026  
**Resultado de aprendizaje:** Gestiona los procesos que se llevan a cabo en los sistemas operativos

**Contenido evaluado:**
- Concepto de proceso y estados (New, Ready, Running, Waiting, Terminated)
- PCB (Process Control Block)
- Cambio de contexto
- Comandos de gestión: ps, top, kill, nice, renice
- Servicios en Linux (systemctl) vs Windows (Get-Service)
- Scripts de monitoreo

**Formato de evaluación teórico-práctico:**
- **Teoría (40%):** Diagrama de estados, comparación Linux vs Windows, análisis de herramientas
- **Práctica (60%):** Scripts bash (monitor_procesos.sh), scripts PowerShell (gestionar_servicios.ps1), video demostración

**Entregables:**
- Informe técnico en PDF
- Script bash funcional (monitor_procesos.sh)
- Script PowerShell funcional (gestionar_servicios.ps1)
- Video demostración (5-10 minutos)
- Capturas de evidencias

---

### E3 - Examen Parcial (20%)

**Tipo actual:** Examen  
**Tipo concertado:** Examen ✅  
**Fecha propuesta:** 25 de marzo de 2026  
**Resultado de aprendizaje:** Administra la memoria, los procesos de entrada y salida, el sistema de archivos, la comunicación entre procesos y la sincronización de los mismos

**Contenido evaluado:**
- Gestión de memoria (paginación, memoria virtual)
- Procesos de entrada y salida
- Sistema de archivos
- Sincronización de procesos (semáforos, mutex, sección crítica)
- Comunicación entre procesos

**Formato de evaluación:**
- **Estructura:**
  - Sección A: Selección múltiple (20 pts)
  - Sección B: Verdadero/Falso con justificación (15 pts)
  - Sección C: Preguntas abiertas (25 pts)
  - Sección D: Problemas de planificación de CPU (20 pts)
  - Sección E: Análisis de escenarios prácticos con comandos (20 pts)
- **Modalidad:** Individual, presencial
- **Duración:** 2 horas 30 minutos

**Nota:** Este es un examen escrito que combina teoría (60%) con análisis práctico de comandos (40%)

---

### E4 - Seguridad en SO (15%)

**Tipo actual:** Reporte  
**Tipo concertado:** Reporte ✅  
**Fecha propuesta:** 22 de abril de 2026  
**Resultado de aprendizaje:** Evalúa la seguridad de los sistemas operativos

**Contenido evaluado:**
- Mecanismos de protección (SELinux, AppArmor, UAC)
- Control de acceso (DAC, MAC, RBAC)
- Permisos en Linux (rwx, SUID, SGID, Sticky)
- Usuarios y grupos (/etc/passwd, /etc/shadow)
- Auditoría de seguridad básica
- Amenazas comunes (buffer overflow, rootkits, ransomware)

**Formato de evaluación teórico-práctico:**
- **Teoría (50%):** Comparación de mecanismos de protección, modelos de control de acceso, análisis de amenazas
- **Práctica (50%):** Auditoría de permisos en Linux, análisis de usuarios/grupos, configuración de seguridad básica

**Entregables:**
- Reporte técnico en PDF
- Matriz de riesgos (mínimo 8 riesgos identificados)
- Recomendaciones de hardening (5 Linux + 5 Windows)
- Evidencias de auditoría realizada

---

### E5 - Conceptos Fundamentales (15%)

**Tipo actual:** Informe ✅
**Tipo concertado:** Informe ✅  
**Fecha propuesta:** 6 de mayo de 2026  
**Resultado de aprendizaje:** Comprende la funcionalidad de conceptos fundamentales de la materia tales como: sistema de archivos, procesos e hilos, memoria, comunicación entre procesos

**Contenido evaluado:**
- Sistema de archivos (estructura, permisos, backup)
- Procesos e hilos (gestión, monitoreo)
- Memoria (administración, monitoreo)
- Comunicación entre procesos (pipes, señales)
- Integración de conceptos del curso

**Formato de evaluación teórico-práctico:**
- **Teoría (40%):** Arquitectura de la solución, análisis de comandos utilizados, comparación Linux vs Windows
- **Práctica (60%):** Scripts integrales de monitoreo (CPU, memoria, disco, servicios, archivos), comunicación entre procesos

**Entregables:**
- Informe técnico en PDF con arquitectura de la solución
- Scripts Linux:
  - monitor_sistema.sh (monitoreo integral)
  - ipc_demo.sh (comunicación entre procesos)
  - gestion_archivos.sh (backup y permisos)
- Scripts Windows:
  - gestion_servidores.ps1 (monitoreo de servicios)
  - configurar_tareas.ps1 (tareas programadas)
- Video demostración (8-12 minutos)
- Capturas de reportes HTML generados

---

### E6 - Examen Final (20%)

**Tipo actual:** Examen  
**Tipo concertado:** Examen ✅  
**Fecha propuesta:** 27 de mayo de 2026  
**Resultado de aprendizaje:** Estudia las interfaces que ofrece el Sistema Operativo al usuario y a los programas de aplicación

**Contenido evaluado:**
- Todo el contenido del curso (Unidades 1-8)
- Énfasis en:
  - Gestión de memoria (paginación, algoritmos de reemplazo)
  - Sistemas de archivos (asignación, journaling)
  - Interfaces de usuario y programas de aplicación
  - Comandos de administración avanzada

**Formato de evaluación:**
- **Estructura:**
  - Sección A: Conceptos fundamentales (25 pts)
  - Sección B: Desarrollo teórico (25 pts)
  - Sección C: Problemas de cálculo (25 pts) - paginación, planificación
  - Sección D: Análisis de escenarios prácticos (25 pts)
- **Modalidad:** Individual, presencial
- **Duración:** 3 horas

---

## Resumen de Correcciones Necesarias

✅ **TODAS LAS CORRECCIONES APLICADAS**

| Eval | Campo | Valor Anterior | Valor Corregido | Estado |
|------|-------|----------------|-----------------|--------|
| E2 | Tipo | Laboratorio | Informe | ✅ Corregido |
| E5 | Tipo | Laboratorio | Informe | ✅ Corregido |

---

## Verificación de Fechas vs. Seguimientos

| Eval | Fecha | Seguimiento | ¿Cumple? | Notas |
|------|-------|-------------|----------|-------|
| E1 | 25/02/2026 | 1° (≤27/03) | ✅ SÍ | 3 clases previas |
| E2 | 11/03/2026 | 1° (≤27/03) | ✅ SÍ | 6 clases previas |
| E3 | 25/03/2026 | 1° (≤27/03) | ✅ SÍ | 9 clases previas |
| E4 | 22/04/2026 | 2° (≤15/05) | ✅ SÍ | Después de Semana Santa |
| E5 | 06/05/2026 | 2° (≤15/05) | ✅ SÍ | 16 clases previas |
| E6 | 27/05/2026 | 3° (≤28/05) | ✅ SÍ | 19 clases previas |

**Total acumulado por seguimiento:**
- 1° seguimiento (27/03): 15% + 15% + 20% = **50%** ✅
- 2° seguimiento (15/05): 15% + 15% = **30%** → Acumulado **80%** ✅
- 3° seguimiento (28/05): 20% → Acumulado **100%** ✅
