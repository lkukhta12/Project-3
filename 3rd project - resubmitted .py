#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install matplotlib')
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
df = pd.read_csv(r'\\Flws-ntxfs\cfr\lkukhta\Desktop\New folder\NYPD_Arrest_Data__Year_to_Date.csv')


# In[2]:


#looking thru the data 
df.head()
df.tail()


# In[3]:


#getting the count for columns
col_count = len(df.columns)
col_count


# In[4]:


#getting the count for rows
row_count = df.shape[0]
row_count


# In[5]:


#creating a new dataframe
df1 = df[['ARREST_KEY','ARREST_DATE', 'OFNS_DESC', 'ARREST_BORO', 'AGE_GROUP', 'PERP_SEX']]


# In[6]:


#looking at the new dataframe head
df1.head(15)


# In[7]:


#dropping missing values
df1 = df1.dropna()


# In[8]:


#repeting steps of rows and columns counts after dropping missing values
col_count = len(df1.columns)
col_count


# In[9]:


row_count = df1.shape[0]
row_count


# In[10]:


#renaming columns for the better and clear data understanding
df1 = df1.rename(columns={'ARREST_KEY': 'Arrest Key', 'ARREST_DATE': 'Date of Arrest', 'OFNS_DESC': 'Criminal Offense Type', 'ARREST_BORO': 'Borough', 'AGE_GROUP' : 'Age Range', 'PERP_SEX' : 'Gender'})


# In[11]:


#testing out to display new columns' names
df1.head()


# In[12]:


#looking at the count of arrests by the Gender: males make up a bigger part than females. 
df1 = df1.groupby(['Gender'])['Arrest Key'].count()
df1.plot.pie()
plt.title("Crimes by Gender")


# In[15]:





# In[ ]:




