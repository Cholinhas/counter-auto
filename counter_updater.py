import os
import subprocess
from datetime import datetime

REPO_PATH = r"C:\counter-auto"
FILE_NAME = "counter.txt"

def run_command(cmd):
    print(f"▶ Ejecutando: {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=REPO_PATH, capture_output=True, text=True)
    print(f"  Código de salida: {result.returncode}")
    if result.stdout:
        print(f"  STDOUT: {result.stdout.strip()}")
    if result.stderr:
        print(f"  STDERR: {result.stderr.strip()}")
    return result

def main():
    os.chdir(REPO_PATH)
    
    # 1. Leer contador
    try:
        with open(FILE_NAME, "r") as f:
            count = int(f.read().strip())
    except FileNotFoundError:
        count = 0
    
    # 2. Incrementar
    count += 1
    print(f"📊 Nuevo contador: {count}")
    
    # 3. Guardar
    with open(FILE_NAME, "w") as f:
        f.write(str(count))
    
    # 4. Git add
    run_command("git add .")
    
    # 5. Git commit
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    run_command(f'git commit -m "Auto-update #{count} - {timestamp}"')
    
    # 6. Git push (con verbose)
    run_command("git push -u origin main")
    
    print(f"✅ Actualizado a {count}")

if __name__ == "__main__":
    main()