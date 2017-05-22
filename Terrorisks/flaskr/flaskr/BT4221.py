
# coding: utf-8

# In[6]:




# # Prelim Analysis

import numpy as np
from sklearn import preprocessing
from sklearn.metrics import roc_curve, auc
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import pandas as pd
from random import randint
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
#import the data and rename the columns


d = pd.read_csv('file.csv', encoding='ISO-8859-1',low_memory=False)#,  usecols=[0, 1, 2, 3, 8, 11, 13, 14, 26, 29, 35, 37, 84, 100, 103])
 
d = d.rename(columns={'eventid':'id', 'iyear':'year', 'imonth':'month', 'iday':'day', 'country_txt':'country', 'provstate':'state', 'success':'success','targtype1_txt':'target', 'targsubtype1_txt' : 'targetsub','weaptype1_txt':'weapon', 'attacktype1_txt':'attack','nkill':'fatalities', 'nwound':'injuries'})


d = d.drop(['id'],axis=1)

df_num = d.select_dtypes(include=[np.number])
df_inf = df_num.replace([np.inf, -np.inf], np.nan)
df_inf.replace([np.inf, -np.inf], np.nan)
df_filled = df_inf.fillna(0)

df_filled = df_filled.drop(['success'],axis=1)


# In[70]:

df_filled.corr().abs()



from numpy import float32
#df_filled.head()
df_transformed = df_filled.astype(float32)
#df_transformed.info()





# In[17]:

lm = LinearRegression()
y = d['success']
X = df_filled[['month', 'day','region','property','propextent','attacktype1','weaptype1','nperps','specificity' ]]
X_train, X_test,y_train, y_test = train_test_split(X,y,random_state=2)
#print(X_train.head())
lm.fit(X_train, y_train)
r = lm.score(X_train, y_train)
#print (r)
pred_train = lm.predict(X_train)
pred_test = lm.predict(X_test)


# In[18]:

#Random Forest
y_random = df_filled['multiple']
X_random = df_filled[['month', 'day','region','property','propextent','attacktype1','weaptype1','nperps','specificity' ]]
features_train, features_test,target_train, target_test = train_test_split(X_random,y_random, test_size = 0.2,random_state=0)
#Random Forest
forest=RandomForestClassifier(n_estimators=10)
forest = forest.fit( features_train, target_train)
output = forest.predict(features_test).astype(int)
forest.score(features_train, target_train )

# In[15]:

from patsy import dmatrices
from sklearn.linear_model import LogisticRegression
#Logistic Regression
y_log, X_log = dmatrices('multiple ~ month + day + region + property + propextent + attacktype1 + weaptype1+ nperps + specificity', df_filled, return_type="dataframe")
y_log = np.ravel(y_log)
# instantiate a logistic regression model, and fit with X and y
model = LogisticRegression()
model = model.fit(X_log, y_log)
X_train_log, X_test_log, y_train_log, y_test_log = train_test_split(X_log, y_log, test_size=0.3, random_state=0)
model2 = LogisticRegression()
model2.fit(X_train, y_train)

def plots(lm,rf,lr):
    counter=randint(1,1000)
    import matplotlib.pyplot as plt
    results = []
    results.append(lm[0])
    results.append(lr[0][1])
    results.append(rf[0][0])
    N = len(results)
    x = [1,2,3]
    #y=['Linear Regression', 'Logistic Regression', 'Random Forest']
    width = 1/1.5
    plt.bar(x,results,width,color = "green",align='center')
    plt.savefig("static/images/fig"+str(counter)+".png")
    plt.clf()
    return "static/images/fig"+str(counter)+".png"

    
