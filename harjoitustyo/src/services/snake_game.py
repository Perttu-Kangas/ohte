import pygame
from enums.game_enums import Difficulty, Color, Direction
from entities.snake import Snake
from entities.apple import Apple


class SnakeGame:

    def __init__(self):
        self.game_x = 300
        self.game_y = 300
        self.display = pygame.display.set_mode((self.game_x, self.game_y))
        self.difficulty = Difficulty.EASY
        self.apple_color = Color.RED
        self.snake_color = Color.BLACK
        self.background_color = Color.GREEN
        self.snake = Snake(self, 150, 150)
        self.apple = Apple(self)
        self.clock = pygame.time.Clock()

    def tick(self):
        if not self.handle_events():
            return True
        if self.snake.collides():
            return True
        if self.apple.collides(self.snake):
            self.snake.grow()
            self.apple.move()
        self.draw()
        pygame.display.update()
        self.clock.tick(self.difficulty.value)

    def draw(self):
        self.display.fill(self.background_color.value)
        for body_part in self.snake.body:
            pygame.draw.rect(self.display, self.snake_color.value, pygame.Rect(body_part[0], body_part[1], 10, 10))
        pygame.draw.rect(self.display, self.apple_color.value, pygame.Rect(self.apple.x, self.apple.y, 10, 10))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.snake.move(Direction.LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.snake.move(Direction.RIGHT)
                elif event.key == pygame.K_UP:
                    self.snake.move(Direction.UP)
                elif event.key == pygame.K_DOWN:
                    self.snake.move(Direction.DOWN)
                else:
                    self.snake.move(None)
                return True
            elif event.type == pygame.QUIT:
                return False
        self.snake.move(None)
        return True
