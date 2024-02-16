import math

import pygame

from gameItem import GameItem

PANTHER_IMG_PATH_PREFIX = 'assets/img/tanks/panzer-4/'

tank_image = dict({
    pygame.K_UP: 'tank-top.png',
    pygame.K_DOWN: 'tank-bottom.png',
    pygame.K_LEFT: 'tank-left.png',
    pygame.K_RIGHT: 'tank-right.png',
})


class Tank(GameItem):
    def __init__(self, size, position):
        super().__init__(size, position)
        self._size = size
        self._horizontal_size = size
        self._vertical_size = (size[1], size[0])

    def get_image(self):
        keys = pygame.key.get_pressed()
        path = f'{PANTHER_IMG_PATH_PREFIX}{tank_image[pygame.K_RIGHT]}'

        for key in tank_image:
            if keys[key]:
                path = f'{PANTHER_IMG_PATH_PREFIX}{tank_image[key]}'
                break
        return pygame.transform.smoothscale(pygame.image.load(path).convert(), self._size)

    def on_move(self, screen, level_map):
        keys = pygame.key.get_pressed()

        for key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
            if keys[key]:
                old_position = self.position
                new_position = self._get_new_position(key)

                if self._collider(level_map, new_position, key):
                    screen.fill((0, 0, 0), (old_position, self.size))
                    self.position = new_position
                    screen.blit(self.get_image(), self.position)

    def _get_new_position(self, key):
        x = int(self.position[0])
        y = int(self.position[1])

        match key:
            case pygame.K_UP:
                y -= 1
            case pygame.K_DOWN:
                y += 1
            case pygame.K_LEFT:
                x -= 1
            case pygame.K_RIGHT:
                x += 1
        return x, y

    def _collider(self, level_map, position, key):
        col = 120/24 + self._size[0]
        return True
