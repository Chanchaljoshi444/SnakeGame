from turtle import Turtle
SEGMENT_POSITIONS = [(0, 0), (-20, 0), (-40, 0),(-60,0)]
class Snake:
    def __init__(self,screen,shape = "square"):  #sets the default value as square, changes if user enters an arg
        self.segments =[]
        self.shape = shape
        self.screen = screen
        self.create_snake()

    # turtle.shapesize(stretch_len=3) this doesn't work because the whole snake takes a turn like a block
    # we need to create three square blocks which move one after the other
    def create_snake(self):
        for position in SEGMENT_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle(self.shape)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def increase_length(self):
        self.add_segment(self.segments[-1].position())


    # when the first segment moves the last one takes place on the second to last and so on
    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            self.segments[segment].goto(self.segments[segment-1].pos())

        self.segments[0].forward(20)

    def go_up(self):

        if self.segments[0].heading() == 0 or self.segments[0].heading() == 180:
            self.segments[0].setheading(90)

    def go_down(self):

        if self.segments[0].heading() == 0 or self.segments[0].heading() == 180:
            self.segments[0].setheading(270)

    def go_right(self):

        if self.segments[0].heading() == 90 or self.segments[0].heading() == 270:
            self.segments[0].setheading(0)

    def go_left(self):

        if self.segments[0].heading() == 90 or self.segments[0].heading() == 270:
            self.segments[0].setheading(180)

    def binding_keys(self):

        self.screen.listen()       #do not forget this otherwise it wouldn't work
        self.screen.onkey(fun = self.go_up, key = "Up" )
        self.screen.onkey(fun = self.go_down, key = "Down")
        self.screen.onkey(fun = self.go_right, key = "Right")
        self.screen.onkey(fun = self.go_left, key = "Left")

