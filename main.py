import matplotlib.pyplot as plt
import pandas as pd
#import data
data = pd.read_csv("C:\\Users\heyse\Downloads\\file.csv")
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
sns.heatmap(data.isnull())
plt.show()

###Questions
#1)show the show id and director for 'House of Cards'
#using isin function
print(data[data['Title'].isin(['House of Cards'])])

# using str.contains
print(data[data['Title'].str.contains('House of Cards')])

#2) which year had the highest number of releases?
#check the data types and convert it from object to date and time(use date time function)
data['Date_N'] = pd.to_datetime(data['Release_Date'].str.strip(), format='%B %d, %Y', errors='coerce')
#dhdmh
#check the number of releases in that year
print(data['Date_N'].dt.year.value_counts())

#show this on a bar graph
data['Date_N'].dt.year.value_counts().plot(kind='bar')
plt.show()

#3) How many movies and shows are there in the dataset? show with pie chart
#use group by function to proceed
print(data.groupby('Category').Category.count())

#show on pie chart
data.groupby('Category').Category.count().plot(kind='bar')
plt.show()
