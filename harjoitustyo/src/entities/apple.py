import random


class Apple:
    """Luokka, joka kuvaa pelin omenaa

    Attributes:
        snake_game: SnakeGame-olio, jossa tämä Apple-olio on käytössä
        apple_x: Kokonaisluku, joka kuvaa omenan x sijaintia pelikentällä
        apple_y: Kokonaisluku, joka kuvaa omenan y sijaintia pelikentällä
    """

    def __init__(self, snake_game):
        """Luokan konstruktori, joka luo uuden omenan.
        Asettaa automaattisesti omenan satunnaiseen paikkaan pelikentällä.

        Args:
            snake_game: SnakeGame-olio, johon tämä Apple-olio tulee käyttöön
        """
        self.snake_game = snake_game
        self.apple_x = random.randrange(
            1, (snake_game.game_x // 10)) * 10
        self.apple_y = random.randrange(
            1, (snake_game.game_y // 10)) * 10

    def move(self):
        """Liikuttaa omenaa kentällä uuteen satunnaiseen paikkaan.

        Returns:
            None
        """
        self.move_to(random.randrange(1, (self.snake_game.game_x // 10)) * 10,
                     random.randrange(1, (self.snake_game.game_y // 10)) * 10)

    def move_to(self, to_x, to_y):
        """Liikuttaa omenaa tiettyyn paikkaan kentällä

        Args:
            to_x: Kokonaisluku, johon omenan x siirretään
            to_y: Kokonaisluku, johon omenan y siirretään

        Returns:
            None
        """
        self.apple_x = to_x
        self.apple_y = to_y

    def collides(self):
        """Tarkastaa onko madon pää omenan kohdalla.

        Returns:
            True, jos omena ja mato ovat samassa kohdassa pelikentällä, muuten False
        """
        return self.snake_game.snake.snake_x == self.apple_x and self.snake_game.snake.snake_y == self.apple_y
