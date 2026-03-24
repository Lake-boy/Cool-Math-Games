import pygame

class Ship:

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""

        self.screen = ai_game.screen
        self.settings =ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship image
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        #start each new ship at the bottom of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #store position floats.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


        #Movement Flags; starts with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        if self.moving_down:
            self.y += self.settings.ship_speed
        if self.moving_up:
            self.y -= self.settings.ship_speed

        # Update rect objects
        self.rect.x = self.x
        self.rect.y = self.y
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)