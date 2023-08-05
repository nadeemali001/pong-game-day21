from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        #self.shapesize(stretch_len=2, stretch_wid=2)
        self.fillcolor('white')
        self.color('white')
        self.goto(0, 0)
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.1
        self.penup()

    def move_ball(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.move_y *= -1

    def x_bounce(self):
        self.move_x *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_bounce()