import csv
from numpy import genfromtxt

my_data = genfromtxt('./frequency_count.csv',delimiter = ',')
print len(my_data) 
print my_data[0][1]
print my_data[1][0]
my_data1 = my_data.tolist()

for i in range(0,len(my_data)):
	my_data1[i][0]=my_data1[i][0]-1
	my_data1[i].append(bin(int(my_data1[i][0]))[2:].zfill(16))

#print my_data1
with open('./frequency_dec2bin.csv','wb') as csvfile:
	spamwriter = csv.writer(csvfile)
	for i in range(0,len(my_data)):
		spamwriter.writerow(my_data1[i])

csvfile.close()

