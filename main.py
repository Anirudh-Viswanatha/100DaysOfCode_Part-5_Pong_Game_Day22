from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

# Designing the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong Game")
screen.tracer(0)

# Creating 2 objects (Right and Left Paddles) from Paddle Class
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# ball creation
ball = Ball()
score = Score()

# Listening to keys to go up/Down
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)            # To slow the ball we can either use this time.sleep or moving ball by less number of pixels mentioned in move method in ball class
    screen.update()
    ball.move()

    #Detect collision with the wall
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.y_bounce()

    # Detect collision with right  and left paddle
    if ball.xcor()> 330 and ball.distance(r_paddle) < 50 or ball.xcor()< -330 and ball.distance(l_paddle) < 50:
        ball.x_bounce()

    # Detect Collision miss by right paddle
    if ball.xcor() > 370:
        ball.ball_reset()
        score.l_point()

    # Detect Collision miss by left paddle
    if ball.xcor() < -370:
        ball.ball_reset()
        score.r_point()









# # Screen Division
# timmy = Turtle("square")
# timmy.color("white")
# timmy.left(90)
# timmy.penup()
# timmy.forward(380)
# timmy.setheading(270)
# for i in range(20):
#     timmy.pendown()
#     timmy.pensize(10)
#     timmy.forward(20)
#     timmy.penup()
#     timmy.forward(20)




screen.exitonclick()

