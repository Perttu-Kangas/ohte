import time

import pygame

from entities.apple import Apple
from entities.player import Player
from entities.snake import Snake
from enums.game_enums import Direction

from repositories.game_repository import (
    game_repository as default_game_repository
)


class SnakeGame:

    def __init__(
            self,
            player: Player,
            game_repository=default_game_repository
    ):
        """Luo uuden snake game -olion

        Args:
            player: Player-olio, joka tulee pelaamaan peliä
            game_repository: Pelitietokantaa vastaava olio
        """
        self.snake_game_loop = None
        self.game_x = 300
        self.game_y = 300
        self.player = player
        self.snake = Snake(self, 150, 150)
        self.apple = Apple(self)
        self.game_repository = game_repository
        self.start_time = None

    def start(self, game_end_view):
        """Aloittaa peliloopin

        Args:
            game_end_view: Pelinpäättymisnäkymä, joka näytetään pelin loppuessa

        Returns:
            None
        """
        self.snake_game_loop = SnakeGameLoop(self, self.player)

        self.start_time = time.time()

        while True:
            if not self.snake_game_loop.tick():
                pygame.quit()
                self.save_game()
                game_end_view(points=self.snake_game_loop.points)
                break

    def save_game(self):
        """Tallentaa pelatun pelin tulokset ylös

        Returns:
            None
        """
        if not self.game_repository:
            return

        duration = int(time.time() - self.start_time)
        self.game_repository.save_game(
            self.player, self.snake_game_loop.points, duration)


class SnakeGameLoop:

    def __init__(self, snake_game: SnakeGame, player: Player):
        """Luo uuden peliloopin

        Args:
            snake_game: Objekti, joka sisältää pelin asetuksia
            player: Player-olio, joka pelaa peliä
        """
        self.player = player
        pygame.init()
        pygame.display.set_caption("Pisteet: 0")
        self.game = snake_game
        self.display = pygame.display.set_mode(
            (self.game.game_x, self.game.game_y))
        self.clock = pygame.time.Clock()
        self.points = 0

    def tick(self):
        """Kutsutaan aina, kun pelin pitäisi päivittyä.
        Hoitaa näppäinpainalluksien kuuntelemisen, pisteiden laskemisen,
        törmäyksien tarkistamisen, piirtämisen ja kaiken,
        mitä pelissä tapahtuukaan.

        Returns:
            False, jos pelin pitäisi päättyä
        """
        if not self.handle_events():
            return False
        if self.game.snake.collides():
            return False
        if self.game.apple.collides():
            self.game.snake.grow()
            self.game.apple.move()
            self.points += 1
            pygame.display.set_caption("Pisteet: " + str(self.points))
        self.draw()
        pygame.display.update()
        self.fps()
        return True

    def fps(self):
        """Ajastaa ruudunpäivitykset, joiden avulla
        määritellään pelin vaikeusastekkin.

        Returns:
            None
        """
        self.clock.tick(self.player.difficulty.value)

    def draw(self):
        """Piirtää pelikentän.
        Täyttää värillä sekä piirtää madon ja omenan

        Returns:
            None
        """
        self.display.fill(self.player.background_color.value)
        for body_part in self.game.snake.body:
            pygame.draw.rect(self.display,
                             self.player.snake_color.value,
                             pygame.Rect(body_part[0], body_part[1], 10, 10))
        pygame.draw.rect(self.display,
                         self.player.apple_color.value,
                         pygame.Rect(self.game.apple.apple_x, self.game.apple.apple_y, 10, 10))

    def handle_events(self):
        """Kuuntelee näppäinpainalluksia,
        sekä liikuttaa matoa niiden mukaan

        Returns:
            False, jos pelin pitäisi päättyä
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.game.snake.move(Direction.LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.game.snake.move(Direction.RIGHT)
                elif event.key == pygame.K_UP:
                    self.game.snake.move(Direction.UP)
                elif event.key == pygame.K_DOWN:
                    self.game.snake.move(Direction.DOWN)
                else:
                    self.game.snake.move(None)
                return True
            if event.type == pygame.QUIT:
                return False
        self.game.snake.move(None)
        return True
