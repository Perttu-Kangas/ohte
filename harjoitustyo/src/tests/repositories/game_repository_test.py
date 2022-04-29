import unittest
from repositories.player_repository import player_repository
from repositories.game_repository import game_repository
from entities.player import Player
from enums.game_enums import Difficulty, Color


class TestGameRepository(unittest.TestCase):
    def setUp(self):
        player_repository.delete_data()
        game_repository.delete_data()
        self.p1 = Player("p1", 1, Difficulty.MEDIUM, Color.BLACK, Color.BLACK, Color.BLACK)

    def test_save_game(self):
        game_repository.save_game(self.p1, 10, 20)
        own_value = game_repository.get_own_best(self.p1)
        self.assertEqual(own_value[0], 10)
        self.assertEqual(own_value[1], 10)
        self.assertEqual(own_value[2], 20)

    def test_get_own_best(self):
        game_repository.save_game(self.p1, 15, 20)
        game_repository.save_game(self.p1, 10, 20)
        game_repository.save_game(self.p1, 30, 20)
        own_value = game_repository.get_own_best(self.p1)
        self.assertEqual(own_value[0], 30)
        self.assertEqual(own_value[1], 55)
        self.assertEqual(own_value[2], 60)

    def test_three_best(self):
        p2 = Player("p2", 1, Difficulty.MEDIUM, Color.BLACK, Color.BLACK, Color.BLACK)
        p3 = Player("p3", 1, Difficulty.MEDIUM, Color.BLACK, Color.BLACK, Color.BLACK)
        p4 = Player("p4", 1, Difficulty.MEDIUM, Color.BLACK, Color.BLACK, Color.BLACK)

        player_repository.create(self.p1)
        player_repository.create(p2)
        player_repository.create(p3)
        player_repository.create(p4)

        game_repository.save_game(self.p1, 10, 1)
        game_repository.save_game(p2, 1, 1)
        game_repository.save_game(p3, 15, 1)
        game_repository.save_game(p4, 40, 1)

        three_best = game_repository.get_three_best(self.p1.difficulty.name)

        self.assertEqual(three_best[0][0], p4.name)
        self.assertEqual(three_best[1][0], p3.name)
        self.assertEqual(three_best[2][0], self.p1.name)

    def test_three_best_difficulty(self):
        p2 = Player("p2", 1, Difficulty.MEDIUM, Color.BLACK, Color.BLACK, Color.BLACK)
        p3 = Player("p3", 1, Difficulty.MEDIUM, Color.BLACK, Color.BLACK, Color.BLACK)

        p4 = Player("p4", 1, Difficulty.HARD, Color.BLACK, Color.BLACK, Color.BLACK)

        player_repository.create(self.p1)
        player_repository.create(p2)
        player_repository.create(p3)
        player_repository.create(p4)

        game_repository.save_game(self.p1, 10, 1)
        game_repository.save_game(p2, 1, 1)
        game_repository.save_game(p3, 15, 1)
        game_repository.save_game(p4, 40, 1)

        three_best = game_repository.get_three_best(self.p1.difficulty.name)

        self.assertEqual(three_best[0][0], p3.name)
        self.assertEqual(three_best[1][0], self.p1.name)
        self.assertEqual(three_best[2][0], p2.name)
