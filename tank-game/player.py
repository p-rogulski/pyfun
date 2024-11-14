import math
import pygame

from tank import Tank, TankVariant
from game_item_variant import GameItemVariant

PLAYER_TANK_VARIANT = TankVariant.BLUE
SINGLE_MOVE = 24

tank_rotation_angle = dict(
    {
        pygame.K_UP: 90,
        pygame.K_DOWN: -90,
        pygame.K_LEFT: 180,
        pygame.K_RIGHT: 0,
    }
)


class Player(Tank):
    def __init__(self, position):
        super().__init__(position, PLAYER_TANK_VARIANT)

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
                y -= SINGLE_MOVE
            case pygame.K_DOWN:
                y += SINGLE_MOVE
            case pygame.K_LEFT:
                x -= SINGLE_MOVE
            case pygame.K_RIGHT:
                x += SINGLE_MOVE
        return x, y

    def _collider(self, level_map, position):
        row = math.ceil(position[0] / self.size[0])
        col = math.ceil(position[1] / self.size[1])

        if level_map[col][row].variant == GameItemVariant.OBSTACLE:
            return False
        return True
