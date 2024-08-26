import pygame


class Ship:
    """Ship management class"""

    def __init__(self, ai_game):
        """Initiate the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Create every new ship at the screen bottom, in the center
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(source=self.image, dest=self.rect)
