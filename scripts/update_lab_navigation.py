#!/usr/bin/env python3
"""
Script para actualizar navegacion en todos los laboratorios HTML.
Agrega barra de navegacion con enlaces a cronograma y rubricas.
"""

import os
import re

# Informacion de laboratorios
LAB_INFO = {
    "lab-00-introduccion-simuladores": {
        "name": "Lab 0: VirtualBox + Ubuntu Server",
        "description": "Instalacion y configuracion inicial"
    },
    "lab-01-comandos-basicos": {
        "name": "Lab 1: Comandos Basicos de Linux",
        "description": "Navegacion y gestion de archivos"
    },
    "lab-02-permisos-usuarios": {
        "name": "Lab 2: Permisos y Usuarios",
        "description": "Gestion de permisos y usuarios en Linux"
    },
    "lab-aws-01-introduccion-ec2": {
        "name": "Lab AWS 1: Introduccion a EC2",
        "description": "Instancias EC2 en AWS"
    },
}

QUICK_NAV_TEMPLATE = '''
        <!-- Quick Navigation Bar -->
        <div class="quick-nav" style="background: white; padding: 1rem; margin-bottom: 2rem; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem;">
            <div style="display: flex; align-items: center; gap: 1rem;">
                <a href="../clases-html/index.html" style="color: var(--primary); text-decoration: none; font-weight: 500;">Inicio</a>
                <span style="color: var(--text-muted);">|</span>
                <span style="color: var(--text-main); font-weight: 600;">{lab_name}</span>
            </div>
            <div style="display: flex; align-items: center; gap: 0.5rem;">
                <a href="../clases-html/cronograma.html" style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.5rem 1rem; background: #10b981; color: white; text-decoration: none; border-radius: 6px; font-weight: 500;">Cronograma</a>
                <a href="../clases-html/rubricas.html" style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.5rem 1rem; background: #3b82f6; color: white; text-decoration: none; border-radius: 6px; font-weight: 500;">Rubricas</a>
            </div>
        </div>
'''

FOOTER_TEMPLATE = '''
    <footer>
        <div class="container">
            <p><strong>IF0099 - Sistemas Operativos I</strong> - {lab_name}</p>
            <p>{description}</p>
            <p style="margin-top: 10px;">
                <a href="../clases-html/index.html" style="color: #10b981;">Inicio</a> |
                <a href="../clases-html/cronograma.html" style="color: #10b981;">Cronograma</a> |
                <a href="../clases-html/rubricas.html" style="color: #3b82f6;">Rubricas</a>
            </p>
        </div>
    </footer>
'''

def update_lab_file(filepath):
    """Actualiza un laboratorio HTML con navegacion."""
    filename = os.path.basename(filepath).replace('.html', '')

    if filename not in LAB_INFO:
        print(f"  [SKIP] {filepath} - no hay informacion definida")
        return False

    lab_info = LAB_INFO[filename]
    lab_name = lab_info["name"]
    description = lab_info["description"]

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Verificar si ya tiene links a cronograma en el body
    if 'cronograma.html' in content and 'quick-nav' in content:
        print(f"  [SKIP] {filepath} - ya tiene navegacion")
        return False

    # 1. Agregar quick nav despues de </header> y antes de <section> o <main>
    quick_nav = QUICK_NAV_TEMPLATE.format(lab_name=lab_name)

    # Buscar el patron: </header> seguido de espacios y <section> o <main>
    insert_pattern = r'(</header>\s*\n\s*)(<(?:section|main|div class="container))'
    if re.search(insert_pattern, content):
        content = re.sub(insert_pattern, r'\1' + quick_nav + r'\n        \2', content)
    else:
        # Intentar insertar despues del header
        content = content.replace('</header>', '</header>\n' + quick_nav)

    # 2. Actualizar footer
    footer_pattern = r'<footer>.*?</footer>'
    new_footer = FOOTER_TEMPLATE.format(lab_name=lab_name, description=description)
    content = re.sub(footer_pattern, new_footer, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  [OK] {filepath} actualizado")
    return True

def main():
    labs_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    labs_dir = os.path.join(labs_dir, 'laboratorios-html')

    print(f"Actualizando laboratorios en: {labs_dir}")

    updated = 0
    for filename in LAB_INFO.keys():
        filepath = os.path.join(labs_dir, f"{filename}.html")
        if os.path.exists(filepath):
            if update_lab_file(filepath):
                updated += 1

    print(f"\nTotal laboratorios actualizados: {updated}")

if __name__ == "__main__":
    main()
