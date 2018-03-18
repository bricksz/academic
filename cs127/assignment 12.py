#terry huang
#feb 13, 2018
#assignment 12

import turtle

turtle.colormode(255)
tess  = turtle.Turtle()
tess.shape('turtle')
tess.backward(100)

for i in range(0,255,10):
    tess.forward(10)
    tess.pensize(i)
    tess.color(0,i,0)