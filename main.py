from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

s = Screen()
s.setup(width=800, height=600)
s.bgcolor('black')
s.title('Pong')
s.tracer(0)

right_paddle = Paddle(350)
left_paddle = Paddle(-350)
ball = Ball()
score = Scoreboard()

s.listen()
s.onkey(right_paddle.up, "Up")
s.onkey(right_paddle.down, "Down")
s.onkey(left_paddle.up, "w")
s.onkey(left_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 60 and ball.xcor() > 320 or ball.distance(left_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() < -380:
        ball.reset_position()
        score.up('right')

    if ball.xcor() > 380:
        ball.reset_position()
        score.up('left')

s.exitonclick()
