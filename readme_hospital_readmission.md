
## Hospital Readmission reduction using Machine Learning

A Hospital readmission is a case when a patient who has been discharged from the hospital is admitted again within a specified period of time. In a program created by CMS to improve quality of healthcare, hospitals are charged for a readmission rate above a threshold. Some data realeted to current scenario of hospital readmission is shown below. 

![hack2.png](attachment:hack2.png)

For those hosptials which are currently being penalized under this program, a solution is to identify with increased risk of readmission beforehand and provide personalized care to these patients. The hospitals can also make arrangements and can increase resources if they have a prediction of readmission cases. 


## Objective

This project attempts to reduce these readmission costs and patient inconvenience by carrying out 3 tasks:

1. Analyzing the patient health to aid doctors in predicting their ailment using their symptoms and history

2. Based on their diagnosis, we determine risk factor of patient re-admission in future. This database will help hospitals from incurring readmission fees if the patient has high risk-score.

3. Using UiPath's RPA, we carry out regular follow-ups with the high risk patients to further improve patient interaction.


## Approach

![appraoch_sdlc.png](attachment:appraoch_sdlc.png)

- As soon as the patient enters hospital, he will fill a form about his symptoms. Before the patient will meet the doctor, a complete report of his previous visits, medical history and other patients with same symptoms will be sent to doctor. This will help doctor provide better treatment. 

- Once the patient is treated and out of hospital, the risk factor of a patient is calculated using machine learning prediction algorithm. Risk factor is the probability of patient coming back to the hospital within 30 days. 

- If the patient risk factor is more, he will be given an aftertreatment using Robotic process automation by continously engaging him with doctors or nurse and keeping a track of his medications and physical health. 

## SETUP

<b>Requirements</b>
- Python 3.7
- Jupyter Notebooks
- UiPath
- Google.Cloud.Speech.V1 = 1.2.0
- Twilio.Activities = 3.0.0
- Pandas
- Scikit-learn
    
<b>Dataset</b>
- Sample data for diabetic patients synthetically generated

<b>Instance</b>
- A simulated run for a returning patient
    
<b>Instructions</b>
- Download the files from Peter folder and run the .xaml file! Rest is all automated :)

## References

 - [Dataset for patient readmission](https://archive.ics.uci.edu/ml/datasets/diabetes+130-us+hospitals+for+years+1999-2008)
 - [Predicting hospital readmission for patients with diabetes using scikit-learn](https://towardsdatascience.com/predicting-hospital-readmission-for-patients-with-diabetes-using-scikit-learn-a2e359b15f0)
 - Bruce E, et. al.; Published:22 April 2009; Reduction of 30‐day postdischarge hospital readmission or emergency department (ED) visit rates in high‐risk elderly medical patients through delivery of a targeted care bundle
