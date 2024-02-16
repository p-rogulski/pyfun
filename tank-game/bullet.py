class Bullet:
    def __init__(self, tank):
        self.x = tank.x
        self.y = tank.y
        self.direction = tank.direction

    def move(self, x, y):
        self.x = x,
        self.y = y
