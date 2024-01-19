from turtle import Turtle, Screen

zelva=Turtle()
zelva.shape("turtle")
zelva.color("black","green")

for i in range(0,4):
    zelva.speed(2)
    zelva.forward(100)
    zelva.right(90)

obrazovka=Screen()
obrazovka.exitonclick()