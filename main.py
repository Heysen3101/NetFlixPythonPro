''''''
#Importing Librabries Needed for this Project
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
''''''

''''''
#Loading and Reading the Data
data = pd.read_csv("C:/Users/heyse/OneDrive/Desktop/portfolio projects/NetflixPythonProject/netflix_titles.csv")
''''''

''''''
#Formatting the Column names (using capitalize function)
data.columns = data.columns.str.capitalize()
''''''

''''''
#Baic Functions used in Python

print(data.columns) #To view the columns in the dataset

print(data.head()) #To view the first 5 datainfo

print(data.tail()) #To view the last 5 datainfo

print(data.shape) #To view the shape of the table

print(data.size) #How many cells are used in the Data

print(data.dtypes) #Data type eg:float,object,int,datetime

print(data.info())  #gives general information about the dataset
''''''

''''''
#Formatting the dataset by checking the duplicates and removing the duplicates
print(data[data.duplicated()]) # checking the duplicates

print(data.drop_duplicates()) # removing the duplicates

data.drop_duplicates(inplace = True) #permanent changes to the dataset
''''''

''''''
#Checking The null values
print(data.isnull().sum()) #null values for each column

sns.heatmap(data.isnull()) #plot the null values on heatmap
plt.show()
''''''

''''''
# Show the director and Show id for 'Cuckoo'
print(data[data['Title'].isin(['Cuckoo'])]) #using isin function
row= data.iloc[514]  # iloc function shows all the information in that row
print(row)

print(data[data['Title'].str.contains('Cuckoo')]) #using contains function for same result
''''''

''''''
# Show the number of releases for every year
#Formatting the existing Date_added column. (datetime function)
data['DateTime_Added'] = pd.to_datetime(data['Date_added'].str.strip(), format='%B %d, %Y', errors='coerce')
data['New_Date_Added'] = data['DateTime_Added'].dt.date

#Formatting the existing Release_year column.
data['Release_Year_A'] = pd.to_datetime(data['Release_year'], format='%Y', errors='coerce')

print(data['Release_Year_A'].dt.year.value_counts()) #count of total releases for each year

#Representation on the bar graph
data['Release_Year_A'].dt.year.value_counts().plot(kind='bar')
plt.show()
''''''

''''''
#How many movies and shows are there in the dataset? Show it with barplot

print(data.groupby('Type').Type.count()) #used group by function to categorise

#show on barplot
sns.set(style="ticks")
plt.figure(figsize=(8, 6))
type_counts = data['Type'].value_counts()
# seaborn
sns.barplot(x=type_counts.index, y=type_counts.values)
plt.xlabel('Type')
plt.ylabel('Count')
plt.title('Distribution of Types')
plt.show()
''''''

''''''
#Show all the movies released in year 2017
print(data[(data['Type']=='Movie') & (data['Release_Year_A']=='2017')]) #And function

#Show only the titles of tv shows where all tv shows were release in india
print(data[(data['Type']=='TV Show') & (data['Country']=='India')]['Title'])
''''''

''''''
#Show Top 10 Directors who gave highest number of tv shows& movies to Netflix

print(data['Director'].value_counts().head(10)) #value_count function
''''''

''''''
# show all the Records where TYPE is movie and LISTED is comedies or country is united kingdom
# Filtering using functions(and,or operators)
print(data[(data['Type']=='Movie') & (data['Listed_in']=='Comedies')])
#and or function
print(data[(data['Type']=='Movie') & (data['Release_Year_A']=='2000') |(data['Country']=='United Kingdom')])
''''''

''''''
# How many movies was Tom Cruise casted in?
#drop na function
data_new=data.dropna()
print(data_new.isnull().sum())

print(data_new[data_new['Cast'].str.contains('Tom Cruise')]) #used contain function to show movies where tom cruise is included
''''''

''''''
#List all different ratings defined by netflix
print(data['Rating'].nunique()) #use nunique() function to show different ratings

print(data['Rating'].unique()) #use unique to show the names of differnt ratings

#List all movies got TV-14 rating in Canada
print(data[(data['Type']=='Movie') & (data['Rating']=='TV-14') &(data['Country']=='Canada')])
print(data[(data['Type']=='Movie') & (data['Rating']=='TV-14') &(data['Country']=='Canada')].shape)

#How many tv show got r rating after 2018
print(data[(data['Type']=='TV Show') & (data['Rating']=='R') &(data['Release_Year_A']>'2015')])
print(data[(data['Type']=='TV Show') & (data['Rating']=='R') &(data['Release_Year_A']>'2015')].shape)
''''''

''''''
#What is the maximum duration of a movie show on netflix

print(data.Duration.unique()) #there are different durations, use unique to find it

data[['minutes','unit']]=data['Duration'].str.split(' ',expand=True) #convert object to numeric use split with new colums
print(data)

#use max function to find highest duration
data['minutes'] = pd.to_numeric(data['minutes']) # Convert 'minutes' column to numeric

max_minutes = data['minutes'].max() # Find the highest value in the 'minutes' column
print("The highest value in the 'minutes' column is:", max_minutes) # Print the highest value

min_minutes = data['minutes'].min() #minimum minutes
print("The lowest value in the 'minutes' column is:", min_minutes)

mean_minutes = data['minutes'].mean() #mean value
print("The mean value in the 'minutes' column is:", mean_minutes)
''''''

''''''
#Which individual country has the highest no of tv shows?
data_tvshow= data[data['Type']=='TV Show']
print(data_tvshow.Country.value_counts().head(1))
''''''

''''''
#Sort the dataset by year? use sort function
print(data.sort_values(by='Release_year', ascending=False).head(5))
''''''

''''''
#Find all the instances where Type is movie and type is dramas |OR| Tpe is tv show and type is Listed_in TV
print(data[(data['Type']=='Movie') & (data['Listed_in']=='Dramas')])

print(data[(data['Type']=='TV Show') & (data['Listed_in']=="Kids' TV")])

print(data[(data['Type']=='Movie') & (data['Listed_in']=='Dramas')|(data['Type']=='TV Show') & (data['Listed_in']=="Kids' TV")])
''''''
