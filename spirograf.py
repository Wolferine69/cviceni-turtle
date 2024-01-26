from turtle import Turtle, Screen, colormode
import random

zelva=Turtle()
zelva.shape("turtle")
zelva.color("black","green")
zelva.speed(9)
my_screen=Screen()
colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color = (r,g,b)
    return random_color

for i in range(0,361,20):
    zelva.setheading(i)
    zelva.pencolor(random_color())
    zelva.circle(50)
  
my_screen.exitonclick()