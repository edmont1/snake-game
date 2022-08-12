from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.shapesize(0.35)
        self.setpos(100,100)


    def refresh(self):
        self.setpos(random.randint(-280,280),random.randint(-280,280))

