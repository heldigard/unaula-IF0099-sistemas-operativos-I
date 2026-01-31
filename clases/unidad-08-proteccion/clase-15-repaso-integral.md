---
marp: true
theme: default
paginate: true
| header: 'IF0099 - Sistemas Operativos I | Repaso' |
footer: 'UNAULA - Ingeniería Informática - 2026-I'

  section {
    font-size: 24px;
  }

---
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
---
## Preparación para el examen final
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


# Clase 15: Repaso Integral
## Preparación para el examen final

**IF0099 - Sistemas Operativos I**
*4° Semestre - Ingeniería Informática*
---

## Objetivos

1. **Consolidar** conceptos clave de todo el curso
2. **Identificar** temas débiles y reforzarlos
3. **Resolver** ejercicios tipo examen

**Duración:** 90 minutos

---

## Mapa del Curso

- Introducción y procesos
- Planificación y sincronización
- Memoria y memoria secundaria
- Sistemas de archivos
- E/S y protección
- Distribuidos e interfaces

---

## Preguntas Clave

1. Diferencia entre proceso e hilo
2. FCFS vs SJF vs RR
3. Deadlock: prevención vs detección
4. Paginación vs segmentación
5. Inodos y directorios
6. Syscalls básicas

---

## Ejercicio 1: Planificación

Datos:
- P1 (llega 0, CPU 8)
- P2 (llega 1, CPU 4)
- P3 (llega 2, CPU 9)
- P4 (llega 3, CPU 5)

Tareas:
- FCFS, SJF, RR (q=2)
- Calcular Turnaround y Waiting Time

---

## Ejercicio 2: Memoria

- Tamaño página: 4KB
- Dirección lógica: 0x12345

Preguntas:
1. ¿Cuál es el número de página?
2. ¿Cuál es el offset?

---

## Ejercicio 3: Archivos

- ¿Qué diferencia un archivo y su inodo?
- ¿Qué significa journaling?

---

## Actividad en Clase

En parejas:
1. Resuelvan 2 ejercicios del banco
2. Sustenten su respuesta en 3 minutos

---

## Cierre

- Dudas finales
- Recomendaciones de estudio
- Lineamientos del examen final

---

## Próxima Clase

### Clase 16: Examen Final

- Evaluación integral de todo el curso

**¡Éxitos!**
