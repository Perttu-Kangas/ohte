import random


class Apple:

    def __init__(self, snake_game):
        self.snake_game = snake_game
        self.apple_x = random.randrange(
            1, (snake_game.game_x // 10)) * 10
        self.apple_y = random.randrange(
            1, (snake_game.game_y // 10)) * 10

    def move(self):
        self.apple_x = random.randrange(1, (self.snake_game.game_x // 10)) * 10
        self.apple_y = random.randrange(1, (self.snake_game.game_y // 10)) * 10

    def collides(self, snake):
        return snake.snake_x == self.apple_x and snake.snake_y == self.apple_y
