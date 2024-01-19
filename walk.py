from turtle import Turtle, Screen
import random

zelva=Turtle()
zelva.shape("turtle")
zelva.color("black","green")
obrazovka=Screen()
barvy=["red", "orange", "green", "cyan", "blue", "purple", "magenta", "pink","orchid","gold","lime","dimgray"]
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
    zelva.pencolor(random.choice(barvy))
    if x<10:
        x+=1
    else:
        x=1
    zelva.pensize(x)


obrazovka.exitonclick()