import os
import sys
import shutil
import time
import zipfile
import re
from cssmin import cssmin as css_minify
from jsmin import jsmin as js_minify

def min_html_content(content):
    content = re.sub(r'', '', content)
    content = re.sub(r'>\s+<', '><', content)
    content = re.sub(r'\s{2,}', ' ', content)
    return content.strip()

def process_directory(source_dir, output_dir):
    for root, dirs, files in os.walk(source_dir):
        relative_path = os.path.relpath(root, source_dir)
        target_root = os.path.join(output_dir, relative_path)
        os.makedirs(target_root, exist_ok=True)
        
        for file in files:
            filepath = os.path.join(root, file)
            ext = os.path.splitext(file)[1].lower()
            target_filepath = os.path.join(target_root, file)
            
            try:
                if ext in ['.css', '.js', '.html']:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    minified = content
                    if ext == '.css':
                        minified = css_minify(content)
                    elif ext == '.js':
                        minified = js_minify(content)
                    elif ext == '.html':
                        minified = min_html_content(content)
                    
                    with open(target_filepath, 'w', encoding='utf-8') as f:
                        f.write(minified)
                    print(f"[MINIFIÉ] {file}")
                
                else:
                    shutil.copy2(filepath, target_filepath)
                    print(f"[COPIÉ] {file}")

            except Exception as e:
                print(f"[ERREUR] Échec du traitement de {file}: {e}")

def create_zip(source_dir, output_filename):
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(source_dir):
            for file in files:
                filepath = os.path.join(root, file)
                arcname = os.path.relpath(filepath, source_dir)
                zf.write(filepath, arcname)

if __name__ == "__main__":
    target_dir = input("Entrez le chemin d'accès absolu du dossier à minifier (Ex: C:\\Users\\...\\MonSite) : ")
    
    if not os.path.isdir(target_dir):
        print(f"Erreur: Le chemin '{target_dir}' n'est pas un répertoire valide.")
        sys.exit(1)

    validation = input(f"Voulez-vous minifier et zipper le contenu de '{target_dir}' ? (oui/non) : ")
    
    if validation.lower() != "oui":
        print("Opération annulée.")
        sys.exit(0)

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    temp_dir_name = f"MINIFIED_TEMP_{timestamp}"
    output_zip_name = f"site_minifie_{timestamp}.zip"
    
    try:
        os.makedirs(temp_dir_name, exist_ok=False)
        print(f"\n--- DÉBUT DE LA MINIFICATION ---")
        process_directory(target_dir, temp_dir_name)
        
        print(f"\n--- CRÉATION DU ZIP ---")
        create_zip(temp_dir_name, output_zip_name)
        print(f"[SUCCÈS] Fichier ZIP créé : {output_zip_name}")
        
    except Exception as e:
        print(f"\n[ERREUR FATALE] {e}")
        
    finally:
        if os.path.exists(temp_dir_name):
            shutil.rmtree(temp_dir_name)
            print(f"[NETTOYAGE] Répertoire temporaire supprimé.")