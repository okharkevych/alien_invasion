import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Ship management class"""

    def __init__(self, ai_game):
        """Initiate the ship and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image and get its rect
        self.image: pygame.Surface = pygame.image.load('images/ship.bmp')
        self.rect: pygame.Rect = self.image.get_rect()

        # Create every new ship at the screen bottom, in the center
        self.rect.midbottom = self.screen_rect.midbottom

        # Save a float value for the ship horizontal position
        self.x: float = float(self.rect.x)

        # Movement indicators
        self.moving_right: bool = False
        self.moving_left: bool = False

    def update(self):
        """
        Update the ship's current location based on
        the movement indicators
        """
        # Update ship.x value, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update the object's rect from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(source=self.image, dest=self.rect)

    def center_ship(self):
        """Center the ship on screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
