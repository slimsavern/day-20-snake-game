from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.start()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        body = Turtle()
        body.color("white")
        body.shape("square")
        body.penup()
        body.goto(position)
        self.segments.append(body)

    def start(self):
        for segment in range(3):
            body = Turtle()
            body.color("white")
            body.shape("square")
            body.penup()
            body.goto(body.xcor() - segment * 20, body.ycor())
            self.segments.append(body)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)

    def reset(self):

        for seg in self.segments:
            seg.goto(1000,1000)

        self.segments.clear()
        self.start()
        self.head = self.segments[0]


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
