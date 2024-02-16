import pygame

from gameItem import GameItem


class Green(GameItem):
    def __init__(self, size, position):
        super().__init__(size, position)

    def get_image(self):
        return pygame.transform.smoothscale(pygame.image.load('assets/img/map/green.png').convert(), self.size)
