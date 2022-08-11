import turtle
from snake import Snake
from food import Food
from score import Score
import time


screen = turtle.Screen()
screen.title('SNAKE')
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkeypress(key='a',fun=snake.left)
screen.onkeypress(key='d',fun=snake.right)
screen.onkeypress(key='w',fun=snake.up)
screen.onkeypress(key='s',fun=snake.down)


while True:
    snake.move()
    time.sleep(0.05)
    screen.update()
    if snake.head.distance(food) < 12:
        food.refresh()
        score.scorecount()
        snake.grow()
    if snake.detect_colision_wall():
        score.set_high_score()
        score.gameover()
        break
    if snake.detectcolisionsnake():
        score.set_high_score()
        score.gameover()
        break



screen.exitonclick()