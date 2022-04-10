import pygame
from enums.game_enums import Difficulty, Color, Direction
from entities.snake import Snake
from entities.apple import Apple


class SnakeGame:

    def __init__(self):
        self.snake_game_loop = None
        self.game_x = 300
        self.game_y = 300
        self.difficulty = Difficulty.EASY
        self.apple_color = Color.RED
        self.snake_color = Color.BLACK
        self.background_color = Color.GREEN
        self.snake = Snake(self, 150, 150)
        self.apple = Apple(self)

    def start(self):
        self.snake_game_loop = SnakeGameLoop(self)
        while True:
            if self.snake_game_loop.tick():
                pygame.quit()
                break


class SnakeGameLoop:

    def __init__(self, snake_game: SnakeGame):
        pygame.init()
        pygame.display.set_caption("Snake Game")
        self.game = snake_game
        self.display = pygame.display.set_mode((self.game.game_x, self.game.game_y))
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
        self.clock.tick(self.game.difficulty.value)

    def draw(self):
        self.display.fill(self.game.background_color.value)
        for body_part in self.game.snake.body:
            pygame.draw.rect(self.display, self.game.snake_color.value, pygame.Rect(body_part[0], body_part[1], 10, 10))
        pygame.draw.rect(self.display, self.game.apple_color.value, pygame.Rect(self.game.apple.x, self.game.apple.y, 10, 10))

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
            elif event.type == pygame.QUIT:
                return False
        self.game.snake.move(None)
        return True
