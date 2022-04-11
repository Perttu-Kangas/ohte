import pygame

from entities.apple import Apple
from entities.player import Player
from entities.snake import Snake
from enums.game_enums import Direction


class SnakeGame:

    def __init__(self, player: Player, show_main_view):
        self.snake_game_loop = None
        self.game_x = 300
        self.game_y = 300
        self.player = player
        self.snake = Snake(self, 150, 150)
        self.apple = Apple(self)
        self.show_main_view = show_main_view

    def start(self):
        self.snake_game_loop = SnakeGameLoop(self, self.player)
        while True:
            if self.snake_game_loop.tick():
                pygame.quit()
                self.show_main_view()
                break


class SnakeGameLoop:

    def __init__(self, snake_game: SnakeGame, player: Player):
        self.player = player
        pygame.init()
        pygame.display.set_caption("Matopeli")
        self.game = snake_game
        self.display = pygame.display.set_mode(
            (self.game.game_x, self.game.game_y))
        self.clock = pygame.time.Clock()

    def tick(self):
        if not self.handle_events():
            return True
        if self.game.snake.collides():
            return True
        if self.game.apple.collides(self.game.snake):
            self.game.snake.grow()
            self.game.apple.move()
        self.draw()
        pygame.display.update()
        self.clock.tick(self.player.difficulty.value)
        return False

    def draw(self):
        self.display.fill(self.player.background_color.value)
        for body_part in self.game.snake.body:
            pygame.draw.rect(self.display,
                             self.player.snake_color.value,
                             pygame.Rect(body_part[0], body_part[1], 10, 10))
        pygame.draw.rect(self.display,
                         self.player.apple_color.value,
                         pygame.Rect(self.game.apple.x, self.game.apple.y, 10, 10))

    def handle_events(self):
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
