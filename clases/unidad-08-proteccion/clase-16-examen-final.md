---
marp: true
theme: default
paginate: true
| header: 'IF0099 - Sistemas Operativos I | Examen Final' |
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
## Evaluación Integral
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

---
## Evaluación Integral

*(continuación...)*



**IF0099 - Sistemas Operativos I**
*4° Semestre - Ingeniería Informática*
---

## Indicaciones Generales

- **Duración:** 90 minutos
- **Formato:** Teórico + práctico
- **Temas:** Todo el curso
- **Reglas:** Sin acceso a internet

---

## Estructura del Examen

1. **Conceptos fundamentales** (20%)
2. **Procesos y planificación** (20%)
3. **Memoria y archivos** (30%)
4. **E/S, protección, distribuidos** (30%)

---

## Recomendaciones

- Leer cada pregunta con calma
- Justificar respuestas con conceptos vistos
- Revisar cálculos de planificación

---

## Inicio del Examen

**¡Éxitos!**



---

## 📝 Guía de Preparación para el Examen Final

### Estructura del Examen

| Sección | Tipo | Puntos | Tiempo |
|---------|------|--------|--------|
| **Parte 1:** Conceptos Teóricos | Selección Múltiple | 30% | 30 min |
| **Parte 2:** Análisis de Casos | Desarrollo | 40% | 45 min |
| **Parte 3:** Ejercicios Prácticos | Cálculos/Código | 30% | 45 min |
| **TOTAL** | | **100%** | **120 min** |

---

## 📚 Temas Principales a Estudiar

### Unidad 1-2: Introducción y Procesos (20%)

**Conceptos clave:**
- ✅ Definición de Sistema Operativo
- ✅ Funciones del SO (gestión de recursos)
- ✅ Modos de operación (usuario vs kernel)
- ✅ Estructura de un proceso (PCB)
- ✅ Estados de proceso (nuevo, listo, ejecución, bloqueado, terminado)
- ✅ Cambio de contexto

**Pregunta tipo:**
> Un proceso ejecuta `read()` para leer de disco. ¿Qué transición de estados ocurre?  
> Respuesta: Ejecución → Bloqueado (esperando I/O)

---

### Unidad 3: Planificación de CPU (15%)

**Algoritmos a dominar:**
- ✅ FCFS (First-Come First-Served)
- ✅ SJF (Shortest Job First)
- ✅ SRTF (Shortest Remaining Time First)
- ✅ Round Robin
- ✅ Prioridades

**Ejercicio tipo:**
> Procesos: P1(24ms), P2(3ms), P3(3ms)  
> Calcular tiempo de espera promedio con FCFS vs SJF

**Solución:**
- FCFS: (0+24+27)/3 = 17ms
- SJF: (0+3+6)/3 = 3ms

---

### Unidad 4: Sincronización (15%)

**Conceptos clave:**
- ✅ Race condition
- ✅ Sección crítica
- ✅ Semáforos (mutex, contador)
- ✅ Problemas clásicos: Productor-Consumidor, Lectores-Escritores

**Código tipo a analizar:**
```c
sem_t mutex = 1;
int counter = 0;

// Thread 1
sem_wait(&mutex);
counter++;
sem_post(&mutex);

// Thread 2
sem_wait(&mutex);
counter--;
sem_post(&mutex);
```
> Pregunta: ¿Hay race condition? No, está protegido por mutex.

---

### Unidad 5: Gestión de Memoria (20%)

**Conceptos clave:**
- ✅ Jerarquía de memoria (registros → cache → RAM → disco)
- ✅ Paginación: dirección virtual → dirección física
- ✅ Tabla de páginas
- ✅ TLB (Translation Lookaside Buffer)
- ✅ Page fault
- ✅ Algoritmos de reemplazo: FIFO, LRU, Óptimo

**Ejercicio tipo:**
> Sistema: páginas de 4KB, RAM de 16MB  
> Dirección virtual: 0x3004  
> ¿Qué página? ¿Qué offset?

**Solución:**
- Página = 0x3004 / 4096 = 3
- Offset = 0x3004 % 4096 = 4

---

### Unidad 6-7: Sistemas de Archivos (15%)

**Conceptos clave:**
- ✅ FAT vs ext4 vs NTFS
- ✅ Inodos: estructura, punteros directos/indirectos
- ✅ Hard links vs Soft links
- ✅ Fragmentación interna vs externa
- ✅ Journaling

**Pregunta tipo:**
> ¿Cuál es la capacidad máxima teórica de un inodo ext4 con:  
> - 12 punteros directos  
> - 1 indirecto simple  
> - Bloques de 4KB  
> - Punteros de 4 bytes (1024 por bloque)

**Solución:**
- Directos: 12 × 4KB = 48KB
- Indirecto: 1024 × 4KB = 4MB
- Total: ~4MB (sin contar doble/triple)

---

### Unidad 8: Protección y Seguridad (10%)

**Conceptos clave:**
- ✅ Autenticación vs Autorización
- ✅ Control de acceso (ACL, matriz)
- ✅ Cifrado simétrico vs asimétrico
- ✅ Firewalls, IDS/IPS

---

### Unidad 9: Sistemas Distribuidos (5%)

**Conceptos clave:**
- ✅ Teorema CAP
- ✅ Replicación
- ✅ Consenso (Raft, Paxos)

---

## 🎯 Ejercicios de Práctica

### Ejercicio 1: Planificación Round Robin

**Datos:**
- Quantum = 4ms
- Procesos: P1(8ms), P2(4ms), P3(9ms)
- Orden de llegada: P1, P2, P3

**Calcular:**
1. Diagrama de Gantt
2. Tiempo de espera de cada proceso
3. Tiempo de espera promedio
4. Tiempo de retorno promedio

**Solución esperada:**
```
Gantt: P1(0-4) P2(4-8) P3(8-12) P1(12-16) P3(16-20) P3(20-21)
Espera: P1=8ms, P2=0ms, P3=7ms → Promedio=5ms
```

---

### Ejercicio 2: Traducción de Direcciones

**Sistema:**
- Páginas: 1KB (1024 bytes)
- Tabla de páginas:

| Página Virtual | Marco Físico |
|----------------|--------------|
| 0 | 5 |
| 1 | 2 |
| 2 | 8 |
| 3 | 1 |

**Traducir:**
1. Dirección virtual 0x0500 (1280 decimal)
2. Dirección virtual 0x0A00 (2560 decimal)

**Solución:**
1. 1280 / 1024 = Página 1, Offset 256 → Marco 2, Offset 256 → Física: 2×1024+256 = 2304
2. 2560 / 1024 = Página 2, Offset 512 → Marco 8, Offset 512 → Física: 8×1024+512 = 8704

---

### Ejercicio 3: Semáforos

Identificar el error en este código:

```c
sem_t s1 = 1, s2 = 1;

// Thread A
sem_wait(&s1);
sem_wait(&s2);
// Critical section
sem_post(&s1);
sem_post(&s2);

// Thread B
sem_wait(&s2);
sem_wait(&s1);
// Critical section
sem_post(&s2);
sem_post(&s1);
```

**Problema:** Deadlock potencial (orden inverso de adquisición)

**Solución:** Ambos threads deben adquirir en el mismo orden.

---

## 📖 Material de Estudio Recomendado

### Recursos Principales
1. **Slides de clase:** Repasar todas las presentaciones
2. **Libro:** "Operating System Concepts" - Silberschatz (Cap. 1-13)
3. **Videos:** 
   - MIT OpenCourseWare: 6.828
   - Neso Academy: Operating Systems playlist

### Práctica Adicional
- **Simulador de planificación:** https://cpuschedulingvisualizer.com/
- **Simulador de paginación:** https://www.cs.usfca.edu/~galles/visualization/PagingTable.html

---

## ✅ Checklist de Preparación

**2 semanas antes:**
- [ ] Revisar todos los slides de clase
- [ ] Identificar temas débiles
- [ ] Resolver ejercicios de cada unidad

**1 semana antes:**
- [ ] Rehacer todas las actividades prácticas
- [ ] Estudiar en grupo (discutir conceptos)
- [ ] Crear resumen de fórmulas y algoritmos

**3 días antes:**
- [ ] Resolver exámenes de años anteriores (si disponibles)
- [ ] Repasar ejercicios que se equivocaron
- [ ] Descansar bien

**Día del examen:**
- [ ] Llegar 15 min antes
- [ ] Leer todas las preguntas primero
- [ ] Administrar tiempo (40 min por sección)

---

## 💡 Consejos para el Examen

1. **Lee cuidadosamente:** Muchos errores son por malinterpretar la pregunta
2. **Administra el tiempo:** No te quedes atascado en una pregunta
3. **Muestra tu trabajo:** En ejercicios de cálculo, los pasos parciales dan puntos
4. **Verifica:** Si terminas antes, revisa respuestas
5. **Mantén la calma:** Si no sabes una, sigue con la siguiente

---

## ❓ Preguntas Frecuentes

**P: ¿Puedo traer material de consulta?**  
R: No, el examen es sin material. Pero puedes traer calculadora básica.

**P: ¿Habrá preguntas de programación?**  
R: Sí, leer/analizar código C (no escribir desde cero).

**P: ¿Qué pasa si no termino?**  
R: Intenta responder algo de cada sección. Puntos parciales cuentan.

**P: ¿Puedo hacer preguntas durante el examen?**  
R: Solo para aclarar enunciados ambiguos, no sobre contenido.

---

## 🎓 ¡Mucho Éxito!

**Recuerda:** El examen evalúa comprensión, no memorización. Enfócate en entender conceptos y saber aplicarlos.

---
