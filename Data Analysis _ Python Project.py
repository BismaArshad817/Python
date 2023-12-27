#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd #downloading libraries


# In[13]:


data = pd.read_csv(r"C:\Users\HP\Downloads\Project Weather.csv") #data importing


# # Data Exploration

# In[22]:


data


# In[23]:


data.head() #shows first five rows of data


# In[24]:


data.shape #Total number of rows and coloumns


# In[25]:


data.index #index of data frames


# In[26]:


data.columns #name of each coloumn


# In[28]:


data.dtypes #data type of each column


# In[32]:


data['Weather'].unique() #shows unique values of that specific coloumn


# In[34]:


data.nunique() #total number of unique values


# In[35]:


data.count() #it means no null values in data


# In[36]:


data['Weather'].value_counts()


# In[37]:


data.info() #provide basic information about data frames


# # Data Analysis

# In[42]:


data.head(2) #Find all unique "Wind Speed" values in the data


# In[43]:


data.nunique()


# In[44]:


data['Wind Speed_km/h'].nunique()


# In[45]:


data['Wind Speed_km/h'].unique()


# In[47]:


data.head(2) #Find number of times when the "Weather is exactly clear"


# In[48]:


data.Weather.value_counts() #Value Count


# In[51]:


#data.head(2) #Filtering
data[data.Weather == 'Clear']


# In[55]:


data.groupby('Weather').get_group('Clear') #Group by


# In[57]:


data.head(2) #number of tmes when the wind speed was exactly 4km/h


# In[58]:


data[data['Wind Speed_km/h'] == 4]


# In[60]:


data.isnull().sum()#find null values in data


# In[61]:


data.notnull().sum()


# In[68]:


data.head(2)


# In[73]:


data.rename(columns = {'Weather':'Weather_Condition'}, inplace = True) #Rename the coloumn name 'Weather' of the dataframe to ' Weather Condition'


# In[74]:


data.head()


# In[75]:


data.head(2)


# In[77]:


data.Visibility_km.mean() #Visibility


# In[79]:


data.Press_kPa.std() #Standard Deviation of "Pressure"


# In[82]:


data['Rel Hum_%'].var() #Variance of Relative Humidity


# In[84]:


data['Weather_Condition'].value_counts()#Instances when 'Snow' was recorded


# In[87]:


data[data['Weather_Condition'] == 'Snow'] #Filtering


# In[89]:


data[data['Weather_Condition'].str.contains('Snow')].tail(50) #str contains


# In[96]:


data.head(2)#instances when "Wind Speed is above 24" and visibility is 25


# In[98]:


data[(data['Wind Speed_km/h']>24) & (data['Visibility_km'] == 25)]


# In[100]:


data.head(2)


# In[104]:


data.groupby('Weather_Condition').mean()  #Mean value of each column against each 'Weather_COndition'


# In[105]:


data.head(2)#Minimum and Maximum value of each column against each 'Weather Condition'


# In[107]:


data.groupby('Weather_Condition').min()


# In[108]:


data.groupby('Weather_Condition').max()


# In[109]:


data[data['Weather_Condition'] == 'Fog']


# In[114]:


data[(data['Weather_Condition'] == 'Clear')| (data['Visibility_km'] >40).head(50)] #instances when weather is clear and visibility above 40


# In[120]:


data[(data['Weather_Condition'] == 'Clear') & (data['Rel Hum_%']>50) | (data['Visibility_km']>40)] #Weather is clear and relative humidity > 50 or visibility > 40


# In[ ]:




