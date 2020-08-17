import numpy as np
import pandas as pd
df=pd.read_excel('Data_Train.xlsx')
df1=pd.read_excel('Data_Test.xlsx')
#print(df)
d=pd.get_dummies(df['Title'])
d1=pd.get_dummies(df['Author'])
#print(d1.columns)
d2=pd.get_dummies(df['Edition'])
#print(d2)
d3=pd.get_dummies(df['Reviews'])
#print(d3)
d4=pd.get_dummies(df['Ratings'])
#print(d4)
d5=pd.get_dummies(df['Genre'])
#print(d5)
d6=pd.get_dummies(df['BookCategory'])
#print(d6.columns)
d7=pd.get_dummies(df['Synopsis'])
#print(d7)#The Scarecrows' Wedding is a wonderfully heartwarming picture book from the creators of The Gruffalo and Stick Man.
merge=pd.concat([df,d,d1,d2,d3,d4,d5,d6,d7],axis='columns')
merged=merge.drop(['Title','Author','Edition','Reviews','Ratings','Genre','BookCategory','Synopsis'],axis='columns')
df2=pd.get_dummies(df['Title'])
df3=pd.get_dummies(df['Author'])
#print(d1.columns)
df4=pd.get_dummies(df['Edition'])
#print(d2)
df5=pd.get_dummies(df['Reviews'])
#print(d3)
df6=pd.get_dummies(df['Ratings'])
#print(d4)
df7=pd.get_dummies(df['Genre'])
#print(d5)
df8=pd.get_dummies(df['BookCategory'])
#print(d6.columns)
df9=pd.get_dummies(df['Synopsis'])

merge1=pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9],axis='columns')

merged1=merge1.drop(['Title','Author','Edition','Reviews','Ratings','Genre','BookCategory','Synopsis'],axis='columns')

x=merged.drop(['Price'],axis=1)
y=merged['Price']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)


from sklearn import metrics,tree
dt = tree.DecisionTreeRegressor()
dt.fit(x_train, y_train) #training the model 
y_pred = dt.predict(merged1) 
#y_pred=dt.predict(df1)#We are predicting the output for the test.csv dataset
#print(y_pred)

f=pd.DataFrame(y_pred,columns=['Price'])#We are taking the value of y_pred in a dataframe
#print(f)
f.to_excel('Sample_Submission.xlsx')#



