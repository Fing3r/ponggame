# filepath: ponggame/utils.py
import pygame

def pause_game(WINDOW, WIDTH, HEIGHT, WHITE, clock):
        paused = True
        return_to_menu = False 

        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:  # Press 'P' again to unpause
                        paused = False
                    if event.key == pygame.K_ESCAPE: # Press 'Esc'to return to main menu
                        return_to_menu = True
                        paused = False
    
            # Display pause message
            pause_font = pygame.font.Font(None, 74)
            pause_text = pause_font.render("Game Paused", True, WHITE)
            WINDOW.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 2))
            pygame.display.flip()
            clock.tick(30)  # Limit frame rate while paused

        return return_to_menu