# filepath: ponggame/game.py
import pygame
from utils import pause_game

def game_loop(WINDOW, WIDTH, HEIGHT, WHITE, BLACK, player, opponent, ball, font):
    clock = pygame.time.Clock()
    running = True
    player_score = 0
    opponent_score = 0
    ball_speed_x = 10
    ball_speed_y = 10

    while running:
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Press 'p' to pause
                  return_to_menu = pause_game(WINDOW, WIDTH, HEIGHT, WHITE, clock)
                  if return_to_menu: # If the user press 'Esc' it returns to the main menu
                        return # Exit the game loop and return to the main menu

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