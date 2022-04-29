from entities.player import Player
from database_connection import get_database_connection
from enums.game_enums import Difficulty, Color


def get_user_by_row(row):
    return Player(row["playername"],
                  row["player_id"],
                  Difficulty[row["difficulty"]],
                  Color[row["apple"]],
                  Color[row["snake"]],
                  Color[row["background"]]) if row else None


class PlayerRepository:
    """Pelaajaan liittyvistä tietokantaoperaatioista vastaava luokka"""

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Tietokantayhteyden Connection-olio
        """
        self.connection = connection

    def find_by_playername(self, playername):
        """Hakee pelaajan annetun pelinimen perusteella.

        Args:
            playername: Merkkijono, joka sisältää pelaajan nimen

        Returns:
            Player-olio tai None, jos pelaajaa ei löydy tietokannasta
        """
        cursor = self.connection.cursor()

        cursor.execute("SELECT P.player_id, P.playername, PS.apple, "
                       "PS.snake, PS.background, PS.difficulty "
                       "FROM players P, player_settings PS "
                       "WHERE P.playername=? AND P.player_id=PS.player_id",
                       (playername,))

        return get_user_by_row(cursor.fetchone())

    def create(self, player: Player):
        """Tallentaa annetun Player-olion tietokantaan

        Args:
            player: Player-olio, jonka tiedot tallennetaan

        Returns:
            Tallennetun Player-olion
        """
        cursor = self.connection.cursor()

        cursor.execute("INSERT INTO players (playername) VALUES (?)",
                       (player.name,))

        player.player_id = cursor.lastrowid

        cursor.execute("INSERT INTO player_settings (player_id, apple, "
                       "snake, background, difficulty) "
                       "VALUES (?, ?, ?, ?, ?)",
                       (player.player_id, player.apple_color.name, player.snake_color.name,
                        player.background_color.name, player.difficulty.name))

        self.connection.commit()

        return player

    def save_settings(self, player: Player):
        """Päivittää annetun Player-olion asetukset tietokantaan

        Args:
            player: Player-olio, jonka asetukset päivitetään

        Returns:
            None
        """
        cursor = self.connection.cursor()

        cursor.execute("UPDATE player_settings SET apple=?, "
                       "snake=?, background=?, difficulty=? "
                       "WHERE player_id=?",
                       (player.apple_color.name, player.snake_color.name,
                        player.background_color.name, player.difficulty.name,
                        player.player_id))

        self.connection.commit()

    def delete_data(self):
        """Poistaa kaikki pelaajat ja asetukset"""
        cursor = self.connection.cursor()

        cursor.execute("DELETE FROM players")
        cursor.execute("DELETE FROM player_settings")

        self.connection.commit()


player_repository = PlayerRepository(get_database_connection())
