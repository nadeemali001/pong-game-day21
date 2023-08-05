from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

scn = Screen()
l_pad = Paddle((-350, 0))
r_pad = Paddle((350, 0))
ball = Ball()
score = Score()


scn.setup(width=800, height=600)
scn.bgcolor('black')
scn.title('Pong Game')
scn.tracer(0)



scn.listen()
scn.onkey(r_pad.move_up, "Up")
scn.onkey(r_pad.move_down, 'Down')
scn.onkey(l_pad.move_up, "w")
scn.onkey(l_pad.move_down, 's')


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    scn.update()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(r_pad) <= 50 and ball.xcor() >= 320 or ball.distance(l_pad) <= 50 and ball.xcor() <= -320:
        ball.x_bounce()

    if ball.xcor() > 380:
        ball.reset()
        score.l_score_up()

    if ball.xcor() < -380:
        ball.reset()
        score.r_score_up()

scn.exitonclick()