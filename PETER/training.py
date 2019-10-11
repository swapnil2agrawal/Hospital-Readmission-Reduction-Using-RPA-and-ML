import numpy as np
import pandas as pd
import sys
import sklearn
import datetime

from sklearn import linear_model
import pandas as pd
import numpy as np
import datetime
import sys

clf = linear_model.LogisticRegression()

def train(X, Y):
    X_new = np.zeros(np.shape(X))
    for i in range(len(X)):
        if(X[i][1] == "Uninsured"):
#             X[i][1] = 0
            X_new[i] = [X[i][0], 0, X[i][2], X[i][3]]
        else:
#             X[i][1] = 1
            X_new[i] = [X[i][0], 1, X[i][2], X[i][3]]
#     print(np.shape(X_new))
    clf.fit(X_new, Y)
    
    return clf

def predict(X, clf):
    
    X_new = np.zeros(np.shape(X))
    if(X[0][1] == "Uninsured"):
        X_new[0] = [X[0][0], 0, X[0][2], X[0][3]]
    else:
        X_new[0] = [X[0][0], 1, X[0][2], X[0][3]]
            
    risk = clf.predict(X_new)
    
    return risk  

def get_data(ids, df):
    
    reqd = df[(df.UID == ids)]
    trimmed_data = reqd[['UID', 'Insurance', 'Age', 'Date Visited', 'number of procedures']]
    dates_ = reqd['Date Visited']
    
    dates = [datetime.datetime.strptime(ts, "%m/%d/%Y") for ts in dates_]
    dates.sort()
    
    if len(dates) == 1:
        prev = 0

    else:
        latest = dates[-1] - dates[-2]

        if latest.days <= 30:
            prev = 1

        else:
            prev = 0
            
    last = dates[-1]
    trimmed_data['Date Visited'] =  pd.to_datetime(trimmed_data['Date Visited'], format="%m/%d/%Y")
#     print(trimmed_data)
    df = trimmed_data[trimmed_data['Date Visited'] == last]
#     print(df)
    df['visited'] = prev
    df_ = df.drop(columns="Date Visited")
#     print(df_)
    out = df_[['UID', 'Insurance', 'Age', 'number of procedures', 'visited']].iloc[0]
    a,b,c,d, e = out
    return a, b, c, d, e

# df = pd.read_csv("patients_100.csv")
# ID = df["UID"][0]
# get_data(ID, df)[:4]

def main():
	df = pd.read_csv("patients_100.csv")
	IDs = np.unique(df["UID"])
	X_train = []
	Y = []

	for i in IDs:
	    X_train.append(get_data(i, df)[:4])
	    Y.append(get_data(i, df)[4])
	       
	clf = train(X_train, Y)

	import pickle
	filename = 'model.sav'
	pickle.dump(clf, open(filename, 'wb'))

main()