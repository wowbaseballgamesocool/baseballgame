while battlepass == False:
			screen.fill(white)
			for i in range(1, 5):
				
				a = page * 4 + i - 4
				
				level = math.floor(xp / 100) + 1
				
				

				if a < level: screen.blit(battlepassboxpast, [-50 + i * 115, 50])
				elif a > level: screen.blit(battlepassboxfuture, [-50 + i * 115, 50])
				else: screen.blit(battlepassboxpresent, [-50 + i * 115, 50])

				if a == 2:
					give("", fieldlist, level, 2)
					snowfield = pygame.image.load('gamefiles/assets/fields/.png').convert_alpha()
					screen.blit(pygame.transform.scale(snowfield, (90, 50)), [-35 + i * 115, 70])
				
				if a == 4:
					give("axebat", batlist, level, 4)
					axebat = pygame.image.load('gamefiles/assets/bats/.png').convert_alpha()
					screen.blit(pygame.transform.scale(axebat, (45, 120)), [-20 + i * 115, 70])
				
				if a == 7:
					give("", fieldlist, level, 7)
					sandfield = pygame.image.load('gamefiles/assets/fields/.png').convert_alpha()
					screen.blit(pygame.transform.scale(sandfield, (90, 50)), [-35 + i * 115, 70])
				
				if a == 15:
					give("", batlist, level, 15)
					coolbat = pygame.image.load('gamefiles/assets/bats/.png').convert_alpha()
					screen.blit(pygame.transform.scale(coolbat, (45, 120)), [-20 + i * 115, 70])
				
				
				
				
				screen.blit(xpicon, [180, 320])
				xp_text = splash_font.render(str(xp), True, green)
			
				screen.blit(xp_text, [187, 305])






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
						if page < 5: page += 1
					if leftrect.collidepoint(event.pos):
						if page > 1: page -= 1
					
				if event.type == pygame.QUIT:
					exit()
			
			
			
			
			
			pygame.display.update()
