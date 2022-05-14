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
        self.apple_x = 0
        self.apple_y = 0
        self.move()

    def move(self):
        """Liikuttaa omenaa kentällä uuteen satunnaiseen paikkaan.

        Returns:
            None
        """

        # Really inefficient way of doing this
        # Way better solution: keep list of free points in board,
        # and from them generate new random spot
        while True:
            new_x = random.randrange(1, (self.snake_game.game_x // 10)) * 10
            new_y = random.randrange(1, (self.snake_game.game_y // 10)) * 10

            if self.apple_x != new_x and self.apple_y != new_y:
                self.move_to(new_x, new_y)
                break

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
        return self.snake_game.snake.snake_x == self.apple_x \
            and self.snake_game.snake.snake_y == self.apple_y
