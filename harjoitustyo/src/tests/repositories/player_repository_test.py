import unittest
from repositories.player_repository import player_repository
from entities.player import Player
from enums.game_enums import Difficulty, Color


class TestPlayerRepository(unittest.TestCase):
    def setUp(self):
        player_repository.delete_data()
        self.p1 = Player("p1", 1, Difficulty.MEDIUM,
                         Color.BLACK, Color.BLACK, Color.BLACK)
        self.p2 = Player("p2", 2, Difficulty.HARD,
                         Color.GREEN, Color.GREEN, Color.GREEN)

    def test_create(self):
        player_repository.create(self.p1)
        created_player = player_repository.find_by_playername("p1")
        self.assertEqual(created_player.name, self.p1.name)
        self.assertEqual(created_player.difficulty, self.p1.difficulty)
        self.assertEqual(created_player.apple_color, self.p1.apple_color)
        self.assertEqual(created_player.snake_color, self.p1.snake_color)
        self.assertEqual(created_player.background_color,
                         self.p1.background_color)

    def test_find_by_name(self):
        player_repository.create(self.p2)
        created_player = player_repository.find_by_playername("p2")
        self.assertEqual(created_player.name, self.p2.name)

    def test_save_settings(self):
        player_repository.create(self.p1)

        self.p1.difficulty = Difficulty.EASY
        self.p1.apple_color = Color.RED
        self.p1.snake_color = Color.RED
        self.p1.background_color = Color.RED

        player_repository.save_settings(self.p1)

        created_player = player_repository.find_by_playername("p1")

        self.assertEqual(created_player.difficulty, Difficulty.EASY)
        self.assertEqual(created_player.apple_color, Color.RED)
        self.assertEqual(created_player.snake_color, Color.RED)
        self.assertEqual(created_player.background_color, Color.RED)
