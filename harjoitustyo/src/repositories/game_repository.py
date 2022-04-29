from database_connection import get_database_connection
from entities.player import Player


class GameRepository:
    """Peliin liittyvistä tietokantaoperaatioista vastaava luokka"""

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Tietokantayhteyden Connection-olio
        """
        self.connection = connection

    def save_game(self, player: Player, points, time):
        """Tallentaa pelin annettujen argumenttien perusteella.

        Args:
            player: Player-olio joka pelasi pelin
            points: Kokonaisluku pelin pistemäärästä
            time: Kokonaisluku sekunteina peliä pelatusta ajast

        Returns:
            None
        """
        cursor = self.connection.cursor()

        cursor.execute("INSERT INTO games (player_id, points, time, difficulty) "
                       "VALUES (?, ?, ?, ?)",
                       (player.player_id, points, time, player.difficulty.name))

        self.connection.commit()

    def get_own_best(self, player: Player):
        """Hakee pelaajan parhaat pisteet, pisteet kaikenkaikkiaan ja aika kaikenkaikkiaan.

        Args:
            player: Player-olio, jonka parhaat tulokset haetaan

        Returns:
            Palauttaa listan, jossa 0 indeksissä on parhaat pisteet,
            1 indeksissä pisteet kaikenkaikkiaan ja
            2 indeksissä pelattu aika
        """
        cursor = self.connection.cursor()

        cursor.execute("SELECT MAX(points), SUM(points), SUM(time) FROM games WHERE player_id=?",
                       (player.player_id,))

        return cursor.fetchone()

    def get_three_best(self, difficulty):
        """Hakee kolme parasta pelaajaa annetulla vaikeusasteella.

        Args:
            difficulty: Merkkijonona vaikeuaste, jonka perusteella kolme parasta pelaajaa haetaan

        Returns:
            Palauttaa listan kolmesta parhaasta pelaajasta, missä 0 indeksissä on paras pelaaja.
            Jokainen indeksi sisältää pelaajanimen 0 indekissä ja pisteed 1 indeksissä.
        """
        cursor = self.connection.cursor()

        cursor.execute("SELECT P.playername, MAX(G.points) "
                       "FROM players P, games G WHERE G.difficulty=? AND P.player_id=G.player_id "
                       "GROUP BY P.player_id ORDER BY MAX(G.points) DESC LIMIT 3",
                       (difficulty,))

        return cursor.fetchall()

    def delete_data(self):
        """Poistaa kaikki pelaajat, asetukset ja pelit"""
        cursor = self.connection.cursor()

        cursor.execute("DELETE FROM players")
        cursor.execute("DELETE FROM player_settings")
        cursor.execute("DELETE FROM games")

        self.connection.commit()


game_repository = GameRepository(get_database_connection())
