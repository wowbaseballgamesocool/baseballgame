#update check
import urllib, requests, os, zipfile
folderpath = os.getcwd()

try: 
    response = requests.get("https://api.github.com/repos/wowbaseballgamesocool/baseballgame/releases/latest")
    latestversion = response.json()["tag_name"].strip("v")
except Exception as e:
    if "Max retries exceeded with url" in str(e):
        print("Could not check for updated version (check internet connection)  [Max retries exceeded]")
    else: print("Could not check for updated version\nError: " + str(e))
    latestversion = version
    internet = False

if str(version) != str(latestversion):
    print("New update, restart game after download finishes   " + str(version) + " -> " + str(latestversion))
    print("downloading...")
    url = "https://github.com/wowbaseballgamesocool/baseballgame/releases/download/" + str(latestversion) + "//Baseball.Game.zip"
    try:
        urllib.request.urlretrieve(url, filename = folderpath + r"//Baseball.Game.zip")
    except: ConnectionAbortedError: print("Dont change your internet while file is downloading")
    import zipfile
    with zipfile.ZipFile(folderpath + "\\Baseball.Game.zip", 'r') as zip_ref:
        os.rename(folderpath + "\\Baseball_game.exe", folderpath + "\\gamefiles\\Old_Baseball_game.exe")
        
        zip_ref.extractall(folderpath + "\\gamefiles\\updateunpack")
        zip_ref.close()
    os.remove(folderpath + "\\Baseball.Game.zip")
    
    
    os.rename(folderpath + "\\gamefiles\\updateunpack\\Baseball_game.exe", folderpath + "\\Baseball_game.exe")
    os.remove(folderpath + "\\gamefiles\\audio\\batsound.mp3")
    os.removedirs(folderpath + "\\gamefiles\\audio")
    os.rename(folderpath + "\\gamefiles\\updateunpack\\gamefiles\\audio", folderpath + "\\gamefiles\\audio")
   
    shutil.rmtree(folderpath + "\\gamefiles\\assets")
    shutil.move(folderpath + "\\gamefiles\\updateunpack\\gamefiles\\assets", folderpath + "\\gamefiles\\assets")
    
    
    #os.remove(folderpath + "\\gamefiles\\Old_Baseball_game.exe")
    
    exit()
else: 
    if internet == True:
        print("playing on latest version (" + str(version) + ")")
