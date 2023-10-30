import turtle
from turtle import Turtle

t = Turtle()
t.speed(0)
t. penup()
t.goto(-200,0)
t.pendown()

for cnt in range(1000):


    t.forward(400)
    t.left(157)
    p = t.heading()


turtle.done()