---
marp: true
theme: default
paginate: true
header: 'IF0099 - Sistemas Operativos I | Unidad 8'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
---

# Clase 12: Protección y Seguridad

<style>
section {
  font-size: 20px;
  overflow: hidden;
}
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
  font-size: 0.95em;
  border-collapse: collapse;
  margin: 0.5em auto;
  table-layout: auto;
}
section th {
  background-color: #1e40af;
  color: white;
  padding: 0.4em 0.6em;
  text-align: left;
  font-size: 0.95em;
  border: 1px solid #ddd;
}
section td {
  padding: 0.4em 0.6em;
  border: 1px solid #ddd;
  vertical-align: top;
  word-wrap: break-word;
  font-size: 0.9em;
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
## Dominios, Control de Acceso y Amenazas

**IF0099 - Sistemas Operativos I**
*4° Semestre - Ingeniería Informática*

![Protección vs Seguridad](../../../assets/infografias/clase-12-proteccion-seguridad-v2.png)

**Conceptos Clave de esta Clase:**

| Área | Pregunta Fundamental |
|------|---------------------|
| **Protección** | ¿Cómo controla el SO quién accede a qué? |
| **Seguridad** | ¿Cómo defendemos el sistema de amenazas? |
| **Dominios** | ¿Cómo agrupamos permisos lógicamente? |
| **Amenazas** | ¿Qué puede atacar nuestro sistema? |

> **Nota:** Esta infografía muestra la diferencia entre **Protección** (mecanismos internos del SO para controlar acceso) y **Seguridad** (defensa contra amenazas externas e internas).

---

## Objetivos de la Clase

Al finalizar esta clase, el estudiante será capaz de:

1. **Diferenciar** protección de seguridad
2. **Explicar** los dominios de protección
3. **Describir** mecanismos de control de acceso
4. **Identificar** amenazas comunes y defensas

**Duración:** 90 minutos

---

## Protección vs Seguridad

### Dos caras de la misma moneda

```
┌─────────────────────────────────────────────────────────────┐
│                      PROTECCIÓN                             │
│  "Mecanismo interno del SO para controlar acceso            │
│   de procesos/usuarios a recursos"                          │
│                                                             │
│  • Control de acceso a archivos                             │
│  • Separación de memoria entre procesos                     │
│  • Permisos de ejecución                                    │
│                                                             │
│  Ejemplo: chmod 755 archivo.txt                             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                       SEGURIDAD                             │
│  "Garantizar que el sistema funcione según lo previsto      │
│   frente a amenazas internas y externas"                    │
│                                                             │
│  • Autenticación de usuarios                                │
│  • Cifrado de datos                                         │
│  • Defensa contra malware                                   │
│  • Auditoría y logs                                         │
│                                                             │
│  Ejemplo: SSH key + contraseñas hasheadas                   │
└─────────────────────────────────────────────────────────────┘
```

**Analogía:**
- **Protección** = Cerraduras en las puertas de tu casa
- **Seguridad** = Sistema de alarma + vigilancia + seguro

> **Insight:** La protección es interna (el SO controla); la seguridad es externa (defenderse de atacantes).

---

## Principios de Protección

### 1. Principio de Mínimo Privilegio

```
                     MAL                          BIEN
           ┌─────────────────────┐     ┌─────────────────────┐
           │ Proceso Web Server  │     │ Proceso Web Server  │
           │                     │     │                     │
           │ Permisos: root      │     │ Permisos:           │
           │ (acceso a TODO)     │     │ - Leer /var/www     │
           │                     │     │ - Escribir /var/log │
           │ Si es comprometido: │     │ - Puerto 80/443     │
           │ ¡Control total!     │     │                     │
           └─────────────────────┘     │ Si es comprometido: │
                                       │ Daño limitado       │
                                       └─────────────────────┘
```

> "Un proceso debe tener exactamente los privilegios que necesita
> para realizar su tarea, nada más."

---

## Dominios de Protección

### Dominio = Conjunto de derechos de acceso

```
                      OBJETOS
              ┌─────┬─────┬─────┬─────┐
              │ F1  │ F2  │ F3  │ Imp │
┌─────────────┼─────┼─────┼─────┼─────┤
│ Dominio D0  │ R   │ RW  │     │     │  ← Usuario común
├─────────────┼─────┼─────┼─────┼─────┤
│ Dominio D1  │ RWX │ R   │ RW  │     │  ← Desarrollador
├─────────────┼─────┼─────┼─────┼─────┤
│ Dominio D2  │ RWX │ RWX │ RWX │ W   │  ← Administrador
└─────────────┴─────┴─────┴─────┴─────┘

R = Leer    W = Escribir    X = Ejecutar
F1, F2, F3 = Archivos       Imp = Impresora
```

**Conceptos clave:**
- **Un proceso ejecuta en un dominio** específico
- **Un usuario puede tener múltiples dominios** (cambia según contexto)
- **Cambios de dominio** = Transiciones de privilegio (ej: `sudo`)

**Ejemplo real:**
- Usuario normal → Dominio D0 (leer documentos)
- Ejecuta `sudo` → Dominio D2 (administrar sistema)
- Ejecuta compilador → Dominio D1 (acceso a herramientas)

---

## Matriz de Acceso

### Implementación de dominios

```
            MATRIZ DE ACCESO (Conceptual)
         ┌────────┬────────┬────────┬────────┬────────┐
         │ /etc/  │ /home/ │ /var/  │ Printer│ D1     │
         │ passwd │ juan   │ log    │        │        │
┌────────┼────────┼────────┼────────┼────────┼────────┤
│ D0     │ R      │        │        │        │ switch │
│ (juan) │        │ RWX    │ R      │ W      │        │
├────────┼────────┼────────┼────────┼────────┼────────┤
│ D1     │ RW     │ RWX    │ RW     │ W      │        │
│ (root) │        │        │        │        │        │
└────────┴────────┴────────┴────────┴────────┴────────┘

"switch" = puede cambiar a otro dominio (ej: sudo)
```

**El problema de la matriz:**
- Sistemas reales: miles de usuarios × millones de objetos
- Matriz **enorme y dispersa** (la mayoría está vacía)
- Almacenarla completa es ineficiente

**Soluciones prácticas:**
1. **ACL (Access Control Lists)** - Lista por cada objeto
2. **Capabilities** - Token que porta cada proceso
3. **Roles** - Agrupar permisos por función (RBAC)

---

## Implementación: ACL vs Capabilities

### ACL (Access Control Lists) - Por objeto

```
Archivo: /etc/passwd
┌────────────────────────────────┐
│  ACL:                          │
│  - juan: R                     │
│  - maria: R                    │
│  - root: RW                    │
│  - grupo admin: RW             │
└────────────────────────────────┘

Ventaja: Fácil ver quién accede a un archivo
Desventaja: Difícil ver a qué accede un usuario
```

**Uso típico:** Unix/Linux (chmod, Windows ACLs)

### Capabilities - Por dominio/proceso

```
Proceso: usuario juan
┌────────────────────────────────┐
│  Capabilities:                 │
│  - /etc/passwd: R              │
│  - /home/juan/*: RWX           │
│  - /var/log: R                 │
└────────────────────────────────┘

Ventaja: Fácil ver permisos de un proceso
Desventaja: Difícil auditar un archivo
```

**Uso típico:** Distribuciones Linux (capsicum), KeyKOS (historioco)

> **Insight:** ACL = "¿Quién puede entrar aquí?" vs Capabilities = "¿A dónde puedo ir yo?"

---

## Permisos en Unix/Linux

### Modelo UGO (User, Group, Others)

```
$ ls -l archivo.txt
-rw-r--r-- 1 juan developers 1024 Feb 15 10:30 archivo.txt
 │││││││││   │     │
 │││││││││   │     └── grupo propietario
 │││││││││   └──────── usuario propietario
 │││││││││
 ││││││└┴┴── others: r-- (solo lectura)
 │││└┴┴───── group: r-- (solo lectura)
 └┴┴──────── user: rw- (lectura y escritura)
 │
 └────────── tipo: - (archivo regular)
```

**Notación octal: 644**
```
  6 (rw-) = 4+2+0 = 110 binario = leer + escribir
  4 (r--) = 4+0+0 = 100 binario = solo leer
  4 (r--) = 4+0+0 = 100 binario = solo leer
```

**Valores octales comunes:**
| Código | Significado |
|--------|-------------|
| `777` | Todos pueden todo (¡peligroso!) |
| `755` | Propietario: todo; otros: leer+ejecutar |
| `644` | Propietario: leer/escribir; otros: leer |
| `600` | Solo el propietario puede leer/escribir |

---

## Permisos Especiales en Linux

### SUID, SGID, Sticky Bit

```
SUID (Set User ID):
-rwsr-xr-x 1 root root /usr/bin/passwd
    ^
    El proceso ejecuta con permisos del PROPIETARIO (root)
    Permite a usuarios cambiar su password en /etc/shadow
```

**¿Por qué SUID es necesario?**
- `/etc/shadow` solo es escribible por root
- Los usuarios necesitan cambiar su contraseña
- `passwd` tiene SUID → se ejecuta como root temporalmente

```
SGID (Set Group ID):
drwxrws--- 2 juan proyecto /proyecto/
       ^
       Nuevos archivos heredan el grupo del directorio
```

**Uso práctico:** Directorios compartidos por equipos
- Todos los archivos creados pertenecen al grupo del proyecto
- Facilita la colaboración sin cambiar permisos manualmente

```
Sticky Bit:
drwxrwxrwt 10 root root /tmp/
          ^
          Solo el propietario puede borrar sus archivos
          (aunque /tmp sea escribible por todos)
```

**Problema que resuelve:** Sin sticky bit, cualquiera podría borrar archivos de otros en `/tmp`

---

## Control de Acceso en Windows

### ACL Discrecional (DACL)

```
Archivo: C:\Documentos\reporte.docx
┌─────────────────────────────────────────────────────────┐
│  Security Descriptor                                    │
│  ├── Owner: DOMAIN\juan                                 │
│  ├── Group: DOMAIN\Users                                │
│  └── DACL:                                              │
│      ├── DOMAIN\juan: Full Control                      │
│      ├── DOMAIN\Managers: Read, Write                   │
│      ├── DOMAIN\Users: Read                             │
│      └── Everyone: (denegado)                           │
└─────────────────────────────────────────────────────────┘
```

**Permisos granulares de Windows:**
| Permiso | Descripción |
|---------|-------------|
| **Read** | Leer contenido |
| **Write** | Modificar contenido |
| **Execute** | Ejecutar programa |
| **Delete** | Borrar archivo |
| **Read Permissions** | Ver permisos |
| **Change Permissions** | Modificar permisos |
| **Take Ownership** | Convertirse en propietario |

**Diferencia clave con Unix:**
- Unix: 3 categorías fijas (User, Group, Others)
- Windows: ACL arbitraria con tantos usuarios como se necesite

---

## Amenazas de Seguridad

### Clasificación de ataques

```
┌─────────────────────────────────────────────────────────────┐
│                    TIPOS DE AMENAZAS                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  MALWARE                    ATAQUES DE RED                  │
│  ├── Virus                  ├── Man-in-the-middle           │
│  ├── Worm (gusano)          ├── DoS/DDoS                    │
│  ├── Trojan                 ├── SQL Injection               │
│  ├── Ransomware             └── Phishing                    │
│  ├── Spyware                                                │
│  └── Rootkit                ATAQUES LOCALES                 │
│                             ├── Privilege escalation        │
│  INGENIERÍA SOCIAL          ├── Buffer overflow             │
│  ├── Phishing               └── Keylogger                   │
│  └── Pretexting                                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Amenazas más comunes en SO:**
| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **Buffer Overflow** | Sobrescribir memoria | Código inyectado |
| **Privilege Escalation** | Obtener más permisos | exploit de sudo |
| **DoS/DDoS** | Sobrecargar servicio | Ataque a servidor web |
| **Malware** | Código malicioso | Ransomware WannaCry |

---

## Amenaza: Buffer Overflow

### Cómo funciona el ataque

```c
void funcion_vulnerable(char *entrada) {
    char buffer[64];
    strcpy(buffer, entrada);  // ¡No verifica tamaño!
}
```

**Antes del ataque:**
```
STACK:
┌───────────────────┐
│ Dirección retorno │ ← Return address (pila de ejecución)
├───────────────────┤
│ Variables locales │
├───────────────────┤
│   buffer[64]      │ ← 64 bytes reservados
└───────────────────┘
```

**Después del ataque:**
```
STACK:
┌─────────────────────────────────────┐
│ Dirección del código malicioso │ ← ¡Sobrescrito!
├─────────────────────────────────────┤
│   NOP NOP NOP ...                   │
├─────────────────────────────────────┤
│   CÓDIGO MALICIOSO (shellcode)      │ ← Payload
├─────────────────────────────────────┤
│   AAAAAAAAAAAAA...                  │ ← Padding
└─────────────────────────────────────┘
```

**Defensas modernas:**
| Mecanismo | Qué hace |
|-----------|----------|
| **Stack Canary** | Valor secreto antes del return address |
| **ASLR** | Direcciones de memoria aleatorias |
| **NX Bit** | No ejecutar código en la pila |
| **Fortify Source** | Funciones que verifican tamaño |

---

## Mecanismos de Defensa

### Estrategias multicapa

| Mecanismo | Descripción | Protege contra | Ejemplo |
| ----------- | ------------- | ---------------- |---------|
| **Autenticación** | Verificar identidad | Acceso no autorizado | Contraseñas, 2FA |
| **Cifrado** | Datos ilegibles sin clave | Intercepción | TLS, AES |
| **Firewall** | Filtrar tráfico de red | Ataques remotos | iptables, pf |
| **Antivirus** | Detectar malware | Virus, trojans | ClamAV, Defender |
| **ASLR** | Direcciones aleatorias | Buffer overflow | Windows, Linux |
| **Sandbox** | Proceso aislado | Malware | Contenedores, jails |
| **Auditoría** | Registro de acciones | Detectar intrusos | auth.log |

**Defensa en profundidad:**
```
┌─────────────────────────────────────────────────────────────┐
│  CAPA 1: Perímetro         Firewall, IDS/IPS               │
│  CAPA 2: Red               VLAN, Segmentación               │
│  CAPA 3: Host              Antivirus, Hardening             │
│  CAPA 4: Aplicación        Validación inputs, Code review   │
│  CAPA 5: Datos             Cifrado, Backups                 │
└─────────────────────────────────────────────────────────────┘
```

> **Principio:** Si una capa falla, las siguientes siguen protegiendo.

---

## Autenticación

### Los tres factores

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  1. ALGO QUE SABES         2. ALGO QUE TIENES              │
│  ┌─────────────────┐       ┌─────────────────┐              │
│  │   Contraseña    │       │  Token físico   │              │
│  │   PIN           │       │  Tarjeta        │              │
│  │   Pregunta sec. │       │  Teléfono (SMS) │              │
│  └─────────────────┘       └─────────────────┘              │
│                                                             │
│  3. ALGO QUE ERES                                           │
│  ┌─────────────────┐                                        │
│  │  Huella digital │                                        │
│  │  Reconocimiento │       MFA = Combinar 2 o más factores │
│  │  facial/iris    │                                        │
│  └─────────────────┘                                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Ejemplos de MFA (Multi-Factor Authentication):**
| Factores | Seguridad | Ejemplo |
|----------|-----------|---------|
| 1 factor | Baja | Solo contraseña |
| 2 factores | Media | Contraseña + SMS |
| 2+ factores | Alta | Contraseña + YubiKey + Huella |

**Consideraciones:**
- **Algo que sabes:** Puede ser robado o adivinado
- **Algo que tienes:** Puede ser robado físicamente
- **Algo que eres:** Difícil de falsificar pero requiere hardware especial

---

## Hash de Contraseñas

### Nunca almacenar contraseñas en texto plano

**INCORRECTO (texto plano):**
```
┌─────────────────────┐
│ usuario │ password  │
├─────────┼───────────┤
│ juan    │ 12345     │  ← ¡Visible si la BD es robada!
│ maria   │ password  │
└─────────┴───────────┘
```

**CORRECTO (hash con salt):**
```
┌─────────────────────────────────┐
│ usuario │ salt  │ hash          │
├─────────┼───────┼───────────────┤
│ juan    │ x7Kg  │ a3f2d1...     │  ← Irreversible
│ maria   │ mN8p  │ 7b2c4e...     │
└─────────┴───────┴───────────────┘
```

**Si la base de datos es robada:**
| Enfoque | Consecuencia |
|---------|--------------|
| Texto plano | ¡Todas las contraseñas expuestas! |
| Hash + salt | Atacante debe crackear cada hash individualmente |

**Algoritmos recomendados (2026):**
| Algoritmo | Ventajas |
|-----------|----------|
| **bcrypt** | Probado, factor de trabajo ajustable |
| **scrypt** | Resistente a hardware especializado (ASIC) |
| **Argon2** | Ganador de Password Hashing Competition 2015 |

---

## Linux: Seguridad de Contraseñas

### Separación de archivos /etc/passwd y /etc/shadow

```bash
# /etc/passwd (legible por todos)
juan:x:1000:1000:Juan Garcia:/home/juan:/bin/bash
     ^
     "x" indica que el hash está en /etc/shadow
```

**¿Por qué /etc/passwd es legible por todos?**
- Contiene información necesaria para el funcionamiento del sistema
- UID, GID, home directory, shell
- Programes necesitan leer estos datos (ls, whoami, etc.)

```bash
# /etc/shadow (solo root)
juan:$6$rounds=5000$salt$hash...:19000:0:99999:7:::
     │  │              │
     │  │              └── Hash de contraseña (SHA-512)
     │  └──────────────── Sal aleatoria (salt)
     └─────────────────── $6$ = SHA-512, $5$ = SHA-256, $1$ = MD5
```

**Verificación de permisos:**
```bash
$ ls -l /etc/shadow
-rw-r----- 1 root shadow 1234 Feb 15 10:30 /etc/shadow
      │    │    │
      │    │    └── Solo root puede leer/escribir
      │    └──────── Grupo shadow puede leer
      └────────────── Propietario root
```

> **Insight:** La separación permite que programas lean info del usuario sin exponer las contraseñas.

---

## Actividad Práctica (10 min)

### Explorando permisos en Linux

**En parejas, realizar:**

```bash
# 1. Ver permisos de passwd y shadow
ls -l /etc/passwd /etc/shadow

# 2. Ver tu usuario y grupos
id

# 3. Crear archivo y cambiar permisos
touch prueba.txt
chmod 750 prueba.txt
ls -l prueba.txt
```

**Interpretar el permiso 750:**
| Categoría | Permisos | Significado |
|-----------|----------|-------------|
| **Propietario** | rwx (7) | Leer, escribir, ejecutar |
| **Grupo** | r-- (5) | Solo leer |
| **Otros** | --- (0) | Sin permisos |

**Preguntas de discusión:**
1. ¿Por qué `/etc/passwd` es legible pero `/etc/shadow` no?
2. ¿Qué pasaría si `/etc/shadow` tuviera permisos 644?
3. ¿Cómo se vería el permiso 755 en formato rwx?

---

## Resumen de la Clase

### Conceptos fundamentales de protección y seguridad

| Concepto | Descripción | Ejemplo práctico |
| ---------- | ------------- |-----------------|
| **Protección** | Mecanismos internos del SO para controlar acceso | `chmod 644 archivo.txt` |
| **Seguridad** | Defensa contra amenazas internas y externas | Firewall, antivirus |
| **Dominio** | Conjunto de derechos de acceso | Usuario, root, desarrollador |
| **ACL** | Lista de permisos por objeto | Windows ACLs |
| **UGO** | Modelo User-Group-Others de Unix | `rwxr-xr-x` |
| **SUID** | Ejecutar con permisos del propietario | `/usr/bin/passwd` |
| **Hash** | Nunca almacenar contraseñas en texto plano | bcrypt, Argon2 |

**Puntos clave para recordar:**
1. **Protección ≠ Seguridad:** La protección es interna; la seguridad incluye defensa externa
2. **Principio de mínimo privilegio:** Dar solo los permisos necesarios
3. **Defensa en profundidad:** Múltiples capas de seguridad
4. **Autenticación fuerte:** MFA + contraseñas hasheadas con salt

---

## Evaluación Final

### Examen Teórico-Práctico - Semana 17-18

**Contenido: Unidades 5-8**

| Unidad | Temas clave |
|--------|-------------|
| **5** | Paginación, memoria virtual, marcos de página |
| **6** | Sistemas de archivos (FAT32, NTFS, ext4) |
| **7** | E/S (polling, interrupciones, DMA) |
| **8** | Protección, seguridad, autenticación |

**Formato del examen:**
| Componente | Porcentaje | Tipo de preguntas |
|------------|-----------|-------------------|
| Conceptual | 40% | Definiciones, comparaciones |
| Práctico | 40% | Ejercicios de permisos, cálculos |
| Análisis | 20% | Casos de estudio, escenarios |

---

## Cierre del Curso

### Recorrido completo del semestre

```
Unidad 1: ¿Qué es un SO?
    ├─ Estructura y componentes
    └─ Evolución histórica
    ↓
Unidad 2-3: Procesos y Planificación
    ├─ Estados del proceso
    ├─ PCB, context switch
    └─ Algoritmos: FCFS, SJF, RR, Priority
    ↓
Unidad 4: Sincronización
    ├─ Sección crítica
    ├─ Semáforos y mutex
    └─ Deadlocks: prevención y detección
    ↓
Unidad 5: Memoria
    ├─ Particiónamiento
    ├─ Paginación y marcos de página
    └─ Memoria virtual y swapping
    ↓
Unidad 6: Sistemas de archivos
    ├─ Estructura (FAT32, NTFS, ext4)
    ├─ Inodos y bloques de datos
    └─ Montaje y desmontaje
    ↓
Unidad 7: E/S
    ├─ Polling vs interrupciones
    ├─ DMA (Direct Memory Access)
    └─ Drivers de dispositivo
    ↓
Unidad 8: Protección y Seguridad
    ├─ Dominios de protección
    ├─ ACL vs Capabilities
    ├─ Permisos (Unix UGO, Windows ACL)
    └─ Autenticación y defensas
```

> **El SO es el corazón de todo sistema computacional!**

---

## Recursos para Seguir Aprendiendo

### Continuar el viaje en sistemas operativos

| Tipo | Recurso | Descripción |
|------|---------|-------------|
| **Libro** | Operating System Concepts (Silberschatz) | El "dinosaurio azul" - referencia clásica |
| **Libro** | Modern Operating Systems (Tanenbaum) | Enfoque práctico y actualizado |
| **Práctica** | xv6 | Unix V6 reescrito en C (MIT) |
| **Práctica** | OSDev wiki | Comunidad de desarrollo de SO |
| **Certificación** | LPIC-1 | Linux Professional Institute |
| **Certificación** | CompTIA Linux+ | Certificación de Linux |
| **Cursos** | Sistemas distribuidos | Próximo nivel académico |
| **Cursos** | Virtualización y contenedores | Docker, KVM, Xen |

### ¡Gracias por su participación!

**Sistemas Operativos I - 2026-I**
UNAULA - Ingeniería Informática
