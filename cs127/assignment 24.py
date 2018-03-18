#terry huang
#feb 18, 2018
#assignment 24

import turtle

tess = turtle.Turtle()
tess.shape('turtle')
myWin = turtle.Screen()     #The graphics window
commands = input("Please enter a command string: ")

for ch in commands:
    #perform action indicated by the character
    if ch == 'F':            #move forward
        tess.forward(50)
    elif ch == 'B':          #move back
        tess.backward(50)
    elif ch == 'S':          #turtle stamp
        tess.stamp()
    elif ch == 'l':          #left 45
        tess.left(45)
    elif ch == 'r':          #right 45
        tess.right(45)
    elif ch == 'p':          #pen color purple
        tess.color('purple')
    elif ch == 'L':          #turn left
        tess.left(90)
    elif ch == 'R':          #turn right
        tess.right(90)
    elif ch == '^':          #lift pen
        tess.penup()
    elif ch == 'v':          #lower pen
        tess.pendown()
    else:                   #for any other character, print an error message
        print("Error: do not know the command:", c)

print("See graphics window for your image")
myWin.exitonclick()         #Close the window when clicked