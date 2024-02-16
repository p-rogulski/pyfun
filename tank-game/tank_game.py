import pygame

from game_map import GameMap
from tank import Tank, TankVariant
from menu import Menu

SCREEN_DISPLAY_WIDTH = 576
SCREEN_DISPLAY_HEIGHT = 576
TIME_DELAY = 90


class TankGame:
    _level_map = None
    _menu = None
    _player = None
    _is_running = True

    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode(
            (SCREEN_DISPLAY_WIDTH, SCREEN_DISPLAY_HEIGHT)
        )
        self._time = pygame.time
        # self._create_menu()
        self._start_game()

    def _create_world(self):
        element_width = self._screen.get_size()[0] / 24
        element_height = self._screen.get_size()[1] / 24
        element_size = (element_width, element_height)
        self._level_map = GameMap(2, element_size).level_map

        for row in self._level_map:
            for element in row:
                if element is not None:
                    self._screen.blit(element.get_image(), element.position)

    def _create_player(self):
        element_width = self._screen.get_size()[0] / 24
        element_height = self._screen.get_size()[1] / 24
        element_size = (element_width, element_height)

        self._player = Tank(TankVariant.HOTCHKISS, element_size, (48, 48))
        self._screen.blit(self._player.get_image(), self._player.position)

    def _create_menu(self):
        self._menu = Menu(SCREEN_DISPLAY_WIDTH, SCREEN_DISPLAY_HEIGHT)
        self._menu.add_button("PLAY", self._start_game)
        self._menu.add_button("QUIT", self._quit_game)

    def _start_game(self):
        self._create_world()
        self._create_player()
        self._init_game_loop()

    def _quit_game(self):
        self._is_running = False

    def _game_renderer(self):
        self._player.on_move(self._screen, self._level_map)

    @staticmethod
    def _screen_renderer():
        pygame.display.update()
        pygame.display.flip()

    def _init_game_loop(self):

        while self._is_running:
            self._time.delay(TIME_DELAY)
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self._quit_game()

            # PoC of main menu
            # self._menu.renderer(events, self._screen)
            self._game_renderer()
            self._screen_renderer()
