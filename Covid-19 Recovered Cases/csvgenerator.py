import csv
import random
import time
import pandas as pd

# This file is basically generating run time or live data here we will update countries name

index = 0
newCases = 0
totalCases = 0
CountriesName = ['US','Brazil','Russia','Germany','Italy','Spain','Turkey','Iran','India','Peru','France','China','Mexico','Saudi Arabia','Canada']
#Here is our top 15 countries data
new = [] # it will save new cases our each 15 countries
total = [] # it will save total cases
fieldnames = ["index", "totalCases", "newCases"] # our run time file will be structured in this way three columns

for i in range(15): #As we are only examining top 15 countries
    df = pd.read_csv(CountriesName[i] + ".csv") # this will read all countries data from their respective csv
    total.append(df[CountriesName[i]]) # all total cases our every country will be append here and new cases will be append in next line
    new.append(df['newCases'])

#print(new)
#print(total)
#print(new[0][9])
#df = pd.read_csv('TotalCases.csv')
#total = df['totalCases']
#new = df['newCases']

count = 0
counter = 0
#print(len(CountriesName))

for i in range(15):
    with open(CountriesName[i] + "1.csv", 'w') as csv_file: # here we are generating live data from already develop csv's but here we are creating new csv with this format US1.csv,china1.csv,etc
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames) #setting header or column name as index , new cases , total cases
        csv_writer.writeheader()

# j represent top 15 countries we will update data of each countries at a time so we will initialize j =0 and will update it timely
# count will indicate the row number ,which current row is this count will start from 0 and end with 130
# #while True:
for i in range(130): # total row count
    for j in range(len(CountriesName)): # this loop will generate live data with the already build csv and creating new csv 
        with open(CountriesName[j] + '1.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            info = {
            "index": index,
            "newCases": new[j][count],
            "totalCases": total[j][count]
            }
            csv_writer.writerow(info)
            print(index,total[j][count],new[j][count])    
    index += 1        
    time.sleep(0.3)        #sleep to have pause in data fetching to have look like live data # now it's time to plot
    count = count + 1    