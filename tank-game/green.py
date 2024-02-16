import pygame

from game_item import GameItem
from game_item_variant import GameItemVariant


class Green(GameItem):
    def __init__(self, size, position):
        super().__init__(size, position, GameItemVariant.TRACK)

    def get_image(self):
        return pygame.transform.smoothscale(
            pygame.image.load("assets/img/map/green.png").convert(), self.size
        )
