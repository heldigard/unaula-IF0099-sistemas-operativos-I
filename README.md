# IF0040 - Sistemas Operativos

**Curso:** IF0040 - Sistemas Operativos
**Pensum:** 302 Pensum 2014-2
**Créditos:** 3
**Semestre:** 2026-I (Enero - Junio)

---

## Descripción del Curso

Este curso de Sistemas Operativos tiene como objetivo que los estudiantes comprendan los conceptos fundamentales de los sistemas operativos modernos, su evolución histórica, y los componentes principales que los conforman. Los estudiantes desarrollarán habilidades prácticas para trabajar con sistemas operativos actuales (Windows, Linux, macOS) y aplicarán estos conocimientos en la resolución de problemas prácticos.

---

## Contenido del Repositorio

```
.
├── .gitignore              # Ignora evaluaciones/
├── README.md               # Este archivo
├── planificacion/
│   ├── syllabus.md         # Programa oficial del curso
│   ├── cronograma.md       # Calendario de clases y evaluaciones
│   └── competencias.md     # Objetivos de aprendizaje
├── clases/
│   ├── unidad-01-introduccion/
│   ├── unidad-02-procesos/
│   ├── unidad-03-memoria/
│   ├── unidad-04-archivos/
│   ├── unidad-05-e-s/
│   └── unidad-06-so-actuales/
├── proyectos/
│   ├── proyecto-01-linux/
│   ├── proyecto-02-scheduler/
│   ├── proyecto-03-memoria/
│   ├── proyecto-04-archivos/
│   └── proyecto-final-comparativa/
├── laboratorios/
├── recursos/
│   ├── bibliografia.md
│   ├── herramientas.md
│   └── enlaces-externos.md
└── memory-bank/
    ├── projectbrief.md
    ├── productContext.md
    ├── systemPatterns.md
    ├── techContext.md
    ├── activeContext.md
    └── progress.md
```

---

## Unidades Temáticas

1. **Introducción a los Sistemas Operativos** (5 temas)
2. **Gestión de Procesos** (6 temas)
3. **Gestión de Memoria** (6 temas)
4. **Gestión de Archivos** (6 temas)
5. **Gestión de Entrada/Salida** (6 temas)
6. **Sistemas Operativos Actuales** (5 temas)

---

## Cronograma de Evaluaciones

| Evaluación | % | Semana | Tipo | Límite |
|------------|---|--------|------|--------|
| Eval 1 | 15% | 4 | Quiz + Taller | Feb 02-06 |
| Eval 2 | 15% | 7 | Laboratorio + sustentación | Feb 23-27 |
| Eval 3 | 20% | 10 | Proyecto integrador | Mar 16-20 |
| Eval 4 | 15% | 14 | Laboratorio + sustentación | Abr 20-24 |
| Eval 5 | 15% | 16 | Proyecto + presentación | May 04-08 |
| Examen Final | 20% | 19 | Examen integral | May 25-28 |

---

## Tecnologías Utilizadas

- **Sistemas Operativos:** Linux (Ubuntu), Windows 11, macOS
- **Lenguajes:** Python, Bash, C (opcional)
- **Virtualización:** VirtualBox
- **Herramientas:** VS Code, GCC, make

---

## Instalación

### Requisitos Previos

- Computadora con 4GB RAM mínimo (8GB recomendado)
- 20GB de espacio libre en disco
- Conexión a internet

### Pasos de Instalación

1. Instalar VirtualBox
2. Descargar Ubuntu Server/Desktop ISO
3. Crear máquina virtual
4. Instalar Ubuntu
5. Instalar herramientas adicionales:
   ```bash
   sudo apt update
   sudo apt install build-essential python3 python3-pip git vim htop
   ```

---

## Uso del Repositorio

### Para Estudiantes

Este repositorio contiene:
- **Material de clase:** Slides, ejemplos de código, ejercicios
- **Guías de laboratorio:** Instrucciones paso a paso
- **Proyectos:** Enunciados y rúbricas
- **Recursos adicionales:** Bibliografía, enlaces, herramientas

**Nota:** Las evaluaciones están en una carpeta separada (oculta) por seguridad.

### Para el Docente

- **Memory Bank:** Ver `memory-bank/` para contexto completo del curso
- **Progreso:** Ver `memory-bank/progress.md` para estado actual
- **Tareas:** Ver `memory-bank/tasks/` para seguimiento de trabajo

---

## Pedagogía

### Enfoque

- **Learning by Doing:** Proyectos prácticos desde la primera semana
- **Flipped Classroom:** Teoría antes de clase, práctica durante clase
- **Talleres en Parejas:** Colaboración + sustentación oral

### Anti-IA

Para evitar el uso deshonesto de IA:
- Sustentaciones orales obligatorias
- Preguntas sobre decisiones de implementación
- Code review en vivo

---

## Convenciones

### Commits

```
feat: agregar clase 01 de introducción
fix: corregir error en algoritmo de scheduler
docs: actualizar syllabus
eval: crear evaluación 1 (oculta)
```

### Branches

- `main`: Rama principal
- `develop`: Desarrollo
- `feature/unidad-X`: Desarrollo por unidad

---

## Licencia

Este material es para uso educativo en el curso IF0040 de la UNAULA.

---

**Docente:** [Nombre]
**Última actualización:** 2026-01-31
