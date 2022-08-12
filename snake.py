import turtle
up = 90
right = 0
left = 180
down = 270

class Snake:
    def __init__(self):
        self.snake_body = []
        self.createsnake()
        self.head = self.snake_body[0]


    def createsnake(self):
        x = 0
        for c in range(3):
            snake = turtle.Turtle('square')
            snake.penup()
            snake.color('white')
            if c == 0:
                snake.color('green')
            snake.shapesize(0.5)
            snake.speed(0)
            x += 10
            self.snake_body.append(snake)


    def move(self):
        for snake_piece in range(len(self.snake_body) - 1, 0, -1):
            pos = self.snake_body[snake_piece - 1].pos()
            self.snake_body[snake_piece].goto(pos)
        self.head.forward(10)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)


    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)


    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)


    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def grow(self):
        snake = turtle.Turtle('square')
        snake.color('white')
        snake.penup()
        snake.shapesize(0.5)
        snake.setpos(self.snake_body[-1].pos())
        self.snake_body.append(snake)

    def detect_colision_wall(self):
        if self.head.xcor() <= -295 or self.head.xcor() >= 295 or self.head.ycor() <= -295 or self.head.ycor() >= 295:
            return True


    def detect_colision_snake(self):
        for i in range(1,len(self.snake_body)):
            if self.head.distance(self.snake_body[i]) < 5:
                return True

    def reset(self):
        for seg in self.snake_body:
            seg.goto(1000,1000)
        self.snake_body.clear()
        self.createsnake()
        self.head = self.snake_body[0]

