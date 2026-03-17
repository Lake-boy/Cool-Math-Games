import sys

import pygame

class AlienInvasion:
    """Overll class to mange games assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

        # Cool background gaming math.
        self.bg_color = (51, 51, 62)
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #watching for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)

            #make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    #Makes a cool math game Instance and run the cool math game.
    ai = AlienInvasion()
    ai.run_game()
