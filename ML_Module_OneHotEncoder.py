from sklearn.ensemble import RandomForestClassifier
from sklearn import model_selection
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn import preprocessing
from mac_vendor_lookup import MacLookup
from sklearn.preprocessing import OneHotEncoder # use OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.compose import make_column_transformer

# MAC lookup example
print(MacLookup().lookup("44:65:0d:56:cc:d3"))

# load csv data
df = pd.read_csv("trainingDataset.csv")
#print(df.head())

# counts the number of devices in each category
sizes = df["Device Type"].value_counts(sort=1)
#print(sizes)

# remove the unnecessary data columns 
df.drop(["Packet ID", "TIME"], axis=1, inplace=True)

#print(df.head())

# handle missing values
df = df.dropna()

# convert strings into numbers so the model can process it
le = preprocessing.LabelEncoder() # use LabelEncoder
df2 = df.apply(le.fit_transform)
print(df2)

# define the dependent variable
Y = df2["Device Type"].values
#print(Y)

# define the independent variable
X = df2.drop(labels=["Device Type"], axis=1)
#print(X)

# use OneHotEncoder to further prepare the data 
preprocessor = make_column_transformer((OneHotEncoder(),[2,3,4,5]),remainder="passthrough")
X = preprocessor.fit_transform(X)
print(df2)

# split data into training set and testing set
from sklearn.model_selection import train_test_split

# the bigger the test_size is the more accurate the results will be 
X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
                                    test_size=0.4, random_state=20)

# create the model 
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators = 10, random_state=20)

# train the model
model.fit(X_train, Y_train)

# test the model
prediction_test = model.predict(X_test)
from sklearn import metrics
print("Accuracy = ", metrics.accuracy_score(Y_test, prediction_test)) 

# check the contribution of each independent variable
feature_list = list(X.columns)
feature_imp = pd.Series(model.feature_importances_, index=feature_list).sort_values(ascending=False)
print(feature_imp)








