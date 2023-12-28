from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.setheading(random.randint(0, 90))
        self.penup()
        self.x_move = 1
        self.y_move = 1
        self.move_speed = 0.01

    def move(self):
        new_x = self.xcor()+ self.x_move  # we can change this to move by any number (number here is pixel it moves, 1 moves slowly, 10 moves fast)
        new_y = self.ycor()+ self.y_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.5

    def ball_reset(self):
        self.goto(0,0)
        self.move_speed = 0.01
        self.x_bounce()





