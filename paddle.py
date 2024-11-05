from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, postions):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.goto(postions)
        self.shapesize(1, 5)
    
    # move the paddle سوف نقوم بانشاء داله لتحريك البادل
    def right(self):
        new_x = self.xcor() + 40
        if new_x < 340:
            self.goto(new_x, self.ycor())
    def left(self):
         new_x = self.xcor() - 40
         if new_x > -340:
            self.goto(new_x, self.ycor())
    
         
        
        