import pygame

from gameMap import GameMap
from tank import Tank

display_width = 576
display_height = 576


class GameScreen:
    _level_map = None
    _player = None

    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode((display_width, display_height))
        self._clock = pygame.time.Clock()
        self._running = True
        self._draw_world()
        self._add_player()
        self._on_running()

    def _draw_world(self):
        element_width = self._screen.get_size()[0] / 24
        element_height = self._screen.get_size()[1] / 24
        element_size = (element_width, element_height)
        self._level_map = GameMap(2, element_size).level_map

        for row in self._level_map:
            for element in row:
                if element is not None:
                    self._screen.blit(element.get_image(), element.position)

    def _add_player(self):
        element_width = self._screen.get_size()[0] / 24
        element_height = self._screen.get_size()[1] / 24
        element_size = (element_width, element_height)

        self._player = Tank(element_size, (0, 0))
        self._screen.blit(self._player.get_image(), self._player.position)

    def _on_running(self):
        while self._running:
            pygame.time.delay(5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False

            self._player.on_move(self._screen, self._level_map)

            pygame.display.update()
            pygame.display.flip()
