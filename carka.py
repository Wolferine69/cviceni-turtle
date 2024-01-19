from turtle import Turtle, Screen
tommy = Turtle()
tommy.shape("turtle")
tommy.color("red","green")

my_screen=Screen()
my_screen.bgcolor("blue")

for i in range(10):
    if i%2!=0:
        tommy.pendown()
    else:
        tommy.penup()
    tommy.forward(20)


my_screen.exitonclick()