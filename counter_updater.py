import os 
import subprocess 
from datetime import datetime 
 
REPO_PATH = r"C:\counter-auto" 
FILE_NAME = "counter.txt" 
 
def run_command(cmd): 
    result = subprocess.run(cmd, shell=True, cwd=REPO_PATH, capture_output=True, text=True) 
    if result.returncode != 0: 
        print(f"Error en: {cmd}") 
        print(result.stderr) 
    return result 
 
def main(): 
    os.chdir(REPO_PATH) 
    try: 
        with open(FILE_NAME, "r") as f: 
            count = int(f.read().strip()) 
    except FileNotFoundError: 
        count = 0 
    count += 1 
    with open(FILE_NAME, "w") as f: 
        f.write(str(count)) 
    run_command("git add .") 
    timestamp = datetime.now().strftime("%%Y-%%m-%%d %%H:%%M:%%S") 
    run_command(f'git commit -m "Auto-update #{count} - {timestamp}"') 
    run_command("git push") 
    print(f"? Actualizado a {count}") 
 
if __name__ == "__main__": 
    main() 
