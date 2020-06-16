from sprites import *


# --- TIMER ---
class Timer:
    # możliwe, że się przyda
    def __init__(self):
        self.time_start = 0

    def start(self):
        self.time_start = pygame.time.get_ticks()

    def current(self):
        return (pygame.time.get_ticks() - self.time_start) / 1000


# --- MAIN GAME CLASS ---
class Game:
    def __init__(self):
        # initializing game display
        self.screen = pygame.display.set_mode(RESOLUTION)
        # game title
        pygame.display.set_caption(TITLE)
        # counting time
        self.clock = pygame.time.Clock()
        # is game running
        self.running = True
        # devs
        self.devs = False

        self.multiplier = multiplier
        self.deaths = 0

        self.jump_sound = pygame.mixer.Sound(os.path.join('sounds', 'Jump2.wav'))
        self.hit_sound = pygame.mixer.Sound(os.path.join('sounds', 'Hit_Hurt.wav'))
        self.coin_sound = pygame.mixer.Sound(os.path.join('sounds', 'Pickup_Coin.wav'))
        self.powerup_sound = pygame.mixer.Sound(os.path.join('sounds', 'Powerup.wav'))

    # start new game
    def new_game(self):
        self.player = PlayerClass(self)
        # self.level = Level.__init__(self, self.player)
        # grouping all sprites
        self.all_sprites = pygame.sprite.Group()
        # platforms group
        self.platforms = pygame.sprite.Group()
        # adding player to sprite group
        self.all_sprites.add(self.player)

        self.point_counter = 0
        self.points_list = pygame.sprite.Group()
        self.boosts_list = pygame.sprite.Group()

        self.timer = Timer()
        self.timer.start()
        self.play_time = 0

        self.level1()

        self.run_game()

    # main game loop
    def run_game(self):

        pygame.mixer.music.load(os.path.join('sounds', 'j-bernardt-motel-official-audio.ogg'))
        pygame.mixer.music.set_volume(0.06)
        pygame.mixer.music.play(loops = -1)
        self.playing = True

        while self.playing:
            # in-game frames per second
            self.clock.tick(FPS)

            # running all game functions
            self.handle_events()
            self.update()
            self.draw()
        pygame.mixer.music.fadeout(500)

    # updating game state
    def update(self):

        self.screen.fill(BLACK)

        if self.devs:
            self.write(100, 100)

        self.all_sprites.update()

        # screen movement when close to the edge
        if self.player.rect.right >= SCREEN_WIDTH - 200 and self.player.velocity.x > 0:
            self.player.rect.right = SCREEN_WIDTH - 200
            for plat in self.platforms:
                plat.rect.x -= abs(self.player.velocity.x)
            for p in self.points_list:
                p.rect.x -= abs(self.player.velocity.x)
            for ciasteczko in self.boosts_list:
                ciasteczko.rect.x -= abs(self.player.velocity.x)

        if self.player.rect.left <= 200 and self.player.velocity.x < 0:
            self.player.rect.left = 200
            for plat in self.platforms:
                plat.rect.x += abs(self.player.velocity.x)
            for p in self.points_list:
                p.rect.x += abs(self.player.velocity.x)
            for ciasteczko in self.boosts_list:
                ciasteczko.rect.x += abs(self.player.velocity.x)

        # collecting points
        pts_hit = pygame.sprite.spritecollide(self.player, self.points_list, True)
        for p in pts_hit:
            self.coin_sound.play()
            p.kill()
            if p.type == 'gold':
                self.point_counter += 5
            elif p.type == 'silver':
                self.point_counter += 1

            print(self.point_counter)

        # ciasteczka boostuja skok w chwili ich zebrania
        boost_hit = pygame.sprite.spritecollide(self.player, self.boosts_list, True)

        for cookie in boost_hit:
            self.powerup_sound.play()
            cookie.kill()
            multiplier = 2
            self.player.velocity.y = self.player.velocity.y * multiplier
            print('COOKIE')

        # collision with spikes and player's death
        if self.player.rect.bottom >= self.spikes1.rect.top and self.player.rect.right >= self.spikes1.rect.left and self.player.rect.left <= self.spikes1.rect.right:
            self.hit_sound.play()
            self.player.kill()
            self.play_time = self.timer.current()
            self.deaths += 1
            game.game_over_menu()

        if self.player.rect.bottom >= self.spikes2.rect.top and self.player.rect.right >= self.spikes2.rect.left and self.player.rect.left <= self.spikes2.rect.right:
            self.hit_sound.play()
            self.player.kill()
            self.play_time = self.timer.current()
            self.deaths += 1
            game.game_over_menu()

        if self.player.rect.bottom >= self.spikes3.rect.top and self.player.rect.right >= self.spikes3.rect.left and self.player.rect.left <= self.spikes3.rect.right:
            self.hit_sound.play()
            self.player.kill()
            self.play_time = self.timer.current()
            self.deaths += 1
            game.game_over_menu()

        if self.player.rect.bottom >= self.spikes4.rect.top and self.player.rect.right >= self.spikes4.rect.left and self.player.rect.left <= self.spikes4.rect.right:
            self.hit_sound.play()
            self.player.kill()
            self.play_time = self.timer.current()
            self.deaths += 1
            game.game_over_menu()

        if self.player.rect.bottom >= self.spikes5.rect.top and self.player.rect.right >= self.spikes5.rect.left and self.player.rect.left <= self.spikes5.rect.right:
            self.hit_sound.play()
            self.player.kill()
            self.play_time = self.timer.current()
            self.deaths += 1
            game.game_over_menu()

        if self.player.rect.bottom >= self.spikes6.rect.top and self.player.rect.right >= self.spikes6.rect.left and \
                self.player.rect.left <= self.spikes6.rect.right and self.player.rect.top <= self.spikes6.rect.bottom:
            self.hit_sound.play()
            self.player.kill()
            self.play_time = self.timer.current()
            self.deaths += 1
            game.game_over_menu()

        if self.player.rect.bottom >= self.spikes7.rect.top and self.player.rect.right >= self.spikes7.rect.left and \
                self.player.rect.left <= self.spikes7.rect.right and self.player.rect.top <= self.spikes7.rect.bottom:
            self.hit_sound.play()
            self.player.kill()
            self.play_time = self.timer.current()
            self.deaths += 1
            game.game_over_menu()


        # go to level 2 when flag touched
        if self.player.rect.right >= self.KONIEC.rect.left and self.player.rect.bottom >= self.KONIEC.rect.top and \
                self.player.rect.left <= self.KONIEC.rect.right and self.player.rect.top <= self.KONIEC.rect.bottom:
            self.player.rect.right = 200
            self.player.rect.bottom = SCREEN_HEIGHT - 50

            # deleting level 1 platforms
            self.all_sprites.remove(self.KONIEC, self.KONIEC1, self.spikes1, self.spikes2, self.spikes3, self.platform44, self.left_wall,
                             self.right_wall, self.platform1, self.platform2, self.platform3, self.platform4,
                             self.platform6, self.platform7, self.platform8, self.platform9, self.platform10, self.platform11, self.platform12,
                             self.platform13, self.platform14, self.platform15, self.platform_end, self.platform5,
                             self.ground, self.ground1, self.ground2, self.ground3, self.golden_point1, self.golden_point2,
                             self.golden_point3, self.golden_point4, self.golden_point5, self.golden_point6,
                             self.golden_point7, self.golden_point8, self.silver_point1, self.silver_point2, self.cookie1)
            self.platforms.remove(self.KONIEC, self.KONIEC1, self.spikes1, self.spikes2, self.spikes3, self.platform44, self.left_wall, self.right_wall,
                           self.platform1, self.platform2, self.platform3, self.platform4, self.platform6,
                           self.platform7, self.platform8, self.platform9, self.platform10, self.platform11, self.platform12,
                           self.platform13, self.platform14, self.platform15, self.platform_end, self.platform5,
                           self.ground, self.ground1, self.ground2, self.ground3)
            self.points_list.remove(self.golden_point1, self.golden_point2, self.golden_point3, self.golden_point4,
                             self.golden_point5, self.golden_point6, self.golden_point7, self.golden_point8, self.silver_point1,
                             self.silver_point2)
            self.boosts_list.remove(self.cookie1)

            # level1 completed
            self.screen.fill(BLACK)
            self.message_to_screen("CONGRATULATIONS", RED, -100, "large")
            self.message_to_screen("You have completed level 1", RED, 0, "med")
            self.message_to_screen("Your score was: {} points ".format(self.point_counter), RED, 100, "med")
            pygame.display.update()

            pygame.time.wait(2000)

            # level2
            self.level2()

        # level2 completed
        if self.player.rect.right >= self.KONIEC1.rect.left and self.player.rect.bottom >= self.KONIEC1.rect.top and \
                self.player.rect.left <= self.KONIEC1.rect.right and self.player.rect.top <= self.KONIEC1.rect.bottom:
            self.play_time = self.timer.current()
            self.screen.fill(BLACK)
            self.message_to_screen("CONGRATULATIONS", RED, -150, "large")
            self.message_to_screen("You have completed level 2", RED, -50, "med")
            self.message_to_screen("Your final score was: {} points ".format(self.point_counter), RED, 50, "med")
            self.message_to_screen("You've died {} times ".format(self.deaths), RED, 100, "med")
            self.message_to_screen("Your time {} s. ".format(self.play_time), RED, 150, "med")
            self.message_to_screen("THANK YOU FOR PLAYING!!!", RED, 250, "med")
            pygame.display.update()

            pygame.time.wait(10000)

            self.playing = False
            self.running = False
            pygame.quit()
            quit()

    # in-game events
    def handle_events(self):

        for event in pygame.event.get():
            # when user clicks x button, quit
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                pygame.quit()
                quit()

            # keyboard events
            if event.type == pygame.KEYDOWN:

                # player movement events
                if event.key == pygame.K_SPACE:
                    self.player.jump()
                if event.key == pygame.K_a:
                    self.player.left()
                if event.key == pygame.K_d:
                    self.player.right()

                # coordinates display
                if event.key == pygame.K_k:
                    if self.devs:
                        self.devs = False
                    elif not self.devs:
                        self.devs = True

                # exit when esc clicked
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    pygame.quit()
                    quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and self.player.velocity.x < 0:
                    self.player.stop()
                if event.key == pygame.K_d and self.player.velocity.x > 0:
                    self.player.stop()

    # drawing sprites
    def draw(self):

        # drawing sprites group
        self.all_sprites.draw(self.screen)

        # text with your points
        self.backg = pygame.Surface((190, 90))
        self.backg.fill((128, 128, 128))
        self.backg.set_alpha(100)
        self.screen.blit(self.backg, (SCREEN_WIDTH - 220, 20))

        self.screen.blit(smallfont.render('Your points: {0}'.format(self.point_counter), True, WHITE), (SCREEN_WIDTH - 210, 30))
        self.screen.blit(smallfont.render('Your deaths: {0}'.format(self.deaths), True, WHITE), (SCREEN_WIDTH - 210, 60))
        self.screen.blit(smallfont.render('Your time: {0}'.format(self.timer.current()), True, WHITE),(SCREEN_WIDTH - 210, 90))

        # updates contents of the screen
        pygame.display.update()

    def level1(self):

        self.KONIEC = EndPlatform(2000, 50)
        self.KONIEC1 = EndPlatform(3000, SCREEN_HEIGHT - 332)

        self.left_wall = Platform(-16, 0, 'sciana.png')
        self.right_wall = Platform(2087, 0, 'sciana.png')

        self.ground = Platform(-16, SCREEN_HEIGHT - 32, 'podloga.png')
        self.ground1 = Platform(580, SCREEN_HEIGHT - 32, 'podloga.png')
        self.ground2 = Platform(1000, SCREEN_HEIGHT - 32, 'podloga.png')
        self.ground3 = Platform(1500, SCREEN_HEIGHT - 32, 'podloga.png')

        # section1
        self.platform1 = Platform(400, SCREEN_HEIGHT - 100, 'sciana.png')
        self.platform2 = Platform(550, SCREEN_HEIGHT - 140, 'sciana.png')
        self.platform3 = Platform(700, SCREEN_HEIGHT - 180, 'sciana.png')
        self.platform4 = Platform(950, SCREEN_HEIGHT - 220, 'hor_platform.png')
        self.platform44 = Platform(0, SCREEN_HEIGHT - 450, 'hor_platform.png')
        self.spikes1 = Spikes(430, SCREEN_HEIGHT - 64, 'spikes.png')

        # section2
        self.platform6 = Platform(750, SCREEN_HEIGHT - 400, 'hor_platform.png')
        self.platform7 = Platform(1050, SCREEN_HEIGHT - 300, 'hor_platform.png')
        self.platform8 = Platform(500, SCREEN_HEIGHT - 400, 'hor_platform.png')
        self.platform9 = Platform(400, SCREEN_HEIGHT - 400, 'hor_platform.png')
        self.platform12 = Platform(650, 70, 'hor_platform.png')
        self.platform10 = Platform(800, 70, 'hor_platform.png')
        self.platform11 = Platform(950, 70, 'hor_platform.png')
        self.platform5 = Platform(1100, 70, 'sciana.png')

        # section3
        self.platform13 = Platform(1500, SCREEN_HEIGHT - 300, 'hor_platform.png')
        self.platform14 = Platform(1300, -150, 'sciana.png')
        self.platform15 = Platform(1300, SCREEN_HEIGHT - 150, 'hor_platform.png')
        self.spikes2 = Spikes(1830, SCREEN_HEIGHT - 64, 'spikes_short.png')
        self.spikes3 = Spikes(1959, SCREEN_HEIGHT - 64, 'spikes_short.png')
        self.spikes4 = Spikes(1959, SCREEN_HEIGHT - 64, 'spikes_short.png')
        self.spikes5 = Spikes(1959, SCREEN_HEIGHT - 64, 'spikes_short.png')
        self.spikes6 = Spikes(1959, SCREEN_HEIGHT - 64, 'spikes_short.png')
        self.spikes7 = Spikes(1959, SCREEN_HEIGHT - 64, 'spikes_short.png')

        # koncowa platforma
        self.platform_end = Platform(1900, 264, 'hor_platform.png')

        self.golden_point1 = GoldPoints(300, SCREEN_HEIGHT - 160)
        self.golden_point2 = GoldPoints(50, SCREEN_HEIGHT - 500)
        self.golden_point3 = GoldPoints(1050, SCREEN_HEIGHT - 60)
        self.golden_point4 = GoldPoints(1150, SCREEN_HEIGHT - 60)
        self.golden_point5 = GoldPoints(1860, SCREEN_HEIGHT - 108)
        self.golden_point6 = GoldPoints(1890, SCREEN_HEIGHT - 108)
        self.golden_point7 = GoldPoints(1920, SCREEN_HEIGHT - 108)
        self.golden_point8 = GoldPoints(1950, SCREEN_HEIGHT - 108)
        self.silver_point1 = SilverPoints(250, SCREEN_HEIGHT - 180)
        self.silver_point2 = SilverPoints(1050, SCREEN_HEIGHT - 400)

        self.cookie1 = BoostPoint(1800, SCREEN_HEIGHT - 150)

        self.all_sprites.add(self.KONIEC, self.spikes1, self.spikes2, self.spikes3,
                             self.platform44, self.left_wall, self.right_wall,
                             self.platform1, self.platform2, self.platform3, self.platform4,
                             self.platform6, self.platform7, self.platform8, self.platform9, self.platform10,
                             self.platform11, self.platform12, self.platform13, self.platform14, self.platform15,
                             self.platform_end, self.platform5,
                             self.ground, self.ground1, self.ground2, self.ground3,
                             self.golden_point1, self.golden_point2, self.golden_point3, self.golden_point4,
                             self.golden_point5, self.golden_point6, self.golden_point7, self.golden_point8,
                             self.silver_point1, self.silver_point2,
                             self.cookie1)
        self.platforms.add(self.KONIEC, self.spikes1, self.spikes2, self.spikes3,
                           self.platform44, self.left_wall, self.right_wall,
                           self.platform1, self.platform2, self.platform3, self.platform4, self.platform6,
                           self.platform7, self.platform8, self.platform9, self.platform10, self.platform11, self.platform12,
                           self.platform13, self.platform14, self.platform15, self.platform_end, self.platform5,
                           self.ground, self.ground1, self.ground2, self.ground3)
        self.points_list.add(self.golden_point1, self.golden_point2, self.golden_point3, self.golden_point4,
                             self.golden_point5, self.golden_point6, self.golden_point7, self.golden_point8,
                             self.silver_point1, self.silver_point2)
        self.boosts_list.add(self.cookie1)

    def level2(self):

        self.KONIEC1 = EndPlatform(1500, SCREEN_HEIGHT - 332)

        # create new level
        self.left_wall = Platform(-16, 0, 'sciana.png')
        self.right_wall = Platform(1590, 0, 'sciana.png')

        self.ground = Platform(-16, SCREEN_HEIGHT - 32, 'podloga.png')
        self.ground1 = Platform(580, SCREEN_HEIGHT - 32, 'podloga.png')
        self.ground2 = Platform(1000, SCREEN_HEIGHT - 32, 'podloga.png')

        self.spikes1 = Spikes(0, SCREEN_HEIGHT - 64, 'spikes_short.png')
        self.spikes2 = Spikes(410, SCREEN_HEIGHT - 64, 'spikes_short.png')
        self.spikes3 = Spikes(700, SCREEN_HEIGHT - 64, 'spikes_short.png')
        self.spikes4 = Spikes(900, SCREEN_HEIGHT - 64, 'spikes_short.png')
        self.spikes5 = Spikes(1100, SCREEN_HEIGHT - 64, 'spikes_short.png')
        self.spikes6 = Spikes(800, SCREEN_HEIGHT - 332, 'spikes_short.png')
        self.spikes7 = Spikes(925, SCREEN_HEIGHT - 332, 'spikes_short.png')

        self.platform20 = Platform(120, SCREEN_HEIGHT - 172, 'hor_platform.png')
        self.platform21 = Platform(120, SCREEN_HEIGHT - 312, 'hor_platform.png')
        self.platform22 = Platform(260, SCREEN_HEIGHT - 312, 'hor_platform.png')
        self.platform23 = Platform(230, SCREEN_HEIGHT - 455, 'hor_platform.png')
        self.platform24 = Platform(0, SCREEN_HEIGHT - 455, 'hor_platform_short.png')
        self.platform25 = Platform(580, SCREEN_HEIGHT - 300, 'hor_platform.png')
        self.platform26 = Platform(740, SCREEN_HEIGHT - 300, 'hor_platform.png')
        self.platform27 = Platform(900, SCREEN_HEIGHT - 300, 'hor_platform.png')
        self.platform28 = Platform(1060, SCREEN_HEIGHT - 300, 'hor_platform.png')
        self.platform29 = Platform(1432, SCREEN_HEIGHT - 300, 'hor_platform.png')

        self.wall1 = Platform(400, SCREEN_HEIGHT - 312, 'sciana_mala.png')
        self.wall2 = Platform(400, SCREEN_HEIGHT - 140, 'sciana_mala.png')
        self.wall3 = Platform(230, SCREEN_HEIGHT - 455, 'sciana_mala.png')
        self.wall4 = Platform(580, SCREEN_HEIGHT - 300, 'sciana_mala.png')
        self.wall5 = Platform(580, SCREEN_HEIGHT - 900, 'sciana.png')
        self.wall6 = Platform(1400, SCREEN_HEIGHT - 300, 'sciana_mala.png')
        self.wall7 = Platform(1400, SCREEN_HEIGHT - 140, 'sciana_mala.png')

        self.silver_point1 = SilverPoints(140, SCREEN_HEIGHT - 200)
        self.silver_point2 = SilverPoints(270, SCREEN_HEIGHT - 350)
        self.silver_point3 = SilverPoints(270, SCREEN_HEIGHT - 380)
        self.silver_point4 = SilverPoints(740, SCREEN_HEIGHT - 180)
        self.silver_point5 = SilverPoints(940, SCREEN_HEIGHT - 180)
        self.silver_point6 = SilverPoints(1140, SCREEN_HEIGHT - 180)

        self.golden_point1 = GoldPoints(40, SCREEN_HEIGHT - 483)
        self.golden_point2 = GoldPoints(40, SCREEN_HEIGHT - 90)
        self.golden_point3 = GoldPoints(630, SCREEN_HEIGHT - 332)
        self.golden_point4 = GoldPoints(670, SCREEN_HEIGHT - 332)

        self.cookie1 = BoostPoint(1350, SCREEN_HEIGHT - 200)

        self.all_sprites.add(self.spikes1, self.spikes2, self.spikes3, self.spikes4, self.spikes5, self.spikes6,
                             self.spikes7,
                             self.platform20, self.wall3, self.platform21, self.platform22, self.platform23,
                             self.platform24, self.platform25, self.platform26, self.platform27, self.platform28,
                             self.platform29,
                             self.silver_point1, self.silver_point2, self.silver_point3, self.silver_point4,
                             self.silver_point5, self.silver_point6,
                             self.golden_point1, self.golden_point2, self.golden_point3, self.golden_point4,
                             self.cookie1,
                             self.left_wall, self.wall1, self.wall2, self.wall4, self.wall5, self.wall6,
                             self.wall7, self.ground, self.ground1, self.ground2, self.KONIEC1, self.right_wall)
        self.platforms.add(self.spikes1, self.spikes2, self.spikes3, self.spikes4, self.spikes5, self.spikes6,
                           self.spikes7,
                           self.platform20, self.wall3, self.platform21, self.platform22, self.platform23,
                           self.platform24, self.platform25, self.platform26, self.platform27, self.platform28,
                           self.platform29,
                           self.left_wall, self.wall1, self.wall2, self.wall4, self.wall5, self.wall6,
                           self.wall7, self.ground, self.ground1, self.ground2, self.KONIEC1, self.right_wall)
        self.points_list.add(self.silver_point1, self.silver_point2, self.silver_point3, self.silver_point4,
                             self.silver_point5, self.silver_point6,
                             self.golden_point1, self.golden_point2, self.golden_point3, self.golden_point4,)
        self.boosts_list.add(self.cookie1)

    # start game screen
    def new_game_menu(self, new_game=True):

        while new_game:
            # game exit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    self.running = False
                    pygame.quit()
                    quit()

            self.screen.fill(BLACK)

            # displays text to screen
            self.message_to_screen("VIGILANT PANCAKE", RED, -100, "large")
            self.message_to_screen("Move and jump on platforms", RED, -30, "small")

            # dummy buttons
            self.dummybutton("PLAY", 200, 500, 100, 50, RED)
            self.dummybutton("CONTROLS", 550, 500, 100, 50, RED)
            self.dummybutton("QUIT", 900, 500, 100, 50, RED)

            # buttons
            self.button("PLAY", 200, 500, 100, 50, RED, LIGHT_RED, action="play")
            self.button("CONTROLS", 550, 500, 100, 50, RED, LIGHT_RED, action="controls")
            self.button("QUIT", 900, 500, 100, 50, RED, LIGHT_RED, action="quit")

            pygame.display.update()
            self.clock.tick(FPS)

    # controls menu
    def controls_menu(self, gcont=True):

        while gcont:
            # game exit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    self.running = False
                    pygame.quit()
                    quit()

            self.screen.fill(BLACK)
            self.message_to_screen("How to play?", RED, -100, "large")
            self.message_to_screen("Move left: 'A'  Move Right: 'D'  Jump: 'Space'", RED, -30, "small")
            self.message_to_screen("Golden coins give you 5 points", RED, -10, "small")
            self.message_to_screen("Silver coins give you 1 point", RED, 10, "small")
            self.message_to_screen("Cookies give you jump boost", RED, 30, "small")

            # dummy buttons
            self.dummybutton("PLAY", 200, 500, 100, 50, RED)
            self.dummybutton("MENU", 550, 500, 100, 50, RED)
            self.dummybutton("QUIT", 900, 500, 100, 50, RED)

            # buttons
            self.button("PLAY", 200, 500, 100, 50, RED, LIGHT_RED, action="play")
            self.button("MENU", 550, 500, 100, 50, RED, LIGHT_RED, action="main")
            self.button("QUIT", 900, 500, 100, 50, RED, LIGHT_RED, action="quit")

            pygame.display.update()
            self.clock.tick(FPS)

    # end game menu
    def game_over_menu(self, dead=True):

        while dead:
            # game exit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    self.running = False
                    pygame.quit()
                    quit()

            self.screen.fill(BLACK)
            self.message_to_screen("YOU DIED", RED, -100, "large")

            # dummy buttons
            self.dummybutton("TRY AGAIN", 300, 400, 200, 120, RED)
            self.dummybutton("QUIT", 700, 400, 200, 120, RED)

            # buttons
            self.button("TRY AGAIN", 300, 400, 200, 120, RED, LIGHT_RED, action="main")
            self.button("QUIT", 700, 400, 200, 120, RED, LIGHT_RED, action="quit")

            pygame.display.update()
            self.clock.tick(FPS)

    # button method
    def button(self, text, x, y, width, height, inactive_color, active_color, action=None):
        # current position of mouse cursor
        cur = pygame.mouse.get_pos()
        # when user clicks
        click = pygame.mouse.get_pressed()

        # when user hovers over button, it changes color
        if x + width > cur[0] > x and y + height > cur[1] > y:
            pygame.draw.rect(self.screen, active_color, (x, y, width, height))
        else:
            pygame.draw.rect(self.screen, inactive_color, (x, y, width, height))

        self.text_to_button(text, WHITE, x, y, width, height)

        if click[0] == 1 and x + width > cur[0] > x and y + height > cur[1] > y:
            while x + width > cur[0] > x and y + height > cur[1] > y:
                pygame.draw.rect(self.screen, active_color, (x, y, width, height))
                self.text_to_button(text, WHITE, x, y, width, height)
                pygame.display.update()
                cur = pygame.mouse.get_pos()

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        if action == "quit":
                            pygame.quit()
                            quit()
                        # takes you to controls menu
                        elif action == "controls":
                            self.controls_menu()
                        # starts game and ends game intro
                        elif action == "play":
                            self.new_game()              
                        # takes you to main menu
                        elif action == "main":
                            self.new_game_menu()

    # button helping not to crash when clicking buttons
    def dummybutton(self, text, x, y, width, height, inactive_color):
        pygame.draw.rect(self.screen, inactive_color, (x, y, width, height))
        self.text_to_button(text, WHITE, x, y, width, height)

    # defining text size function
    def text_objects(self, text, color, size):
        global textSurface
        if size == "small":
            textSurface = smallfont.render(text, True, color)
        elif size == "med":
            textSurface = medfont.render(text, True, color)
        elif size == "large":
            textSurface = largefont.render(text, True, color)

        return textSurface, textSurface.get_rect()

    # printing text to button function
    def text_to_button(self, msg, color, buttonx, buttony, buttonwidth, buttonheight, size="small"):
        textSurf, textRect = self.text_objects(msg, color, size)
        textRect.center = ((buttonx + (buttonwidth / 2)), (buttony + 10 + (buttonheight / 2)))
        self.screen.blit(textSurf, textRect)

    # displaying text to the center of screen
    def message_to_screen(self, msg, color, y_displace=0, size="small"):
        textSurf, textRect = self.text_objects(msg, color, size)
        textRect.center = (SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2 + y_displace)
        self.screen.blit(textSurf, textRect)

    # developer tools
    def write(self, x, y):
        self.screen.blit(smallfont.render('velocity x: {0}'.format(self.player.velocity.x), True, WHITE), (x, y))
        self.screen.blit(smallfont.render('velocity y: {0}'.format(self.player.velocity.y), True, WHITE), (x, y + 15))
        self.screen.blit(smallfont.render('position x: {0}'.format(self.player.rect.x), True, WHITE), (x, y + 30))
        self.screen.blit(smallfont.render('position y: {0}'.format(self.player.rect.y), True, WHITE), (x, y + 45))


# --- CREATE GAME OBJECT ---
game = Game()

# --- GAME LOOP ---
while game.running:
    game.new_game_menu()
    game.game_over_menu()

pygame.quit()
