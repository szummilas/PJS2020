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

        if collisions:
            self.velocity.y = -13


    def update(self):
        # gravity acceleration
        self.acceleration = vector(0, gravity)

        # player movement when user presses a key
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.acceleration.x = -player_velocity
        if keys[pygame.K_d]:
            self.acceleration.x = player_velocity

        # apply friction to slow down player movement
        self.acceleration.x += self.velocity.x * friction

        # apply velocity
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration

        # screen boundaries
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH

        # player position calculated from the middle bottom
        self.rect.midbottom = self.position


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(RED) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
