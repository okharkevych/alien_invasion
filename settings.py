class Settings:
    """Class to store all the game settings"""

    def __init__(self):
        """Initiate constant game settings"""
        # Screen settings
        self.screen_width: int = 1200
        self.screen_height: int = 800
        self.bg_color: tuple[int, int, int] = (230, 230, 230)

        # Ship settings
        self.ship_limit: int = 3

        # Bullet settings
        self.bullet_width: int = 3
        self.bullet_height: int = 15
        self.bullet_color: tuple[int, int, int] = (60, 60, 60)
        self.bullets_allowed: int = 3

        # Alien settings
        self.fleet_drop_speed: int = 10

        # Difficulty modifiers
        self.medium_difficulty = 1.5
        self.hard_difficulty = 2.0

        # How quickly should the game speed up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initiate variable game settings"""
        self.ship_speed: float = 1.5
        self.bullet_speed: float = 1.5
        self.alien_speed: float = 1.0

        # fleet_direction 1 means moving to the right; -1 -- to the left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
