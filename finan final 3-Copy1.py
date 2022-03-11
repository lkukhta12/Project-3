#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install matplotlib')
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv(r'\\Flws-ntxfs\cfr\lkukhta\Desktop\New folder\NYPD_Arrest_Data__Year_to_Date.csv')


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


#getting teh count for columns
col_count = len(df.columns)
col_count


# In[6]:


#getting the count for rows
row_count = df.shape[0]
row_count


# In[7]:


#creating a new dataframe
df1 = df[['ARREST_DATE', 'OFNS_DESC', 'ARREST_BORO', 'AGE_GROUP', 'PERP_SEX']]


# In[8]:


#looking at the new dataframe head
df1.head(15)


# In[9]:


#dropping missing values
df1 = df1.dropna()


# In[10]:


#repeting steps of rows and columns counts after dropping missing values
col_count = len(df1.columns)
col_count


# In[11]:


row_count = df1.shape[0]
row_count


# In[12]:


#renaming columns for the better and clear data understanding
df1 = df1.rename(columns={'ARREST_DATE': 'Date of Arrest', 'OFNS_DESC': 'Criminal Offense Type', 'ARREST_BORO': 'Borough', 'AGE_GROUP' : 'Age Range', 'PERP_SEX' : 'Gender'})


# In[13]:


#testing out to display new columns' names
df1.head()


# In[16]:


import matplotlib.pyplot as plt
from matplotlib import style


# In[49]:


sns.pairplot(df1)


# In[ ]:




