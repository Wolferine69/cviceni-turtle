from turtle import Turtle, Screen, colormode
import random

zelva=Turtle("turtle")
zelva.color("black","green")
zelva.speed(8)
colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color = (r,g,b)
    return random_color

for i in range(10,101,5):
    zelva.circle(i)
    zelva.pencolor(random_color())

obrazovka=Screen()
obrazovka.exitonclick()