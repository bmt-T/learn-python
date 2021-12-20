import turtle
import random

number = random.uniform(0,3)

intnumber = int(number)

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("circle")

ball = turtle.Turtle()
ball.shape('circle')

if intnumber<1:
    ball.color('green')
elif intnumber<2:
    ball.color('yellow')
else:
    ball.color('red')

turtle.done()