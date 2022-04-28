import unittest
from enums.game_enums import Direction, Difficulty, Color
from services.snake_game import SnakeGame
from entities.player import Player


class TestApple(unittest.TestCase):
    def setUp(self):
        self.player = Player("test", 1, Difficulty.MEDIUM,
                             Color.BLACK, Color.BLACK, Color.BLACK)
        self.snake_game = SnakeGame(self.player)
        self.snake = self.snake_game.snake
        self.apple = self.snake_game.apple

    def test_first_position(self):
        self.assertNotEqual(self.apple.apple_x, 0)
        self.assertNotEqual(self.apple.apple_y, 0)

    def test_move_does_something(self):
        old_x = self.apple.apple_x
        old_y = self.apple.apple_y
        self.apple.move()
        self.assertNotEqual(self.apple.apple_x, old_x)
        self.assertNotEqual(self.apple.apple_y, old_y)

    def test_move(self):
        self.apple.move_to(1, 1)
        self.assertEqual(self.apple.apple_x, 1)
        self.assertEqual(self.apple.apple_y, 1)

    def test_collides_snake(self):
        self.apple.move_to(150, 140)
        self.snake.move(Direction.UP)
        self.assertTrue(self.apple.collides(self.snake))
