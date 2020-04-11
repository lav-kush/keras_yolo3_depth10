import csv
import glob
import math

dataset={
	'car': 0,
	'heavy vehicle': 1,
	'default': 2
}

retinanet_folder = [
		'test_retinanet/',
		'train_retinanet/',
		'train_retinanet/other/',
		'test_retinanet/new/'
]

yolo_folder = [
		'test/',
		'train/',
		'train/other/',
		'test/new/'
]

for i, folder in enumerate(retinanet_folder):
	print("\nfolder : ", folder, i)
	for file in glob.glob(folder+"*.csv"):
		print("file: ", file)
		file_name = file.split("/")[-1]
		target_folder = yolo_folder[i]

		output = {}
		with open(file) as csv_file:
		    csv_reader = csv.reader(csv_file, delimiter=',')
		    count = 0
		    for row in sorted(csv_reader):
		    	# print (row[0])
		    	row[5] = str(dataset[row[5]])
		    	if output.get(row[0], False):
			    	output[row[0]].append([row[1], row[2], row[3], row[4], row[5]])
		    	else:
			    	output[row[0]] = [[row[1], row[2], row[3], row[4], row[5]]]

		with open(target_folder+file_name, 'w') as csvfile:
			csvwriter = csv.writer(csvfile, delimiter="\t") 
			for key in  sorted(output.keys()):
				string_value = key+" "
				for value in output[key]:
					string_value += ",".join(value) + " "
				string_value = string_value[:-1]
				# print (key, output[key], string_value)
				csvwriter.writerow([string_value])  