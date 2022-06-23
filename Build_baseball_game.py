import subprocess, os, shutil, time
folderpath = os.getcwd(); start = time.time()
print("Building BaseballGame...")
def run_command(command):
    process = subprocess.Popen(command, shell=True)
    process.wait()
while True:
    run_command('pyminify main.py --output Baseball_game.py')
    run_command('pyinstaller Baseball_game.py --onefile --noconfirm --log-level ERROR')
    try: 
        os.rename(folderpath + '//dist//Baseball_game.exe', folderpath + '//Baseball_game.exe')
        break
    except FileNotFoundError:
        if os.path.isfile('Baseball_game.py') == False: run_command("pip install python-minifier")
        elif os.path.isfile("dist//main.exe") == False: run_command("pip install pyinstaller")
    except FileExistsError:
        os.remove(folderpath + '//Baseball_game.exe')
        continue
for file in ['//Baseball_game.py', '//dist', '//build', '//Baseball_game.spec']:
    try:
        if os.path.isfile(folderpath + file): os.remove(folderpath + file)
        else: shutil.rmtree(folderpath + file)
    except FileNotFoundError: pass
print("done (" + str(round(time.time()-start, 0)).replace(".0", "") + "s)")