from settings import *


class PlayerClass(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('sprites', 'playersprite1.png')).convert()
        self.rect = self.image.get_rect()

        self.movex = 0
        self.movey = 0

        self.level = None

    def update(self):

        self.calc_gravity()

        self.rect.x += self.movex

        # checking horizontal collision
        plat_hit_list = pygame.sprite.spritecollide(self, self.level.platforms, False)
        for block in plat_hit_list:
            if self.movex > 0:
                self.rect.right = block.rect.left
            elif self.movex < 0:
                self.rect.left = block.rect.right

        self.rect.y += self.movey

        # checking vertical collision
        plat_hit_list = pygame.sprite.spritecollide(self, self.level.platforms, False)
        for block in plat_hit_list:
            if self.movey > 0:
                self.rect.bottom = block.rect.top
            elif self.movey < 0:
                self.rect.top = block.rect.bottom
                self.movey += 0.5

    # method to apply gravity
    def calc_gravity(self):
        if self.movey == 0:
            self.movey = 1
        else:
            self.movey += .35

        # checking collision with ground
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.movey >= 0:
            self.movey = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    # jumping method
    def jump(self):
        self.rect.y += 2
        plat_hit_list = pygame.sprite.spritecollide(self, self.level.platforms, False)
        self.rect.y -= 2

        if len(plat_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.movey = -10

    # movement methods
    def go_left(self):
        self.movex = -6

    def go_right(self):
        self.movex = 6

    def stop(self):
        self.movex = 0


class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(RED) 
        self.rect = self.image.get_rect()


class Level(object):
    def __init__(self, player):
        self.platforms = pygame.sprite.Group()
        self.player = player

    def update(self):
        self.platforms.update()

    def draw(self, screen):
        screen.fill(BLACK)

        self.platforms.draw(screen)


class Level_1(Level):
    def __init__(self, player):
        Level.__init__(self, player)

        # array to specify platform positions on a level
        level = [[210, 70, 500, 500],
                 [210, 70, 200, 400],
                 [210, 70, 600, 300],
                 [SCREEN_WIDTH, 70, 0, SCREEN_HEIGHT - 40],
                 ]

        # iterating over platforms defined in level and adding them to platforms group
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platforms.add(block)
