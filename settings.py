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
