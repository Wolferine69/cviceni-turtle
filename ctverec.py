from turtle import Turtle, Screen

zelva=Turtle()
zelva.shape("turtle")
zelva.color("black","green")
zelva.begin_fill()
for i in range(0,4):
    zelva.speed(2)
    zelva.forward(100)
    zelva.right(90)
zelva.end_fill()
obrazovka=Screen()
obrazovka.exitonclick()