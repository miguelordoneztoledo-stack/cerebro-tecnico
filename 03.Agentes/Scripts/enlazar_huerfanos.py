import os
import glob

DIR_MD = r"C:\IA_Proyectos\Cerebro_Tecnico\03.Agentes\Obsidian_Brain\Videotutoriales_MD"
ENLACE = "\n\n---\n**Índice Principal:** [[MOC_Videotutoriales_Ingenieria]]\n"

def conectar_huerfanos():
    if not os.path.exists(DIR_MD):
        print(f"Directorio no encontrado: {DIR_MD}")
        return
        
    archivos_md = glob.glob(os.path.join(DIR_MD, "*.md"))
    conectados = 0
    
    for md_path in archivos_md:
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        if "[[MOC_Videotutoriales_Ingenieria]]" not in content:
            with open(md_path, "a", encoding="utf-8") as f:
                f.write(ENLACE)
            conectados += 1
            
    print(f"Archivos huérfanos reconectados al grafo: {conectados}")

if __name__ == "__main__":
    conectar_huerfanos()
