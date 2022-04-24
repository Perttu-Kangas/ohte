from database_connection import get_database_connection
from entities.player import Player


class GameRepository:

    def __init__(self, connection):
        self.connection = connection

    def save_game(self, player: Player, points, time):
        cursor = self.connection.cursor()

        cursor.execute("INSERT INTO games (player_id, points, time, difficulty) VALUES (?, ?, ?, ?)",
                       (player.player_id, points, time, player.difficulty.name))

        self.connection.commit()

    def get_own_best(self, player: Player):
        cursor = self.connection.cursor()

        cursor.execute("SELECT MAX(points), SUM(points), SUM(time) FROM games WHERE player_id=?",
                       (player.player_id,))

        return cursor.fetchone()

    def get_ten_best(self, difficulty):
        cursor = self.connection.cursor()

        cursor.execute("SELECT P.playername, MAX(G.points) "
                       "FROM players P, games G WHERE G.difficulty=? AND P.player_id=G.player_id "
                       "GROUP BY P.player_id ORDER BY MAX(G.points) DESC LIMIT 3",
                       (difficulty,))

        return cursor.fetchall()


game_repository = GameRepository(get_database_connection())
