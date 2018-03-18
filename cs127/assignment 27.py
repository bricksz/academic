#terry huang
#march 4, 2018
#assignment 27

import pandas as pd


#Open the CSV file and store in pop
pop = pd.read_csv('nycHistPop.csv',skiprows=5)

x = input("Enter borough name: ")

print(pop[x].mean())
print(pop[x].max())


