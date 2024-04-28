import turtle
position = [(0,0), (-20,0), (-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[len(self.segments)-1]

    
    def create_snake(self):
        for i in position:
            new_turtle = turtle.Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(i)
            self.segments.append(new_turtle)

    def up(self):
        if self.head.heading() != DOWN:

            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_pos = self.segments[seg_num-1].position()
            self.segments[seg_num].goto(new_pos)
        self.head.forward(20)
    
    def length(self):
        new_x=self.tail.xcor()
        new_y = self.tail.ycor()
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(new_x, new_y)
        self.segments.append(new_turtle)
    
    def wall_collision(self):
        if self.head.xcor()== 280:
            self.head.goto(x=-280,y=self.head.ycor())

        if self.head.xcor()== -280:
            self.head.goto(x=280,y=self.head.ycor())

        if self.head.ycor()== 280:
            self.head.goto(x=self.head.xcor(),y=-280)

        if self.head.ycor()== -280:
            
            self.head.goto(x=self.head.xcor(),y=280)
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]



        
        
    
    

