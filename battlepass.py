forplayingscoring = 15
derbyhomerunsscoring = 3.2
homerunsscoring = 2.8
singlesscoring = 1.6
doublesscoring = 2.4	
	
	
	
	while battlepass == False:
			screen.fill(white)
			for i in range(1, 5):
				
				a = page * 4 + i - 4
				
				level = math.floor(xp / 100) + 1

				
				

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
				
				if a == 12:
					
					hockeybat = pygame.image.load('gamefiles/assets/bats/hockeybat.png').convert_alpha()
					screen.blit(pygame.transform.scale(hockeybat, (45, 120)), [-20 + i * 115, 70])
				
				if a == 14:
					
					waterfield = pygame.image.load('gamefiles/assets/fields/waterfield.png').convert_alpha()
					screen.blit(pygame.transform.scale(waterfield, (90, 50)), [-35 + i * 115, 70])
				
				
				
				screen.blit(xpicon, [180, 320])
				xp_text = splash_font.render(str(xp), True, blue)
			
				screen.blit(xp_text, [188, 305])






				ab = verybig_font.render(str(a), True, grey)
				screen.blit(ab, [-10 + i * 115, 230])
				
				

			screen.blit(right_arrow, [500, 300])
			screen.blit(left_arrow, [15, 300])
			rightrect = pygame.Rect(500, 300, 100, 100)
			leftrect = pygame.Rect(15, 300, 100, 100)



			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE: battlepass = True
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					if rightrect.collidepoint(event.pos):
						if page < 5: page += 1 # max. 10 later
					if leftrect.collidepoint(event.pos):
						if page > 1: page -= 1
					
				if event.type == pygame.QUIT:
					exit()
			
			
			
			
			
			pygame.display.update()
