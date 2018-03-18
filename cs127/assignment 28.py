#terry huang
#march 4, 2018
#assignment 28

import datetime

x = datetime.datetime.now()
if x.hour <= 12:
    print('Good Morning')
elif x.hour <= 17:
    print('Good Afternoon')
else:
    print('Good Evening')

def hellotime():
    y = input("Enter hour now: ")
    if y <= '12':
        print('Good Morning')
    elif y <= '17':
        print('Good Afternoon')
    else:
        print('Good Evening')

#hellotime()
help(datetime.date)
