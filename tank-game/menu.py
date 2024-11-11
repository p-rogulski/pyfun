from pygame import mixer

import pygame_menu

GAME_TITLE = "RETRO TANKS BATTLE'24"
MUSIC_VOLUME = 0.9
MUSIC_LOOP = 99

MUSIC_FILE_PATH = "./assets/music/main-menu.ogg"
MENU_BACKGROUND_PATH = "assets/img/main-menu.jpg"


EVENTS = pygame_menu.events


class Menu:
    def __init__(self, menu_width, menu_height):
        self._menu = pygame_menu.Menu(
            GAME_TITLE, menu_width, menu_height, theme=self._get_menu_theme()
        )
        self._play_menu_music()

    @property
    def is_enabled(self):
        return self._menu.is_enabled()

    def close(self):
        self._menu.close()

    def add_button(self, label, click_handler):
        self._menu.add.button(label, click_handler)

    def renderer(self, events, screen):
        self._menu.update(events)
        self._menu.draw(screen)

    @staticmethod
    def _get_menu_theme():
        theme = pygame_menu.themes.THEME_DARK.copy()
        theme.background_color = pygame_menu.baseimage.BaseImage(
            image_path=MENU_BACKGROUND_PATH,
            drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
        )
        return theme

    @staticmethod
    def _play_menu_music():
        mixer.music.load(MUSIC_FILE_PATH)
        mixer.music.set_volume(MUSIC_VOLUME)
        mixer.music.play(loops=MUSIC_LOOP)
