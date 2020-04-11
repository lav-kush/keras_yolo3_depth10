import csv
import glob
import math


import csv
output = {}
with open('0train.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    count = 0
    for row in sorted(csv_reader):
    	print row[0]
    	if output.get(row[0], False):
	    	output[row[0]].append([row[1], row[2], row[3], row[4], row[5]])
    	else:
	    	output[row[0]] = [[row[1], row[2], row[3], row[4], row[5]]]

with open("0finaltrain.csv", 'w') as csvfile:
	csvwriter = csv.writer(csvfile) 
	for key in  sorted(output.keys()):
		string_value = key+" "
		for value in output[key]:
			string_value += ",".join(value) + " "
		string_value = string_value[:-1]
		print (key, output[key], string_value)
		csvwriter.writerow([string_value])  
