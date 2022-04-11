import random


class Apple:

    def __init__(self, snake_game):
        self.snake_game = snake_game
        self.x = random.randrange(1, (snake_game.game_x // 10)) * 10  # pylint: disable=invalid-name
        self.y = random.randrange(1, (snake_game.game_y // 10)) * 10  # pylint: disable=invalid-name

    def move(self):
        self.x = random.randrange(1, (self.snake_game.game_x // 10)) * 10
        self.y = random.randrange(1, (self.snake_game.game_y // 10)) * 10

    def collides(self, snake):
        return snake.x == self.x and snake.y == self.y
