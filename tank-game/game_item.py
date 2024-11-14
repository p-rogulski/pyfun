from abc import abstractmethod


class GameItem:
    def __init__(self, position, variant):
        self.size = (24, 24)
        self.position = position
        self.variant = variant

    @abstractmethod
    def get_image(self):
        pass
