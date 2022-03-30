#Note: settings was removed in 1.2


while settingsback == False:
            



            
            screen.blit(optionsmenustatsback_sprite, (0, 0))

            if menuplace == 1:
                screen.blit(ball_settings, (105, 20))
            if menuplace == 2:
                screen.blit(ball_settings, (145, 70))

            settingstitle = big_font.render("Settings", True, black)
            screen.blit(settingstitle, [dis_width - 300, dis_height - 395])
            mesg11 = med_font.render("Volume      " + str(volume), True, black)
            screen.blit(mesg11, [dis_width - 595, dis_height - 370])
            mesg12 = med_font.render("Sfx Volume      " + str(sfxvolume), True, black)
            screen.blit(mesg12, [dis_width - 595, dis_height - 320])
            

                
            volume = round(volume, 1)
            sfxvolume = round(sfxvolume, 1)







            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        menuplace -= 1
                        if menuplace <= 0:
                            menuplace = 2
                    if event.key == pygame.K_DOWN:
                        menuplace += 1
                        if menuplace >= 3:
                            menuplace = 1
                    if event.key == pygame.K_RIGHT:
                        
                        if menuplace == 1:
                            volume += 0.1

                            if volume > 1.0:
                                volume = 1.0
                            mixer.music.set_volume(volume)
                        if menuplace == 2:
                            sfxvolume += 0.1
                            if sfxvolume > 1.0:
                                sfxvolume = 1.0
                            mixer.music.set_volume(volume)
                        
                    if event.key == pygame.K_LEFT:
                        if menuplace == 1:
                            volume -= 0.1
                        if volume < 0.0:
                            volume = 0.0
                        mixer.music.set_volume(volume)

                        if menuplace == 2:
                            sfxvolume -= 0.1
                            if sfxvolume < 0.0:
                                sfxvolume = 0.0

                    
                    
                    if event.key == pygame.K_SPACE:
                        settingsback = True
                        menuplace = 2
                        start = False
                        try:
                            with open(folderpath + "//gamefiles//settings.json", "r") as settings:
                                jsonfile = settings.read()
                                settings.close()
                            jsonfile = json.loads(jsonfile)
                            jsonfile["settings"]["volume"] = volume
                            jsonfile["settings"]["sfxvolume"] = sfxvolume
                            sfxvolume = float(sfxvolume)
                            with open(folderpath + "\\gamefiles\\settings.json", "w") as savesettings:
                
                                savesettings.write(json.dumps(jsonfile))
                                savesettings.close()
                        except:
                            print("skipped crash")
                            #del(volume)
                            #del(sfxvolume) # forget vars so won't update without new data
                            pass
