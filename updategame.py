#update check
import urllib, requests, os, zipfile
folderpath = os.getcwd()

try: os.remove(folderpath + "\\Baseball.Game.zip")
except: pass
try: os.remove(folderpath + "\\gamefiles\\Old_Baseball_game.exe")
except: pass

try: 
	response = requests.get("https://api.github.com/repos/wowbaseballgamesocool/baseballgame/releases")
	latestversion = response.json()[0]["tag_name"].strip("v")
except Exception as e:
	if "Max retries exceeded with url" in str(e):
		print("Could not check for updated version (check internet connection)  [Max retries exceeded]")
	elif str(e) == "'tag_name'" or str(e) == "0":
		print("Could not check for updated version\nError: API rate limit exceeded (Try again later)")
		ratelimit = True


		
	else: 
		print("Could not check for updated version\nError: " + str(e))
	
	internet = False
if internet == True:
	if str(version) != str(latestversion):
		print("\nNew update   " + str(version) + " -> " + str(latestversion))
		
		
		print("downloading update...")
		
		url = "https://github.com/wowbaseballgamesocool/baseballgame/releases/download/" + str(latestversion) + "//Baseball.Game.zip"
		try:
			urllib.request.urlretrieve(url, filename = folderpath + r"//Baseball.Game.zip")
		except: ConnectionAbortedError: print("Dont change your internet while file is downloading")
		with zipfile.ZipFile(folderpath + "\\Baseball.Game.zip", 'r') as zip_ref:
			os.rename(folderpath + "\\Baseball_game.exe", folderpath + "\\gamefiles\\Old_Baseball_game.exe")
			
			zip_ref.extractall(folderpath + "\\gamefiles\\updateunpack")
			zip_ref.close()
		os.remove(folderpath + "\\Baseball.Game.zip")
		
		
		os.rename(folderpath + "\\gamefiles\\updateunpack\\Baseball_game.exe", folderpath + "\\Baseball_game.exe")
		if os.path.exists(folderpath + "\\gamefiles\\save.txt") == False:
			os.rename(folderpath + "\\gamefiles\\updateunpack\\gamefiles\\save.txt", folderpath + "\\gamefiles\\save.txt")
		if os.path.exists(folderpath + "\\gamefiles\\customballs.txt") == False:
			os.rename(folderpath + "\\gamefiles\\updateunpack\\gamefiles\\customballs.txt", folderpath + "\\gamefiles\\customballs.txt")
		if os.path.exists(folderpath + "\\gamefiles\\custombats.txt") == False:
			os.rename(folderpath + "\\gamefiles\\updateunpack\\gamefiles\\custombats.txt", folderpath + "\\gamefiles\\custombats.txt")
		if os.path.exists(folderpath + "\\gamefiles\\customfields.txt") == False:
			os.rename(folderpath + "\\gamefiles\\updateunpack\\gamefiles\\customfields.txt", folderpath + "\\gamefiles\\customfields.txt")

		
		shutil.rmtree(folderpath + "\\gamefiles\\audio")
		
		shutil.move(folderpath + "\\gamefiles\\updateunpack\\gamefiles\\audio", folderpath + "\\gamefiles")
		
                                
		shutil.rmtree(folderpath + "\\gamefiles\\assets")
		
		shutil.move(folderpath + "\\gamefiles\\updateunpack\\gamefiles\\assets", folderpath + "\\gamefiles")
		
		
		
		os.startfile(folderpath + "\\Baseball_game.exe")
		exit()
	else: 
		
		print("playing on latest version (" + str(version) + ")")
