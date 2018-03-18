#terry huang
#3/x/2018
#assignment 25

import turtle
import time

bubba = turtle.Turtle()

def redblue():
    n = int(input("Enter whole number: "))
    x = (n%2)
    if x == 1:
        bubba.color('red')
        bubba.right(0)
        bubba.forward(100)
    else:
        bubba.color('blue')
        bubba.left(180)
        bubba.forward(100)
    time.sleep(5)
    return
redblue()


