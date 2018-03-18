#terry huang
#feb 13, 2018
#assignment 15

binString = input('Gimme yo binary number: ')
decNum = 0
for c in binString:
    n = int(c)
    decNum = 2 * decNum + n
print('Your number in decimal is', decNum)