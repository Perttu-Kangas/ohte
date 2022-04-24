from entities.player import Player
from enums.game_enums import Difficulty, Color

from repositories.player_repository import (
    player_repository as default_player_repository
)

from repositories.game_repository import (
    game_repository as default_game_repository
)


class UILogic:

    def __init__(
            self,
            player_repository=default_player_repository,
            game_repository=default_game_repository
    ):
        self.player = None
        self.player_repository = player_repository
        self.game_repository = game_repository

    def login(self, playername):
        player = self.player_repository.find_by_playername(playername)

        if not player:
            player = Player(playername, -1, Difficulty.MEDIUM,
                            Color.RED, Color.BLACK, Color.GREEN)
            self.player = self.player_repository.create(player)
            return
        else:
            self.player = player

    def save_player(self):
        self.player_repository.save_settings(self.player)

    def get_own_best(self):
        return self.game_repository.get_own_best(self.player)

    def get_ten_best(self):
        return self.game_repository.get_ten_best(self.player.difficulty.name)


ui_logic = UILogic()
