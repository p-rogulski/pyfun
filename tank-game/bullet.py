import pygame

from game_item import GameItem
from game_item_variant import GameItemVariant


class Bullet(GameItem):
    def __init__(self, size, position):
        super().__init__(size, position, GameItemVariant.BULLET)
        self.x = position.x
        self.y = position.y

    def get_image(self):
        return pygame.transform.smoothscale(
            pygame.image.load("assets/img/map/pipe.png").convert(), self.size
        )
