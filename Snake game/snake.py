from turtle import Turtle, Screen

x = [0, 20, 40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

screen = Screen()


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for turtle in range(0, 3):
            ryu = Turtle(shape="square")
            ryu.shape("square")
            ryu.color("white")
            ryu.penup()
            ryu.goto(x=x[turtle], y=0)
            self.segments.append(ryu)

    def move(self):
        for seg_num in range(2, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading != LEFT:
            self.head.setheading(RIGHT)


