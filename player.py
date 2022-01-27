from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.go_to_start()
        self.move_speed = 10

    def go_up(self):
        self.setheading(90)
        self.forward(10)

    def go_down(self):
        self.setheading(270)
        self.forward(10)

    def go_left(self):
        self.setheading(180)
        self.forward(10)

    def go_right(self):
        self.setheading(0)
        self.forward(10)

    def go_to_start(self):
        self.goto(self.xcor(), -280)

    def is_at_finish(self):
        if self.ycor() > 280:
            return True
        else:
            return False
