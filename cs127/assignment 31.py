#terry huang
#march 4, 2018
#assignment 31

import pandas as pd
import matplotlib.pyplot as plt

a1 = input("Enter File name: ")
homeless = pd.read_csv(a1)
homeless['Fraction Children'] = homeless['Total Children in Shelter']/homeless['Total Individuals in Shelter']
homeless.plot(x = "Date of Census", y = "Fraction Children")

fig = plt.gcf()

a2 = input("Enter output file name: ")
fig.savefig(a2)

