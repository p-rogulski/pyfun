from tank import Tank, TankVariant
from bot_strategy_type import BotStrategyType
from bot_strategy import BotStrategy
from heuristic_bot_strategy import HeuristicBotStrategy
from basic_bot_strategy import BasicBotStrategy


class GameBot(Tank):
    _strategy: BotStrategy

    def __init__(self, position, strategy=BotStrategyType.BASIC):
        super().__init__(position, TankVariant.RED)
        self._set_strategy(strategy)

    def _set_strategy(self, strategy):
        match strategy:
            case BotStrategyType.BASIC:
                self._strategy = BasicBotStrategy()
            case BotStrategyType.HEURISTIC:
                self._strategy = HeuristicBotStrategy()
