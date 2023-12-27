#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd      #Importing all necessary libraries
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/advertising.csv")  #Improting Data Set
print(data.head())


# In[4]:


print(data.isnull().sum()) #to check whether data has any null value


# In[5]:


import plotly.express as px # visualization of the relationship between the amount spent on advertising on TV and units sold
import plotly.graph_objects as go
figure = px.scatter(data_frame = data, x="Sales",
                    y="TV", size="TV", trendline="ols")
figure.show()


# In[13]:


figure = px.scatter(data_frame = data, x="Sales",
                    y="Newspaper", size="Newspaper", trendline="ols")
figure.show() #visualization of the relationship between the amount spent on advertising on newspapers and units sold:


# In[7]:


figure = px.scatter(data_frame = data, x="Sales",
                    y="Radio", size="Radio", trendline="ols")
figure.show() #visualize the relationship between the amount spent on advertising on radio and units sold:


# In[8]:


correlation = data.corr()
print(correlation["Sales"].sort_values(ascending=False)) #correlation of all the columns with the sales column


# In[14]:


x = np.array(data.drop(["Sales"], 1))
y = np.array(data["Sales"])
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42) #split the data into training and test sets
model = LinearRegression()
model.fit(xtrain, ytrain) #train the model to predict future sales
print(model.score(xtest, ytest))
#features = [[TV, Radio, Newspaper]] #input values into the model according to the features we have used to train it and predict how many units of the product can be sold based on the amount spent on its advertising on various platforms
features = np.array([[230.1, 37.8, 69.2]])
print(model.predict(features))


# In[ ]:




