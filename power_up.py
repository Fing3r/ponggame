import pygame
import random 

class PowerUp:
    def __init__(self, width, height):
        self.size = 30  # Size of the power-up (example value)
        self.rect = pygame.Rect(0, 0, self.size, self.size)  # Power up rectangle
        self.active = False # Whether the power up is active
        self.type = None # Type of power up
        self.width = width # Screen width
        self.height = height # Screen height
        self.duration = 5000 # Duration of the power-up effect in milliseconds (e.g., 5 seconds)
        self.start_time = None # Time when the power-up effect starts

    def spawn(self):
        """Randomly spawn a power-up on the screen."""
        self.rect.x = random.randint(50, self.width - 50)
        self.rect.y = random.randint(50, self.height - 50)
        self.type = random.choice(["speed", "slow"])  # Randomly choose a power-up type
        self.active = True
        self.start_time = None # Reset the start time when spawning

    def draw(self, window):
        """Draw the power-up on the screen."""
        if self.active:
            if self.type == "speed":
                pygame.draw.rect(window, (0, 255, 0), self.rect)  # Green for speed
            elif self.type == "slow":
                pygame.draw.rect(window, (255, 0, 0), self.rect)  # Red for slow