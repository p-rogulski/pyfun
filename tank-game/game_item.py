from abc import abstractmethod


class GameItem:
    def __init__(self, size, position, variant):
        self.size = size
        self.position = position
        self.variant = variant

    @abstractmethod
    def get_image(self):
        pass
