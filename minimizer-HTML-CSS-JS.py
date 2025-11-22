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

def process_directory(source_dir, output_dir, metrics):
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
                    original_size = os.path.getsize(filepath)
                    
                    minified = content
                    if ext == '.css':
                        minified = css_minify(content)
                    elif ext == '.js':
                        minified = js_minify(content)
                    elif ext == '.html':
                        minified = min_html_content(content)
                    
                    minified_content_size = len(minified.encode('utf-8'))
                    
                    metrics['original'] += original_size
                    metrics['minified'] += minified_content_size
                    
                    with open(target_filepath, 'w', encoding='utf-8') as f:
                        f.write(minified)
                    print(f"[MINIFIED] {file}")
                
                else:
                    shutil.copy2(filepath, target_filepath)
                    
                    size = os.path.getsize(filepath)
                    metrics['original'] += size
                    metrics['minified'] += size
                    
                    print(f"[COPIED] {file}")

            except Exception as e:
                print(f"[ERROR] Failed to process {file}: {e}")

def create_zip(source_dir, output_filename):
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(source_dir):
            for file in files:
                filepath = os.path.join(root, file)
                arcname = os.path.relpath(filepath, source_dir)
                zf.write(filepath, arcname)

if __name__ == "__main__":
    
    target_dir = input("Enter the absolute path of the folder to minify (e.g., C:\\Users\\...\\MySite) : ")
    
    if not os.path.isdir(target_dir):
        print(f"Error: The path '{target_dir}' is not a valid directory.")
        sys.exit(1)

    validation = input(f"Do you want to minify and zip the content of '{target_dir}'? (yes/no) : ")
    
    if validation.lower() != "yes":
        print("Operation canceled.")
        sys.exit(0)

    start_time = time.time()
    
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    temp_dir_name = f"MINIFIED_TEMP_{timestamp}"
    output_zip_name = f"site_minified_{timestamp}.zip"
    metrics = {'original': 0, 'minified': 0}
    
    try:
        os.makedirs(temp_dir_name, exist_ok=False)
        print(f"\n--- STARTING MINIFICATION ---")
        process_directory(target_dir, temp_dir_name, metrics)
        
        print(f"\n--- CREATING ZIP FILE ---")
        create_zip(temp_dir_name, output_zip_name)
        
    except Exception as e:
        print(f"\n[FATAL ERROR] {e}")
        sys.exit(1)
        
    finally:
        end_time = time.time()
        elapsed_time = round((end_time - start_time), 2)
        
        if os.path.exists(temp_dir_name):
            shutil.rmtree(temp_dir_name)
            print(f"[CLEANUP] Temporary directory deleted.")
        
        original_size = metrics['original']
        minified_size = metrics['minified']
        bytes_saved = original_size - minified_size
        
        if original_size > 0:
            percentage_saved = round((bytes_saved / original_size) * 100, 2)
        else:
            percentage_saved = 0.0

        def convert_bytes(bytes_val):
            if bytes_val >= 1024 * 1024:
                return f"{round(bytes_val / (1024 * 1024), 2)} MB"
            elif bytes_val >= 1024:
                return f"{round(bytes_val / 1024, 2)} KB"
            else:
                return f"{bytes_val} bytes"

        print("\n==============================================")
        print(f"✅ SUCCESS: Minification and zipping complete!")
        print("----------------------------------------------")
        print(f"⏱️ Time taken: {elapsed_time} seconds")
        print(f"📦 Original Size: {convert_bytes(original_size)}")
        print(f"🗜️ Final Minified Size: {convert_bytes(minified_size)}")
        print(f"💾 Total Saved: {convert_bytes(bytes_saved)} ({percentage_saved}%)")
        print("----------------------------------------------")
        print(f"📁 Minified ZIP file location: {os.path.abspath(output_zip_name)}")
        print("==============================================")