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
    def __init__(self, position, tank_variant):
        super().__init__(position, GameItemVariant.TANK)
        self.tank_variant = tank_variant

    def get_image(self):
        keys = pygame.key.get_pressed()
        path = f"{TANK_IMG_PATH_PREFIX}/{self.tank_variant.value}"
        angle = 0

        for key in tank_rotation_angle:
            if keys[key]:
                angle = tank_rotation_angle[key]
                break
        img = pygame.transform.rotate(pygame.image.load(path), angle)
        return pygame.transform.smoothscale(img, self.size)
