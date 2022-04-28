from entities.player import Player
from enums.game_enums import Difficulty, Color

from repositories.player_repository import (
    player_repository as default_player_repository
)

from repositories.game_repository import (
    game_repository as default_game_repository
)


class UILogic:
    """Sovelluksen käyttöliittymälogiikasta vastaava luokka"""

    def __init__(
            self,
            player_repository=default_player_repository,
            game_repository=default_game_repository
    ):
        """Luokan konstruktori. Luo uuden käyttöliittymälogiikasta vastaavan palvelun.

        Args:
            player_repository:
                Vapaaehtoinen, oletusarvolaan PlayerRepository-olio.
                Olio, jolla on PlayerRepository-luokkaa vastaavat metodit.
            game_repository:
                Vapaaehtoinen, oletusarvolaan GameRepository-olio.
                Olio, jolla on GameRepository-luokkaa vastaavat metodit.
        """
        self.player = None
        self.player_repository = player_repository
        self.game_repository = game_repository

    def login(self, playername):
        """Kirjaa pelaajan sisään, tai luo uuden pelaajan ja kirjaa sisään.

        Args:
            playername: Merkkijono, joka sisältää pelaajan nimen

        Returns:
            None
        """
        player = self.player_repository.find_by_playername(playername)

        if not player:
            player = Player(playername, -1, Difficulty.MEDIUM,
                            Color.RED, Color.BLACK, Color.GREEN)
            self.player = self.player_repository.create(player)
        else:
            self.player = player

    def save_player(self):
        """Päivittää kirjautuneen pelaajan asetukset tietokantaan.

        Returns:
            None
        """
        self.player_repository.save_settings(self.player)

    def get_own_best(self):
        """Hakee kirjatuneen pelaajan parhaat pisteet, aikaa pelattu, sekä pisteitä kaikenkaikkiaan.

        Returns:
            Palauttaa listan, jossa 0 indeksissä on parhaat pisteet,
            1 indeksissä pisteet kaikenkaikkiaan ja
            2 indeksissä pelattu aika
        """
        return self.game_repository.get_own_best(self.player)

    def get_three_best(self):
        """Hakee kirjautuneen käyttäjän vaikeuasteella kolme parasta pelaajaa.

        Returns:
            Palauttaa listan kolmesta parhaasta pelaajasta, missä 0 indeksissä on paras pelaaja.
            Jokainen indeksi sisältää pelaajanimen 0 indekissä ja pisteed 1 indeksissä.
        """
        return self.game_repository.get_three_best(self.player.difficulty.name)


ui_logic = UILogic()
