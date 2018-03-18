#terry huang
#march 4, 2018
#assignment 26

import matplotlib.pyplot as plt
import pandas as pd

#Open the CSV file and store in pop
pop = pd.read_csv('nycHistPop.csv',skiprows=5)

x = input("Enter borough name: ")

#Compute the fraction of the population in the Bronx, and save as new column:
pop['Fraction'] = pop[x]/pop['Total']

#Create a plot of year versus fraction of pop. in Bronx (with labels):
pop.plot(x = 'Year', y = 'Fraction')

#Save to the file:  fractionBX.png
fig = plt.gcf()

y = input("Enter output file name: ")
fig.savefig(y)

