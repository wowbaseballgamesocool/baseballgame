				if event.key == pygame.K_SPACE and menuplace == 4:
          				asset = False
					screen.fill(white)
					balllist = ["ball", "ball"]
					fieldlist = ["field", "snowfield", "sandfield"]
					batlist = ["bat", "axe_bat", "cool_bat"]
					field_display = pygame.image.load('gamefiles/assets/fields/' + fieldlist[fieldlistnumber] + '.png').convert_alpha()
					ball_display = pygame.image.load('gamefiles/assets/' + balllist[balllistnumber] + '.png').convert_alpha()
					bat_display = pygame.image.load('gamefiles/assets/bats/' + batlist[batlistnumber] + '.png').convert_alpha()
				if event.key == pygame.K_SPACE and menuplace == 3:
					start = False
					optionsmenu = False

		while asset == False:
			

			if balllistnumber > len(balllist) - 1:
				balllistnumber = 0
			if batlistnumber < 0: balllistnumber = len(balllist) - 1
			if batlistnumber > len(batlist) - 1:
				batlistnumber = 0
			if batlistnumber < 0: batlistnumber = len(batlist) - 1
			if fieldlistnumber > len(fieldlist) - 1:
				fieldlistnumber = 0
			if fieldlistnumber < 0: fieldlistnumber = len(fieldlist) - 1
			
			screen.fill(white)

			screen.blit(right_arrow, [375, 25])
			screen.blit(left_arrow, [100, 25])
			
			screen.blit(right_arrow, [375, 150])
			screen.blit(left_arrow, [100, 150])

			screen.blit(right_arrow, [375, 275])
			screen.blit(left_arrow, [100, 275])
			#try:
				#ball_display = pygame.image.load('gamefiles/assets/' + balllist[balllistnumber] + '.png').convert_alpha()
			#except: ball_display = pygame.image.load('gamefiles/assets/' + balllist[0] + '.png').convert_alpha()
			
			
			
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



			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				
					if leftballrect.collidepoint(event.pos):
						ball_display = pygame.image.load('gamefiles/assets/' + balllist[balllistnumber] + '.png').convert_alpha()
						balllistnumber -= 1
					elif rightballrect.collidepoint(event.pos):
						ball_display = pygame.image.load('gamefiles/assets/' + balllist[balllistnumber] + '.png').convert_alpha()
						balllistnumber += 1
					elif leftfieldrect.collidepoint(event.pos):
						field_display = pygame.image.load('gamefiles/assets/fields/' + fieldlist[fieldlistnumber] + '.png').convert_alpha()
						fieldlistnumber -= 1
					elif rightfieldrect.collidepoint(event.pos):
					
						field_display = pygame.image.load('gamefiles/assets/fields/' + fieldlist[fieldlistnumber] + '.png').convert_alpha()
						fieldlistnumber += 1
					elif leftbatrect.collidepoint(event.pos):
						
						bat_display = pygame.image.load('gamefiles/assets/bats/' + batlist[batlistnumber] + '.png').convert_alpha()
						batlistnumber -= 1
					elif rightbatrect.collidepoint(event.pos):
						
						bat_display = pygame.image.load('gamefiles/assets/bats/' + batlist[batlistnumber] + '.png').convert_alpha()
						batlistnumber += 1








				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						asset = True
						optionsmenu = True
						menuplace = 3
				if event.type == pygame.QUIT:
					exit()
			
			
			
			pygame.display.update()
