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

        # Launch the game in windowed mode
        self.screen: pygame.Surface = pygame.display.set_mode(
            size=(self.settings.screen_width, self.settings.screen_height)
        )

        # Launch the game in fullscreen mode
        # self.screen: pygame.Surface = pygame.display.set_mode(
        #     size=(0, 0), flags=pygame.FULLSCREEN
        # )
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption(title='Alien Invasion')

        self.ship = Ship(ai_game=self)

    def run_game(self) -> None:
        """Begin the game main cycle"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """React to key presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event: pygame.KEYDOWN):
        """React to key presses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event: pygame.KEYUP):
        """React when a key isn't pressed"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Update image on screen and switch to the next screen"""
        self.screen.fill(color=self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    # Create a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
