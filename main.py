# Importing necessary modules for our project
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Using our dataset and cleaning empty and other data
data = pd.read_csv("forbes.csv")
data['netWorth'] = data['netWorth'].str.strip('$')
data['netWorth'] = data['netWorth'].str.strip('B')
data['netWorth'] = data['netWorth'].astype(float)


st.title('Billoniare Dataset Analyis')


st.write(' ### Oldest Billioniares in the World ')

oldest_person = data.sort_values(by=['age'], ascending=False).head(10)
# oldest_person
oldest_person['countryOfCitizenship'].value_counts()


st.write(" Bar Chart Showing Age Wise Distribution of Shows")
fig = plt.figure(figsize=(10, 4))
sns.barplot(x="age", y='personName', data=oldest_person)
st.pyplot(fig)
st.write('The table above shows the list of the 10 oldest billioniares from the world. This shows that 3 of the oldest billioniares were from United States and the oldest billoniare is from Malaysia, "Robert Kuok" who is 97 years of age. The graph below shows the result being shown in barplot.')


# Categories of Billioniares
st.write('Category wise Divison of Billioniares')
count = plt.figure(figsize=(10, 4))
sns.countplot(y=data.category)
st.pyplot(count)
st.write('The count plot above shows the number of billioniares according to their industry. The data shows that Finance & Investments sector has the highest number of billioniares followed by Technology field. Sports industries has lowest number of billioniares.')


# ### Billioniare's Country
# country = data['countryOfCitizenship'].value_counts().head()
# country
# index = ['USA', 'China', 'Germany', 'Russia', 'India']
# plt.pie(country, labels=index)
# plt.title("Top 5 Countires With Billioniares")
# fig = plt.gcf()
# fig.gca().add_artist(central_circle);
# The pie diagram above shows the top 5 countries with billioniares. We can see that most of the billioniares are from USA which are followed by China.
# ### Japanese Billioniares Data
# This query was runed to find out the billioniares who are from Japan. This shows that there are 15 billioniares from Japan in the list. Overally, 29th ranked Masayoshi Son is the richest person in Japan with a networth of 45.4B.
# japan = data.query("countryOfCitizenship == 'Japan'")
# japan
# sns.barplot(data=japan, x="netWorth", y='age');
# plt.title('Age wise NetWorth Distribution');
# The bar plot above shows the age vs networth graph of the Japanese billioniares in the data. This shows that most of the people are above 40 years of age.
# category = japan.category.value_counts()
# index = ['Fashion & Retail', 'Telecom', 'Manufacturing', 'Real Estate', 'Technology', 'Media & Entertainment'];
# plt.pie(category, labels=index);
# The pie chart above shows the industires the billioniares from Japan have invested and earned their wealth from. This shows that
# most of the billioniares from Japan have invested a lot in Fashion and Retail sector.
# ### Asking Questions

# ####  1. Who are the top 5 billioniares from Real Estate Industry?
# realestate = data.query("category == 'Real Estate'").head()
# realestate
# # investments = data.query("category == 'Real Estate'").value_counts()
# The result above provide us the top 5 billioniares in the real estate industry. Most of the billioniares on real estate busienss are from China and the billioniare with highest networth is Mr.Lee Shau Kee of China with 31.7B.
# #### 2. Find the average age of the billioniares in the dataset.
# average_age = data['age'].mean()
# average_age
# The average age of the billioniares in the dataset is 64.4.

data2 = data.head(20)
sns.scatterplot(x='netWorth', y='personName', data=data2)
plt.title("Scatter Plot Showing networth varitation between top 20 billioniares")
