import pygame

from gameItem import GameItem


class Pipe(GameItem):
    def __init__(self, size, position):
        super().__init__(size, position)

    def get_image(self):
        return pygame.transform.smoothscale(pygame.image.load('assets/img/map/pipe.png').convert(), self.size)
