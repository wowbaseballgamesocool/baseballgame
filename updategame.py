#update check
import urllib, requests, os, zipfile
folderpath = os.getcwd()
try: 
    response = requests.get("https://api.github.com/repos/wowbaseballgamesocool/baseballgame/releases/latest")
    latestversion = response.json()["tag_name"].strip("v")
except: 
    print("Could not check for updated version (check internet connection)")
    latestversion = version
    internet = False

if str(version) != str(latestversion):
    print("New update, restart game after download finishes")
    url = "https://github.com/wowbaseballgamesocool/baseballgame/releases/download/" + str(latestversion) + "//Baseball.Game.zip"
    urllib.request.urlretrieve(url, filename = folderpath + r"//Baseball.Game.zip")
    with zipfile.ZipFile(folderpath + "\\Baseball.Game.zip", 'r') as zip_ref:
        os.rename(folderpath + "\\Baseball_game.exe", folderpath + "\\gamefiles\\Old_Baseball_game.exe")
        zip_ref.extractall(folderpath)
        zip_ref.close()
    os.remove(folderpath + "\\Baseball.Game.zip")
    exit()
else: 
    if internet == True:
        print("playing on latest version (" + str(version) + ")")
