import unittest
from enums.game_enums import Direction, Difficulty, Color
from services.snake_game import SnakeGame
from entities.player import Player


class TestSnake(unittest.TestCase):
    def setUp(self):
        self.player = Player("test", 1, Difficulty.MEDIUM,
                             Color.BLACK, Color.BLACK, Color.BLACK)
        self.snake_game = SnakeGame(self.player)
        self.snake = self.snake_game.snake

    def test_first_position(self):
        self.assertEqual(self.snake.snake_x, 150)
        self.assertEqual(self.snake.snake_y, 150)

    def test_move_none(self):
        self.snake.move(None)
        self.assertEqual(self.snake.snake_x, 160)
        self.assertEqual(self.snake.snake_y, 150)

    def test_move_right(self):
        self.snake.move(Direction.RIGHT)
        self.assertEqual(self.snake.snake_x, 160)
        self.assertEqual(self.snake.snake_y, 150)

    def test_move_down(self):
        self.snake.move(Direction.DOWN)
        self.assertEqual(self.snake.snake_x, 150)
        self.assertEqual(self.snake.snake_y, 160)

    def test_move_left(self):
        self.snake.move(Direction.LEFT)
        self.assertEqual(self.snake.snake_x, 140)
        self.assertEqual(self.snake.snake_y, 150)

    def test_move_up(self):
        self.snake.move(Direction.UP)
        self.assertEqual(self.snake.snake_x, 150)
        self.assertEqual(self.snake.snake_y, 140)

    def test_grow(self):
        self.snake.grow()
        self.assertEqual(len(self.snake.body), 2)

    def test_collision_no_false_positive(self):
        self.snake.move_to(10, 50)
        self.assertTrue(not self.snake.collides())

    def test_collision_left(self):
        self.snake.move_to(-10, 10)
        self.assertTrue(self.snake.collides())

    def test_collision_top(self):
        self.snake.move_to(10, -10)
        self.assertTrue(self.snake.collides())

    def test_collision_right(self):
        self.snake.move_to(self.snake_game.game_x, 10)
        self.assertTrue(self.snake.collides())

    def test_collision_bottom(self):
        self.snake.move_to(10, self.snake_game.game_y)
        self.assertTrue(self.snake.collides())




    def test_collision_body(self):
        self.snake.move(Direction.RIGHT)
        self.snake.grow()
        self.snake.move(Direction.UP)
        self.snake.grow()
        self.snake.move(Direction.LEFT)
        self.snake.grow()
        self.snake.move(Direction.DOWN)
        self.snake.grow()
        self.assertTrue(self.snake.collides())
