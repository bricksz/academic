#terry huang
#3/27/2018
#assigntment 46

import turtle
import random

trey = turtle.Turtle()
trey.speed(10)

for i in range(100):
  trey.forward(10)
  a = random.randrange(0,360,1)
  trey.right(a)