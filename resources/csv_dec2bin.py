import csv
from numpy import genfromtxt
from collections import Counter

def frequency(value, arrayLength, array):
	count = 0
	for i in range(arrayLength):
		if array[i] == value:
			count = count +1
	return count

dir_name = './frequency_results/'
file_name = 'frequency_3000count.csv'
my_data = genfromtxt(dir_name+file_name,delimiter = ',')
print len(my_data) 
print my_data[0][1]
print my_data[1][0]
my_data1 = my_data.tolist() #my_data1 is the 2-d array of csv file

bin_len = 16
for i in range(0,len(my_data)):
	my_data1[i][0]=my_data1[i][0]-1
#convert a decimanl value to a binary string and append the string to row array
	my_data1[i].append(bin(int(my_data1[i][0]))[2:].zfill(bin_len))
#print my_data1[i][2]
#count the frequency of 1s of binary string and append the results to row array
	c = my_data1[i][2].count('1')
	my_data1[i].append(c)
	my_data1[i].append(float(c)/bin_len)

#print my_data1
with open('./frequency_dec2bin.csv','wb') as csvfile:
	spamwriter = csv.writer(csvfile)
	for i in range(0,len(my_data)):
		spamwriter.writerow(my_data1[i])

csvfile.close()

