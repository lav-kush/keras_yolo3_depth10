import csv
import glob
import math
from PIL import Image

def objectName(objectid):
	switcher = {
		0: 'car',
		1: 'person',
		2: 'cycle',
		3: 'boat',
		4: 'heavy vehicle',
		5: 'plane',
		6: 'train'
	}
	return switcher.get(objectid, "nothing")

s1=[]
out_file = open('0dlr_train.csv','w')
writer = csv.writer(out_file)
#firstImage = input('Enter first image name')
#path = input('Enter path name')
path = '/home/lavkush/C/final year project/keras-retinanet-master/images/'
count = 0

for filename in sorted(glob.glob('*.txt')):
	f = open(filename)
	print(filename.strip('.txt')+'.jpg')
	im = Image.open(filename.strip('.txt')+'.jpg')
	img_width, img_height = im.size
	print(img_width, img_height)
	lines = f.readline()
	count += 1
	# if(count > 1000):
	# 	break
	while lines:
		s=[]
		stripped = lines.strip('\n').split(" ")
		stripped[1] = float(stripped[1])* img_width
		stripped[2] = float(stripped[2])* img_height
		stripped[3] = float(stripped[3])* img_width
		stripped[4] = float(stripped[4])* img_height
		s.append(path+ filename.strip('.txt')+'.jpg/,')
		s.append(int(math.ceil(stripped[1]- (stripped[3]/2) )))
		s.append(int(math.ceil(stripped[2]- (stripped[4]/2))))
		s.append(int(math.ceil(stripped[1]+ (stripped[3]/2))))
		s.append(int(math.ceil(stripped[2]+ (stripped[4]/2))))
		s.append(objectName(int(stripped[0])))
		lines = f.readline()
		writer.writerow(s)
print("train data count ", count)
f.close()
out_file.close()
