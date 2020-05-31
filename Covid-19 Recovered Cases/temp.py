import pandas as pd
import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plt
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
from matplotlib.pyplot import figure

#for plotting
plt.style.use('seaborn-darkgrid') #we will use plot style as seaborn-darkgrid
CountriesName = ['US','Brazil','Russia','Germany','Italy','Spain','Turkey','Iran','India','Peru','France','China','Mexico','Saudi Arabia','Canada']

data = []
x = []
y = []
i= 0
k = 0
l = 0
def animate(i):
	global k
	k = 0
	global l
	l = 0 
	#here we are reading all live data from new csv in the format china1.csv,US1.csv,etc
	data = pd.read_csv(CountriesName[k] + '1.csv')
	data1 = pd.read_csv(CountriesName[k+1] + '1.csv')
	data2 = pd.read_csv(CountriesName[k+2] + '1.csv')
	data3 = pd.read_csv(CountriesName[k+3] + '1.csv')
	data4 = pd.read_csv(CountriesName[k+4] + '1.csv')
	data5 = pd.read_csv(CountriesName[k+5] + '1.csv')
	data6 = pd.read_csv(CountriesName[k+6] + '1.csv')
	data7 = pd.read_csv(CountriesName[k+7] + '1.csv')
	data8 = pd.read_csv(CountriesName[k+8] + '1.csv')
	data9 = pd.read_csv(CountriesName[k+9] + '1.csv')
	data10 = pd.read_csv(CountriesName[k+10] + '1.csv')
	data11 = pd.read_csv(CountriesName[k+11] + '1.csv')
	data12 = pd.read_csv(CountriesName[k+12] + '1.csv')
	data13 = pd.read_csv(CountriesName[k+13] + '1.csv')
	data14 = pd.read_csv(CountriesName[k+14] + '1.csv') # As We are plotting top 15 countries only
	#data15 = pd.read_csv(CountriesName[k+15] + '1.csv')
	#data16 = pd.read_csv(CountriesName[k+16] + '1.csv')
	# data17 = pd.read_csv(CountriesName[k+17] + '1.csv')
	# data18 = pd.read_csv(CountriesName[k+18] + '1.csv')
	# data19 = pd.read_csv(CountriesName[k+19] + '1.csv')
	# data20 = pd.read_csv(CountriesName[k+20] + '1.csv')
	# data21 = pd.read_csv(CountriesName[k+21] + '1.csv')
	# data22 = pd.read_csv(CountriesName[k+22] + '1.csv')
	# data23 = pd.read_csv(CountriesName[k+23] + '1.csv')
	# data24 = pd.read_csv(CountriesName[k+24] + '1.csv')
	# data25 = pd.read_csv(CountriesName[k+25] + '1.csv')
	y = data['newCases']
	x = data['totalCases']
	y1 = data1['newCases']
	x1 = data1['totalCases']
	y2 = data2['newCases']
	x2 = data2['totalCases']
	y3 = data3['newCases']
	x3 = data3['totalCases']
	y4 = data4['newCases']
	x4 = data4['totalCases']
	y5 = data5['newCases']
	x5 = data5['totalCases']
	y6 = data6['newCases']
	x6 = data6['totalCases']
	y7 = data7['newCases']
	x7 = data7['totalCases']
	y8 = data8['newCases']
	x8 = data8['totalCases']
	y9 = data9['newCases']
	x9 = data9['totalCases']
	y10 = data10['newCases']
	x10 = data10['totalCases']
	y11 = data11['newCases']
	x11 = data11['totalCases']
	y12 = data12['newCases']
	x12 = data12['totalCases']
	y13 = data13['newCases']
	x13 = data13['totalCases']
	y14 = data14['newCases']
	x14 = data14['totalCases']
	#y15 = data15['newCases']
	#x15 = data15['totalCases']
	#y16 = data16['newCases']
	#x16 = data16['totalCases']
	# y17 = data17['newCases']
	# x17 = data17['totalCases']
	# y18 = data18['newCases']
	# x18 = data18['totalCases']
	# y19 = data19['newCases']
	# x19 = data19['totalCases']
	# y20 = data20['newCases']
	# x20 = data20['totalCases']
	# y21 = data21['newCases']
	# x21 = data21['totalCases']
	# y22 = data22['newCases']
	# x22 = data22['totalCases']
	# y23 = data23['newCases']
	# x23 = data23['totalCases']
	# y24 = data24['newCases']
	# x24 = data24['totalCases']
	# y25 = data25['newCases']
	# x25 = data25['totalCases']	
	
	plt.cla()
	plt.plot(x,y) # plotting countries data total cases in x axis and new cases in y axis 
	plt.text(x.iloc[-1] , y.iloc[-1],CountriesName[0]) #creating a plot with text of that country name
	plt.plot(x1,y1)
	plt.text(x1.iloc[-1] , y1.iloc[-1],CountriesName[1])
	plt.plot(x2,y2)
	plt.text(x2.iloc[-1] , y2.iloc[-1],CountriesName[2])
	plt.plot(x3,y3)
	plt.text(x3.iloc[-1] , y3.iloc[-1],CountriesName[3])
	plt.plot(x4,y4)
	plt.text(x4.iloc[-1] , y4.iloc[-1],CountriesName[4])
	plt.plot(x5,y5)
	plt.text(x5.iloc[-1] , y5.iloc[-1],CountriesName[5])
	plt.plot(x6,y6)
	plt.text(x6.iloc[-1] , y6.iloc[-1],CountriesName[6])
	plt.plot(x7,y7)
	plt.text(x7.iloc[-1] , y7.iloc[-1],CountriesName[7])
	plt.plot(x8,y8)
	plt.text(x8.iloc[-1] , y8.iloc[-1],CountriesName[8])
	plt.plot(x9,y9)
	plt.text(x9.iloc[-1] , y9.iloc[-1],CountriesName[9])
	plt.plot(x10,y10)
	plt.text(x10.iloc[-1] , y10.iloc[-1],CountriesName[10])
	plt.plot(x11,y11)
	plt.text(x11.iloc[-1] , y11.iloc[-1],CountriesName[11])
	plt.plot(x12,y12)
	plt.text(x12.iloc[-1] , y12.iloc[-1],CountriesName[12])
	plt.plot(x13,y13)
	plt.text(x13.iloc[-1] , y13.iloc[-1],CountriesName[13])
	plt.plot(x14,y14)
	plt.text(x14.iloc[-1] , y14.iloc[-1],CountriesName[14])
	# plt.plot(x15,y15)
	# plt.text(x15.iloc[-1] , y15.iloc[-1],CountriesName[15])
	# plt.plot(x16,y16)
	# plt.text(x16.iloc[-1] , y16.iloc[-1],CountriesName[16])
	# # plt.plot(x17,y17)
	# plt.text(x17.iloc[-1] , y17.iloc[-1],CountriesName[17])
	# plt.plot(x18,y18)
	# plt.text(x18.iloc[-1] , y18.iloc[-1],CountriesName[18])
	# plt.plot(x19,y19)
	# plt.text(x19.iloc[-1] , y19.iloc[-1],CountriesName[19])
	# plt.plot(x20,y20)
	# plt.text(x20.iloc[-1] , y20.iloc[-1],CountriesName[20])
	# plt.plot(x21,y21)
	# plt.text(x21.iloc[-1] , y21.iloc[-1],CountriesName[21])
	# plt.plot(x22,y22)
	# plt.text(x22.iloc[-1] , y22.iloc[-1],CountriesName[22])
	# plt.plot(x23,y23)
	# plt.text(x23.iloc[-1] , y23.iloc[-1],CountriesName[23])
	# plt.plot(x24,y24)
	# plt.text(x24.iloc[-1] , y24.iloc[-1],CountriesName[24])
	# plt.plot(x25,y25)
	# plt.text(x25.iloc[-1] , y25.iloc[-1],CountriesName[25])
	plt.ylabel("New Recovered Cases (in the Past Week)" , color = "Red") # labelling
	plt.xlabel("Total Recovered Cases" , color = "Red")
	plt.title("Trajectory of COVID-19 Recovered Cases", color = "Red")
	#plt.legend(CountriesName)

	plt.tight_layout() # for dynamically updating our plot
	
ani = FuncAnimation(plt.gcf() , animate , interval = 200) #matplotlib animation function
plt.tight_layout()
plt.show() # to show the graph



#here we are complete with our data so let plot it we will run csvgenerator.py and temp.py simmultaneously to have result







