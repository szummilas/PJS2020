import os
from settings import *


class PlayerClass(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.image.load(os.path.join('sprites', 'playersprite1.png')).convert()
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        # position of player is calculated using a 2d vector
        self.position = vector(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        # player velocity
        self.velocity = vector(0, 0)
        # player acceleration
        self.acceleration = vector(0, 0)

    def jump(self):
        self.rect.y += 1
        collisions = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 1

        if len(collisions) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.velocity.y = -13

    def update(self):
        self.calc_gravity()

        self.rect.x += self.velocity.x

        collisions_list = pygame.sprite.spritecollide(self, self.game.platforms, False)
        for plat in collisions_list:
            if self.velocity.x > 0:
                self.rect.right = plat.rect.left
            elif self.velocity.x < 0:
                self.rect.left = plat.rect.right

        self.rect.y += self.velocity.y
        collisions_list = pygame.sprite.spritecollide(self, self.game.platforms, False)
        for plat in collisions_list:
            if self.velocity.y > 0:
                self.rect.bottom = plat.rect.top
            elif self.velocity.y < 0:
                self.rect.top = plat.rect.bottom

            self.velocity.y = 0

        # # gravity acceleration
        # self.acceleration = vector(0, gravity)
        #
        # # player movement when user presses a key
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_a]:
        #     self.acceleration.x = -player_velocity
        # if keys[pygame.K_d]:
        #     self.acceleration.x = player_velocity
        #
        # # apply friction to slow down player movement
        # self.acceleration.x += self.velocity.x * friction
        #
        # # apply velocity
        # self.velocity += self.acceleration
        # self.position += self.velocity + 0.5 * self.acceleration
        #
        # # screen boundaries
        # if self.position.x > SCREEN_WIDTH:
        #     self.position.x = 0
        # if self.position.x < 0:
        #     self.position.x = SCREEN_WIDTH
        #
        # # player position calculated from the middle bottom
        # self.rect.midbottom = self.position

    def calc_gravity(self):
        if self.velocity.y == 0:
            self.velocity.y = 1
        else:
            self.velocity.y += 0.35

        # see if we are on the ground
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.velocity.y >= 0:
            self.velocity.y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def left(self):
        self.velocity.x = -6

    def right(self):
        self.velocity.x = 6

    def stop(self):
        self.velocity.x = 0

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(RED) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
