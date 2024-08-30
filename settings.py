class Settings:
    """Class to store all the game settings"""

    def __init__(self):
        """Initiate the game settings"""
        # Screen settings
        self.screen_width: int = 1200
        self.screen_height: int = 800
        self.bg_color: tuple[int, int, int] = (230, 230, 230)

        # Ship settings
        self.ship_speed: float = 1.5

        # Bullet settings
        self.bullet_speed: float = 1.5
        self.bullet_width: int = 3000
        self.bullet_height: int = 15
        self.bullet_color: tuple[int, int, int] = (60, 60, 60)
        self.bullets_allowed: int = 3

        # Alien settings
        self.alien_speed: float = 1.0
        self.fleet_drop_speed: int = 10
        # fleet_direction 1 means moving to the right; -1 -- to the left
        self.fleet_direction = 1
