
#Introducción a Pandas

#Import Library

import Numpy as np # linear algebra
import Pandas as pd # import in pandas

import os

#Pandas Data Structure

mySeries = pd.Series([3,-5,7,4], index=['a','b','c','d'])
type(mySeries)

#DataFrame
data = {'Country' : ['Belgium', 'India', 'Brazil' ],
        'Capital': ['Brussels', 'New Delhi', 'Brassilia'],
        'Population': [1234,1234,1234]}
datas = pd.DataFrame(data, columns=['Country','Capital','Population'])
print(type(data))
print(type(datas))

#Import Library
df = pd.read_csv('DJIA_table.csv')
type(df)
# If your Python file is not in the same folder as your CSV file, you should do this as follows.
# df = pd.read_csv('/home/desktop/Iris.csv')

#Excel

# pd.read_excel('filename')
# pd.to_excel('dir/dataFrame.xlsx', sheet_name='Sheet1')

#Others(json, SQL, table, html)

# pd.read_sql(query,connection_object) -> Reads from a SQL table/database
# pd.read_table(filename) -> From a delimited text file(like TSV)
# pd.read_json(json_string) -> Reads from a json formatted string, URL or file
# pd.read_html(url) -> Parses an html URL, string or file and extracts tables to a list of dataframes
# pd.read_clipboard() -> Takes the contentes of your clipboard and passes it to read_table()
# pd.DataFrame(dict) -> From a dict, keys for columns names, values for data as lists

#Exporting Data

# df.to_csv(filename) -> Writes to a CSV file
# df.to_excel(filename) -> Writes on an Excel file
# df.to_sql(table_name, connection_object) -> Writes to a SQL table
# df.to_json(filename) -> Writes to a file in JSON format
# df.to_html(filename) -> Saves as an HTML table
# df.to_clipboard() -> Writes to the clipboard

#Create Test Objects

pd.DataFrame(np.random.rand(20,5)) # 5 columns and 20 rows of random floats

#Summarize Data
### **df.info()** <a id="14"></a>
### **df.info()** <a id="14"></a>


#df.info()

df.info()

#df.shape()

df.shape

#df.index
df.index

#df.columns

df.columns

#df.count()

df.count()

#df.sum()

df.sum()

#df.cumsum()

df.cumsum().head()

#df.min()

df.min()

#df.max()

df:max()

#idxmin()

print("df: ",df['Open'].idxmin())
print("series", mySeries.idxmin())

#idxmax()
print("df: ",df['Open'].idxmax())
print("series: ",mySeries.idxmax())

#df.describe()

df.describe()

#df.mean()

df.mean()

#df.median()
df.median()

#df.quantile([0.25,0.75])

df.quantile([0.25,0.75])

#df.var()
df.var()

#df.std()
df.std()

#df.cummax()
df.cummax()

#df.cummin()
df.cummin()

#df['columnName'].cumproad()

df['Open'].cumprod().head()

# len(df)

len(df)


#df.isnull()

df.isnull().head()

#df.corr()
df.corr()

#Selection & Filtering


#mySeries['b']

mySeries['b']

#df[n:n]

df[1982:]
#Or
#df[5:7]

#df.iloc[[n],[n]]

df.iloc[[0],[3]]

#df.loc[n:n]

#df.loc[n:]
# OR
df.loc[5:7]

#df['columnName']

df['Open'].head()
# OR
# df.Open

#df['columnName'][n]

df['Open'][0]
# OR
# df.Open[0]
# df["Open"][1]
# df.loc[1,["Open"]]

#df['columnName'].nunique()

df['Open'].nunique()

#df['columnName'].unique()

df['Open'].unique()
# We can write the above code as follows:: df.Open.unique()

#df.columnName
df.Open.head()

#df['columnName'].value_counts(dropna =False)

print(df.Open.value_counts(dropna =True).head())
# OR
# print(df['Item'].value_counts(dropna =False))

#df.head(n)

df.head()
# OR
# df.head(15)

#df.tail(n)

df.tail()
# OR
# df.tail(20)

#df.sample(n)

df.sample(5)

#df.sample(frac=0.5)

df.sample(frac=0.5).head()

#df.nlargest(n,'columnName')
df.nlargest(5,'Open')

#df.nsmallest(n,'columnName')

df.nsmallest(3,'Open')

#df[df.columnName < 5]

df[df.Open > 18281.949219]

#df[['columnName','columnName']]

df[['High','Low']].head()
# df.loc[:,["High","Low"]]

#df.loc[:,"columnName1":"columnName2"]
df.loc[:,"Date":"Close"].head()
# OR
# data.loc[:3,"Date":"Close"]

#Create Filter
filters = df.Date > '2016-06-27'
df[filters]

#df.filter(regex = 'code')

df.filter(regex='^L').head()

#np.logical_and

df[np.logical_and(df['Open']>18281.949219, df['Date']>'2015-05-20' )]

#Filtering with &

df[(df['Open']>18281.949219) & (df['Date']>'2015-05-20')]

#Sort Data

df.sort_values('Open').head()

#df.sort_values('columnName', ascending=False)

df.sort_values('Date', ascending=False).head()

#df.sort_index()

df.sort_index().head()

#Rename & Defining New & Change Columns

#df.rename(columns= {'columnName' : 'newColumnName'})

df.rename(columns= {'Adj Close' : 'Adjclose'}).head()
# df = df.rename(columns= {'Id' : 'Identif'}, inplace=True) -> True way
# inplace= True or False; This meaning, overwrite the data set.
# Other Way
# df.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'adjclose']

#Defining New Column

df["Difference"] = df.High - df.Low
df.head()

#Change Index Name

print(df.index.name)
df.index.name = "index_name"
df.head()

#Make all columns lowercase

#df.columns = map(str.lower(), df.columns)

#Make all columns uppercase

#df.columns = map(str.upper(), df.columns)

#Drop Data

#df.drop(columns=['columnName'])

df.drop(columns=['Adj Close']).head()
# df = df.drop(columns=['Id']) -> True way
# OR
# df = df.drop('col', axis=1)
# axis = 1 is meaning delete columns
# axis = 0 is meaning delete rows

#mySeries.drop(['a'])

mySeries.drop(['a'])

#Drop an observation (row)

# df.drop(['2016-07-01', '2016-06-27'])

#Drop a variable (column)

# df.drop('Volume', axis=1)

#Convert Data Types

#df.dtypes

df.dtypes

#df['columnName'] = df['columnName'].astype('dataType')

df.Date.astype('category').dtypes
# OR Convert Datetime
# df.Date= pd.to_datetime(df.Date)

#pd.melt(frame=dataFrameName,id_vars = 'columnName', value_vars= ['columnName'])

df_new = df.head()
melted = pd.melt(frame=df_new,id_vars = 'Date', value_vars= ['Low'])
melted

#Apply Function

#Method 1

def examples(x):   #create a function
    return x*2

df.Open.apply(examples).head()  #use the function with apply() 

#Method 2

df.Open.apply(lambda x: x*2).head()

#Utilities Code

# pd.get_option OR pd.set_option
# pd.reset_option("^display")

# pd.reset_option("display.max_rows")
# pd.get_option("display.max_rows")
# pd.set_option("max_r",102)                 -> specifies the maximum number of rows to display.
# pd.options.display.max_rows = 999          -> specifies the maximum number of rows to display.

# pd.get_option("display.max_columns")
# pd.options.display.max_columns = 999       -> specifies the maximum number of columns to display.

# pd.set_option('display.width', 300)

# pd.set_option('display.max_columns', 300)  -> specifies the maximum number of rows to display.
# pd.set_option('display.max_colwidth', 500) -> specifies the maximum number of columns to display. 

# pd.get_option('max_colwidth')
# pd.set_option('max_colwidth',40)
# pd.reset_option('max_colwidth')

# pd.get_option('max_info_columns')
# pd.set_option('max_info_columns', 11)
# pd.reset_option('max_info_columns')

# pd.get_option('max_info_rows')
# pd.set_option('max_info_rows', 11)
# pd.reset_option('max_info_rows')

# pd.set_option('precision',7) -> sets the output display precision in terms of decimal places. This is only a suggestion.
# OR
# pd.set_option('display.precision',3)

# pd.set_option('chop_threshold', 0) -> sets at what level pandas rounds to zero when it displays a Series of DataFrame. This setting does not change the precision at which the number is stored.
# pd.reset_option('chop_threshold') 