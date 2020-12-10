from sklearn.ensemble import RandomForestClassifier
from sklearn import model_selection
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder # use OneHotEncoder
from sklearn.compose import ColumnTransformer
import pyrebase
import random 
import time 

# 1) Prepare the data for training
# 2) Train the model
# 3) Prepare the testing data
# 4) Extract the time scale from the database
# 5) Choose the module to use and train it with the respective dataset 
# 6) Go over the captured data in the sheet and predict the devices with the ML model
# 7) Update the firebase db with the predicted devices

# Data preparation:

# load csv data

# Training set for the 5 min time scale
df_5m_unsw = pd.read_csv("unsw_dataset_features_mapped_5m.csv", low_memory=False)
# Training set for the 15 min time scale
df_15m_unsw = pd.read_csv("unsw_dataset_features_mapped_15m.csv", low_memory=False)
# Training set for the 30 min time scale
df_30m_unsw = pd.read_csv("unsw_dataset_features_mapped_30m.csv", low_memory=False) 

df_5m = pd.read_csv("output_5m_mapped.csv", low_memory=False) # Training set for the 5 min time scale
df_15m = pd.read_csv("output_15m_mapped.csv", low_memory=False) # Training set for the 15 min time scale
df_30m = pd.read_csv("output_30m_mapped.csv", low_memory=False) # Training set for the 30 min time scale

# counts the number of devices detected
print(df_5m_unsw["Device Type"].value_counts(sort=1))
numOfDevices = len(df_5m_unsw["Device Type"].value_counts(sort=1))
print("Number of types detected is: " + str(numOfDevices) + " types")
print("\n")

# remove the unnecessary data columns 
df_5m.drop(["device_co", "Device Name", "MAC_address"], axis=1, inplace=True)
df_15m.drop(["device_co", "Device Name", "MAC_address"], axis=1, inplace=True)
df_30m.drop(["device_co", "Device Name", "MAC_address"], axis=1, inplace=True)

# handle missing values
df_5m = df_5m.dropna()
df_15m = df_15m.dropna()
df_30m = df_30m.dropna()
#pred = pred.dropna()

# define the dependent variable
Y5m = df_5m["Device Type"].values
Y15m = df_15m["Device Type"].values
Y30m = df_30m["Device Type"].values

# convert strings into numbers so the model can process it
le = preprocessing.LabelEncoder() # use LabelEncoder
df_5m['rdap_asn'] = le.fit_transform(df_5m['rdap_asn'])
df_5m['Connection Type'] = le.fit_transform(df_5m['Connection Type'])
df_15m['rdap_asn'] = le.fit_transform(df_15m['rdap_asn'])
df_15m['Connection Type'] = le.fit_transform(df_15m['Connection Type'])
df_30m['rdap_asn'] = le.fit_transform(df_30m['rdap_asn'])
df_30m['Connection Type'] = le.fit_transform(df_30m['Connection Type'])


# define the independent variable
X5m = df_5m.drop(labels=["Device Type"], axis=1)
X15m = df_15m.drop(labels=["Device Type"], axis=1)
X30m = df_30m.drop(labels=["Device Type"], axis=1)


# split data into training set and testing set
from sklearn.model_selection import train_test_split

# the bigger the test_size is the more accurate the results will be 
X_train_5m, X_test_5m, Y_train_5m, Y_test_5m = train_test_split(X5m, Y5m, test_size=0.2, random_state=10, shuffle=True)
X_train_15m, X_test_15m, Y_train_15m, Y_test_15m = train_test_split(X15m, Y15m, test_size=0.2, random_state=10, shuffle=True)
X_train_30m, X_test_30m, Y_train_30m, Y_test_30m = train_test_split(X30m, Y30m, test_size=0.2, random_state=10, shuffle=True)


# create the model 
from sklearn.ensemble import RandomForestClassifier

model_5m = RandomForestClassifier(n_estimators = 10, random_state=30)
model_15m = RandomForestClassifier(n_estimators = 10, random_state=30)
model_30m = RandomForestClassifier(n_estimators = 10, random_state=30)

# train the model
model_5m.fit(X_train_5m, Y_train_5m)
model_15m.fit(X_train_15m, Y_train_15m)
model_30m.fit(X_train_30m, Y_train_30m)

# test the model
prediction_test_5m = model_5m.predict(X_test_5m)
prediction_test_15m = model_15m.predict(X_test_15m)
prediction_test_30m = model_30m.predict(X_test_30m)


from sklearn import metrics

print("Testing results for the 5 minutes time scale model...")
print("Accuracy = ", metrics.accuracy_score(Y_test_5m, prediction_test_5m)) 
# check the contribution of each independent variable
feature_list = list(X5m.columns)
feature_imp = pd.Series(model_5m.feature_importances_, index=feature_list).sort_values(ascending=False)
print(feature_imp)

print("\n\n\n")

print("Testing results for the 15 minutes time scale model...")
print("Accuracy = ", metrics.accuracy_score(Y_test_15m, prediction_test_15m)) 
# check the contribution of each independent variable
feature_list = list(X15m.columns)
feature_imp = pd.Series(model_15m.feature_importances_, index=feature_list).sort_values(ascending=False)
print(feature_imp)

print("\n\n\n")

print("Testing results for the 30 minutes time scale model...")
print("Accuracy = ", metrics.accuracy_score(Y_test_30m, prediction_test_30m)) 
# check the contribution of each independent variable
feature_list = list(X30m.columns)
feature_imp = pd.Series(model_30m.feature_importances_, index=feature_list).sort_values(ascending=False)
print(feature_imp)

# firebase configuration
config = {
    "apiKey":"AIzaSyBJqqj1jgw0sNgCD-iC_uKbKPLqdg5Ytp8",
    "authDomain":"harpy-c8519.firebaseapp.com",
    "databaseURL":"https://harpy-c8519.firebaseio.com/",
    "projectId":"harpy-c8519",
    "storageBucket":"harpy-c8519.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
ID = '-MHfQDfcvO17vmKEFUOc'

timeScale = db.child(ID).get().val()['timeScale']

first_row = True

print(timeScale)
print("\n")

while (1):
    
    captured_set_sample = pd.read_csv("test_output.csv") # A sample of a captured dataset
    captured_set_sample = captured_set_sample.dropna()
    captured_set_sample_enc = captured_set_sample[0:]

    le = preprocessing.LabelEncoder() # use LabelEncoder
    captured_set_sample_enc['rdap_asn'] = le.fit_transform(captured_set_sample_enc['rdap_asn'])
    captured_set_sample_enc['Connection Type'] = le.fit_transform(captured_set_sample_enc['Connection Type'])
    captured_set_sample_enc.drop(["device_co", "Device Name", "MAC_address", "Device Type"], axis=1, inplace=True)
    
    db_content = []
    timeScale = db.child(ID).get().val()['timeScale']
    if (timeScale == 5):
        chosenModel = model_5m
    elif (timeScale == 15):
        chosenModel = model_15m
    elif (timeScale == 30):
        chosenModel = model_30m
    
    for row1, row2 in zip(captured_set_sample_enc.iterrows(), captured_set_sample.iterrows()):
        features = list(row2)[1]
        if (not first_row):
            if (features[13].strip() not in db_content):
                device_type = chosenModel.predict(list(row1)[1:12])
                
                db_content+= [features[13].strip()]
                if(device_type[0]=='Hub'):
                    iconName = 'device-hub'
                    
                elif(device_type[0]=='Camera'):
                    iconName = 'camera-alt'
              
                elif(device_type[0]=='Computer'):
                    iconName = 'computer'
                  
                elif(device_type[0]=='Appliance'):
                    iconName = 'home-filled'
                   
                elif(device_type[0]=='Sensor'):
                    iconName = 'settings-remote'
                   
                elif(device_type[0]=='Misc'):
                    iconName = 'miscellaneous-services'
                    
                elif(device_type[0]=='Network'):
                    iconName = 'router-wireless'
                   
                db.child(ID).child(features[13].strip()).update({
                    "Device Type": device_type[0],
                    "Device MAC": features[13].strip(),
                    "Device Name": features[12].strip(),
                    "Device Total Active Time": features[1],
                    "Device Total Flow Volume": features[2],
                    "Device Flow Rate": features[3],
                    "Device Avarage Packet Size": features[4],
                    "Number of Servers": features[5],
                    "Number of Protocols Used": features[6],
                    "iconName": iconName,
                    "safety": False,
                    })
              
        first_row= False



