import pygame

class Ship:
    """A class to manage the ship

    """

    def __init__(self, ai_game):
        """Initialize the ship and sets its starting
        the self reference and a reference to the current instance of the AlienInvasion class
        """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen
        # place midbottom of the ship at the position midbottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom        # midbottom is shortcut atribute
        #self.rect.midbottom = (100,500)        # random position
        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the ship at its current location"""
        # https://stackoverflow.com/questions/37800894/what-is-the-surface-blit-function-in-pygame-what-does-it-do-how-does-it-work
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1