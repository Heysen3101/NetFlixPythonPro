import matplotlib.pyplot as plt
import pandas as pd
#import data
data = pd.read_csv("C:/Users/heyse/OneDrive/Desktop/portfolio projects/NetflixPythonProject/netflix_titles.csv")
print(data)

#head
#print(data.head())

#tail
#print(data.tail())

#shape
#print(data.shape)

#size
#print(data.size)

#column names
#print(data.columns)

#datatypes
#print(data.dtypes)

#datainformation
#print(data.info())

#print(data.shape)

##TASK 1= ARE THERE ANY DUPLICATE VALUES? IF YES REMOVE THE DUPLICATE VALUES.
#find out the duplicate data
print(data[data.duplicated()])

#remove the duplicate data
print(data.drop_duplicates())

#to make the changes permanent add inplace=true
data.drop_duplicates(inplace = True)

### TASK 2 = IS THERE ANY NULL VALUE? IF ANY , show them on heat map

#show the null values
print(data.isnull())

#show the sum of null values for each column
print(data.isnull().sum())

#show on heat map(Seaborn Library)
import seaborn as sns
#sns.heatmap(data.isnull())
#plt.show()

#1)show the show id and director for 'House of Cards'
#using isin function
print(data[data['title'].isin(['House of Cards'])])
row= data.iloc[1059]  # DataFrame is 0-indexed, so 99 represents the 100th row
print(row)

# using str.contains
print(data[data['title'].str.contains('House of Cards')])

#2) which year had the highest number of releases?
#convert int64 into str
data['release_year'] = data['release_year'].astype(str)
#check the data types and convert it from object to date and time(use date time function)
data['Date_N'] = pd.to_datetime(data['release_year'].str.strip(), format='%Y', errors='coerce')
#dhdmh
#check the number of releases in that year
print(data['Date_N'].dt.year.value_counts())

#show this on a bar graph
#data['Date_N'].dt.year.value_counts().plot(kind='bar')
#plt.show()

print(data.columns)

#3) How many movies and shows are there in the dataset? show with count plot
#use group by function to proceed
print(data.groupby('type').type.count())

#show on pie chart
#data['Category'] = data['Category'].str.strip()
#sns.countplot(data=data['Category'])
#plt.show()
category_counts = data['type'].value_counts()

# Create a count plot using the counts
#sns.barplot(x=category_counts.index, y=category_counts.values)
#plt.show()

#4 SHow all the movies that were release in 2000
#filtering
print(data[(data['type']=='Movie') & (data['Date_N']=='2000')])

#5 Show only the titles of tv shows where all tv shows were release in india
print(data[(data['director']=='TV Show') & (data['country']=='India')]['title'])

#6 Show top 10 directors, who gave highest number of tv shows& movies to Netflix.
#value_count()functions used

print(data['director'].value_counts().head(10))

#7 show all the Records where category is movie and type is comedies or country is united kingdom
# filtering using functions(and,or operators)
print(data[(data['type']=='Movie') & (data['listed_in']=='Comedies')])
#addid or function
print(data[(data['type']=='Movie') & (data['Date_N']=='2000') |(data['country']=='United Kingdom')])

#8 in how many movies , tom cruise was cast
#we should use contain function but before we should remove null values
#drop na function
data_new=data.dropna()

print(data_new.isnull().sum())

#use contain function to show movies where tom cruise is included
print(data_new[data_new['cast'].str.contains('Tom Cruise')])

#9 what are different ratings defined by netflix
#use nunique() function to show different ratings

print(data['rating'].nunique())

#use unique to show the names of differnt ratings
print(data['rating'].unique())

#9.1 how many movies got TV-14 rating in canada
print(data[(data['type']=='Movie') & (data['rating']=='TV-14') &(data['country']=='Canada')])

print(data[(data['type']=='Movie') & (data['rating']=='TV-14') &(data['country']=='Canada')].shape)

#9.2 how many tv show got r rating after 2018
print(data[(data['type']=='TV Show') & (data['rating']=='R') &(data['Date_N']>'2018')])
print(data[(data['type']=='TV Show') & (data['rating']=='R') &(data['Date_N']>'2018')].shape)

#Q 10 What is the maximum duration of a movie show on netflix

#there are different durations, use unique to find it
print(data.duration.unique())

#convert object to numeric use split with new colums
data[['minutes','unit']]=data['duration'].str.split(' ',expand=True)
print(data)

#use max function to find highest duration
data['minutes'].max


