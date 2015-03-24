print "Test Program"
import pandas as pd
import collections
import matplotlib.pyplot as plt

### for review
#1 - lists are mutable and can change, use li=[]. 
#2 - tuples are immutable. tp = ().
#3 - sets are like lists with only unique values

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

data = data.splitlines()
data = [i.split(', ') for i in data]

column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

print df

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

print df['Alcohol'].mean() 
# 5.4436363636363634
#df['Alcohol'].median() 

print df['Alcohol'][2]



def show_lists(a,b,c):
	li = [a,b,c]

	print li[0]

	li.append(5)

	print li[3]	

	print li[::-1]

	print len(li)


def show_tuples():

	tup = (3,7,45)

	print tup[1]

	bookmark1 = (35, 5)
	bookmark2 = (86, 15)
	bookmark3 = (106, 11)
	notes = [bookmark1, bookmark2, bookmark3]

	print notes


def show_sets():
	my_set = {1,2,3}
	your_set = {4,2,6}

	print my_set & your_set


show_lists(3,66,77)

