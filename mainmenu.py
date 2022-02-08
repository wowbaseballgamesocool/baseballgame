while True:
    

    pygame.display.set_caption('Baseball Game -- Menu')
    while start == False:
        endtimer,outs = 0, 0
        ball_sprite = pygame.image.load('gamefiles/assets/ball.png').convert_alpha()
        ball_sprite = pygame.transform.scale(ball_sprite, (40, 40)) #size of ball
        bat_sprite = pygame.image.load('gamefiles/assets/bat.png').convert_alpha()
        bat_sprite = pygame.transform.scale(bat_sprite, (20, 70)) #size of bat old: 15, 70
        

        
        optionsmenu = False
        startderby = False
        startplay = False
        hit = False
        firstswing = True
        
        strikes = 0
        start = False
        runs = 0
        runner = 0
        singles = 0
        doubles = 0
        homeruns = 0
        hit_type = 0
        ballx = 265
        bally = 100
        batx = 260
        baty = 310
        screen.blit(menubg_sprite, (0, 0))
        space2start = small_font.render("space and arrow keys to Select", True, black)
        
        if menuplace == 1:
            screen.blit(menubg_sprite, (0, 0))
            screen.blit(menuplay_sprite, (0, 0))
            screen.blit(space2start, [dis_width / 2 - 250, dis_height / 2 + 150])
        if menuplace == 2:
            screen.blit(menubg_sprite, (0, 0))
            screen.blit(menuderby_sprite, (0, 0))
            screen.blit(space2start, [dis_width / 2 - 250, dis_height / 2 + 150])
        if menuplace == 3:
            screen.blit(menubg_sprite, (0, 0))
            screen.blit(menuoptions_sprite, (0, 0))
            screen.blit(space2start, [dis_width / 2 - 250, dis_height / 2 + 150])
        if menuplace == 4:
            screen.blit(menubg_sprite, (0, 0))
            screen.blit(menuexit_sprite, (0, 0))
            screen.blit(space2start, [dis_width / 2 - 250, dis_height / 2 + 150])
        
        
        pygame.display.flip()
        for event in pygame.event.get(): 
            
            if event.type == pygame.QUIT: exit()
            if event.type == pygame.KEYDOWN:
                sfxvolume = 0.1
                if event.key == pygame.K_SPACE and menuplace == 1:
                    play("batsound.mp3", sfxvolume)
                    pygame.display.set_caption('Baseball Game -- Play')
                    
                    start = True
                    startplay = True
                    
                if event.key == pygame.K_SPACE and menuplace == 2:
                    play("batsound.mp3", sfxvolume)
                    pygame.display.set_caption('Baseball Game -- Derby')
                    
                    
                    start = True
                    startderby = True

                if event.key == pygame.K_SPACE and menuplace == 3:
                    play("batsound.mp3", sfxvolume)
                    pygame.display.set_caption('Baseball Game -- Options')
                    
                    start = True
                    optionsmenu = True
                    menuplace = 1
                    


                
                if event.key == pygame.K_SPACE and menuplace == 4:
                    exit()
                    
                if event.key == pygame.K_RIGHT:
            
                    menuplace += 1
                    if menuplace >= 5:
                        menuplace = 1

                    
                if event.key == pygame.K_LEFT:
            
                    menuplace -= 1
                    if menuplace <= 0:
                        menuplace = 4
