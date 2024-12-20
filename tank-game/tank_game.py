import random
import pygame

from game_map import GameMap
from player import Player
from game_item_variant import GameItemVariant
from game_bot import GameBot
from menu import Menu, EVENTS

SCREEN_DISPLAY_WIDTH = 576
SCREEN_DISPLAY_HEIGHT = 576
TIME_DELAY = 90
BOTS_COUNT = 7


class TankGame:
    _map = None
    _menu = None
    _player = None
    _boots = []
    _is_game_started = False

    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode(
            (SCREEN_DISPLAY_WIDTH, SCREEN_DISPLAY_HEIGHT)
        )
        self._time = pygame.time
        self._menu = self._create_menu()
        self._init_menu_loop()

    def _create_world(self):
        element_width = self._screen.get_size()[0] / 24
        element_height = self._screen.get_size()[1] / 24
        element_size = (element_width, element_height)
        self._map = GameMap(2, element_size)

        for row in self._map.level_map:
            for element in row:
                if element is not None:
                    self._screen.blit(element.get_image(), element.position)

    def _create_boots(self):
        positions = list(
            map(
                lambda track: track.position,
                self._map.get_map_sectors_by_variant(GameItemVariant.TRACK),
            )
        )

        for _ in range(BOTS_COUNT):
            position = random.choice(positions)
            game_bot = GameBot(position)
            self._screen.blit(game_bot.get_image(), game_bot.position)
            positions.remove(position)

    def _create_player(self):
        element_width = self._screen.get_size()[0] / 24
        element_height = self._screen.get_size()[1] / 24
        element_size = (element_width, element_height)

        self._player = Player(element_size)
        self._screen.blit(self._player.get_image(), self._player.position)

    def _create_menu(self):
        menu = Menu(SCREEN_DISPLAY_WIDTH, SCREEN_DISPLAY_HEIGHT)
        menu.add_button("Play", self._start_game)
        # TODO: Implementation
        menu.add_button("Settings", EVENTS.EXIT)
        menu.add_button("About", EVENTS.EXIT)
        menu.add_button("Quit", EVENTS.EXIT)
        return menu

    def _start_game(self):
        self._menu.close()
        self._create_world()
        self._create_boots()
        self._create_player()
        self._is_game_started = True
        self._init_game_loop()

    def _game_renderer(self):
        self._player.on_move(self._screen, self._map.level_map)

    @staticmethod
    def _screen_renderer():
        pygame.display.update()
        pygame.display.flip()

    def _init_menu_loop(self):

        while self._menu.is_enabled:
            self._time.delay(TIME_DELAY)
            self._menu.renderer(pygame.event.get(), self._screen)
            self._screen_renderer()

    def _init_game_loop(self):
        while self._is_game_started:
            self._time.delay(TIME_DELAY)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._is_game_started = False

            self._game_renderer()
            self._screen_renderer()
