from turtle import Turtle, Screen, colormode
import random

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color = (r,g,b)
    return random_color

zelva=Turtle()
zelva.shape("turtle")
zelva.color("black","green")
obrazovka=Screen()
colormode(255)
# barvy=["red", "orange", "green", "cyan", "blue", "purple", "magenta", "pink","orchid","gold","lime","dimgray"]

zelva.speed(8)
zelva.pensize(1)
x=0

while x<20:
    zelva.forward(20)
    smer=random.randint(1,2)
    if smer ==1:
        zelva.right(random.randrange(0,180,90))
    else:
        zelva.left(random.randrange(0,180,90))
    zelva.pencolor(random_color())
    if x<10:
        x+=1
    else:
        x=1
    zelva.pensize(x)


obrazovka.exitonclick()