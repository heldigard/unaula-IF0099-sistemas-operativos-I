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
| Claude-Opus | claude-opus-4.5 | ACTIVO | 2026-02-01 14:30 | 2026-02-01 15:00 |
| Claude Code | deepseek-chat | Activo | 2026-02-01 12:08 | 2026-02-01 12:08 |

## Agentes activos
| Agente | Modelo | Estado | Inicio | Último update |
|---|---|---|---|---|
| Claude-Opus | claude-opus-4.5 | ACTIVO | 2026-02-01 14:30 | 2026-02-01 15:15 |
| Claude Code | deepseek-chat | Activo | 2026-02-01 12:08 | 2026-02-01 12:08 |

## Locks (tareas reclamadas)
| Clase/Archivo | Agente | Estado | Inicio | Último update | TTL | Notas |
|---|---|---|---|---|---|---|
| clase-05 | Claude-Opus | DONE | 2026-02-01 14:30 | 2026-02-01 14:45 | - | Sección crítica y semáforos |
| clase-06 | Claude-Opus | DONE | 2026-02-01 14:45 | 2026-02-01 15:00 | - | Gestión de memoria |
| clase-07 | Claude Code | IN_PROGRESS | 2026-02-01 12:08 | 2026-02-01 12:08 | 45min | Paginación y memoria virtual |
| clase-08 | Claude-Opus | DONE | 2026-02-01 15:00 | 2026-02-01 15:15 | - | Memoria secundaria y discos |
| clase-09 | Claude-Opus | IN_PROGRESS | 2026-02-01 15:15 | 2026-02-01 15:15 | 45min | Sistemas de archivos |

## Bitácora (chat entre agentes)
(Entradas cortas con timestamp)
- 2026-02-01 14:30 — [Claude-Opus] Iniciando sesión. Detectadas clases 01-04 ya generadas. Procedo con clase-05 (Sección Crítica y Semáforos).
- 2026-02-01 14:45 — [Claude-Opus] clase-05 COMPLETADA. HTML generado con scroll, 3 infografías integradas (clase-05-seccion-critica.png, clase-05-semaforos.png, clase-05-semaforos-mutex.png). Procedo con clase-06.
- 2026-02-01 12:10 — [Claude Code] Registrado. Tomando LOCK de clase-07 (Paginación y memoria virtual). Generaré HTML en clases-html/clase-07.html. Fuente: clases/unidad-05-memoria/clase-07-paginacion-memoria-virtual.md. Imágenes disponibles: clase-07-tabla-paginas.png. Riesgo: contenido puede estar compactado, necesitaré expandir.
- 2026-02-01 15:00 — [Claude-Opus] clase-06 COMPLETADA. HTML generado con scroll, 3 infografías integradas (clase-06-jerarquia-memoria.png, clase-06-fragmentacion.png, clase-06-traduccion-direcciones.png). Veo que clase-07 está tomada por Claude Code, tomo LOCK de clase-08.
- 2026-02-01 15:15 — [Claude-Opus] clase-08 COMPLETADA. HTML generado con scroll, 1 infografía integrada (clase-08-estructura-disco.png). Continuo con clase-09.

## Backlog sugerido
- P0: clases de mañana (pendiente definir con usuario)
- P1: clase-07 (LOCK por Claude Code), clase-09 (LOCK por Claude-Opus), clase-10
- P2: resto del curso (clases 11-16)

---

## Estado del repositorio (descubrimiento automático)
- Clases HTML existentes: 01, 02, 03, 04, 05, 06, 08
- Clases pendientes: 07, 09-16 (9 clases)
- Infografías disponibles: 23+ en assets/infografias/
- Estructura contenido: clases/unidad-*/clase-*.md
