import pygame
from services.snake_game import SnakeGame

pygame.init()
pygame.display.set_caption("Snake Game")
snake_game = SnakeGame()

while True:
    if snake_game.tick():
        pygame.quit()
        break
