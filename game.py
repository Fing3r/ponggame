# filepath: ponggame/game.py
import pygame
from utils import pause_game

BALL_SIZE = 10 #size of the ball

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
        if ball.colliderect(player):
            ball_speed_x = abs (ball_speed_x) # Ensure the ball moves to the right
            #Influences ball's vertical speed basede on where it hits the paddle
            ball_speed_y += (ball.centery - player.centery) // 10 # Adjust sppeed proportionally
            # Limit ball's vertical speed
            if ball_speed_y > 15:
                ball_speed_y = 15
            elif ball_speed_y < -15:
                ball_speed_y = -15

        if ball.colliderect(opponent):
            ball_speed_x = -abs(ball_speed_x) # Ensure the ball moves to the left
            #Influences ball's vertical speed basede on where it hits the paddle
            ball_speed_y += (ball.centery - opponent.centery) // 10 # Adjust sppeed proportionally
            # Limit ball's vertical speed
            if ball_speed_y > 15:
                ball_speed_y = 15
            elif ball_speed_y < -15:
                ball_speed_y = -15

        # Scoring
        if ball.left <= 0: # Opponent scores
            opponent_score += 1
            display_message(WINDOW, WIDTH, HEIGHT, "Opponent Scores!", font, WHITE) # Show Message
            pygame.time.delay(1000) # Pause for 3 seconds
            ball.center = (player.right + BALL_SIZE, player.centery) 
            ball_speed_x = abs(ball_speed_x)

        if ball.right >= WIDTH: # Player scores
            player_score += 1
            display_message(WINDOW, WIDTH, HEIGHT, "Player Scores!", font, WHITE) # Show Message
            pygame.time.delay(1000) # Pause for 3 seconds
            ball.center = (opponent.left - BALL_SIZE, opponent.centery)
            ball_speed_x = -abs(ball_speed_x)

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

def display_message(WINDOW, WIDTH, HEIGHT, message, font, WHITE):
    text = font.render(message, True, WHITE)
    WINDOW.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()