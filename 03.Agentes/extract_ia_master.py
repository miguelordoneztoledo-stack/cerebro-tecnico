import os
import glob
from pathlib import Path

# Requiere: pip install pymupdf4llm
try:
    import pymupdf4llm
except ImportError:
    print("Por favor instala pymupdf4llm: pip install pymupdf4llm")
    exit(1)

SOURCE_DIR = r"F:\IA"
TARGET_DIR = r"C:\IA_Proyectos\Cerebro_Tecnico\03.Agentes\Obsidian_Brain\IA_Master_MD"

def main():
    print(f"🔍 Escaneando {SOURCE_DIR} en busca de PDFs principales...")
    
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)
        print(f"📁 Creada carpeta de destino: {TARGET_DIR}")

    # Buscar todos los PDFs en F:\IA
    pdf_files = glob.glob(os.path.join(SOURCE_DIR, "**", "*.pdf"), recursive=True)
    
    # Filtrar solo los documentos principales (MIA_A...) o índices
    target_pdfs = [f for f in pdf_files if "MIA_" in os.path.basename(f) or "Índice" in os.path.basename(f)]
    
    print(f"📄 Se encontraron {len(target_pdfs)} PDFs principales para extracción.")
    
    for pdf_path in target_pdfs:
        filename = os.path.basename(pdf_path)
        md_filename = filename.replace(".pdf", ".md")
        target_path = os.path.join(TARGET_DIR, md_filename)
        
        if os.path.exists(target_path):
            print(f"⏭️ Omitiendo {filename} (ya existe)")
            continue
            
        print(f"⚙️ Extrayendo texto de: {filename}...")
        try:
            # Extraer a Markdown usando PyMuPDF4LLM (optimizado para LLMs)
            md_text = pymupdf4llm.to_markdown(pdf_path)
            
            with open(target_path, "w", encoding="utf-8") as f:
                f.write(f"---\ntags:\n  - master_ia\n  - teoria\nsource: {filename}\n---\n\n")
                f.write(md_text)
            print(f"✅ Guardado: {md_filename}")
        except Exception as e:
            print(f"❌ Error procesando {filename}: {str(e)}")
            
    print("\n🚀 Proceso completado. Revisa tu bóveda de Obsidian en MOC_Arquitectura_IA.")

if __name__ == "__main__":
    main()
