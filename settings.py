import pygame
pygame.font.init()

# setting screen dimensions
screen_width = 1200
screen_height = 600

# defining basic colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 180)
light_blue = (40, 80, 250)
red = (180, 0, 0)
light_red = (255, 0, 0)

# player behaviour settings
gravity = 1
velocity = 1
acceleration = 0.5
friction = -0.15

# basic frames per second
fps = 30

# title of the game
game_title = "Platformer"

# defining fonts
smallfont = pygame.font.SysFont("suruma", 25)
medfont = pygame.font.SysFont("surma", 50)
largefont = pygame.font.SysFont("surma", 80)
