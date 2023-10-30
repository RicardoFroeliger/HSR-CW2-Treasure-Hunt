
import turtle
from turtle import Turtle
t = Turtle()

angle = 90
distances = [165, 215, 100, 530, 50, 225, 405, 235, 155, 245, 130, 140, 190, 165, 125, 155, 115, 235, 165, 140, 185, 200, 125, 195, 185, 125, 155, 215, 250, 215, 110, 180, 215, 165, 190, 180, 125, 120, 130, 215, 110, 130, 230, 150, 150, 100, 170, 150, 100, 245,35]

for d in distances:
    t.forward(d)
    t.left(angle)

turtle.done()





