from entities.player import Player
from enums.game_enums import Difficulty, Color

from repositories.player_repository import (
    player_repository as default_player_repository
)


class UILogic:

    def __init__(
            self,
            player_repository=default_player_repository
    ):
        self.player = None
        self.player_repository = player_repository

    def login(self, playername):
        player = self.player_repository.find_by_playername(playername)

        if not player:
            player = Player(playername, -1, Difficulty.MEDIUM, Color.RED, Color.BLACK, Color.GREEN)
            self.player = self.player_repository.create(player)
            return
        else:
            self.player = player

    def save(self):
        if not self.player:
            return
        self.player_repository.save_settings(self.player)


ui_logic = UILogic()
