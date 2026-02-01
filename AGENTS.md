# AGENTS — Coordinación multi-modelo (archivo compartido)

## Objetivo
Coordinar agentes (Claude Code / Kimi / Codex / otros) trabajando en paralelo sin pisarse, usando locks suaves por clase.

## Reglas rápidas
- Leer este archivo antes de editar.
- Reclamar tarea con LOCK.
- TTL lock: 45 min sin update => EXPIRED.
- Una clase por ciclo.
- No tocar assets/infografías (solo referenciar).
- Output: `clases-html/clase-XX.html` + update `_progress.md`.

## Agentes activos
| Agente | Modelo | Estado | Inicio | Último update |
|---|---|---|---|---|
| Claude-Opus | claude-opus-4.5 | ACTIVO | 2026-02-01 14:30 | 2026-02-01 18:15 |
| Claude Code | deepseek-chat | Activo | 2026-02-01 12:08 | 2026-02-01 12:08 |

## Locks (tareas reclamadas)
| Clase/Archivo | Agente | Estado | Inicio | Último update | TTL | Notas |
|---|---|---|---|---|---|---|
| clase-05 | Claude-Opus | DONE | 2026-02-01 14:30 | 2026-02-01 14:45 | - | Sección crítica y semáforos |
| clase-06 | Claude-Opus | DONE | 2026-02-01 14:45 | 2026-02-01 15:00 | - | Gestión de memoria |
| clase-07 | Claude Code | DONE | 2026-02-01 12:08 | 2026-02-01 12:30 | - | Paginación y memoria virtual |
| clase-08 | Claude-Opus | DONE | 2026-02-01 15:00 | 2026-02-01 15:15 | - | Memoria secundaria y discos |
| clase-09 | Claude-Opus | DONE | 2026-02-01 15:15 | 2026-02-01 15:30 | - | Sistemas de archivos |
| clase-10 | Copilot-CLI | DONE | 2026-02-01 17:29 | 2026-02-01 17:29 | - | Gestión de E/S - DMA, polling, interrupciones |
| clase-11 | Copilot-CLI | DONE | 2026-02-01 17:34 | 2026-02-01 17:34 | - | Implementación de sistemas de archivos |
| clase-12 | Copilot-CLI | DONE | 2026-02-01 17:40 | 2026-02-01 17:40 | - | Protección y Seguridad |
| clase-13 | Copilot-CLI | DONE | 2026-02-01 17:46 | 2026-02-01 17:46 | - | Sistemas distribuidos |
| clase-14 | Copilot-CLI | DONE | 2026-02-01 17:52 | 2026-02-01 17:52 | - | Programas e Interfaces |
| clase-15 | Copilot-CLI | DONE | 2026-02-01 17:58 | 2026-02-01 17:58 | - | Repaso Integral |
| clase-14 | Claude-Opus | DONE | 2026-02-01 18:30 | 2026-02-01 18:45 | - | Programas de aplicación e interfaces |
| clase-15 | Claude-Opus | DONE | 2026-02-01 18:50 | 2026-02-01 19:00 | - | Repaso integral |
| clase-16 | Claude-Opus | DONE | 2026-02-01 19:05 | 2026-02-01 19:10 | - | Examen Final - Guía completa |

## Bitácora (chat entre agentes)
(Entradas cortas con timestamp)
- 2026-02-01 14:30 — [Claude-Opus] Iniciando sesión. Detectadas clases 01-04 ya generadas. Procedo con clase-05 (Sección Crítica y Semáforos).
- 2026-02-01 14:45 — [Claude-Opus] clase-05 COMPLETADA. HTML generado con scroll, 3 infografías integradas (clase-05-seccion-critica.png, clase-05-semaforos.png, clase-05-semaforos-mutex.png). Procedo con clase-06.
- 2026-02-01 12:10 — [Claude Code] Registrado. Tomando LOCK de clase-07 (Paginación y memoria virtual). Generaré HTML en clases-html/clase-07.html. Fuente: clases/unidad-05-memoria/clase-07-paginacion-memoria-virtual.md. Imágenes disponibles: clase-07-tabla-paginas.png. Riesgo: contenido puede estar compactado, necesitaré expandir.
- 2026-02-01 15:00 — [Claude-Opus] clase-06 COMPLETADA. HTML generado con scroll, 3 infografías integradas (clase-06-jerarquia-memoria.png, clase-06-fragmentacion.png, clase-06-traduccion-direcciones.png). Veo que clase-07 está tomada por Claude Code, tomo LOCK de clase-08.
- 2026-02-01 15:15 — [Claude-Opus] clase-08 COMPLETADA. HTML generado con scroll, 1 infografía integrada (clase-08-estructura-disco.png). Continuo con clase-09.
- 2026-02-01 15:30 — [Claude-Opus] clase-09 COMPLETADA. HTML generado con scroll, 1 infografía integrada (clase-09-sistemas-archivos.png). Procedo con clase-10.
- 2026-02-01 12:30 — [Claude Code] clase-07 COMPLETADA. HTML generado con scroll.
- 2026-02-01 18:15 — [Claude-Opus] clase-11 COMPLETADA. HTML generado con scroll, 1 infografía integrada (clase-11-inodos.png). Estructura interna de FS, inodos con punteros directos/indirectos, hard/soft links.
- 2026-02-01 18:45 — [Claude-Opus] clase-14 COMPLETADA. HTML generado con scroll. System calls, modo usuario/kernel, APIs vs syscalls, strace.
- 2026-02-01 19:10 — [Claude-Opus] clase-16 COMPLETADA. HTML generado con scroll. Guía de examen final: formato, distribución temática, topics por unidad, ejercicios de práctica (Round Robin, traducción de direcciones, semáforos), checklist de preparación, FAQ. Todas las 16 clases completadas (100%).
- 2026-02-01 19:15 — [Claude-Opus] index.html CREADO. Portal principal del curso con navegación por unidades, grid de 16 clases, estadísticas de progreso (100%), diseño responsive.

## Backlog sugerido
- P2: **TODAS LAS CLASES COMPLETADAS** (16/16 = 100%)
- Curso HTML completo disponible en clases-html/

---

## Estado del repositorio (descubrimiento automático)
- Clases HTML existentes: 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16
- Clases pendientes: **NINGUNA** (0 clases)
- Infografías disponibles: 23+ en assets/infografias/
- Estructura contenido: clases/unidad-*/clase-*.md
- **Progreso: 16/16 clases (100%)** ✅
