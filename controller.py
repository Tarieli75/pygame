class Player:
    def __init__(self):
        self.size = 50
        self.y = 275
        self.x = 375
        self.speed = 5

    def move_player(self, x_position, y_position):
        self.x += x_position * self.speed
        self.y += y_position * self.speed
