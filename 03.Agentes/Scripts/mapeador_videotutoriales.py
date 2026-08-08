import os
import urllib.parse
from collections import defaultdict

# Configuración de Rutas
SOURCE_DIR = r"F:\VIDEOTUTORIALES"
OUTPUT_FILE = r"C:\IA_Proyectos\Cerebro_Tecnico\03.Agentes\Obsidian_Brain\MOC_Videotutoriales_Ingenieria.md"

# Categorías de extensiones
CATEGORIES = {
    "🎥 Videos y Cursos": ['.mp4', '.ts', '.mkv', '.avi'],
    "📊 Plantillas y Dashboards (Excel)": ['.xlsx', '.xlsm', '.xls', '.csv'],
    "📝 Documentos de Trabajo (Word)": ['.docx', '.doc'],
    "📚 Documentación Teórica (PDFs)": ['.pdf'],
    "📐 Modelos y CAD": ['.dwg', '.shp', '.shx', '.dbf', '.prj', '.mxd'],
}

def get_category(ext):
    ext = ext.lower()
    for cat, exts in CATEGORIES.items():
        if ext in exts:
            return cat
    return "📦 Otros Archivos"

def generate_moc():
    print(f"Iniciando escaneo de {SOURCE_DIR}...")
    
    # Asegurar que el directorio de destino exista
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    
    # Estructura: { Categoria: { Subcarpeta: [ (nombre, ruta_absoluta) ] } }
    catalog = defaultdict(lambda: defaultdict(list))
    
    total_files = 0
    
    for root, _, files in os.walk(SOURCE_DIR):
        rel_path = os.path.relpath(root, SOURCE_DIR)
        folder_name = "Raíz" if rel_path == "." else rel_path
        
        for file in files:
            total_files += 1
            ext = os.path.splitext(file)[1]
            cat = get_category(ext)
            abs_path = os.path.join(root, file)
            catalog[cat][folder_name].append((file, abs_path))
            
    print(f"Archivos escaneados: {total_files}")
    
    # Escribir el Markdown
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write("tags:\n")
        f.write("  - moc\n")
        f.write("  - ingenieria\n")
        f.write("  - videotutoriales\n")
        f.write("---\n")
        f.write("# 🏗️ MOC Videotutoriales y Herramientas de Ingeniería\n\n")
        f.write("Este índice agrupa y categoriza automáticamente todo el conocimiento técnico y plantillas ubicados en `F:\\VIDEOTUTORIALES`. Se han generado enlaces directos a los archivos originales para no duplicar almacenamiento.\n\n")
        
        # Orden de categorías predefinido para mantener estructura lógica
        ordered_cats = list(CATEGORIES.keys()) + ["📦 Otros Archivos"]
        
        for cat in ordered_cats:
            if cat not in catalog or not catalog[cat]:
                continue
                
            f.write(f"## {cat}\n\n")
            
            for folder, files in sorted(catalog[cat].items()):
                f.write(f"### 📁 {folder}\n")
                for file_name, file_path in sorted(files):
                    path_for_uri = file_path.replace("\\", "/")
                    encoded_path = urllib.parse.quote(path_for_uri)
                    file_uri = f"file:///{encoded_path}"
                    
                    f.write(f"- [{file_name}]({file_uri})\n")
                f.write("\n")
                
    print(f"MOC generado exitosamente en: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_moc()
