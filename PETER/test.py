import pickle
from sklearn import linear_model
import pandas as pd
import numpy as np
import datetime
import sys

filename = 'model.sav'
clf = pickle.load(open(filename, 'rb'))

def predict(X, clf):
    
    X_new = np.zeros(np.shape(X))
    if(X[0][1] == "Uninsured"):
        X_new[0] = [X[0][0], 0, X[0][2], X[0][3]]
    else:
        X_new[0] = [X[0][0], 1, X[0][2], X[0][3]]
            
    risk = clf.predict(X_new)
    
    return risk  


def values(ids, df):
    
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
    df = trimmed_data[trimmed_data['Date Visited'] == last]
    df_ = df.drop(columns="Date Visited")
    out = df_[['UID', 'Insurance', 'Age', 'number of procedures']].iloc[0]
    a,b,c,d = out
    return a, b, c, d


# def main():

# 	df = pd.read_csv("patients_100.csv")
# 	UID = int(sys.argv[1])
# 	# UID = 60
# 	X = np.array(values(UID, df)).reshape(1, -1)
# 	risk = predict(X, clf)[0]

# 	return risk


def detail(ids, df):
    
	file = "chat.txt"
	X = np.array(values(ids, df)).reshape(1, -1)
	risk = int(predict(X, clf)[0])

	reqd = df[(df.UID == ids)]
	trimmed_data = reqd[['UID', 'FName', 'LName', 'Age', 'Thurst & hunger', 'Loss-Gain', 'Fatigue','Blurred Vision', 'Slow Healing Wounds', 'Nausea', 'Skin Infection', 'Frequent Urination']]

	greet = 'Hey '
	ending = '\n - Peter'

	with open(file, "w") as f:

		f.write(greet + str(trimmed_data.iloc[-1].FName))
		f.write('\n')

		if(risk == 1):
		    if trimmed_data.iloc[-1]['Thurst & hunger'] == 1:
		        f.write("Just wanted to check on you, Hope you are eating healthy!")
		        f.write(ending)
		    
		    elif trimmed_data.iloc[-1]['Loss-Gain'] == 1:
		        f.write("Don't forget to take your medicines on time.")
		        f.write(ending)
		        
		    elif trimmed_data.iloc[-1]['Fatigue'] == 1:
		        f.write("Are you taking enough rest?")
		        f.write(ending)
		        
		    elif trimmed_data.iloc[-1]['Blurred Vision'] == 1:
		        f.write("Hope you are feeling better! Feel free to call me anytime you feel uncomfortable.")
		        f.write(ending)
		        
		    elif trimmed_data.iloc[-1]['Slow Healing Wounds'] == 1:
		        f.write("Stay Safe. I'm Sure you will get better soon.")
		        f.write(ending)
		        
		    elif trimmed_data.iloc[-1]['Nausea'] == 1:
		        f.write("Don't forget to stay hydrated and drink some Lemonade!")
		        f.write(ending)
		        
		    elif trimmed_data.iloc[-1]['Skin Infection'] == 1:
		        f.write("Have you applied the ointement?")
		        f.write(ending)
		        
		    elif trimmed_data.iloc[-1]['Frequent Urination'] == 1:
		        f.write("How are you feeling today? Don't forget to take your meds.")
		        f.write(ending)

		else:
			f.write(greet + str(trimmed_data.iloc[-1].FName))
			f.write('\n')
			f.write("Thanks for visiting us!")


	return None

df = pd.read_csv("patients_100.csv")
UID = int(sys.argv[1])

detail(UID, df)