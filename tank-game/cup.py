import pygame

from game_item import GameItem
from game_item_variant import GameItemVariant


class Cup(GameItem):
    def __init__(self, position):
        super().__init__(position, GameItemVariant.TROPHY)

    def get_image(self):
        return pygame.transform.smoothscale(
            pygame.image.load("assets/img/map/cup.png").convert(), self.size
        )
