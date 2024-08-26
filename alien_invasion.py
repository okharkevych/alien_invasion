import sys

import pygame


class AlienInvasion:
    """General class to manage game resources and behavior"""

    def __init__(self):
        """Initiate the game, create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode(size=(1200, 800))
        pygame.display.set_caption(title='Alien Invasion')

    def run_game(self) -> None:
        """Begin the game main cycle"""
        while True:
            # Track mouse & keyboard events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Display the last screen drawn
            pygame.display.flip()


if __name__ == '__main__':
    # Create a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
