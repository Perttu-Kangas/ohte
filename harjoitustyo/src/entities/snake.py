from enums.game_enums import Direction


class Snake:

    def __init__(self, snake_game, x, y):
        self.snake_game = snake_game
        self.direction = Direction.RIGHT
        self.body = [[x, y]]
        self.x = x
        self.y = y

    def move(self, direction):
        if not direction:
            direction = self.direction
        self.direction = direction
        self.move_to(self.x + direction.value[0], self.y + direction.value[1])

    def move_to(self, x, y):
        self.x = x
        self.y = y
        self.body.append([self.x, self.y])
        self.body.pop(0)

    def grow(self):
        self.body.append([self.x, self.y])

    def collides(self):
        # Border collisions
        if self.x < 0 or self.y < 0 or self.x > self.snake_game.game_x or self.y > self.snake_game.game_y:
            return True
        # Body collisions
        for body_part in self.body[:-1]:
            if self.x == body_part[0] and self.y == body_part[1]:
                return True
        return False
