import unittest
from enums.game_enums import Difficulty, Color
from repositories.player_repository import player_repository
from repositories.game_repository import game_repository
from services.ui_logic import UILogic
from entities.player import Player


class TestUILogic(unittest.TestCase):
    def setUp(self):
        player_repository.delete_data()
        game_repository.delete_data()
        self.player = Player("test", 1, Difficulty.MEDIUM,
                             Color.BLACK, Color.BLACK, Color.BLACK)
        self.ui_logic = UILogic()

    def test_login_non_existing_player(self):
        self.ui_logic.login("aaaa")
        self.assertEqual(self.ui_logic.player.difficulty, Difficulty.MEDIUM)
        self.assertEqual(self.ui_logic.player.apple_color, Color.RED)
        self.assertEqual(self.ui_logic.player.snake_color, Color.BLACK)
        self.assertEqual(self.ui_logic.player.background_color, Color.GREEN)

    def test_login_existing_player(self):
        player_repository.create(self.player)
        self.ui_logic.login("test")
        self.assertEqual(self.ui_logic.player.difficulty, Difficulty.MEDIUM)
        self.assertEqual(self.ui_logic.player.apple_color, Color.BLACK)
        self.assertEqual(self.ui_logic.player.snake_color, Color.BLACK)
        self.assertEqual(self.ui_logic.player.background_color, Color.BLACK)
