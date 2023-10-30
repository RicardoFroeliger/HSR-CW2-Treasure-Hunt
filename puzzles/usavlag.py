import turtle
from turtle import Turtle
t = Turtle()
t.speed(0)
t.hideturtle()

red,white,blue = "red","white","blue"

a = 0
b = 5
c = 2000

def part1(x,y):
    t.penup()
    t.goto(x,y)
    t.color(red)
    t.pendown()
    t.begin_fill()
    t.forward(400)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(400)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.end_fill()

def part2(x,y):
    t.penup()
    t.goto(x,y)
    t.color(blue)
    t.pendown()
    t.begin_fill()
    t.forward(150)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.end_fill()

def part3(x,y):
    t.penup()
    t.goto(x, y)
    t.color(white)
    t.pendown()
    s = "\u2605"
    t.write(s)



def part4(x,y,value):
    t.penup()
    t.color(blue)
    t.goto(x,y)
    t.penup()
    t.write(str(value)+"-"+str(value+1),font=("Arial", 18, "normal"))
    t.hideturtle()




for i in range(b):
    part1(-200,40*i)

part2(a,160)

for x in range(-180,-55,25):
    for y in range(240,140,-25):
        part3(x,y)

part4(0,-100,c)

turtle.done()