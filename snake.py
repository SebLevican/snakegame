from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_CONSTANT = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self,turtle):            
        new_turtle = Turtle('square')
        new_turtle.color('white')
        new_turtle.penup()
        new_turtle.goto(turtle)
        self.segments.append(new_turtle)


    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):

        for seg_num in range(len(self.segments) -1, 0, -1 ):
            new_x= self.segments[seg_num -1].xcor()
            new_y= self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_CONSTANT)

    def Up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)
    
    def Down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def Left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
    
    def Right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    
    
    
    
        