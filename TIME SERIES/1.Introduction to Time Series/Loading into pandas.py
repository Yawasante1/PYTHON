
        ##loading data into pandas
        ## Data name = pandas.read_csv("data or data path")
        ##To Load a non-csv file, just replace csv with file type, example, 
        ##Data name = pandas.read_filetype.filetype-extension("data or data path.extension")

import pandas as pd

#import csv file
df = pd.read_csv("C:/Users/Yaw Asante/Dropbox/PYTHON/1.Introduction to Time Series/concise.csv")

#import excel file
#data = pd.read_excel("C:/Users/Yaw Asante/Dropbox/PYTHON/1.Introduction to Time Series/Ghana.xlsx")

        ##import text data
#data = pd.read_csv("C:/Users/Yaw Asante/Dropbox/PYTHON/1.Introduction to Time Series/pokem.txt")
#data = pd.read_csv("C:/Users/Yaw Asante/Dropbox/PYTHON/1.Introduction to Time Series/pokem.txt", delimiter='\t')

        ###View all data
#print(data)

        #View the top n rows
#print(data.head(10))

        #View the last n rows
#print(data.tail(3))

        ##Reading Data in Pandas
        #Read Headers
#data.columns

        #Read each Column, or a number of columns, by Column Names
#print(data['Name'])
#print(data['Legendary'][10:26])
#print(data[['Name','Type 1','HP']][10:20])



        #Read Each Row
        #to show the top n rows
#print(data.head(4))

        # to transform the ith row into column, using iloc
#print(data.iloc[1])

        # to transform a range of rows into n columns
#print(data.iloc[2:2])

        #Read a Specific Location(R,C), in a Row and Column coordinates, using ","
#print(data.iloc[2,1])

        #to arrange row and columns separately
#for index, row in data.iterrows():
        #print(index, row)

#for index, row in data.iterrows():
        #print(index, row['Name'])
        
        # to select a column, that has a particular row name or item, 
        #example, Type 1 Column, with a fire 
#data.loc[data['Type 1']=="Fire"]

        
        #Descriptive Statistics   Describe
#print(df)
df
