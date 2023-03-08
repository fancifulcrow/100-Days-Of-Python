from turtle import Turtle

# Variables used but are outside the class are written in upper case
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []

        for snake_index in range(0, 3):
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(x=(snake_index * -20), y=0)
            self.segments.append(new_segment)

        self.head = self.segments[0]

    def move(self):
        for seg_index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_index - 1].xcor()
            new_y = self.segments[seg_index - 1].ycor()
            self.segments[seg_index].goto(x=new_x, y=new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
