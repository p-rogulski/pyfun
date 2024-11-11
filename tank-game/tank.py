import pygame

from enum import Enum

from game_item import GameItem
from game_item_variant import GameItemVariant

TANK_IMG_PATH_PREFIX = "assets/img/tanks"


class TankVariant(Enum):
    BLUE = "blue.png"
    RED = "red.jpg"


tank_rotation_angle = dict(
    {
        pygame.K_UP: 90,
        pygame.K_DOWN: -90,
        pygame.K_LEFT: 180,
        pygame.K_RIGHT: 0,
    }
)


class Tank(GameItem):
    def __init__(self, size, position, variant):
        super().__init__(size, position, GameItemVariant.TANK)
        self.variant = variant
        self._size = size
        self._horizontal_size = size
        self._vertical_size = (size[1], size[0])

    def get_image(self):
        keys = pygame.key.get_pressed()
        path = f"{TANK_IMG_PATH_PREFIX}/{self.variant.value}"
        angle = 0

        for key in tank_rotation_angle:
            if keys[key]:
                angle = tank_rotation_angle[key]
                break
        img = pygame.transform.rotate(pygame.image.load(path), angle)
        return pygame.transform.smoothscale(img, self._size)
