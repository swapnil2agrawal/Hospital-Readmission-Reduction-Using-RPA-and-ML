import numpy as np 
import pandas as pd 
import sys 
import datetime

# python .\get_data.py Syn.csv UID Disease
data = sys.argv[1]
uid = int(sys.argv[2])


# '''Remove int below if working w/ string'''
# disease = int(sys.argv[3])  

df = pd.read_csv(data)

reqd = df[ (df.UID == uid)]  # 

dates_ = reqd["Date Visited"]
dates = [datetime.datetime.strptime(ts, "%m/%d/%Y") for ts in dates_]
dates.sort()

'''Difference between recent most dates'''
latest = dates[-1] - dates[-2]
diff_in_days = latest.days

print(diff_in_days)
# print(diff_in_days)
# if diff_in_days > 30:
    # return 