# dependencies: Pip

import subprocess, os, shutil
folderpath = os.getcwd()
def run_command(command):
    process = subprocess.Popen(command, shell=True)
    process.wait()
while True:
    run_command('pyminify main.py --output Baseball_game.py')
    run_command('pyinstaller Baseball_game.py --onefile --noconfirm')
    try: 
        os.rename(folderpath + '//dist//Baseball_game.exe', folderpath + '//Baseball_game.exe')
        break
    except FileNotFoundError:
        if os.path.isfile('Baseball_game.py') == False:
            run_command("pip install python-minifier")
        elif os.path.isfile("dist//main.exe") == False:
            run_command("pip install pyinstaller")
    except FileExistsError:
        os.remove(folderpath + '//Baseball_game.exe')
        continue



shutil.rmtree(folderpath + '//dist')
shutil.rmtree(folderpath + '//build')
os.remove(folderpath + '//Baseball_game.spec')
os.remove(folderpath + '//main.spec')
os.remove(folderpath + '//Baseball_game.py')
print("done")





