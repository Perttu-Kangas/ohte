from enums.game_enums import Direction


class Snake:
    """Luokka, joka kuvaa pelin matoa.

    Attributes:
        snake_game: SnakeGame-olio, jossa tämä Mato-olio on käytössä
        direction: Direction-olio, joka kuvaa madon nykyistä suuntaa
        body: Lista, joka kuvaa madon osia
        snake_x: Kokonaisluku, joka kuvaa madon pään x sijaintia pelikentällä
        snake_y: Kokonaisluku, joka kuvaa madon pään y sijaintia pelikentällä
    """

    def __init__(self, snake_game, snake_x, snake_y):
        """Luokan konstruktori, joka luo uuden madon.
        Asettaa automaattisesti ensimmäiseksi suunnaksi RIGHT.

        Args:
            snake_game: SnakeGame-olio, jossa tämä Mato-olio on käytössä
            snake_x: Kokonaisluku, joka määrittää madon x aloituspaikan
            snake_y: Kokonaisluku, joka määrittää madon y aloituspaikan
        """
        self.snake_game = snake_game
        self.direction = Direction.RIGHT
        self.body = [[snake_x, snake_y]]
        self.snake_x = snake_x
        self.snake_y = snake_y

    def move(self, direction):
        """Liikuttaa matoa annettuun suuntaan.
        Liikuessa, madon vanhin osa poistuu, ja etupäähän tulee uusi osa.
        Mato ei voi liikkua vastakkaiseen suuntaan kuin äsken.

        Args:
            direction: Direction-olio, joka määrittää madon uuden suunnan.
            Jos None, niin madon suunta ei muutu

        Returns:
            None
        """
        if not direction:
            direction = self.direction

        if self.direction == direction.opposite(direction):
            direction = self.direction

        self.direction = direction
        self.move_to(self.snake_x +
                     direction.value[0], self.snake_y + direction.value[1])

    def move_to(self, to_x, to_y):
        """Liikuttaa madon pään annettuun paikkaan kentällä, sekä päivittää vanhat osat.
        Liikuessa, madon vanhin osa poistuu, ja etupäähän tulee uusi osa.

        Args:
            to_x: Kokonaisluku, johon madon x siirretään
            to_y: Kokonaisluku, johon madon y siirretään

        Returns:
            None
        """
        self.snake_x = to_x
        self.snake_y = to_y
        self.body.append([self.snake_x, self.snake_y])
        self.body.pop(0)

    def grow(self):
        """Kasvattaa madon kokoa yhdellä sen nykyisissä koordinaateissa

        Returns:
            None
        """
        self.body.append([self.snake_x, self.snake_y])

    def collides(self):
        """Tarkastaa törmääkö mato seinien tai itsensä kanssa

        Returns:
            True, jos törmää seinän tai itsensä kanssa, muuten False
        """

        # Border collisions
        if self.snake_x < 0 or self.snake_y < 0 \
                or self.snake_x > self.snake_game.game_x - 10 \
                or self.snake_y > self.snake_game.game_y - 10:
            return True
        # Body collisions
        for body_part in self.body[:-1]:
            if self.snake_x == body_part[0] and self.snake_y == body_part[1]:
                return True
        return False
