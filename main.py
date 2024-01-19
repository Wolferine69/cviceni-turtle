from turtle import Turtle, Screen
tommy = Turtle()
tommy.shape("turtle")
tommy.color("red","green")

my_screen=Screen()
my_screen.bgcolor("blue")

tommy.forward(100)
tommy.right(90)
tommy.forward(100)
tommy.backward(150)

my_screen.exitonclick()
