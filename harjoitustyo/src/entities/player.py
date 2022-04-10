from enums.game_enums import Difficulty, Color


class Player:

    def __init__(self, name):
        self.name = name
        self.difficulty = Difficulty.EASY
        self.apple_color = Color.RED
        self.snake_color = Color.BLACK
        self.background_color = Color.GREEN
