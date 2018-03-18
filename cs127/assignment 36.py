#terry huang
#3/15/2018
#assignment 36

import pandas as pd

x = input ('Enter file name: ')
tickets = pd.read_csv(x)
y = input ('Enter attribute: ')

print('The 10 worst offenders are: ')
print(tickets[y].value_counts()[:10])
