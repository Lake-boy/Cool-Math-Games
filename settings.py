class Settings:
    """A class to store all setting for alien Invasion."""

    def __init__(self):
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #Ship settings
        self.ship_speed = 3.5

        #Bullet settings
        self.bullet_speed = 4.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3