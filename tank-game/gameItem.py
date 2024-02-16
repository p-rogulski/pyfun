from abc import abstractmethod


class GameItem:

    def __init__(self, size, position):
        self.size = size
        self.position = position

    @abstractmethod
    def get_image(self):
        pass
