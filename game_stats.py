class GameStats:
    """Track game statistics"""

    def __init__(self, ai_game):
        """Initiate the statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start game in an inactive state
        self.game_active = False

    def reset_stats(self):
        """Initiate the statistics that can change thoughout the game"""
        self.ships_left = self.settings.ship_limit
