#terry huang
#3/27/2018
#assignment 39

import pandas as pd

'''
Enter CSV file name:  collisionsNewYears2016.csv
Top three contributing factors for collisions:
Driver Inattention/Distraction    136
Unspecified                       119
Following Too Closely              37
Name: CONTRIBUTING FACTOR VEHICLE 1, dtype: int64
'''


infile = input("Enter CSV file name: ")
df = pd.read_csv(infile)
cont1 = 'CONTRIBUTING FACTOR VEHICLE 1'
top3_cont1 = df[cont1].value_counts()[0:3]      #[0:3] start, end or [:3]
print(top3_cont1)
