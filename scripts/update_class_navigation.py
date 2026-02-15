#!/usr/bin/env python3
"""
Script para actualizar navegación y fechas en todas las clases HTML.
Agrega barra de navegación con enlaces a cronograma y rúbricas.
"""

import os
import re

# Mapeo de clases a fechas según cronograma
# Cada sesión tiene 2 slots: contenido (6:00-8:00) y práctica (8:00-9:00)
CLASS_DATES = {
    "clase-01": {"date": "04 de Febrero 2026", "time": "Teoría: 6:00-8:00 AM"},
    "clase-02": {"date": "04 de Febrero 2026", "time": "Práctica: 8:00-9:00 AM"},
    "clase-03": {"date": "11 de Febrero 2026", "time": "Teoría: 6:00-8:00 AM"},
    "clase-04": {"date": "11 de Febrero 2026", "time": "Práctica: 8:00-9:00 AM"},
    "clase-05": {"date": "18 de Febrero 2026", "time": "Teoría: 6:00-8:00 AM"},
    "clase-06": {"date": "18 de Febrero 2026", "time": "Práctica: 8:00-9:00 AM"},
    "clase-07": {"date": "25 de Febrero 2026", "time": "Teoría: 6:00-8:00 AM"},
    "clase-08": {"date": "04 de Marzo 2026", "time": "Teoría: 6:00-8:00 AM"},
    "clase-09": {"date": "04 de Marzo 2026", "time": "Práctica: 8:00-9:00 AM"},
    "clase-10": {"date": "11 de Marzo 2026", "time": "Teoría: 6:00-8:00 AM"},
    "clase-11": {"date": "18 de Marzo 2026", "time": "Teoría: 6:00-8:00 AM"},
    "clase-12": {"date": "18 de Marzo 2026", "time": "Práctica: 8:00-9:00 AM"},
    "clase-13": {"date": "15 de Abril 2026", "time": "Teoría: 6:00-8:00 AM"},
    "clase-14": {"date": "15 de Abril 2026", "time": "Práctica: 8:00-9:00 AM"},
    "clase-15": {"date": "22 de Abril 2026", "time": "Teoría: 6:00-8:00 AM"},
    "clase-16": {"date": "29 de Abril 2026", "time": "Teoría: 6:00-8:00 AM"},
}

# Nombres de clases para navegación
CLASS_NAMES = {
    "clase-01": "¿Qué es un Sistema Operativo?",
    "clase-02": "Linux Terminal - Comandos Esenciales",
    "clase-03": "Windows Server 2022",
    "clase-04": "Estructura del Sistema Operativo",
    "clase-05": "Procesos en Linux",
    "clase-06": "Procesos en Windows",
    "clase-07": "Hilos y Sincronización",
    "clase-08": "Comunicación entre Procesos (IPC)",
    "clase-09": "Permisos y Seguridad en Linux",
    "clase-10": "Permisos y Seguridad en Windows",
    "clase-11": "Almacenamiento LVM",
    "clase-12": "Memoria Virtual",
    "clase-13": "Servidor Web Apache",
    "clase-14": "Servidor Web IIS",
    "clase-15": "Servidor FTP",
    "clase-16": "Active Directory",
}

QUICK_NAV_TEMPLATE = '''
        <!-- Quick Navigation Bar -->
        <div class="quick-nav" style="background: white; padding: 1rem; margin-bottom: 2rem; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem;">
            <div style="display: flex; align-items: center; gap: 1rem;">
                <a href="index.html" style="color: var(--primary); text-decoration: none; font-weight: 500;">Inicio</a>
                <span style="color: var(--text-muted);">|</span>
                <span style="color: var(--text-main); font-weight: 600;">{class_name}</span>
            </div>
            <div style="display: flex; align-items: center; gap: 0.5rem;">
                <a href="cronograma.html" style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.5rem 1rem; background: #10b981; color: white; text-decoration: none; border-radius: 6px; font-weight: 500;">Cronograma</a>
                <a href="rubricas.html" style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.5rem 1rem; background: #3b82f6; color: white; text-decoration: none; border-radius: 6px; font-weight: 500;">Rubricas</a>
            </div>
        </div>
'''

FOOTER_TEMPLATE = '''
    <footer>
        <div class="container">
            <p><strong>IF0099 - Sistemas Operativos I</strong> - {class_name}</p>
            <p>Fecha: {date} | Plan Practico v2.0</p>
            <p style="margin-top: 10px;">
                <a href="index.html" style="color: #10b981;">Inicio</a> |
                <a href="cronograma.html" style="color: #10b981;">Cronograma</a> |
                <a href="rubricas.html" style="color: #3b82f6;">Rubricas</a>
            </p>
        </div>
    </footer>
'''

def update_class_file(filepath):
    """Actualiza una clase HTML con navegación y fecha."""
    class_key = os.path.basename(filepath).replace('.html', '')

    if class_key not in CLASS_DATES:
        print(f"  [SKIP] {filepath} - no hay fecha definida")
        return False

    date_info = CLASS_DATES[class_key]
    class_name = CLASS_NAMES.get(class_key, class_key)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Verificar si ya tiene links a cronograma en el body
    if 'href="cronograma.html"' in content and 'quick-nav' in content:
        print(f"  [SKIP] {filepath} - ya tiene navegacion")
        return False

    # 1. Actualizar meta con fecha
    # Buscar patron de header .meta
    meta_pattern = r'(<p class="meta">)[^<]*(</p>)'
    new_meta = f'<p class="meta">Fecha: {date_info["date"]} | {date_info["time"]} | Plan Practico v2.0</p>'
    content = re.sub(meta_pattern, new_meta, content)

    # 2. Agregar quick nav despues de </header> y antes de <nav>
    quick_nav = QUICK_NAV_TEMPLATE.format(class_name=class_name)

    # Buscar el patron: </header> seguido de espacios y <nav>
    insert_pattern = r'(</header>\s*\n\s*)(<nav>)'
    content = re.sub(insert_pattern, r'\1' + quick_nav + r'\n        \2', content)

    # 3. Actualizar footer
    footer_pattern = r'<footer>.*?</footer>'
    new_footer = FOOTER_TEMPLATE.format(class_name=class_name, date=date_info["date"])
    content = re.sub(footer_pattern, new_footer, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  [OK] {filepath} actualizado")
    return True

def main():
    classes_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    classes_dir = os.path.join(classes_dir, 'clases-html')

    print(f"Actualizando clases en: {classes_dir}")

    updated = 0
    for i in range(1, 17):
        filename = f"clase-{i:02d}.html"
        filepath = os.path.join(classes_dir, filename)
        if os.path.exists(filepath):
            if update_class_file(filepath):
                updated += 1

    print(f"\nTotal clases actualizadas: {updated}")

if __name__ == "__main__":
    main()
