from turtle import Turtle

WIDTH = 8
HEIGHT = 1


class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.penup()
        self.shape('square')
        self.turtlesize(stretch_wid=WIDTH, stretch_len=HEIGHT)
        self.color('white')
        self.goto(x_pos, 0)

    def move(self):
        self.forward(10)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
