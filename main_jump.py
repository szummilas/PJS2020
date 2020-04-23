from sprites_jump import *


# main game class
class Game:
    def __init__(self):
        # initializing pygame
        pygame.init()
        # initializing game display
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        # game title
        pygame.display.set_caption(game_title)
        # counting time
        self.clock = pygame.time.Clock()
        # is game running
        self.running = True

    # start new game
    def newgame(self):
        # grouping all sprites
        self.all_sprites = pygame.sprite.Group()
        # plarforms group
        self.platforms = pygame.sprite.Group()
        # creating player object and adding to sprite group
        self.player = PlayerClass(self)
        self.all_sprites.add(self.player)

        # creating platform objects and adding them to sprite groups
        p1 = PlatformClass(300, screen_height - 20, 0, 0)
        p2 = PlatformClass(0, screen_height - 20, 0, 0)
        self.p3 = PlatformClass(350, screen_height - 150, 0, 0)
        self.all_sprites.add(p1, p2, self.p3)
        self.platforms.add(p1, p2, self.p3)

        self.rungame()

    # main game loop
    def rungame(self):
        self.playing = True

        while self.playing:
            # in-game frames per second
            self.clock.tick(fps)

            # running all game functions
            self.eventsgame()
            self.updategame()
            self.drawgame()

    # updating game state
    def updategame(self):
        self.all_sprites.update()

        if self.player.vel.y > 0:
            # checking for player and platform collisions
            collisions = pygame.sprite.spritecollide(self.player, self.platforms, False)
            if collisions:

                self.player.pos.y = collisions[0].rect.top
                self.player.vel.y = 0

# tu coś nie działaaaaaaa
                if self.player.rect.collidepoint(self.player.rect.midtop) == collisions[0].rect.bottom:
                    print("dupa")
                    self.player.vel.y = 0


    # in-game events
    def eventsgame(self):
        for event in pygame.event.get():
            # when user clicks x button, quit
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                pygame.quit()
                quit()
            # # jump when space pressed
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE:
            #         self.player.isJump(True)

# flip sprite do ogarnięcia
#                 if event.key == pygame.K_d:
#                     self.player.image = self.player.image
#                 if event.key == pygame.K_a:
#                     self.player.image = self.player.image_l

    # drawing objects
    def drawgame(self):
        # background color of the window
        self.screen.fill(black)
        # drawing sprites group
        self.all_sprites.draw(self.screen)
        # updates contents of the screen
        pygame.display.update()

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

            self.screen.fill(black)

            # displays text to screen
            self.message_to_screen("Progress: 24.04.2020", red, -100, "large")
            self.message_to_screen("Move and jump on platforms", red, -30, "small")

            # dummy buttons
            self.dummybutton("Play", 200, 500, 100, 50, red)
            self.dummybutton("Controls", 550, 500, 100, 50, red)
            self.dummybutton("Quit", 900, 500, 100, 50, red)

            # buttons
            self.button("Play", 200, 500, 100, 50, red, light_red, action="play")
            self.button("Controls", 550, 500, 100, 50, red, light_red, action="controls")
            self.button("Quit", 900, 500, 100, 50, red, light_red, action="quit")

            pygame.display.update()
            self.clock.tick(fps)

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

            self.screen.fill(black)
            self.message_to_screen("Controls", red, -100, "large")
            self.message_to_screen("Move left: 'A'  Move Right: 'D'  Jump: 'Space'", red, -30, "small")

            # dummy buttons
            self.dummybutton("Play", 200, 500, 100, 50, red)
            self.dummybutton("Menu", 550, 500, 100, 50, red)
            self.dummybutton("Quit", 900, 500, 100, 50, red)

            # buttons
            self.button("Play", 200, 500, 100, 50, red, light_red, action="play")
            self.button("Menu", 550, 500, 100, 50, red, light_red, action="main")
            self.button("Quit", 900, 500, 100, 50, red, light_red, action="quit")

            pygame.display.update()
            self.clock.tick(fps)

    # end game menu
    def over_game_menu(self):
        pass

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

        self.text_to_button(text, white, x, y, width, height)

        if click[0] == 1 and x + width > cur[0] > x and y + height > cur[1] > y:
            while x + width > cur[0] > x and y + height > cur[1] > y:
                pygame.draw.rect(self.screen, active_color, (x, y, width, height))
                self.text_to_button(text, white, x, y, width, height)
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
                            self.newgame()
                        # takes you to main menu
                        elif action == "main":
                            self.new_game_menu()

    # button helping not to crash when clicking buttons
    def dummybutton(self, text, x, y, width, height, inactive_color):
        pygame.draw.rect(self.screen, inactive_color, (x, y, width, height))
        self.text_to_button(text, black, x, y, width, height)

    # defining text size function
    def text_objects(self, text, color, size):
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
        textRect.center = (screen_width / 2), (screen_height / 2 + y_displace)
        self.screen.blit(textSurf, textRect)


# creating game object
game = Game()

# game loop
while game.running:
    game.new_game_menu()

    game.over_game_menu()

pygame.quit()
