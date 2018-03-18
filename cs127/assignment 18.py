#terry huang
#feb 13, 2018
#assignment 18

import turtle

red = turtle.Turtle()

for i in range(5):
    x = input('Enter a number: ')
    print(x)
    red.left(float(x))
    red.forward(100)
