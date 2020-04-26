import pygame
import os

# --- INITIALIZE PYGAME ---
pygame.font.init()          # FONTS
pygame.mixer.init()         # SOUND EFFECTS
pygame.init()
vector = pygame.math.Vector2

# --- SETTINGS ---
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
RESOLUTION = [SCREEN_WIDTH, SCREEN_HEIGHT]
FPS = 30
TITLE = "Vigilant Pancake"

# --- COLORS ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 180)
LIGHT_BLUE = (40, 80, 250)
RED = (180, 0, 0)
LIGHT_RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# --- PLAYER BEHAVIOUR SETTINGS ---
gravity = 1
player_velocity = 1
player_acceleration = 0.5
friction = -0.15

# --- FONTS ---
smallfont = pygame.font.Font(os.path.join('font', 'PressStart2P-Regular.ttf'), 10)
medfont = pygame.font.Font(os.path.join('font', 'PressStart2P-Regular.ttf'), 30)
largefont = pygame.font.Font(os.path.join('font', 'PressStart2P-Regular.ttf'), 40)
