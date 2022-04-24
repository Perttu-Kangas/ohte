from enums.game_enums import Direction


class Snake:

    def __init__(self, snake_game, snake_x, snake_y):
        self.snake_game = snake_game
        self.direction = Direction.RIGHT
        self.body = [[snake_x, snake_y]]
        self.snake_x = snake_x
        self.snake_y = snake_y

    def move(self, direction):
        if not direction:
            direction = self.direction
        self.direction = direction
        self.move_to(self.snake_x +
                     direction.value[0], self.snake_y + direction.value[1])

    def move_to(self, to_x, to_y):
        self.snake_x = to_x
        self.snake_y = to_y
        self.body.append([self.snake_x, self.snake_y])
        self.body.pop(0)

    def grow(self):
        self.body.append([self.snake_x, self.snake_y])

    def collides(self):
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
