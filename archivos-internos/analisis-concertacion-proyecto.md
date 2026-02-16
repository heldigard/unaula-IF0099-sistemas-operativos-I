# ANÁLISIS CRÍTICO - IF0099 Concertación
## Revisión para Proyecto Final Incremental

**Fecha de análisis:** 16 de febrero de 2026
**Enfoque requerido:** Proceso incremental de proyecto final

---

## 🚨 PROBLEMAS IDENTIFICADOS

### 1. **INCOHERENCIA EN TIPOS DE EVALUACIÓN**

**Estructura ACTUAL:**
| Eval | Tipo | Problema |
|------|------|----------|
| E1 | Taller | ❌ Aislado, no conectado a proyecto |
| E2 | Informe | ❌ Documento independiente |
| E3 | Examen | ❌ No es entrega de proyecto |
| E4 | Reporte | ❌ Otro documento aparte |
| E5 | Informe | ❌ Repetitivo, no avance de proyecto |
| E6 | Examen | ❌ No es entrega final de proyecto |

**Problema:** 6 tipos diferentes que NO forman un proyecto coherente.

### 2. **FALTA DE CONTINUIDAD DEL PROYECTO**

Un proyecto incremental debería tener:
- ✅ **Un único objetivo** que evoluciona
- ✅ **Entregas conectadas** (cada una construye sobre la anterior)
- ✅ **Tipos de evaluación coherentes** (idealemnte "Proyecto" o "Seguimiento")
- ✅ **Producto final tangible** (no solo exámenes y documentos sueltos)

**Actualmente:** Las evaluaciones son trabajos aislados sin conexión entre sí.

### 3. **EXÁMENES (E3 Y E6) ROMpen el FLUJO**

- E3 (20%) y E6 (20%) son exámenes teórico-prácticos
- **Problema:** Un proyecto incremental no debería tener exámenes tradicionales
- **Solución:** Convertir en "Entregas de Proyecto" con sustentación

---

## ✅ PROPUESTA: PROYECTO "ADMINISTRACIÓN DE SERVIDORES LINUX/WINDOWS"

### **Objetivo del Proyecto:**
Diseñar, implementar y asegurar una infraestructura de servidores híbrida (Linux + Windows) para una empresa ficticia, aplicando todos los conceptos del curso.

### **Fases del Proyecto (6 entregas incrementales):**

#### **E1 - Proyecto: Fase 1 - Investigación y Diseño (15%)**
**Tipo:** Proyecto (PANDORA código: 14) o Investigación (código: 8)
**Fecha:** 25 febrero
**Contenido:**
- Análisis de necesidades de la empresa ficticia
- Comparativa de arquitecturas SO (monolítico vs microkernel vs híbrido)
- Selección de distribuciones Linux y versión Windows Server
- Diagrama de arquitectura propuesta
- Lista de servicios requeridos

**Entregables:**
- Documento PDF: "Diseño de Arquitectura de Servidores"
- Diagrama de red y componentes
- Presentación de 5-7 diapositivas
- Justificación técnica de decisiones

**RA:** Identifica la estructura y los tipos de los sistemas operativos ✅

---

#### **E2 - Proyecto: Fase 2 - Gestión de Procesos y Servicios (15%)**
**Tipo:** Proyecto (código: 14)
**Fecha:** 11 marzo
**Contenido:**
- Configuración de procesos críticos del servidor
- Scripts de monitoreo de recursos (CPU, memoria, procesos)
- Implementación de servicios esenciales
- Gestión de prioridades y políticas de planificación
- Documentación de procedimientos

**Entregables:**
- Scripts funcionales (Bash + PowerShell)
- Informe técnico de configuración
- Video demostración (5-7 min)
- Matriz de procesos y servicios

**RA:** Gestiona los procesos que se llevan a cabo en los sistemas operativos ✅

**Conexión con E1:** Implementa lo diseñado en la arquitectura

---

#### **E3 - Proyecto: Fase 3 - Memoria, Almacenamiento y E/S (20%)**
**Tipo:** Proyecto (código: 14) - **NO EXAMEN**
**Fecha:** 25 marzo
**Contenido:**
- Configuración de memoria y swap
- Diseño de sistema de archivos (EXT4/XFS vs NTFS)
- Implementación de RAID o LVM
- Gestión de dispositivos de E/S
- Optimización de rendimiento
- Planificación de respaldos

**Entregables:**
- Sistema de archivos configurado (evidencias)
- Scripts de gestión de almacenamiento
- Plan de respaldo y recuperación
- Análisis de rendimiento con métricas
- Sustentación técnica (10 min)

**RA:** Administra la memoria, los procesos de entrada y salida, el sistema de archivos... ✅

**Conexión:** Integra con E2 (procesos acceden a memoria y archivos)

---

#### **E4 - Proyecto: Fase 4 - Seguridad y Control de Acceso (15%)**
**Tipo:** Proyecto (código: 14)
**Fecha:** 22 abril
**Contenido:**
- Implementación de políticas de seguridad
- Configuración de permisos avanzados (ACLs, SUID/SGID)
- Hardening de servidores (Linux y Windows)
- Configuración de firewall básico
- Auditoría y monitoreo de seguridad
- Matriz de riesgos y mitigaciones

**Entregables:**
- Documento de políticas de seguridad
- Scripts de hardening automatizado
- Matriz de riesgos (8+ identificados)
- Evidencias de configuraciones seguras
- Video de auditoría de seguridad (5-8 min)

**RA:** Evalúa la seguridad de los sistemas operativos ✅

**Conexión:** Protege todo lo construido en E1, E2, E3

---

#### **E5 - Proyecto: Fase 5 - Integración y Servicios Web (15%)**
**Tipo:** Proyecto (código: 14)
**Fecha:** 6 mayo
**Contenido:**
- Instalación y configuración de servidores web (Apache + IIS)
- Configuración de virtual hosts
- Implementación de SSL/HTTPS
- Scripts de monitoreo integral (CPU, memoria, disco, red, servicios)
- Documentación de operación

**Entregables:**
- Servidores web funcionales (accesibles)
- Scripts de monitoreo completo
- Sitios web de prueba configurados
- Informe de integración de servicios
- Sustentación final del proyecto (15 min)

**RA:** comprende la funcionalidad de conceptos fundamentales... ✅

**Conexión:** Integra TODAS las fases anteriores (arquitectura + procesos + almacenamiento + seguridad + servicios)

---

#### **E6 - Proyecto: Fase 6 - Entrega Final y Sustentación (20%)**
**Tipo:** Proyecto (código: 14) - **NO EXAMEN**
**Fecha:** 27 mayo
**Contenido:**
- **NO es examen escrito**, es sustentación final del proyecto completo
- Presentación del proyecto integrado
- Demostración en vivo del servidor funcionando
- Documentación técnica completa
- Manual de administración del sistema
- Video promocional del proyecto (5 min)

**Entregables:**
- **Infraestructura funcionando:** Servidores Linux y Windows operativos
- **Documentación completa:** Manual técnico y de usuario
- **Presentación final:** 15-20 diapositivas
- **Sustentación:** 20 minutos + preguntas
- **Portafolio digital:** Evidencias de todo el proceso

**RA:** Estudia las interfaces que ofrece el Sistema Operativo al usuario... ✅

**Conexión:** Producto final que integra TODO el curso

---

## 📊 COMPARATIVA: ACTUAL vs PROPUESTA

| Aspecto | ACTUAL | PROPUESTA (Proyecto Incremental) |
|---------|--------|----------------------------------|
| **Enfoque** | Evaluaciones aisladas | Proyecto único en 6 fases |
| **Tipos** | Mixto (Taller, Informe, Examen, Reporte) | Unificado (Proyecto) |
| **Continuidad** | ❌ Trabajos sueltos | ✅ Cada fase construye sobre la anterior |
| **Producto final** | ❌ Examen escrito | ✅ Servidores reales funcionando |
| **Coherencia** | ❌ Temas dispersos | ✅ Todo conectado al mismo proyecto |
| **Practicidad** | ⚠️ 50/50 teoría-práctica | ✅ 100% aplicado a proyecto real |

---

## ✅ VENTAJAS DE LA PROPUESTA

### **Para el Estudiante:**
1. **Motivación:** Trabaja en un proyecto real desde el inicio
2. **Aprendizaje:** Construye conocimiento de forma acumulativa
3. **Portafolio:** Al final tiene un proyecto profesional para mostrar
4. **Comprensión:** Ve cómo todo se conecta (no temas aislados)

### **Para el Docente:**
1. **Seguimiento:** Facilita ver el progreso del estudiante
2. **Evaluación:** Cada entrega es parte del mismo proyecto
3. **Coherencia:** Todo el curso alineado a un objetivo común
4. **Cumplimiento:** Cumple la concertación con enfoque práctico

### **Cumplimiento de Seguimientos:**
- ✅ **1° Seguimiento (27 mar, 50%):** E1 + E2 + E3 = Fases 1-3 del proyecto
- ✅ **2° Seguimiento (15 may, 80%):** E4 + E5 = Fases 4-5 del proyecto
- ✅ **3° Seguimiento (28 may, 100%):** E6 = Entrega final del proyecto

---

## 🎯 RECOMENDACIÓN FINAL

**Cambiar en PANDORA:**
1. Tipo de E1: Taller → **Proyecto** (código 14)
2. Tipo de E2: Informe → **Proyecto** (código 14)
3. Tipo de E3: Examen → **Proyecto** (código 14)
4. Tipo de E4: Reporte → **Proyecto** (código 14)
5. Tipo de E5: Informe → **Proyecto** (código 14)
6. Tipo de E6: Examen → **Proyecto** (código 14)

**Alternativa:** Usar **"Seguimiento"** (código 21) para todas si se prefiere seguimientos explícitos.

**Resultado:** Curso 100% basado en proyecto incremental, coherente y muy práctico.

---

**¿Apruebas esta reestructuración para implementarla?**
