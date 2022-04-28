class Player:
    """Luokka, joka kuvaa pelaajaa

    Attributes:
        name: Merkkijono, joka sisältää pelaajanimen
        player_id: Kokonaisluku, joka on uniikki jokaiselle pelaajalle
        difficulty: Difficulty-olio, joka on pelaajan valitsema vaikeusaste
        apple_color: Color-olio, joka on pelaajan valitsema omenan väri
        snake_color: Color-olio, joka on pelaajan valitsema madon väri
        background_color: Color-olio, joka on pelaajan valitsema pelikentän väri
    """

    def __init__(self, name, player_id, difficulty, apple, snake, background):
        """Luokan konstruktori, joka luo uuden pelaajan.

        Args:
            name: Merkkijono pelaajan nimestä
            player_id: Kokonaislukuna pelaajan id
            difficulty: Difficulty-oliona pelaajan vaikeusaste
            apple: Color-oliona pelaajan omenan väri
            snake: Color-oliona pelaajan madon väri
            background:  Color-oliona pelaajan pelikentän väri
        """
        self.name = name
        self.player_id = player_id
        self.difficulty = difficulty
        self.apple_color = apple
        self.snake_color = snake
        self.background_color = background
