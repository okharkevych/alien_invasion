import sys
from time import sleep

import pygame

from alien import Alien
from bullet import Bullet
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
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

        # Create an instance to save game statistics
        # and scoreboard on screen
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(ai_game=self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Create Play button
        self.play_button = Button(self, msg='Play')

    def run_game(self) -> None:
        """Begin the game main cycle"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game once user presses the 'Play' button"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()

    def _start_game(self):
        # Reset game statistics
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()

        # Remove excess aliens and bullets
        self.aliens.empty()
        self.bullets.empty()

        # Create a new fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()

        # Hide mouse cursor
        pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event: pygame.KEYDOWN):
        """React to key presses"""
        if event.key == pygame.K_RIGHT and self.stats.game_active:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT and self.stats.game_active:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_p and not self.stats.game_active:
            self._start_game()
        elif event.key == pygame.K_SPACE and self.stats.game_active:
            self._fire_bullet()

    def _check_keyup_events(self, event: pygame.KEYUP):
        """React when a key isn't pressed"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet: Bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update bullets position and get rid of the old bullets"""
        # Update bullets position
        self.bullets.update()

        # Get rid of the bullets that disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Reaction to collisions between bullets and aliens"""
        # Delete all bullets and aliens that collided
        collisions = pygame.sprite.groupcollide(
            groupa=self.bullets,
            groupb=self.aliens,
            dokilla=True,
            dokillb=True
        )

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # Destroy existing bullets and create a new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level
            self.stats.level += 1
            self.sb.prep_level()

    def _update_aliens(self):
        """
        Check if the fleet is on the screen's edge,
        then update positions of all the aliens in the fleet
        """
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for an alien that has reached the screen bottom
        self._check_aliens_bottom()

    def _ship_hit(self):
        """React to collision between an alien and the ship"""
        if self.stats.ships_left > 0:
            # Reduce ships_left
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Remove excess aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Check if some alien has reached the screen bottom"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Reach as if the ship has been hit
                self._ship_hit()
                break

    def _create_fleet(self):
        """Create an alien fleet"""
        # Create aliens and determine aliens number in a row
        # Distance between aliens equals one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the aliens number that fits on the screen
        ship_height = self.ship.rect.height
        available_space_y = (
            self.settings.screen_height - (3 * alien_height) - ship_height
        )
        number_rows = available_space_y // (2 * alien_height)

        # Create a whole alien fleet
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and add it to the row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """
        Reacts based on whether an alien has reached the screen's edge
        """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Moving the whole fleet down and changing its direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Update image on screen and switch to the next screen"""
        self.screen.fill(color=self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Draw score information
        self.sb.show_score()

        # Draw a Play button if game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # Create a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
