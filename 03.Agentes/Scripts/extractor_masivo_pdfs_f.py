import os
import pymupdf4llm

# Configuraciones
SOURCE_DIR = r"F:\VIDEOTUTORIALES"
DEST_DIR = r"C:\IA_Proyectos\Cerebro_Tecnico\03.Agentes\Obsidian_Brain\Videotutoriales_MD"

def sanitize_filename(filename):
    """Limpia nombres de archivo para evitar errores en Windows u Obsidian."""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, "_")
    return filename

def extract_pdfs():
    os.makedirs(DEST_DIR, exist_ok=True)
    
    # Recolectar todos los PDFs
    pdf_files = []
    for root, _, files in os.walk(SOURCE_DIR):
        for f in files:
            if f.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(root, f))
                
    total_pdfs = len(pdf_files)
    print(f"[{total_pdfs}] PDFs encontrados. Iniciando extracción segura...")
    
    procesados = 0
    errores = 0
    omitidos = 0

    for idx, pdf_path in enumerate(pdf_files, 1):
        filename = os.path.basename(pdf_path)
        safe_name = sanitize_filename(filename)
        md_filename = safe_name.replace(".pdf", ".md").replace(".PDF", ".md")
        md_path = os.path.join(DEST_DIR, md_filename)
        
        # Saltar si ya fue procesado (Idempotencia)
        if os.path.exists(md_path):
            omitidos += 1
            continue
            
        print(f"[{idx}/{total_pdfs}] Extrayendo: {filename[:40]}...")
        
        try:
            # Extracción a Markdown puro
            md_text = pymupdf4llm.to_markdown(pdf_path)
            
            # Guardar con metadatos de Obsidian
            with open(md_path, "w", encoding="utf-8") as f:
                f.write("---\n")
                f.write("tags:\n")
                f.write("  - pdf_extraido\n")
                f.write("  - videotutoriales_f\n")
                f.write(f"original_path: \"{pdf_path}\"\n")
                f.write("---\n\n")
                f.write(md_text)
                
            procesados += 1
        except Exception as e:
            print(f" ❌ Error en {filename}: {str(e)}")
            errores += 1

    print("\n--- RESUMEN DE EXTRACCIÓN ---")
    print(f"Procesados exitosamente: {procesados}")
    print(f"Omitidos (ya existían): {omitidos}")
    print(f"Errores (encriptados/dañados): {errores}")

if __name__ == "__main__":
    extract_pdfs()
