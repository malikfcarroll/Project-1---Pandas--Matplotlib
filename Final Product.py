#!/usr/bin/env python
# coding: utf-8

# In[267]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

#Importing tools and libraries needed 


# In[268]:


pl_one_data = pd.read_csv('nbadatasets/allen.csv')
pl_two_data = pd.read_csv('nbadatasets/billups.csv')
pl_three_data = pd.read_csv('nbadatasets/bryant.csv')
pl_four_data = pd.read_csv('nbadatasets/carter.csv')
pl_five_data = pd.read_csv('nbadatasets/duncan.csv')
pl_six_data = pd.read_csv('nbadatasets/garnett.csv')
pl_seven_data = pd.read_csv('nbadatasets/iverson.csv')
pl_eight_data = pd.read_csv('nbadatasets/kidd.csv')
pl_nine_data = pd.read_csv('nbadatasets/marion.csv')
pl_ten_data = pd.read_csv('nbadatasets/mcgrady.csv')
pl_eleven_data = pd.read_csv('nbadatasets/nash.csv')
pl_twelve_data = pd.read_csv('nbadatasets/nowitski.csv')
pl_thirteen_data = pd.read_csv('nbadatasets/oneal.csv')
pl_fourteen_data = pd.read_csv('nbadatasets/pierce.csv')
pl_fifteen_data = pd.read_csv('nbadatasets/stojakovic.csv')

#Reading each of the fifteen csv files in as separate variables
#Each file contains data for each of the fifteen players in our population


# In[269]:


pl_eight_data.head()

#Printing the first five lines of one of the data sets to see what our table looks like
#Also making note of the titles of our columns of interest for later use


# In[270]:


allen = pl_one_data[['Age', 'PTS', 'TRB', 'AST', 'FG%']]
billups = pl_two_data[['Age', 'PTS', 'TRB', 'AST', 'FG%']]
bryant = pl_three_data[['Age', 'PTS', 'TRB', 'AST', 'FG%']]
carter = pl_four_data[['Age', 'PTS', 'TRB', 'AST', 'FG%']]
duncan = pl_five_data[['Age', 'PTS', 'TRB', 'AST', 'FG%']]
garnett = pl_six_data[['Age', 'PTS', 'TRB', 'AST', 'FG%']]
iverson = pl_seven_data[['Age', 'PTS', 'TRB', 'AST', 'FG%']]
kidd = pl_eight_data[['Age', 'PTS', 'TRB', 'AST', 'FG%']]
marion = pl_nine_data[['Age', 'PTS', 'TRB', 'AST', 'FG%']]
mcgrady = pl_ten_data[['Age', 'PTS', 'TRB', 'AST', 'FG%']]
nash = pl_eleven_data[['Age', 'PTS', 'TRB', 'AST', 'FG%']]
nowitski = pl_twelve_data[['Age', 'PTS', 'TRB', 'AST', 'FG%']]
oneal = pl_thirteen_data[['Age', 'PTS', 'TRB', 'AST', 'FG%']]
pierce = pl_fourteen_data[['Age', 'PTS', 'TRB', 'AST', 'FG%']]
stojakovic = pl_fifteen_data[['Age', 'PTS', 'TRB', 'AST', 'FG%']]

#Assigning the relevant columns to fifteen new data frames for each player
#Considered dropping the unwanted columns instead, but want to preserve the original data sets


# In[272]:


allen['Name'] = 'Ray Allen'
billups['Name'] = 'Chauncey Billups'
bryant['Name'] = 'Kobe Bryant'
carter['Name'] = 'Vince Carter'
duncan['Name'] = 'Tim Duncan'
garnett['Name'] = 'Kevin Garnett'
iverson['Name'] = 'Allen Iverson'
kidd['Name'] = 'Jason Kidd'
marion['Name'] = 'Shawn Marion'
mcgrady['Name'] = 'Tracy McGrady'
nash['Name'] = 'Steve Nash'
nowitski['Name'] = 'Dirk Nowitski'
oneal['Name'] = "Shaquille O'Neal"
pierce['Name'] = 'Paul Pierce'
stojakovic['Name'] = 'Peja Stojakovic'

#Appending each player's name to the corresponding data frame
#This will make it easier to use the 'groupby' function later
#Rather than remembering the index, we can now call directly by name


# In[273]:


df = pd.concat(
    [allen, billups, bryant, carter, duncan, garnett, iverson, kidd, marion, mcgrady, nash, nowitski, oneal, pierce, stojakovic]
)

#Combining the data frames of each player, now also including their unique name identifier, into one table
#This will make it easier to just call columns and rows from one specific data frame instead of fifteen


# In[274]:


df.info()
print(df.head())

#Optional step
#Confirms that our new data frame df is properly formatted and should contain the information we need


# In[275]:


df_grouped = df.groupby(['Name', 'Age'])['PTS'].unique().reset_index()
print(df_grouped.head())

#For the first analysis, sorting the number of points scored by the player and their age for the season


# In[276]:


df_pivoted = df_grouped.pivot(index='Name', columns='Age', values='PTS').reset_index()
print(df_pivoted)

#Creating a pivot table showing the number of points each player scored at each age
#For the analysis, will only use ages 22 to 34
#As shown in table, ages outside of this range have fewer than five values
#It would be hard to make meaningful conclusions off of one or two values


# In[277]:


for i in range(22, 35):
    print('Average points for age ' + str(i) + ': ' + str(df_pivoted[i].mean()))
    
#Before plotting, looking at any obvious trends in the averages    


# In[278]:


for i in range(22, 35):
    print('Maximum points for age ' + str(i) + ': ' + str(df_pivoted[i].max()))
    
#Looking for any obvious trends in the maximums    


# In[279]:


df = df.loc[(df['Age'] >= 22) & (df['Age'] <= 34)]

ages = df['Age']
points = df['PTS']
rebounds = df['TRB']
assists = df['AST']
field_goal_percentage = df['FG%']

plt.figure(figsize=(6,4))

plt.scatter(ages, points, color='purple', marker='X')

plt.xlabel('Age')
plt.ylabel('Points')
plt.title('Points vs Age')
plt.axis([20, 35, 10, 35])

plt.savefig('Points versus Age.jpg')

plt.show()

#Declaraing x and y variables needed for analyses
#Creating a figure
#Plotting points over the course of a player's career
#Scatter plot makes the most sense here as it is effectively time series data
#Setting up parameter for the graph
#Saving image of plot


# In[281]:


get_ipython().run_line_magic('matplotlib', 'inline')

plt.figure(figsize=(9,6))
x = np.linspace(20, 35, 200)

lobf_pts = np.polyfit(ages, points, 2)
plt.plot(x, np.polyval(lobf_pts, x), color='red',  linestyle='--')

plt.scatter(ages, points, color='blue', marker='o')

plt.xlabel('Age')
plt.ylabel('Points')
plt.title('Points vs Age (with trend line)')
plt.axis([21, 35, 10, 35])
plt.legend(['Curve of best fit'])

plt.savefig('Points versus Age with trend line.png')

plt.show()


print('Quadratic function of best fit is: ' + str(lobf_pts[0]) + 'x^2 + ' + str(lobf_pts[1]) + 'x - ' + str(lobf_pts[2]*-1))

#Creating and plotting a line of best fit for the relationship between points and age
#Using a quadratic as I expect the data to follow somewhat of a bell curve
#Using 'inline' magic function to plot the line of best fit over the scatter plot
#Adding a legend to identify the regression line


# In[264]:


get_ipython().run_line_magic('matplotlib', 'inline')

plt.figure(figsize=(9,6))

lobf_reb = np.polyfit(ages, rebounds, 2)
plt.plot(x, np.polyval(lobf_reb, x), color='#FFB266', linestyle=':')

plt.scatter(ages, rebounds, color='#808080', marker='^')

plt.xlabel('Age')
plt.ylabel('Rebounds')
plt.title('Rebounds vs Age (with trend line)')
plt.legend(['Curve of best fit'])
plt.axis([21, 35, 0, 15])
plt.savefig('Rebounds versus Age with trend line.png')

plt.show()

print('Quadratic function of best fit is: ' + str(lobf_reb[0]) + 'x^2 + ' + str(lobf_reb[1]) + 'x + ' + str(lobf_reb[2]))

#Plotting Rebounds versus Age
#No real relationship seen here, independent of linear, quadratic, cubic, etc regression


# In[259]:


get_ipython().run_line_magic('matplotlib', 'inline')

plt.figure(figsize=(9,6))

lobf_ast = np.polyfit(ages, assists, 1)
plt.plot(x, np.polyval(lobf_ast, x), color='#E4E95B', linestyle='-')

plt.scatter(ages, assists, color='#2BC46D', marker='+')

plt.xlabel('Age')
plt.ylabel('Assists')
plt.title('Assists vs Age (with trend line)')
plt.legend(['Line of best fit'])
plt.axis([21, 35, 0, 15])
plt.savefig('Assists versus Age with trend line.png')

plt.show()

slope, intercept, r_value, p_value, std_err = stats.linregress(ages, assists)
print('Line of best fit is: y = ' + str(slope) + 'x - ' + str(intercept*-1))
print('R^2 value is: ' + str(r_value**2))

#Plotting Assists versus Age
#No real relationship seen here, independent of linear, quadratic, cubic, etc. regression


# In[283]:


get_ipython().run_line_magic('matplotlib', 'inline')

plt.figure(figsize=(9,6))

lobf_fgp = np.polyfit(ages, field_goal_percentage, 2)
plt.plot(x, np.polyval(lobf_fgp, x), color='#4BFAD1', linestyle='-.')

plt.scatter(ages, field_goal_percentage, color='#000000', marker='2')

plt.xlabel('Age')
plt.ylabel('Field Goal Percentage (%)')
plt.title('Field Goal Percentage vs Age (with trend line)')
plt.legend(['Curve of best fit'])
plt.axis([21, 35, 0.35, 0.60])
plt.savefig('Field Goal Percentage versus Age with trend line.png')

plt.show()

print('Quadratic function of best fit is: ' + str(lobf_fgp[0]) + 'x^2 - ' + str(lobf_fgp[1]*-1) + 'x + ' + str(lobf_fgp[2]))

#Plotting FG% versus Age
#No real relationship seen here, independent of linear, quadratic, cubic, etc. regression


# In[ ]:




