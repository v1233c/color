#Initialization
import turtle
vicky = turtle.Turtle()
import random
turtle.colormode(255)
vicky.speed(100)

#Functions

def randomDot():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    c = random.randint(0,100)
    vicky.color(r,g,b)
    vicky.begin_fill()
    vicky.circle(c)
    vicky.end_fill()
  
    
#Main
for i in range(100):
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    vicky.penup()
    vicky.goto(x,y)
    vicky.pendown()
    randomDot()
