# filepath ponggame/menu.py
import pygame

def show_menu(WINDOW, WIDTH, HEIGHT, WHITE, BLACK):
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