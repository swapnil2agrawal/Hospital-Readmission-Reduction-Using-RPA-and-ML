import numpy as np 
import pandas as pd
import sys
import csv

patient_data = sys.argv[1]

# df = pd.read_csv(patient_data)

# with open(patient_data) as csv_file:
#     reader = csv.reader(csv_file, delimiter=',')
    
#     for row in reversed(reader):
#         print(row)

df = pd.read_csv(patient_data)

recent = df.tail(1)


# print(df.head())

