from turtle import Turtle, Screen, colormode
import random

barvy=[["PaleGreen","LightGreen","LimeGreen","Lime","ForestGreen","Green","DarkGreen","SeaGreen","MediumSeaGreen","SpringGreen"],["Blue","MediumBlue","DarkBlue","MidnightBlue","Navy"],["Gold"],["Black"],["Crimson"],["Indigo"]]
zelva=Turtle("arrow")
zelva.color("black","green")
zelva.speed(10)
my_screen=Screen()
my_screen.exitonclick
colormode(255)
beh=10

for beh in range(10,300,10):
    for i in range(6):
        zelva.pencolor(random.choice(barvy[i]))
        zelva.forward(beh)
        zelva.right(60)
    zelva.penup()
    zelva.left(120)
    zelva.forward(10)
    zelva.right(120)
    zelva.pendown()


