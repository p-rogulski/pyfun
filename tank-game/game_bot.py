from game_item import GameItem

from bot_strategy_type import BotStrategyType
from bot_strategy import BotStrategy
from heuristic_bot_strategy import HeuristicBotStrategy
from basic_bot_strategy import BasicBotStrategy


class GameBot(GameItem):
    _strategy: BotStrategy

    def __init__(self, size, position, variant, strategy):
        super().__init__(size, position, variant)
        self._set_strategy(strategy)

    def get_image(self):
        pass

    def _set_strategy(self, strategy):
        match strategy:
            case BotStrategyType.BASIC:
                self._strategy = BasicBotStrategy()
            case BotStrategyType.HEURISTIC:
                self._strategy = HeuristicBotStrategy()
