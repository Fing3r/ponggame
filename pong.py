import pygame
import random

# Initialize game
pygame.init()

#display
WIDTH = 900
HEIGHT = 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong by: Finger")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle Properties
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 132
player = pygame.Rect(5, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT) #Player Position
opponent = pygame.Rect(WIDTH - 5 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT) #Opponent Position

# Ball Properties
BALL_SIZE = 10
ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)
ball_speed_x = 10 * random.choice((1, -1))
ball_speed_y = 10 * random.choice((1, -1))

# Score Properties
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 36)

def show_menu():
    menu_running = True
    while menu_running:
        WINDOW.fill(BLACK)

        # Display menu texts
        title_font = pygame.font.Font(None, 74)
        menu_font = pygame.font.Font(None, 36)
        title_text = title_font.render("Finger's Pong Game", True, WHITE)
        start_text = menu_font.render("Press SPACE to Start", True, WHITE)
        quit_text = menu_font.render("Press ESC to Quit", True, WHITE)
                                     
        # Position text
        WINDOW.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 3))
        WINDOW.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2))
        WINDOW.blit(quit_text, (WIDTH // 2 - quit_text.get_width() // 2, HEIGHT // 2 + 50))

        pygame.display.flip()

        # Handle Menu Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu_running = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()



# Main Program
show_menu() # Show Menu before start

# Game Loop
clock =pygame.time.Clock()
running = True

while running:
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: # Press 'p' to pause
                pause_game()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player.top > 0:
        player.y -= 10
    if keys[pygame.K_s] and player.bottom < HEIGHT:
        player.y += 10

    # Opponent AI movement (simple: follows ball)
    if opponent.centery < ball.centery and opponent.bottom < HEIGHT:
        opponent.y += 10
    if opponent.centery > ball.centery and opponent.top > 0:
        opponent.y -= 10

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Ball collision with paddles
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    # Scoring
    if ball.left <= 0:
        opponent_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
    if ball.right >= WIDTH:
        player_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)

    # Drawing
    WINDOW.fill(BLACK)
    pygame.draw.rect(WINDOW, WHITE, player)
    pygame.draw.rect(WINDOW, WHITE, opponent)
    pygame.draw.ellipse(WINDOW, WHITE, ball)
    pygame.draw.aaline(WINDOW, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Display Scores
    player_text = font.render(str(player_score), False, WHITE)
    opponent_text = font.render(str(opponent_score), False, WHITE)
    WINDOW.blit(player_text, (WIDTH // 4, 20))
    WINDOW.blit(opponent_text, (3 * WIDTH // 4, 20))

    # Update Display
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

    def pause_game():
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:  # Press 'P' again to unpause
                        paused = False
    
            # Display pause message
            pause_font = pygame.font.Font(None, 74)
            pause_text = pause_font.render("Game Paused", True, WHITE)
            WINDOW.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 2))
            pygame.display.flip()
            clock.tick(30)  # Limit frame rate while paused


# Quit Game
pygame.quit()