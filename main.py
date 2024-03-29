import pygame, random, os, json, requests, urllib, shutil, ast, math, base64, datetime
# TODO:
# Create 4 new sprites for item shop
# fix release notes
# fix home run not showing in play (fixed)
# add new hit display to derby (done)
# add buck collection after games (done)

folderpath = os.getcwd()
version = "1.3"
# make sure version is the same as github tag
ITEM_SHOP_ENABLED = False
# locks shop button and buck collection (except from bp cause it might ruin saves)

forplayingscoring = 13
derbyhomerunsscoring = 3.5
homerunsscoring = 2.8
singlesscoring = 1.8
doublesscoring = 2.7
derbyhomerunsbucks = 5.2
homerunsbucks = 8.8


def weeks():
	year, week, day = datetime.date.today().isocalendar(); week += 4
	for i in range(year - 2022): week += 52
	for i in range(day - 6): week += 1
	for i in range(year - 2022): week += math.floor((365 / 7 - 52) * (round(year - 2020, 0) / 4))
	return str(week).replace(".0", "")




def give(asset, list, level, unlocktier):
	if level >= unlocktier: 
		if asset not in list: list.append(asset)

def givebucks(list, level, unlocktier, bucks, togive):
	if level >= unlocktier:
		if unlocktier not in list:
			list.append(unlocktier)
			bucks += togive
	return bucks
			
def buy(asset, bucks, cost, list):
	if bucks >= cost:
		if asset not in list: 
			list.append(asset)
			return bucks-cost, list
	return bucks, list
	



def opensave():
	with open(folderpath + "\\gamefiles\\save.txt", "r") as save:
		data = save.read()
		save.close()
	if data == [0, 0, 0] or data == "[0, 0, 0]":
		data = [0, 0, 0, 0, 0, "['ball']", "['bat']", "['field']", "[0]"]
	elif data != "" and data != None and data != "b'WzAsIDAsIDAsIDBd'":
		data = data.strip("b''")
		while len(data)%4 != 0: data += "="
		data = base64.b64decode(data)
		data = str(data, "utf-8")
		data = ast.literal_eval(data)
	else: data = [0, 0, 0, 0, 0, "['ball']", "['bat']", "['field']", "[0]"]
	return data



def save(list):
	with open(folderpath + "\\gamefiles\\save.txt", "w") as save:
		data = str([ball, bat, field, xp, bucks, balllist, batlist, fieldlist, buckslist])
		data = base64.b64encode(data.encode("utf-8"))
		data = str(data, "utf-8")
		save.write(data)
		save.close()
	return



ratelimit = False
ball, bat, field, xp, bucks, balllist, batlist, fieldlist, buckslist = opensave()

balllist = ast.literal_eval(str(balllist))
batlist = ast.literal_eval(str(batlist))
fieldlist = ast.literal_eval(str(fieldlist))
buckslist = ast.literal_eval(str(buckslist))

if random.randint(0, 1) == 1: ABK = "+" + str(round(random.uniform(1.06, 4.24), 2)) + "%"
else: ABK = "-" + str(round(random.uniform(2.34, 0.16), 2)) + "%"



splashmessage = random.choice([
								#"Battle Pass soon!",
								"Now on PS4!",
								#"Better than real baseball!",
								weeks() + " weeks!",
								"sponsored by Bayloadgs!",
								"Why are you playing this?",
								"ABK Stock " + ABK,
								#""
								#""
							])



internet = True
print("cwd = " + folderpath + "  W = " + weeks())


try: os.remove(folderpath + "\\Baseball.Game.zip")
except: pass
try: os.remove(folderpath + "\\gamefiles\\Old_Baseball_game.exe")
except: pass
try: os.remove(folderpath + "\\gamefiles\\customballs.txt")
except: pass
try: os.remove(folderpath + "\\gamefiles\\custombats.txt")
except: pass
try: os.remove(folderpath + "\\gamefiles\\customfields.txt")
except: pass

# check updates

try: 
	response = requests.get("https://api.github.com/repos/wowbaseballgamesocool/baseballgame/releases")
	latestversion = response.json()[0]["tag_name"].strip("v")
	if latestversion == "1.2.1": raise Exception("Github returned wrong version")
	with open(folderpath + "/gamefiles/cache.txt", "w") as file:
		file.write(str(response.json())); file.close()
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
		from time import sleep
		print("\nNew update   " + str(version) + " -> " + str(latestversion))
		sleep(1.5)
		print("downloading update...")
		
		url = "https://github.com/wowbaseballgamesocool/baseballgame/releases/download/" + str(latestversion) + "//Baseball.Game.zip"
		try:
			urllib.request.urlretrieve(url, filename = folderpath + r"//Baseball.Game.zip")
		except ConnectionAbortedError: raise Exception("Don't change your internet while file is downloading")
		from zipfile import ZipFile
		with ZipFile(folderpath + "\\Baseball.Game.zip", 'r') as zip_ref:
			os.rename(folderpath + "\\Baseball_game.exe", folderpath + "\\gamefiles\\Old_Baseball_game.exe")
			
			zip_ref.extractall(folderpath + "\\gamefiles\\updateunpack")
			zip_ref.close()
		os.remove(folderpath + "\\Baseball.Game.zip")
		
		
		os.rename(folderpath + "\\gamefiles\\updateunpack\\Baseball_game.exe", folderpath + "\\Baseball_game.exe")
		if os.path.exists(folderpath + "\\gamefiles\\save.txt") == False:
			os.rename(folderpath + "\\gamefiles\\updateunpack\\gamefiles\\save.txt", folderpath + "\\gamefiles\\save.txt")


		#shutil.move(folderpath + "\\gamefiles\\updateunpack\\gamefiles\\audio", folderpath + "\\gamefiles\\audio")
		#os.rename(folderpath + "\\gamefiles\\updateunpack\\gamefiles\\assets", folderpath + "\\gamefiles\\assets")
		shutil.rmtree(folderpath + "\\gamefiles\\audio")
		
		shutil.move(folderpath + "\\gamefiles\\updateunpack\\gamefiles\\audio", folderpath + "\\gamefiles")

		shutil.rmtree(folderpath + "\\gamefiles\\assets")

		shutil.move(folderpath + "\\gamefiles\\updateunpack\\gamefiles\\assets", folderpath + "\\gamefiles")
		
		
		#os.remove(folderpath + "\\gamefiles\\Old_Baseball_game.exe")
		os.startfile(folderpath + "\\Baseball_game.exe")
		exit()
	else: 
		
		print("playing on latest version (" + str(version) + ")")



if os.path.exists(folderpath + "\\gamefiles\\cache.txt") == False:
	os.mkfile(folderpath + "\\gamefiles\\cache.txt")
else:
	with open(folderpath + "\\gamefiles\\cache.txt", "r") as cachefile:
		response = str(cachefile.read())
		cachefile.close()
with open(folderpath + "\\gamefiles\\hplay.json", "r") as hjson:
	file = hjson.read()
	hjson.close()
jsonfile = json.loads(file)
highhomeruns = int(jsonfile["play"]["homeruns"])
highsingles = int(jsonfile["play"]["singles"])
highdoubles = int(jsonfile["play"]["doubles"])
highruns = int(jsonfile["play"]["runs"])

with open(folderpath + "\\gamefiles\\hderby.json", "r") as hjson:
	file = hjson.read()
	hjson.close()
jsonfile = json.loads(file)
highderbyhomeruns = int(jsonfile["derby"]["homeruns"])

with open(folderpath + "\\gamefiles\\settings.json", "r") as settings:
	file = settings.read()
	settings.close()
jsonfile = json.loads(file)
volume = int(jsonfile["settings"]["volume"])


data = opensave()


balllistnumber = data[0]
batlistnumber = data[1]
fieldlistnumber = data[2]
xp = data[3]



try:
	balllist[balllistnumber]
	batlist[batlistnumber]
	fieldlist[fieldlistnumber]
except: 
	balllistnumber = 0
	batlistnumber = 0
	fieldlistnumber = 0


grey = (50, 50, 50)
white = (255, 255, 255)
yellow = (215, 215, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
dis_width = 600
dis_height = 400

pygame.init()
screen = pygame.display.set_mode((dis_width, dis_height))
releasenotescroll = 0
#message = ""; startticks = 2; time = 0
fpslist = []
splashsize = 35
splashsizemode, page, shoppage = 1, 1, 1
fps, averagefps = 0, 0
altaltsplashmessage = ""
pygame.display.set_caption('Baseball Game')
alreadyrendered = False

# def refresh_sprites(): 

ball_sprite = pygame.image.load('gamefiles/assets/balls/' + balllist[balllistnumber] + '.png').convert_alpha()
ball_sprite = pygame.transform.scale(ball_sprite, (40, 40)) #size of ball
menubg_sprite = pygame.image.load('gamefiles/assets/menubg.png').convert_alpha()
out0_sprite = pygame.image.load('gamefiles/assets/outs/0outs.png').convert_alpha()
out0_sprite = pygame.transform.scale(out0_sprite, (95, 30)) #size of text
out1_sprite = pygame.image.load('gamefiles/assets/outs/1outs.png').convert_alpha()
out1_sprite = pygame.transform.scale(out1_sprite, (95, 30)) #size of text
out2_sprite = pygame.image.load('gamefiles/assets/outs/2outs.png').convert_alpha()
out2_sprite = pygame.transform.scale(out2_sprite, (95, 30)) #size of text
out3_sprite = pygame.image.load('gamefiles/assets/outs/3outs.png').convert_alpha()
out3_sprite = pygame.transform.scale(out3_sprite, (95, 30)) #size of text
optionsmenu_sprite = pygame.image.load('gamefiles/assets/optionsmenu.png').convert_alpha()
assetsback_sprite = pygame.image.load('gamefiles/assets/assetsback.png').convert_alpha()
back_sprite = pygame.image.load('gamefiles/assets/back.png').convert_alpha()
releasenotesbg = pygame.image.load('gamefiles/assets/releasenotesbg.png').convert_alpha()
battlepassboxpast = pygame.image.load('gamefiles/assets/battlepassboxpast.png').convert_alpha()
battlepassboxpresent = pygame.image.load('gamefiles/assets/battlepassboxpresent.png').convert_alpha()
battlepassboxfuture = pygame.image.load('gamefiles/assets/battlepassboxfuture.png').convert_alpha()
xpicon = pygame.image.load('gamefiles/assets/xpicon.png').convert_alpha()
bucksicon = pygame.image.load('gamefiles/assets/bucks.png').convert_alpha()
bucksicon100 = pygame.image.load('gamefiles/assets/bucks100.png').convert_alpha()
bucksicon75 = pygame.image.load('gamefiles/assets/bucks75.png').convert_alpha()
right_arrow = pygame.image.load('gamefiles/assets/arrow.png').convert_alpha()
buy1 = pygame.image.load('gamefiles/assets/buy1.png').convert_alpha()
buy2 = pygame.image.load('gamefiles/assets/buy2.png').convert_alpha()
left_arrow = pygame.transform.rotate(right_arrow, 180)
field_sprite = pygame.image.load('gamefiles/assets/fields/' + fieldlist[fieldlistnumber] + '.png').convert_alpha()
field_sprite = pygame.transform.scale(field_sprite, (620, 420)) #size of field
shopbox = pygame.transform.scale(battlepassboxfuture, (220, 180))

font = pygame.font.SysFont(None, 40)
def message_to_screen(msg, color, size, x, y):

	screen_text = font.render(msg, True, color)
	screen.blit(screen_text, [x, y])


med_font = pygame.font.SysFont("Mochiy Pop One", 30)
font_style = pygame.font.SysFont("Mochiy Pop One", 50)
small_font = pygame.font.SysFont("Mochiy Pop One", 20)
big_font = pygame.font.SysFont("Mochiy Pop One", 40)
verybig_font = pygame.font.SysFont("Mochiy Pop One", 70)
#mesg = font_style.render("", True, red)
space2swing = small_font.render("Press space to swing", True, black)
#menuplace = 1
start, openreleasenotes = False, False
clock = pygame.time.Clock()
updateevent = pygame.USEREVENT + 1
secondevent = pygame.USEREVENT + 2
pygame.time.set_timer(secondevent, 1000)
pygame.time.set_timer(updateevent, 750)











while True:
	try:
		level = math.floor(xp / 100) + 1
		give("snowfield", fieldlist, level, 2)
		give("axebat", batlist, level, 4)
		give("sandfield", fieldlist, level, 7)
		give("coolbat", batlist, level, 15)
		give("hammerbat", batlist, level, 19)
		give("christmasball", balllist, level, 10)
		give("starball", balllist, level, 17)
		give("hockeybat", batlist, level, 12)
		give("waterfield", fieldlist, level, 14)
		give("roseball", balllist, level, 6)
		if ITEM_SHOP_ENABLED:
			bucks = givebucks(buckslist, level, 16, bucks, 100)
			bucks = givebucks(buckslist, level, 11, bucks, 100)
			bucks = givebucks(buckslist, level, 9, bucks, 75)
			bucks = givebucks(buckslist, level, 8, bucks, 100)
		save([balllistnumber, batlistnumber, fieldlistnumber, xp, bucks, balllist, batlist, fieldlist, buckslist])
	except: pass
	pygame.mouse.set_visible(True) 
	pygame.display.set_caption('Baseball Game -- Menu')
	mesg = ""
	endtimer,outs = 0, 0
	ball_sprite = pygame.image.load('gamefiles/assets/balls/' + balllist[balllistnumber] + '.png').convert_alpha()
	ball_sprite = pygame.transform.scale(ball_sprite, (40, 40)) #size of ball
	bat_sprite = pygame.image.load('gamefiles/assets/bats/' + batlist[batlistnumber] + '.png').convert_alpha()
	bat_sprite = pygame.transform.scale(bat_sprite, (20, 70)) #size of bat old: 15, 70
	asset = True
	battlepass = True
	optionsmenu = False
	startderby = False
	startplay = False
	hit = False
	firstswing = True
	strikes, runs, runner, singles, doubles, homeruns, hit_type = 0, 0, 0, 0, 0, 0, 0
	start = False
	ballx = 265
	bally = 100
	batx = 260
	baty = 310
	while start == False:
		



		screen.blit(menubg_sprite, (0, 0))
		#splashscreen
		if openreleasenotes == False:
			if "*" in splashmessage: altaltsplashmessage = splashmessage
			if splashsize >= 32: splashsizemode = 0
			if splashsize <= 25: splashsizemode = 1
			if splashsizemode == 0: splashsize -= 0.02
			if splashsizemode == 1: splashsize += 0.02
			splash_font = pygame.font.SysFont("Mochiy Pop One", int(round(splashsize, 0))) # 45
			if "*" in altaltsplashmessage:
				splashmessage, altsplashmessage = altaltsplashmessage.split("*")
				
				altsplash_text = splash_font.render(altsplashmessage, True, yellow)
				altsplash_text = pygame.transform.rotate(altsplash_text, 345)
				screen.blit(altsplash_text, [310, 65])
			
			
			splash_text = splash_font.render(splashmessage, True, yellow)
			
			splash_text = pygame.transform.rotate(splash_text, 345)
			#pygame.transform.scale(bat_sprite, (20, 70))
			screen.blit(splash_text, [320, 45])


		# print(alreadyrendered)
		elif openreleasenotes:
			
			
			
			if internet or response != "":
				
				pushdownupdateinfo = 0
				updatelinecount = 0
				screen.blit(releasenotesbg, [0, 0])
				screen.blit(releasenotesbg, [0, 0])
				# if True:
					
				try:
					response = ast.literal_eval(response)
				except: pass
				
				for i in range(15):
					try:
						updatelinecount = 0
						updatetitlething___ = response[i]["name"] + "  --  " + response[i]["tag_name"]
						if str(response[i]["tag_name"]) == str(version): 

							updatetitlething___ += "     [ Latest ]"

						updateinfotitle = med_font.render(updatetitlething___, True, grey)
						updateinfo = small_font.render(response[i]["body"], True, black)
						if dis_height - 330 + pushdownupdateinfo + releasenotescroll < 335 and dis_height - 330 + pushdownupdateinfo + releasenotescroll > 30:
							screen.blit(updateinfotitle, [dis_width - 520, dis_height - 330 + pushdownupdateinfo + releasenotescroll])
						if "\n" not in str(response[i]["body"]) and dis_height - 300 + pushdownupdateinfo + releasenotescroll < 335 and dis_height - 300 + pushdownupdateinfo + releasenotescroll > 30:
							screen.blit(updateinfo, [dis_width / 2 - 250, dis_height - 300 + pushdownupdateinfo + releasenotescroll])
							pushdownupdateinfo += 30
						else:
							
								a = str(response[i]["body"])
								b = r"\r\n"
								try:
									for b in a:
										c = a.split("\r\n")
										d = c[updatelinecount]
										d = small_font.render(d, True, black)
										if dis_height - 300 + pushdownupdateinfo + releasenotescroll < 335 and dis_height - 300 + pushdownupdateinfo + releasenotescroll > 30:
											screen.blit(d, [dis_width / 2 - 250, dis_height - 290 + pushdownupdateinfo + releasenotescroll])
										pushdownupdateinfo += 20
										updatelinecount += 1
								except: pass
						pushdownupdateinfo += 55
						# alreadyrendered = True
					except: pass
					pygame.display.update()

			
				
			if openreleasenotes:
				
				for event in pygame.event.get():
					if event.type == pygame.QUIT: exit()
					if event.type == pygame.MOUSEBUTTONDOWN:
						
						
						if event.button >= 4:
							alreadyrendered = False
							if ".0" in str(event.button / 2):
								if releasenotescroll <= 50: releasenotescroll += 30
							else:
								if releasenotescroll >= -950: releasenotescroll -= 30
						else: openreleasenotes = False; alreadyrendered = False
					if event.type == pygame.KEYDOWN:
						openreleasenotes = False
						alreadyrendered = False

				pygame.display.update()
					

					
					
		
	
			else:	# might have to move this error text if stats/settings were to go here
				updateinfo = small_font.render("Try again later", True, black)
				screen.blit(updateinfo, [20, dis_height - 110])




		
		playrect = pygame.Rect(210, dis_height - 170, 175, 45)
		derbyrect = pygame.Rect(220, dis_height - 125, 155, 40)
		optionsrect = pygame.Rect(225, dis_height - 85, 145, 40)
		exitrect = pygame.Rect(245, dis_height - 45, 100, 25)
		releaserect = pygame.Rect(30, dis_height - 100, 100, 50)




		# if random.randint(1, 2) == 1:
			# pygame.draw.rect(screen,red,(playrect))
			# pygame.draw.rect(screen,red,(derbyrect))
			# pygame.draw.rect(screen,red,(optionsrect))
			# pygame.draw.rect(screen,red,(exitrect))
			# pygame.draw.rect(screen,red,(releaserect))
		
		for event in pygame.event.get():

			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				
				if exitrect.collidepoint(event.pos): exit()
				if optionsrect.collidepoint(event.pos):
					
					pygame.display.set_caption('Baseball Game -- Options')
					
					start = True
					optionsmenu = True
				if derbyrect.collidepoint(event.pos):
					
					pygame.display.set_caption('Baseball Game -- Derby')
					
					start_ticks = pygame.time.get_ticks()
					start = True
					startderby = True
				if playrect.collidepoint(event.pos):
					
					pygame.display.set_caption('Baseball Game -- Play')
					start_ticks = pygame.time.get_ticks()
					start = True
					startplay = True

				if releaserect.collidepoint(event.pos):
					openreleasenotes = True
					
					
			
			if event.type == pygame.QUIT: exit()
			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_ESCAPE:
					exit()
		pygame.display.update()
	while startplay == True:


		

		pygame.mouse.set_visible(False) #########
		screen.blit(field_sprite, (0, 0))
		
		screen.blit(space2swing, [dis_width / 6 + 260, dis_height / 3 + 250])
		screen.blit(ball_sprite, (ballx, bally))
		screen.blit(bat_sprite, (batx, baty))
		if mesg != "":
			message_to_screen(str(mesg), (0, 0, 0), "sus", 5, 340)




		if outs == 0:
			screen.blit(out0_sprite, (0, 370))
		elif outs == 1:
			screen.blit(out1_sprite, (0, 370))
		elif outs == 2:
			screen.blit(out2_sprite, (0, 370))
		while outs == 3:
			screen.blit(field_sprite, (0, 0))
			screen.blit(out3_sprite, (0, 370))
			endtimer += 1
			if endtimer >= 775: # 4500
				xp += math.floor(int(singles) * singlesscoring)
				xp += math.floor(int(doubles) * doublesscoring)
				xp += math.floor(int(homeruns) * homerunsscoring)
				xp += forplayingscoring
				if ITEM_SHOP_ENABLED: bucks += math.floor(int(homeruns) * homerunsbucks)
				save([balllistnumber, batlistnumber, fieldlistnumber, xp, bucks, balllist, batlist, fieldlist, buckslist])
				outs = 0
				startplay = False
				start = False
			bally, ballx, batx, baty = -10, -10, -10, -10


			for event in pygame.event.get():
				if event.type == updateevent: 
					with open(folderpath + "//gamefiles//hplay.json", "r") as playh:
						jsonfile = playh.read()
						playh.close()
					jsonfile = json.loads(jsonfile)
				
					if int(highruns) < int(runs):
						highruns = runs
						jsonfile["play"]["runs"] = runs
				

					if int(highsingles) < int(singles):
						highsingles = singles
						jsonfile["play"]["singles"] = singles
					if int(highdoubles) < int(doubles):
						highdoubles = doubles
						jsonfile["play"]["doubles"] = doubles
					if int(highhomeruns) < int(homeruns):
						highhomeruns = homeruns
						jsonfile["play"]["homeruns"] = homeruns



					with open(folderpath + "\\gamefiles\\hplay.json", "w") as hplay:
				
						hplay.write(json.dumps(jsonfile))
						hplay.close()



		   
			
		
		#screen.blit(mesg, [dis_width / 2 + 125, dis_height / 2])
		
		
		if hit == False:
			bally += 0.07
		if bally > 750:
			bally = 100
			strikes += 1
			firstswing = True
			if strikes == 3:
				strikes = 0
				outs += 1
			bat_sprite = pygame.image.load('gamefiles/assets/bats/' + batlist[batlistnumber] + '.png').convert_alpha()
			bat_sprite = pygame.transform.scale(bat_sprite, (20, 70)) #size of bat
		if bally <= 0:
			strikes = 0
			if hit_type == 1:
				
				homeruns += 1
				runs += 1
				mesg = "Home Run!"
				if runner != 0:
					runner = 0
					runs += 1
					
				
					
				
				
			if hit_type == 2 or hit_type == 4:
				randhit2 = random.randint(1,5)
				if randhit2 == 1 or randhit2 == 2:
					runner += 2
					doubles += 1
					if runner >= 4:
						runner = 0
						runs += 1
						
					mesg = "Double!"
					#screen.blit(mesg, [dis_width / 6, dis_height / 3])
					
				
				if randhit2 == 3 or randhit2 == 4:
					
					mesg = "Caught!"
					#screen.blit(mesg, [dis_width / 6, dis_height / 3])
					outs += 1
					
				
					
				if randhit2 == 5:
					
					mesg = "Single!"
					#screen.blit(mesg, [dis_width / 6, dis_height / 3])
					runner += 1
					singles += 1
					if runner >= 4:
						runner = 0
						runs += 1
					
					
			if hit_type == 3 or hit_type == 5:
				
				mesg = "Caught!"
				#screen.blit(mesg, [dis_width / 6, dis_height / 3])
				outs += 1
			if hit_type == 7:
				
				strikes += 1
				mesg = "Foul!"
				#screen.blit(mesg, [dis_width / 6, dis_height / 3])
				

			bally = 100
			ballx = 265
			ball_sprite = pygame.image.load('gamefiles/assets/balls/' + balllist[balllistnumber] + '.png').convert_alpha() # refresh ball cause it messed up
			ball_sprite = pygame.transform.scale(ball_sprite, (40, 40)) #size of ball
			bat_sprite = pygame.image.load('gamefiles/assets/bats/' + batlist[batlistnumber] + '.png').convert_alpha()
			bat_sprite = pygame.transform.scale(bat_sprite, (20, 70)) #size of bat
			hit = False
			firstswing = True
		
			#screen.blit(mesg, [dis_width / 6, dis_height / 3])
			

		if hit == True:
			if hit_type == 1:

				bally -= 0.1
			
				if bally < 75:
					ball_sprite = pygame.transform.scale(ball_sprite, (25, 25)) #size of ball
					if bally < 35:
						ball_sprite = pygame.transform.scale(ball_sprite, (10, 10)) #size of ball
			if hit_type == 2:

				bally -= 0.09
				ballx -= 0.03
			
				if bally < 100:
					ball_sprite = pygame.transform.scale(ball_sprite, (25, 25)) #size of ball
					if bally < 90:
						ball_sprite = pygame.transform.scale(ball_sprite, (10, 10)) #size of ball
						if bally < 80:
							ball_sprite = pygame.transform.scale(ball_sprite, (0, 0)) #size of ball
			if hit_type == 3:

				bally -= 0.03
				ballx -= 0.01
			
				if bally < 225:
					ball_sprite = pygame.transform.scale(ball_sprite, (60, 60)) #size of ball
					if bally < 155:
						ball_sprite = pygame.transform.scale(ball_sprite, (20, 20)) #size of ball
						if bally < 135:
							bally -= 0.04
							ball_sprite = pygame.transform.scale(ball_sprite, (0, 0)) #size of ball
			if hit_type == 4:

				bally -= 0.09
				ballx += 0.03
			
				if bally < 100:
					ball_sprite = pygame.transform.scale(ball_sprite, (25, 25)) #size of ball
					if bally < 90:
						ball_sprite = pygame.transform.scale(ball_sprite, (10, 10)) #size of ball
						if bally < 80:
							ball_sprite = pygame.transform.scale(ball_sprite, (0, 0)) #size of ball
			if hit_type == 5:

				bally -= 0.03
				ballx += 0.01
			
				if bally < 225:
					ball_sprite = pygame.transform.scale(ball_sprite, (60, 60)) #size of ball
					if bally < 155:
						ball_sprite = pygame.transform.scale(ball_sprite, (20, 20)) #size of ball
						if bally < 135:
							bally -= 0.04
							ball_sprite = pygame.transform.scale(ball_sprite, (0, 0)) #size of ball
			if hit_type == 7:

				bally -= 0.04
				ballx += 0.06
			
				

			
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				
				exit()
						
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					start = False
					startplay = False
					break
				if event.key == pygame.K_SPACE:
					if firstswing == True and hit == False:
						firstswing = False
						
						bat_sprite = pygame.transform.rotate(bat_sprite, 150)
					if bally >= 298 and bally <= 304:
						hit_type = 1
						hit = True
					if bally >= 277 and bally <= 297:
						rand23 = random.randint(1,3)
						if rand23 == 1:
							hit_type = 3
							hit = True
						else:
							hit_type = 2
							hit = True
					if bally >= 305 and bally <= 318:
						rand23 = random.randint(1,7)
						if rand23 == 7:
							
							hit_type = 7
							hit = True
						if rand23 == 5 or rand23 == 6:
							hit_type = 5
							hit = True
						if rand23 <= 4:
							hit_type = 4
							hit = True
							
							
						
						
						
							
					
						
		
		pygame.display.update()
	while startderby == True:
		#clock.tick(2200)
		seconds = pygame.time.get_ticks() - start_ticks# / 1000
		seconds /= 1000
		seconds = str(round(seconds, 1))
		fps += 1
		
		screen.blit(field_sprite, (0, 0))
		if float(seconds) <= 60:
			timertext = font_style.render(str(seconds), True, black)
			screen.blit(timertext, [dis_width - 85, dis_height - 400])
		while float(homeruns) > 350:
			homeruns -= 350
		
		if homeruns: message_to_screen("Home Run!", (0, 0, 0), "ignore", 5, 340)
		#homeruntext = med_font.render("HomeRuns : " + str(homeruns), True, black)
		#screen.blit(homeruntext, [dis_width - 600, dis_height - 400])
		#besthomeruntext = med_font.render("Best : " + str(highderbyhomeruns), True, black)
		#screen.blit(besthomeruntext, [dis_width - 600, dis_height - 380])
		screen.blit(space2swing, [dis_width / 6 + 260, dis_height / 3 + 250])
		screen.blit(ball_sprite, (ballx, bally))
		screen.blit(bat_sprite, (batx, baty))
		if float(seconds) >= 60:
			endtimer += 1

			if endtimer >= 70:

				startderby = False
				start = False
				for i in fpslist:
					averagefps += i
				averagefps /= float(seconds)

				xp += math.floor(int(homeruns) * derbyhomerunsscoring)
				xp += forplayingscoring
				if ITEM_SHOP_ENABLED: bucks += math.floor(int(homeruns) * homerunsbucks)
				save([balllistnumber, batlistnumber, fieldlistnumber, xp, bucks, balllist, batlist, fieldlist, buckslist])

			timertext = font_style.render("60.00", True, black)
			screen.blit(timertext, [dis_width - 85, dis_height - 400])
			if int(highderbyhomeruns) < int(homeruns):
				with open(folderpath + "//gamefiles//hderby.json", "r") as derbyh:
					jsonfile = derbyh.read()
					derbyh.close()
					jsonfile = json.loads(jsonfile)
				jsonfile["derby"]["homeruns"] = homeruns

				with open(folderpath + "\\gamefiles\\hderby.json", "w") as highscorehomeruns:
					homeruns = str(homeruns)
					highhomeruns = homeruns
					highscorehomeruns.write(json.dumps(jsonfile))
					highscorehomeruns.close()
			mesg1 = font_style.render("Game Over!", True, black)
			screen.blit(mesg1, [dis_width / 5, dis_height / 3])
			bally = -50
			ballx = 0
			batx = 0
			baty = -50
			
		
		
		
		if hit == False:
			bally += 0.09 ### 0.07
		if bally > 600:
			bally = 100
			bat_sprite = pygame.image.load('gamefiles/assets/bats/' + batlist[batlistnumber] + '.png').convert_alpha()
			bat_sprite = pygame.transform.scale(bat_sprite, (20, 70)) #size of bat
			hit = False
			firstswing = True
		if bally <= 0:
			
			bally = 100
			ballx = 265
			ball_sprite = pygame.image.load('gamefiles/assets/balls/' + balllist[balllistnumber] + '.png').convert_alpha() # refresh ball cause it messed up
			ball_sprite = pygame.transform.scale(ball_sprite, (40, 40)) #size of ball
			bat_sprite = pygame.image.load('gamefiles/assets/bats/' + batlist[batlistnumber] + '.png').convert_alpha()
			bat_sprite = pygame.transform.scale(bat_sprite, (25, 70)) #size of bat
			hit = False
			firstswing = True


			if hit_type != 1:
				mesg = font_style.render("Home Run!", False, red)
				
		if hit == True:
			
			if hit_type == 1:

				bally -= 0.1
			
				if bally < 75:
					ball_sprite = pygame.transform.scale(ball_sprite, (25, 25)) #size of ball
					if bally < 35:
						ball_sprite = pygame.transform.scale(ball_sprite, (10, 10)) #size of ball
						
						homeruns = int(homeruns) + 1
						
			if hit_type == 2:

				bally -= 0.09
				ballx -= 0.03
			
				if bally < 100:
					ball_sprite = pygame.transform.scale(ball_sprite, (25, 25)) #size of ball
					if bally < 90:
						ball_sprite = pygame.transform.scale(ball_sprite, (10, 10)) #size of ball
						if bally < 80:
							ball_sprite = pygame.transform.scale(ball_sprite, (0, 0)) #size of ball
			if hit_type == 3:

				bally -= 0.03
				ballx -= 0.01
			
				if bally < 225:
					ball_sprite = pygame.transform.scale(ball_sprite, (60, 60)) #size of ball
					if bally < 155:
						ball_sprite = pygame.transform.scale(ball_sprite, (20, 20)) #size of ball
						if bally < 135:
							bally -= 0.04
							ball_sprite = pygame.transform.scale(ball_sprite, (0, 0)) #size of ball
			if hit_type == 4:

				bally -= 0.09
				ballx += 0.03
			
				if bally < 100:
					ball_sprite = pygame.transform.scale(ball_sprite, (25, 25)) #size of ball
					if bally < 90:
						ball_sprite = pygame.transform.scale(ball_sprite, (10, 10)) #size of ball
						if bally < 80:
							ball_sprite = pygame.transform.scale(ball_sprite, (0, 0)) #size of ball
			if hit_type == 5:

				bally -= 0.03
				ballx += 0.01
			
				if bally < 225:
					ball_sprite = pygame.transform.scale(ball_sprite, (60, 60)) #size of ball
					if bally < 155:
						ball_sprite = pygame.transform.scale(ball_sprite, (20, 20)) #size of ball
						if bally < 135:
							bally -= 0.04
							ball_sprite = pygame.transform.scale(ball_sprite, (0, 0)) #size of ball
			if hit_type == 7:
				

				bally -= 0.04
				ballx += 0.06
				
				
		
			
		for event in pygame.event.get():
			if event.type == secondevent:
				
				fpslist.append(fps)
				fps = 0
			if event.type == updateevent: 
				pygame.mouse.set_visible(False)
				#pygame.display.set_caption('Baseball Game  -- Derby   ' + str(seconds) + "   " + str(homeruns) + " hrs")
			if event.type == pygame.QUIT:
				
				exit()
						
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					start = False
					startderby = False
					
				if event.key == pygame.K_SPACE:
					if firstswing == True and hit == False:
						firstswing = False
						
						bat_sprite = pygame.transform.rotate(bat_sprite, 150)
					if bally >= 298 and bally <= 304:
						
						hit_type = 1
						hit = True
					if bally >= 277 and bally <= 297:
						rand23 = random.randint(1,3)
						
						if rand23 == 1:
							hit_type = 3
							hit = True
						else:
							hit_type = 2
							hit = True
					if bally >= 305 and bally <= 318:
						
						rand23 = random.randint(1,7)
						if rand23 == 7:
							hit_type = 7
							hit = True
						if rand23 == 5 or rand23 == 6:
							hit_type = 5
							hit = True
						if rand23 <= 4:
							hit_type = 4
							hit = True
					
		pygame.display.update()
	while optionsmenu == True:
		statsback = True
		settingsback = True
		shopback = True
		screen.blit(optionsmenu_sprite, (0, 0))
		
		
		statsrect = pygame.Rect(70, dis_height - 290, 130, 95)
		settingsrect = pygame.Rect(210, dis_height - 350, 165, 130)
		battlepassrect = pygame.Rect(120, dis_height - 170, 125, 85)
		assetrect = pygame.Rect(290, dis_height - 175, 220, 80)
		shoprect = pygame.Rect(350, dis_height - 265, 185, 75)
		backrect = pygame.Rect(90, dis_height - 70, 410, 50)
		
		#if random.randint(1, 2) == 1:
			#pygame.draw.rect(screen,red,(statsrect))
			#pygame.draw.rect(screen,red,(settingsrect))
			#pygame.draw.rect(screen,red,(backrect))
			#pygame.draw.rect(screen,red,(assetrect))
			#pygame.draw.rect(screen,red,(shoprect))
			#pygame.draw.rect(screen,red,(battlepassrect))
		for event in pygame.event.get():
			
			if event.type == pygame.KEYDOWN: 
				if event.key == pygame.K_ESCAPE: optionsmenu = False; start = False
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				
				
				if statsrect.collidepoint(event.pos): statsback = False
				if shoprect.collidepoint(event.pos): shopback = False; screen.fill(white)
				if battlepassrect.collidepoint(event.pos): 
					battlepass = False
					data = opensave()
					xp = data[3]
					
				if assetrect.collidepoint(event.pos): 
					asset = False
					ball, bat, field, xp, bucks, balllist, batlist, fieldlist, buckslist = opensave()

					balllist = ast.literal_eval(str(balllist))
					batlist = ast.literal_eval(str(batlist))
					fieldlist = ast.literal_eval(str(fieldlist))
					
					field_display = pygame.image.load('gamefiles/assets/fields/' + fieldlist[fieldlistnumber] + '.png').convert_alpha()
					ball_display = pygame.image.load('gamefiles/assets/balls/' + balllist[balllistnumber] + '.png').convert_alpha()
					bat_display = pygame.image.load('gamefiles/assets/bats/' + batlist[batlistnumber] + '.png').convert_alpha()
				
				if backrect.collidepoint(event.pos): start = False; optionsmenu = False
			if event.type == pygame.QUIT:
				exit()
		pygame.display.update()

		while statsback == False:
			screen.blit(back_sprite, (0, 0))
			try:
				with open(folderpath + "\\gamefiles\\hplay.json", "r") as hjson:
					file = hjson.read()
					hjson.close()
			except: pass

			jsonfile = json.loads(file)
			
			
			highhomeruns = str(jsonfile["play"]["homeruns"])
			highruns = str(jsonfile["play"]["runs"])
			highsingles = str(jsonfile["play"]["singles"])
			highdoubles = str(jsonfile["play"]["doubles"])
			try:
				with open(folderpath + "\\gamefiles\\hderby.json", "r") as hjson:
					file = hjson.read()
					hjson.close()
			except: pass
			jsonfile = json.loads(file)
			highderbyhomeruns = str(jsonfile["derby"]["homeruns"])
			
			mesg = med_font.render("Best Runs : " + highruns, True, black)
			screen.blit(mesg, [dis_width - 595, dis_height - 395])
			mesg = med_font.render("Best Singles : " + highsingles, True, black)
			screen.blit(mesg, [dis_width - 595, dis_height - 375])
			mesg = med_font.render("Best Doubles : " + highdoubles, True, black)
			screen.blit(mesg, [dis_width - 595, dis_height - 355])
			mesg = med_font.render("Best Home Runs : " + highhomeruns, True, black)
			screen.blit(mesg, [dis_width - 595, dis_height - 335])
			mesg = big_font.render("Derby Scores", True, black)
			screen.blit(mesg, [dis_width - 300, dis_height - 395])
			mesg = med_font.render("Best Home Runs : " + highderbyhomeruns, True, black)
			screen.blit(mesg, [dis_width - 290, dis_height - 355])
		   
			highderbyhomeruns = int(highderbyhomeruns)
			


			backrect = pygame.Rect(360, 265, 110, 55)
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
			
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					if backrect.collidepoint(event.pos):
						statsback = True
				
			
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE: statsback = True
					if event.key == pygame.K_SPACE:
						statsback = True
					
					
			pygame.display.update()
				
		while asset == False:
			
			screen.fill(white)

			screen.blit(right_arrow, [375, 25])
			screen.blit(left_arrow, [100, 25])
			
			screen.blit(right_arrow, [375, 150])
			screen.blit(left_arrow, [100, 150])

			screen.blit(right_arrow, [375, 275])
			screen.blit(left_arrow, [100, 275])
			
			
			
			screen.blit(pygame.transform.scale(ball_display, (80, 80)), [240, 20])
			screen.blit(pygame.transform.scale(bat_display, (40, 140)), [260, 125])
			
			screen.blit(pygame.transform.scale(field_display, (150, 105)), [210, 275])
			
			screen.blit(assetsback_sprite, [0, 0])
			
			
			rightballrect = pygame.Rect(375, 25, 100, 100)
			leftballrect = pygame.Rect(100, 25, 100, 100)

			rightbatrect = pygame.Rect(375, 150, 100, 100)
			leftbatrect = pygame.Rect(100, 150, 100, 100)

			rightfieldrect = pygame.Rect(375, 275, 100, 100)
			leftfieldrect = pygame.Rect(100, 275, 100, 100)

			backrect = pygame.Rect(480, 320, 100, 50)
			
			for event in pygame.event.get():

				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				
					if leftballrect.collidepoint(event.pos):
						
						balllistnumber -= 1
					elif rightballrect.collidepoint(event.pos):
						
						balllistnumber += 1
					elif leftfieldrect.collidepoint(event.pos):
						
						fieldlistnumber -= 1
					elif rightfieldrect.collidepoint(event.pos):
					
						
						fieldlistnumber += 1
					elif leftbatrect.collidepoint(event.pos):
						
						
						batlistnumber -= 1
					elif rightbatrect.collidepoint(event.pos):
						
						
						batlistnumber += 1
					
					elif backrect.collidepoint(event.pos):
						asset = True
						optionsmenu = True
						menuplace = 3
					
					
					
					if balllistnumber > len(balllist) - 1:
						balllistnumber = 0
					if batlistnumber < 0: balllistnumber = len(balllist) - 1
					if batlistnumber > len(batlist) - 1:
						batlistnumber = 0
					if batlistnumber < 0: batlistnumber = len(batlist) - 1
					if fieldlistnumber > len(fieldlist) - 1:
						fieldlistnumber = 0
					if fieldlistnumber < 0: fieldlistnumber = len(fieldlist) - 1
					
					
					
					
					
					
					field_display = pygame.image.load('gamefiles/assets/fields/' + fieldlist[fieldlistnumber] + '.png').convert_alpha()
					ball_display = pygame.image.load('gamefiles/assets/balls/' + balllist[balllistnumber] + '.png').convert_alpha()
					bat_display = pygame.image.load('gamefiles/assets/bats/' + batlist[batlistnumber] + '.png').convert_alpha()

					

					if balllistnumber > len(balllist) - 1:
						balllistnumber = 0
					if batlistnumber < 0: balllistnumber = len(balllist) - 1
					if batlistnumber > len(batlist) - 1:
						batlistnumber = 0
					if batlistnumber < 0: batlistnumber = len(batlist) - 1
					if fieldlistnumber > len(fieldlist) - 1:
						fieldlistnumber = 0
					if fieldlistnumber < 0: fieldlistnumber = len(fieldlist) - 1


					data = opensave()
					

					
					save([balllistnumber, batlistnumber, fieldlistnumber, xp, bucks, balllist, batlist, fieldlist, buckslist])
					
					ball_sprite = pygame.image.load('gamefiles/assets/balls/' + balllist[balllistnumber] + '.png').convert_alpha()
					bat_sprite = pygame.image.load('gamefiles/assets/bats/' + batlist[batlistnumber] + '.png').convert_alpha()
					field_sprite = pygame.image.load('gamefiles/assets/fields/' + fieldlist[fieldlistnumber] + '.png').convert_alpha()
					field_sprite = pygame.transform.scale(field_sprite, (620, 420)) #size of field
					bat_sprite = pygame.transform.scale(bat_sprite, (20, 70))
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE: asset = True; optionsmenu = True
					if event.key == pygame.K_SPACE:
						asset = True
						optionsmenu = True
						
				if event.type == pygame.QUIT:
					exit()
			
			
			
			pygame.display.update()

	
		while shopback == False and ITEM_SHOP_ENABLED:
			
			#save([balllistnumber, batlistnumber, fieldlistnumber, xp, bucks, balllist, batlist, fieldlist, buckslist])
			screen.blit(back_sprite, (-50, 50))
			if shoppage < 3:
				screen.blit(right_arrow, [500, 300])
			if shoppage != 1:
				screen.blit(left_arrow, [15, 300])
			rightrect = pygame.Rect(500, 300, 100, 100)
			leftrect = pygame.Rect(15, 300, 100, 100)
			backrect = pygame.Rect(310, 315, 110, 55)
			
			evenbuyrect = pygame.Rect(80, 210, 167, 65)
			oddbuyrect = pygame.Rect(80 + 1 * 250, 210, 167, 65)

			screen.blit(bucksicon, (150, 320))
			bucks_text = splash_font.render(str(opensave()[4]), True, yellow)
			screen.blit(bucks_text, [175, 360])
			for i in range(2):

				a = shoppage * 2 + i - 2
				screen.blit(shopbox, [60 + i * 250, 35])

				
				#if random.randint(1, 2) == 1:
					#pygame.draw.rect(screen,red,(buyrect))

				if a == 0:
					smileball = pygame.image.load('gamefiles/assets/balls/smileball.png').convert_alpha()
					screen.blit(pygame.transform.scale(smileball, (125, 120)), [105 + i * 250, 43])
					screen.blit(bucksicon100, [135 + i * 250, 130])
					if "smileball" not in opensave()[5]: screen.blit(pygame.transform.scale(buy1, (167, 65)), [80 + i * 250, 210])
					else: screen.blit(pygame.transform.scale(buy2, (167, 65)), [80 + i * 250, 210])
				if a == 1:
					baseballball = pygame.image.load('gamefiles/assets/balls/baseballball.png').convert_alpha()
					screen.blit(pygame.transform.scale(baseballball, (125, 120)), [105 + i * 250, 43])
					if "baseballball" not in opensave()[5]: screen.blit(pygame.transform.scale(buy1, (167, 65)), [80 + i * 250, 210])
					else: screen.blit(pygame.transform.scale(buy2, (167, 65)), [80 + i * 250, 210])
				if a == 2:
					axebat = pygame.image.load('gamefiles/assets/bats/axebat.png').convert_alpha()
					screen.blit(pygame.transform.scale(axebat, (45, 120)), [140 + i * 250, 43])
					if "axebat" not in opensave()[6]: screen.blit(pygame.transform.scale(buy1, (167, 65)), [80 + i * 250, 210])
					else: screen.blit(pygame.transform.scale(buy2, (167, 65)), [80 + i * 250, 210])
				if a == 3:
					roseball = pygame.image.load('gamefiles/assets/balls/roseball.png').convert_alpha()
					screen.blit(pygame.transform.scale(roseball, (125, 120)), [105 + i * 250, 43])
					if "roseball" not in opensave()[5]: screen.blit(pygame.transform.scale(buy1, (167, 65)), [80 + i * 250, 210])
					else: screen.blit(pygame.transform.scale(buy2, (167, 65)), [80 + i * 250, 210])
				if a == 5:
					roseball = pygame.image.load('gamefiles/assets/balls/roseball.png').convert_alpha()
					screen.blit(pygame.transform.scale(roseball, (125, 120)), [105 + i * 250, 43])
					if "roseball" not in opensave()[5]: screen.blit(pygame.transform.scale(buy1, (167, 65)), [80 + i * 250, 210])
					else: screen.blit(pygame.transform.scale(buy2, (167, 65)), [80 + i * 250, 210])
				if a == 6:
					roseball = pygame.image.load('gamefiles/assets/balls/roseball.png').convert_alpha()
					screen.blit(pygame.transform.scale(roseball, (125, 120)), [105 + i * 250, 43])
					if "roseball" not in opensave()[5]: screen.blit(pygame.transform.scale(buy1, (167, 65)), [80 + i * 250, 210])
					else: screen.blit(pygame.transform.scale(buy2, (167, 65)), [80 + i * 250, 210])

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE: shopback = True
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					if backrect.collidepoint(event.pos):
						shopback = True
					if rightrect.collidepoint(event.pos):
						if shoppage < 3: shoppage += 1; screen.fill(white)
					if leftrect.collidepoint(event.pos):
						if shoppage != 1: shoppage -= 1
					if evenbuyrect.collidepoint(event.pos):
						if shoppage == 1: bucks, balllist = buy("smileball", bucks, 100, balllist)
						if shoppage == 2: bucks, batlist = buy("axebat", bucks, 100, batlist)
						if shoppage == 3: bucks, batlist = buy("roseball", bucks, 100, batlist)
						save([balllistnumber, batlistnumber, fieldlistnumber, xp, bucks, balllist, batlist, fieldlist, buckslist])
					if oddbuyrect.collidepoint(event.pos):
						if shoppage == 1: bucks, balllist = buy("baseballball", bucks, 100, balllist)
						if shoppage == 2: bucks, balllist = buy("roseball", bucks, 100, balllist)
						if shoppage == 3: bucks, balllist = buy("roseball", bucks, 100, balllist)
						save([balllistnumber, batlistnumber, fieldlistnumber, xp, bucks, balllist, batlist, fieldlist, buckslist])
					
				if event.type == pygame.QUIT:
					exit()
			pygame.display.update()
		

		#xp = 0
		while battlepass == False:
			screen.fill(white)
			screen.blit(back_sprite, (-50, 50))
			
			for i in range(1,5):

				a = page * 4 + i - 4

				level = math.floor(xp / 100) + 1

				# Giving is at start


				if a < level: screen.blit(battlepassboxpast, [-50 + i * 115, 50])
				elif a > level: screen.blit(battlepassboxfuture, [-50 + i * 115, 50])
				else: screen.blit(battlepassboxpresent, [-50 + i * 115, 50])

				if a == 2:
					
					snowfield = pygame.image.load('gamefiles/assets/fields/snowfield.png').convert_alpha()
					screen.blit(pygame.transform.scale(snowfield, (90, 50)), [-35 + i * 115, 70])
				
				if a == 4:
					
					axebat = pygame.image.load('gamefiles/assets/bats/axebat.png').convert_alpha()
					screen.blit(pygame.transform.scale(axebat, (45, 120)), [-20 + i * 115, 70])
				
				if a == 7:
					
					sandfield = pygame.image.load('gamefiles/assets/fields/sandfield.png').convert_alpha()
					screen.blit(pygame.transform.scale(sandfield, (90, 50)), [-35 + i * 115, 70])
				
				if a == 15:

					coolbat = pygame.image.load('gamefiles/assets/bats/coolbat.png').convert_alpha()
					screen.blit(pygame.transform.scale(coolbat, (45, 120)), [-20 + i * 115, 70])
			
				if a == 19:
					
					hammerbat = pygame.image.load('gamefiles/assets/bats/hammerbat.png').convert_alpha()
					screen.blit(pygame.transform.scale(hammerbat, (45, 120)), [-20 + i * 115, 70])
				
				if a == 10:
					
					christmasball = pygame.image.load('gamefiles/assets/balls/christmasball.png').convert_alpha()
					screen.blit(pygame.transform.scale(christmasball, (80, 80)), [-30 + i * 115, 70])
				
				if a == 17:
					
					starball = pygame.image.load('gamefiles/assets/balls/starball.png').convert_alpha()
					screen.blit(pygame.transform.scale(starball, (80, 80)), [-30 + i * 115, 70])
				
				if a == 6:
					
					roseball = pygame.image.load('gamefiles/assets/balls/roseball.png').convert_alpha()
					screen.blit(pygame.transform.scale(roseball, (80, 80)), [-30 + i * 115, 70])
				
				if a == 12:
					
					hockeybat = pygame.image.load('gamefiles/assets/bats/hockeybat.png').convert_alpha()
					screen.blit(pygame.transform.scale(hockeybat, (45, 120)), [-20 + i * 115, 70])
				
				if a == 14:
					
					waterfield = pygame.image.load('gamefiles/assets/fields/waterfield.png').convert_alpha()
					screen.blit(pygame.transform.scale(waterfield, (90, 50)), [-35 + i * 115, 70])
				
				if a == 16:
								
					screen.blit(bucksicon100, [-35 + i * 120, 70])
					
				
				if a == 11:
					
					screen.blit(bucksicon100, [-75 + i * 135, 70])
				
				if a == 9:
					
					screen.blit(bucksicon75, [-35 + i * 135, 70])
					
				if a == 8:
					
					screen.blit(bucksicon100, [-75 + i * 135, 70])
				
				
				
				screen.blit(xpicon, [180, 320])
				xp_text = splash_font.render(str(xp), True, blue)
			
				screen.blit(xp_text, [188, 305])






				ab = verybig_font.render(str(a), True, grey)
				screen.blit(ab, [-10 + i * 115, 230])
				
			
			if page != 5:
				screen.blit(right_arrow, [500, 300])
			if page != 1:
				screen.blit(left_arrow, [15, 300])
			rightrect = pygame.Rect(500, 300, 100, 100)
			leftrect = pygame.Rect(15, 300, 100, 100)
			backrect = pygame.Rect(310, 315, 110, 55)



			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE: battlepass = True
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					#screen.fill(white)
					if backrect.collidepoint(event.pos):
						battlepass = True
					if rightrect.collidepoint(event.pos):
						if page < 5: page += 1 # max. 10 later
					if leftrect.collidepoint(event.pos):
						if page > 1: page -= 1
					
				if event.type == pygame.QUIT:
					exit()
			
			
			
			
			
			pygame.display.update()