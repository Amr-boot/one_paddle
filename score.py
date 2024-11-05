from turtle import Turtle

class Scorebord(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.goto(x= 0, y = 340)
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.color("white")
        self.goto(0, 310)
        self.write(f" Score {self.score}", align= "center" ,font=("courier", 24, "normal"))
        
        
        
    def incress_score(self, point):
        self.clear()
        self.score =+ point
        # self.write(f"Score {self.score}", align = "center", font=("courier", 24, "bold"))
        self.update_score()
    
    def reset_points(self):
        self.clear()
        self.score  = 0
        self.write(f"Score {self.score}", align = "center", font=("courier", 24, "bold"))
    
        
    
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=('courier', 24, 'bold'))
        self.update_score()
        
        
