from turtle import Turtle 
import random

class Shaps(Turtle):
    def __init__(self):
        super().__init__()
        self.shapes = ["triangle", "square", "circle", "turtle"]
        self.colors = ["red", "orange", "blue", "yellow"]
        self.y_move = -10
        self.randomly()


    def move(self):
        self.penup()
        self.goto(self.xcor(), self.ycor() + self.y_move )
        
    # اختيار مكان عشوائي للشيب 
    def randomly(self):
        random_x = random.randint(-340, 340)
        self.goto(random_x, y = 350)
    
    # اختيار شكل عشوائي
        random_shape = random.choice(self.shapes)
        self.shape(random_shape)
        
        # اختيار لون عشوائي
        # 10% choses Turtle
        if random_shape == 'turtle' and random.randint(1, 10) == 1:
            self.color("white")
        
        else:
            self.color(random.choice(self.colors))
        
        # حجم عشوائي
        # float
        random_size = random.uniform(0.5, 2)  
        self.shapesize(stretch_wid=random_size , stretch_len=random_size)
            
    
        