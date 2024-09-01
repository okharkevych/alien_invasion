import pygame.font


class Scoreboard:
    """Class to display game score"""

    def __init__(self, ai_game):
        """Initiate attributes related to game score"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Score display font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare a starting score image
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """Transform score into image"""
        rounded_score = round(self.stats.score, -1)
        score_str = '{:,}'.format(rounded_score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color
        )

        # Display score in the top right screen corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Generate highscore into image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = '{:,}'.format(high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color
        )

        # Center highscore horizontally
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Check if a new highscore has been achieved"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Display score on screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
