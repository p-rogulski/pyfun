from player import Player
from game_item_type import GameItemType
from game_item import GameItem
from brick import Brick
from cup import Cup
from pipe import Pipe
from green import Green
from constants import LEVEL_FILES


class GameMap:
    _level_map: list[list[GameItem]] = []

    def __init__(self, level, element_size):
        self._element_size = element_size
        self._level = level
        self._set_level_map()

    @property
    def level_map(self):
        return self._level_map

    def get_map_sectors_by_variant(self, variant):
        elements = []
        for row in self._level_map:
            for element in row:
                if element is not None and element.variant.value == variant.value:
                    elements.append(element)

        return elements

    def _set_level_map(self):
        level_file = open(LEVEL_FILES.get(self._level), "r", encoding="utf8")
        level_lines = level_file.readlines()

        for line_index, line in enumerate(level_lines):
            self._level_map.insert(line_index, [])
            for c_index, c in enumerate(line):
                position = (
                    c_index * self._element_size[0],
                    line_index * self._element_size[1],
                )
                self._level_map[line_index].insert(c_index, self._get_item(c, position))

    def _get_item(self, code, position):
        match code:
            case GameItemType.BRICK.value:
                return Brick(position)
            case GameItemType.TANK.value:
                return Player(position)
            case GameItemType.CUP.value:
                return Cup(position)
            case GameItemType.PIPE.value:
                return Pipe(position)
            case GameItemType.GREEN.value:
                return Green(position)
            case _:
                return None

    def _get_map_sector_by_position(self, position):
        pass
