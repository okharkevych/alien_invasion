import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """General class to manage game resources and behavior"""

    def __init__(self):
        """Initiate the game, create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen: pygame.Surface = pygame.display.set_mode(
            size=(self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption(title='Alien Invasion')

        self.ship = Ship(ai_game=self)

    def run_game(self) -> None:
        """Begin the game main cycle"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """React to key presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update image on screen and switch to the next screen"""
        self.screen.fill(color=self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    # Create a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
