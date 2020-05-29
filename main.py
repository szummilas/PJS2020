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

        self.player = PlayerClass(self)

    # start new game
    def new_game(self):

        # tutaj nie mam pojecia czemu podkresla self ¯\_(ツ)_/¯
        # self.level = Level.__init__(self, self.player)
        # grouping all sprites
        self.all_sprites = pygame.sprite.Group()
        # platforms group
        self.platforms = pygame.sprite.Group()
        # adding player to sprite group
        self.all_sprites.add(self.player)

        self.level1()

        self.run_game()

    # main game loop
    def run_game(self):

        self.playing = True

        while self.playing:
            # in-game frames per second
            self.clock.tick(FPS)

            # running all game functions
            self.handle_events()
            self.update()
            self.draw()

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

        if self.player.rect.left <= 200 and self.player.velocity.x < 0:
            self.player.rect.left = 200
            for plat in self.platforms:
                plat.rect.x += abs(self.player.velocity.x)



        # collision with spikes and player's death
        if self.player.rect.bottom >= self.spikes1.rect.top and self.player.rect.right >= self.spikes1.rect.left and self.player.rect.right <= self.spikes1.rect.right:
            self.player.kill()
            game.game_over_menu()



        # jak to na górze zloopować żeby zaczęło od nowa??



        # go to level 2 when flag touched
        if self.player.rect.right >= self.KONIEC.rect.left and self.player.rect.bottom <= self.KONIEC.rect.bottom:
            self.player.rect.right = 200
            self.player.rect.bottom = SCREEN_HEIGHT - 50

            # deleting level 1 platforms
            self.all_sprites.remove(self.ground, self.ground1, self.ground2, self.left_wall, self.KONIEC, self.platform1,
                                    self.platform1, self.platform2, self.platform3, self.platform4, self.platform5,
                                    self.platform6, self.platform7, self.platform8, self.platform9, self.platform10,
                                    self.platform11, self.platform12, self.platform13, self.platform14, self.platform15,
                                    self.platform_end, self.spikes1)
            self.platforms.remove(self.ground, self.ground1, self.ground2, self.left_wall, self.KONIEC, self.platform1,
                                    self.platform2, self.platform3, self.platform4, self.platform5, self.platform6,
                                    self.platform7, self.platform8, self.platform9, self.platform10, self.platform11,
                                    self.platform12, self.platform13, self.platform14, self.platform15, self.platform_end,
                                    self.spikes1)

            self.level2()

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

        # updates contents of the screen
        pygame.display.update()

    def level1(self):

        self.KONIEC = EndPlatform(1900, 200, 'flag.png')

        self.left_wall = Platform(-16, 0, 'sciana.png')

        self.ground = Platform(-16, SCREEN_HEIGHT - 32, 'podloga.png')
        self.ground1 = Platform(580, SCREEN_HEIGHT - 32, 'podloga.png')
        self.ground2 = Platform(1000, SCREEN_HEIGHT - 32, 'podloga.png')
        self.ground3 = Platform(1500, SCREEN_HEIGHT - 32, 'podloga.png')

        # section1
        self.platform1 = Platform(400, SCREEN_HEIGHT - 100, 'sciana.png')
        self.platform2 = Platform(550, SCREEN_HEIGHT - 140, 'sciana.png')
        self.platform3 = Platform(700, SCREEN_HEIGHT - 180, 'sciana.png')
        self.platform4 = Platform(950, SCREEN_HEIGHT - 220, 'hor_platform.png')
        self.spikes1 = Spikes(430, SCREEN_HEIGHT - 65, 'spikes.png')

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

        # koncowa platforma
        self.platform_end = Platform(1800, 232, 'hor_platform.png')

        self.all_sprites.add(self.KONIEC, self.spikes1, self.left_wall, self.platform1,
                             self.platform2, self.platform3, self.platform4, self.platform6,
                             self.platform7, self.platform8, self.platform9,
                             self.platform10, self.platform11, self.platform12,
                             self.platform13, self.platform14, self.platform15, self.platform_end, self.platform5,
                             self.ground, self.ground1, self.ground2, self.ground3)
        self.platforms.add(self.KONIEC, self.spikes1, self.left_wall, self.platform1,
                           self.platform2, self.platform3, self.platform4, self.platform6,
                           self.platform7, self.platform8, self.platform9,
                           self.platform10, self.platform11, self.platform12,
                           self.platform13, self.platform14, self.platform15, self.platform_end, self.platform5,
                           self.ground, self.ground1, self.ground2, self.ground3)

    def level2(self):

        # create new level
        self.left_wall = Platform(-16, 0, 'sciana.png')
        self.ground = Platform(-16, SCREEN_HEIGHT - 32, 'podloga.png')
        self.ground1 = Platform(580, SCREEN_HEIGHT - 32, 'podloga.png')

        self.all_sprites.add(self.ground, self.ground1, self.left_wall)
        self.platforms.add(self.ground, self.ground1, self.left_wall)

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
            self.message_to_screen("Progress: 28.05.2020", RED, -100, "large")
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
            self.message_to_screen("Controls", RED, -100, "large")
            self.message_to_screen("Move left: 'A'  Move Right: 'D'  Jump: 'Space'", RED, -30, "small")

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
            self.button("TRY AGAIN", 300, 400, 200, 120, RED, LIGHT_RED, action="play")
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
