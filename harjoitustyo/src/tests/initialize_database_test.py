import unittest

from database_connection import get_database_connection
import initialize_database


class TestInitializeDatabase(unittest.TestCase):
    def setUp(self):
        self.connection = get_database_connection()
        initialize_database.drop_tables(self.connection)

    def test_tables_are_created_on_init(self):
        initialize_database.initialize_database()
        # These would throw OperationalError if not found, causing test failure
        self.connection.cursor().execute("SELECT * FROM players")
        self.connection.cursor().execute("SELECT * FROM player_settings")
        self.connection.cursor().execute("SELECT * FROM games")
        self.connection.commit()
