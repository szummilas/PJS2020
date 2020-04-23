import os
from settings import *
vec = pygame.math.Vector2


class PlayerClass(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.image.load(os.path.join('sprites', 'playersprite1.png')).convert()
        self.image_l = pygame.transform.flip(pygame.image.load(os.path.join('sprites', 'playersprite1.png')).convert(), True, False)
        self.rect = self.image.get_rect()
        self.rect.center = (0.1 * SCREEN_WIDTH, 0.8 * SCREEN_HEIGHT)
        # position of player is calculated using a 2d vector
        self.pos = vec(0.1 * SCREEN_WIDTH, 0.8 * SCREEN_HEIGHT)
        # player velocity
        self.vel = vec(0, 0)
        # player acceleration
        self.acc = vec(0, 0)

        self.isJump = False
        self.jumpCount = 12

    def jump(self, isJump):
        self.rect.y += 1
        collisions = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 1

        if collisions:
            if not self.isJump:
                self.isJump = isJump
            else:
                if self.isJump:
                    if self.jumpCount >= -12:
                        neg = 1
                        if self.jumpCount < 0:
                            neg = -1
                        self.vel.y -= self.jumpCount ** 2 * 0.1 * neg
                        self.jumpCount -= 12
                    else:
                        self.isJump = False
                        self.jumpCount = 12

    def update(self):
        # gravity acceleration
        self.acc = vec(0, gravity)

        # player movement when user presses a key
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.acc.x = -velocity
            # self.image = self.image_l
        if keys[pygame.K_d]:
            self.acc.x = velocity
            # self.image = self.image

        # player jumping when space clicked
        if keys[pygame.K_SPACE]:
            self.jump(True)
        # player not jumping when space not clicked
        if not keys[pygame.K_SPACE]:
            self.jump(False)

        # apply friction to slow down player movement
        self.acc.x += self.vel.x * friction

        # apply velocity
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # screen boundaries
        if self.pos.x > SCREEN_WIDTH - 20:
            self.pos.x = SCREEN_WIDTH - 20
        if self.pos.x < 20:
            self.pos.x = 20

        # player position calculated from the middle bottom
        self.rect.midbottom = self.pos


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(RED) 
        # self.image = pygame.image.load(os.path.join('sprites', 'platformsprite.png')).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
