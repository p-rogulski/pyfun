import pygame_menu

GAME_TITLE = "RETRO TANKS BATTLE'24"
EVENTS = pygame_menu.events

class Menu:
    def __init__(self, menu_width, menu_height):
        self._menu = pygame_menu.Menu(
            GAME_TITLE, menu_width, menu_height, theme=pygame_menu.themes.THEME_BLUE
        )

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
