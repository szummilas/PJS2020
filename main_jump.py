from sprites_jump import *


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

        self.player = PlayerClass(self)

    # start new game
    def new_game(self):

        # tutaj nie mam pojecia czemu podkresla self ¯\_(ツ)_/¯
        self.level = Level.__init__(self, self.player)
        # grouping all sprites
        self.all_sprites = pygame.sprite.Group()
        # plarforms group
        self.platforms = pygame.sprite.Group()
        # creating player object and adding to sprite group

        self.all_sprites.add(self.player)

        # creating platform objects and adding them to sprite groups
        self.left_wall = Platform(-250, 0, 270, SCREEN_HEIGHT)
        self.ground = Platform(0, SCREEN_HEIGHT - 20, 2000, 20)
        self.test_platform = Platform(350, SCREEN_HEIGHT - 150, 150, 60)
        self.test_platform1 = Platform(600, SCREEN_HEIGHT - 40, 30, 40)
        self.all_sprites.add(self.ground, self.left_wall, self.test_platform, self.test_platform1)
        self.platforms.add(self.ground, self.left_wall, self.test_platform, self.test_platform1)

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
        self.all_sprites.update()

        # PRZESUWANIE SIE PLANSZY
        if self.player.rect.right >= SCREEN_WIDTH - 200 and self.player.velocity.x > 0:
            self.player.rect.right = SCREEN_WIDTH - 200
            for plat in self.platforms:
                plat.rect.x -= abs(self.player.velocity.x)

        if self.player.rect.left <= 200 and self.player.velocity.x < 0:
            self.player.rect.left = 200
            for plat in self.platforms:
                plat.rect.x += abs(self.player.velocity.x)


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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()
                if event.key == pygame.K_a:
                    self.player.left()
                if event.key == pygame.K_d:
                    self.player.right()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and self.player.velocity.x < 0:
                    self.player.stop()
                if event.key == pygame.K_d and self.player.velocity.x > 0:
                    self.player.stop()

    # drawing objects
    def draw(self):
        # # background color of the window
        # self.screen.fill(BLACK)
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

            self.screen.fill(BLACK)

            # displays text to screen
            self.message_to_screen("Progress: 12.05.2020", RED, -100, "large")
            self.message_to_screen("Move and jump on platforms", RED, -30, "small")

            # dummy buttons
            self.dummybutton("Play", 200, 500, 100, 50, RED)
            self.dummybutton("Controls", 550, 500, 100, 50, RED)
            self.dummybutton("Quit", 900, 500, 100, 50, RED)

            # buttons
            self.button("Play", 200, 500, 100, 50, RED, LIGHT_RED, action="play")
            self.button("Controls", 550, 500, 100, 50, RED, LIGHT_RED, action="controls")
            self.button("Quit", 900, 500, 100, 50, RED, LIGHT_RED, action="quit")

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
            self.dummybutton("Play", 200, 500, 100, 50, RED)
            self.dummybutton("Menu", 550, 500, 100, 50, RED)
            self.dummybutton("Quit", 900, 500, 100, 50, RED)

            # buttons
            self.button("Play", 200, 500, 100, 50, RED, LIGHT_RED, action="play")
            self.button("Menu", 550, 500, 100, 50, RED, LIGHT_RED, action="main")
            self.button("Quit", 900, 500, 100, 50, RED, LIGHT_RED, action="quit")

            pygame.display.update()
            self.clock.tick(FPS)

    # end game menu
    def game_over_menu(self):
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
        self.text_to_button(text, BLACK, x, y, width, height)

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
    def message_to_screen(self, msg, color, y_displace = 0, size="small"):
        textSurf, textRect = self.text_objects(msg, color, size)
        textRect.center = (SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2 + y_displace)
        self.screen.blit(textSurf, textRect)


# --- LEVEL ---
class Level(Game):

    # 'player' refers to object created in class Game
    def __init__(self, player):
        Game.__init__(self)
        self.platform_list = pygame.sprite.Group()
        self.player = player

    def update(self):
        self.platform_list.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.platform_list.draw(self.screen)


class Level01(Level):

    def __init__(self, player):
        Level.__init__(self, player)



# --- CREATE GAME OBJECT ---
game = Game()

# --- GAME LOOP ---
while game.running:
    game.new_game_menu()
    game.game_over_menu()

pygame.quit()
