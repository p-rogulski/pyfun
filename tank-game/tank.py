import math
import pygame

from enum import Enum

from game_item import GameItem
from game_item_variant import GameItemVariant

TANK_IMG_PATH_PREFIX = "assets/img/tanks"


class TankVariant(Enum):
    PANZER_4 = "panzer-4"
    HOTCHKISS = "hotchkiss"


tank_rotation_file_name = dict(
    {
        pygame.K_UP: "tank-top.png",
        pygame.K_DOWN: "tank-bottom.png",
        pygame.K_LEFT: "tank-left.png",
        pygame.K_RIGHT: "tank-right.png",
    }
)


class Tank(GameItem):
    def __init__(self, variant: TankVariant, size, position):
        super().__init__(size, position, GameItemVariant.PLAYER)
        self.variant = variant
        self._size = size
        self._horizontal_size = size
        self._vertical_size = (size[1], size[0])

    def get_image(self):
        keys = pygame.key.get_pressed()
        path = f"{TANK_IMG_PATH_PREFIX}/{self.variant.value}/{tank_rotation_file_name[pygame.K_RIGHT]}"

        for key in tank_rotation_file_name:
            if keys[key]:
                path = f"{TANK_IMG_PATH_PREFIX}/{self.variant.value}/{tank_rotation_file_name[key]}"
                break
        return pygame.transform.smoothscale(
            pygame.image.load(path).convert(), self._size
        )

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
                y -= 24
            case pygame.K_DOWN:
                y += 24
            case pygame.K_LEFT:
                x -= 24
            case pygame.K_RIGHT:
                x += 24
        return x, y

    @staticmethod
    def _collider(level_map, position, key):
        row = math.ceil(position[0] / 24)
        col = math.ceil(position[1] / 24)

        if level_map[col][row].variant == GameItemVariant.OBSTACLE:
            return False
        return True
