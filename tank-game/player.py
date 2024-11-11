import math
import pygame

from tank import Tank, TankVariant
from game_item_variant import GameItemVariant

PLAYER_TANK_VARIANT = TankVariant.BLUE

tank_rotation_angle = dict(
    {
        pygame.K_UP: 90,
        pygame.K_DOWN: -90,
        pygame.K_LEFT: 180,
        pygame.K_RIGHT: 0,
    }
)


class Player(Tank):
    def __init__(self, size, position):
        super().__init__(size, position, PLAYER_TANK_VARIANT)
        self.variant = PLAYER_TANK_VARIANT
        self._size = size
        self._horizontal_size = size
        self._vertical_size = (size[1], size[0])

    def on_move(self, screen, level_map):
        keys = pygame.key.get_pressed()

        for key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
            if keys[key]:
                old_position = self.position
                new_position = self._get_new_position(key)

                if self._collider(level_map, new_position):
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
    def _collider(level_map, position):
        row = math.ceil(position[0] / 24)
        col = math.ceil(position[1] / 24)

        if level_map[col][row].variant == GameItemVariant.OBSTACLE:
            return False
        return True
