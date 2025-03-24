# filepath: ponggame/main.py
import pygame
from menu import show_menu
from game import game_loop
from power_up import PowerUp

# Initialize game
pygame.init()

# Display
WIDTH = 900
HEIGHT = 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong by: Finger")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Entities
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 132
player = pygame.Rect(5, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent = pygame.Rect(WIDTH - 5 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
BALL_SIZE = 10
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
font = pygame.font.Font(None, 36)

# Main loop
while True:
    show_menu(WINDOW, WIDTH, HEIGHT, WHITE, BLACK) # Main Menu
    game_loop(WINDOW, WIDTH, HEIGHT, WHITE, BLACK, player, opponent, ball, font) # Start Game

# Quit game
pygame.quit()