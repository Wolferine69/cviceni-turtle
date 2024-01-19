from turtle import Turtle, Screen
import random

zelva=Turtle()
zelva.shape("turtle")
zelva.color("black","green")
obrazovka=Screen()
barvy=["red", "orange", "green", "cyan", "blue", "purple", "magenta", "pink"]
x=3
zelva.speed(5)
zelva.pensize(2)

while x<13:
    zelva.pencolor(random.choice(barvy))
    for i in range(x):
        zelva.forward(50)
        zelva.right(360/x)
    x+=1

obrazovka.exitonclick()