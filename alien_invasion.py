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
            # Track mouse & keyboard events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # Redraw the screen on every cycle iteration
                self.screen.fill(color=self.settings.bg_color)
                self.ship.blitme()

            # Display the last screen drawn
            pygame.display.flip()


if __name__ == '__main__':
    # Create a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
