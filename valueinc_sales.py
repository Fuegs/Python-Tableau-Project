# -*- coding: utf-8 -*-
"""
Created on Fri May  6 10:09:00 2022

@author: alest
"""

import pandas as pd

#file_name = pd.read_csv('file.csv') <-- Format of read_csv

data = pd.read_csv('transaction.csv')
#you can refer to files not in a directory but you need to input the whole path

data = pd.read_csv('transaction.csv', sep=';')

#summary of data
data.info()

#working with calculations
#defining variables
CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

#math operations on tableau
ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberofItemsPurchased*ProfitPerItem
CostPerTransaction = CostPerItem*NumberofItemsPurchased
SellingPricePerTransaction = SellingPricePerItem*NumberofItemsPurchased

#costpertansaction column calculation
#CostPerTransaction = CostPerItem * NumberofItemsPurchased
#variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPurchased

#adding new column to dataframe
data['CostPerTransaction'] = CostPerTransaction

#salespertransaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit formula: Profit=Sale-Cost
#Markup formula: Markup=(Sale-Cost)/Cost
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']
data['Markup'] = data['ProfitPerTransaction'] / data['CostPerTransaction']

#rounding markup
roundmarkup = round(data['Markup'],2)
data['Markup'] = roundmarkup

#combining the date
my_name = 'Ale' + 'Storni'
my_date = 'Day' + '-' + 'Month' + '-' + 'Year'

#checking columns data type
print(data['Day'].dtype)
#change columns type
day = data['Day'].astype(str)
print(day.dtype)

my_date = day + '-' + data['Month'] + '-'

year = data['Year'].astype(str)

my_date = day + '-' + data['Month'] + '-' + year

#had to change both day and year to strings so it could combine with month
data['date'] = my_date

#using iloc to view specific columns/rows
data.iloc[0] #views row with index = 0
data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 5 rows

data.head(5) #brings in first 5 rows
data.iloc[:,2] #brings in all rows of certain column
data.iloc[4,2] #brings in 4th row of 2nd column

#client keywords can be split into Age, Job, length
#split: new_var = column.str.split('sep', expand = True)
split_col = data['ClientKeywords'].str.split(',',expand = True)
#creating new colmns
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

#using replace function
data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LengthofContract'] = data['LengthofContract'].str.replace(']','')


#using lower function to make lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files
#bringing in new data set
seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#merging files: merge_df = pd.merge(df_old , df_new , on = 'key')
data = pd.merge(data, seasons , on = 'Month') 

#dropping columns
#df = df.drop('columnname' , axis = 1)
data = data.drop('Year' , axis = 1)
data = data.drop('Month' , axis = 1)
data = data.drop('Day' , axis = 1)
data = data.drop('ClientKeywords' , axis = 1)

#exproting into csv
data.to_csv('ValueInc_cleaned.csv' , index = False) 











