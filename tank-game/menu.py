import pygame_menu

GAME_TITLE = "RETRO TANKS BATTLE'24"


class Menu:
    def __init__(self, menu_width, menu_height):
        self._menu = pygame_menu.Menu(
            GAME_TITLE, menu_width, menu_height, theme=pygame_menu.themes.THEME_BLUE
        )

    def add_button(self, label, click_handler):
        self._menu.add.button(label, click_handler)

    def renderer(self, events, screen):
        if self._menu.is_enabled():
            self._menu.update(events)
            self._menu.draw(screen)
