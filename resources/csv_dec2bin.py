import csv
from numpy import genfromtxt

def frequency(value, arrayLength, array):
	count = 0
	for i in range(arrayLength):
		if array[i] == value:
			count = count +1
	return count

dir_name = './frequency_results/'
file_name = 'frequency_2original10000.csv'
my_data = genfromtxt(dir_name+file_name,delimiter = ',')
print len(my_data) 
print my_data[0][1]
print my_data[1][0]
my_data1 = my_data.tolist() #my_data1 is the 2-d array of csv file

bin_len = 16
for i in range(0,len(my_data)):
	my_data1[i][0]=my_data1[i][0]-1
#convert a decimanl value to a binary string and append the string to row array
	my_data1[i].append('b'+(bin(int(my_data1[i][0]))[2:].zfill(bin_len)))
#print my_data1[i][2]
#count the frequency of 1s of binary string and append the results to row array
	c = my_data1[i][2].count('1')
	my_data1[i].append(c)
	my_data1[i].append(float(c)/bin_len)
#count No. of bit changes	
	counter_change =0
	t = (len(my_data1[i][2])-1)/2
	for j in range(1,t):
		if my_data1[i][2][j] != my_data1[i][2][j+1]:
			counter_change = counter_change +1
	if my_data1[i][2][1] != my_data1[i][2][t]:
		counter_change = counter_change +1
	my_data1[i].append(counter_change)

	for j in range(t+1,2*t):
		if my_data1[i][2][j] != my_data1[i][2][j+1]:
			counter_change = counter_change +1
	if my_data1[i][2][t+1] != my_data1[i][2][2*t]:
		counter_change = counter_change +1	
	my_data1[i].append(counter_change)




#print my_data1
with open('./frequency_dec2bin.csv','wb') as csvfile:
	spamwriter = csv.writer(csvfile)
	for i in range(0,len(my_data)):
		spamwriter.writerow(my_data1[i])

csvfile.close()

