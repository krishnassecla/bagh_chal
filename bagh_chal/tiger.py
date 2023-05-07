import pygame, os
from pygame.sprite import Sprite
from piece import Piece

"""Tiger class to manage behaviour of tigers"""

# path = "/home/pravesh/Desktop/bagh_chal/"


class Tiger(Sprite, Piece):
    def __init__(self, pos_x, pos_y, x, y):
        """Initialize the tiger pieces and set their starting position"""
        super(Tiger, self).__init__()
        # self.image = pygame.image.load(os.path.join(path, "images", "tiger.png"))
        self.image = pygame.image.load("./images/tiger.png")
        self.rect = self.image.get_rect()
        self.rect.center = pos_x, pos_y
        self.is_selected = False
        self.notation = "t"
        self.x, self.y = (x, y)
        self.isinwhatposition = None
        self.trapped = False
