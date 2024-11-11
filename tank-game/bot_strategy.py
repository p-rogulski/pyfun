from abc import abstractmethod


class BotStrategy:
    @abstractmethod
    def get_next_move(self):
        pass

