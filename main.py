from turtle import Turtle , Screen
from paddle import Paddle
from shaps import Shaps
from score import Scorebord
import time

window = Screen()
window.title("One paddle")
window.bgcolor("black")
window.setup(700, 700)
window.tracer(0)

# opject paddle 
paddle = Paddle((0, -280))

# object shapas
shapes = Shaps()

score = Scorebord()

#onkey استدعاء دالة التحريك وهي 
window.listen()
window.onkey(paddle.right, "Right")
window.onkey(paddle.left, "Left")

game_on = True

shapes_speed = 0.1

while game_on:
    window.update()
    time.sleep(shapes_speed)
    shapes.move()
    if shapes.distance(paddle) < 50 and shapes.ycor() < -330:
        shape_type = shapes.shape()
        shape_color = shapes.color()[0]
        
        if shape_type == "turtle":
            if shape_color =="white":
                game_on = False
                score.game_over()
            else:
                point = 5
                score.incress_score(point)
        elif shape_type == 'circle':
            point = 1
            score.incress_score(point) 
        elif shape_type == 'square':
            point = 2
            score.incress_score(point)
        elif shape_type == 'triangle':
            score.reset_points()
    
        shapes.randomly()
        shapes_speed *= 0.9
    
    if shapes.ycor() <  -330:
            shapes.randomly()
    
    
    



window.exitonclick()