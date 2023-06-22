#!/usr/bin/env python
# coding: utf-8

# In[11]:


print("Name:")
print("We will be cleaning heart disease data, and conclude which age group has high risk of heart stroke as per diabetes and hight blood pressure level")
print("We will also find which gender has the most not normal platelets count in blood, and plot a pie chart around it")



# # Task 1 - Find the diabetic and hight blood pressure patients across all age groups, and conclude the risk heart stroke is higher in which age group

# In[10]:


#Import libraries
import pandas as pd
import matplotlib.pyplot as plt 

#read the csv
df = pd.read_csv('heart_disease.csv')
df


# In[2]:


#Filter by diabetes(condition will be who has diabetes) and create new dataframe
diabetic_patient=df.loc[df['diabetes'] == 1]
diabetic_patient


# In[3]:


#On this new data frame perform group operation as per age and create new dataframe 
groupby_age_diabetes = diabetic_patient.groupby('age')['diabeties'].count().reset_index(0)
groupby_age_diabetes


# In[4]:


#Filter by high_blood_pressure(condition will be who has high_blood_pressure) and create new dataframe
patient_high_bp = df.loc[df['high_blood_pressure'] == 1]
patient_high_bp


# In[5]:


#On this new data frame perform group operation as per age and create new dataframe 
groupby_age_bp= patient_high_bp.groupby('age')['high_blood_pressure'].count().reset_index()
groupby_age_bp


# In[6]:


#plot the scatter graph to show which age group is more prone to diabetes
plt.figure(figsize=(10, 8))

diabetes = groupby_age_diabetes['diabetes']
age =groupby_age_diabetes['age']

plt.scatter(age, diabetes, label = "diabetic patients")

age2=groupby_age_bp['age']
bp = groupby_age_bp['high_blood_pressure']
plt.scatter(age2, bp, label = "patients with high bp")

plt.xlabel("Age Group", size=12)
plt.ylabel("Diabetic and high blood pressure level", size=12)

plt.legend()


# Conclusion - 

# # Task 2 - Find as per gender who has not normal platelets level in blood

# In[6]:


#Filter by platelets(condition lesser then 150000 OR greater then 450000) and create new dataframe
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('heart_disease.csv')
df

platelets= df.loc[(df['platelets']<=150000.00) | (df['platelets']>=450000.00)]
platelets


# In[3]:


#On this new dataframe perform group operation as per gender and create new dataframe 
groupby_gender= platelets.groupby('gender')['platelets'].count().reset_index()
groupby_gender


# In[9]:


#Plot a pie chart as per the gender to show the percentage of male and female who has not normal platelets
value =groupby_gender['platelets']
label = groupby_gender['gender']
plt.pie(values, labels=label, autopct='%%2%%', radius=4)
plt.show()


# Conclusion - 

# In[ ]:




