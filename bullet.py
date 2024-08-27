import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class to manage bullets shot from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create bullet rect at (0, 0) and set the correct position
        self.rect = pygame.Rect(
            left=0,
            top=0,
            width=self.settings.bullet_width,
            height=self.settings.bullet_height
        )
        self.rect.midtop = ai_game.ship.rect.midtop

        # Save the bullet position as a float
        self.y: float = float(self.rect.y)

    def update(self) -> None:
        """Move the bullet up the screen"""
        # Update the bullet's float position
        self.y -= self.settings.bullet_speed
        # Update rect position
        self.rect.y = self.y

    def draw_bullet(self) -> None:
        """Draw a bullet on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
