from PIL import Image
import numpy as np
import argparse
from scipy import misc

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help = "image")
ap.add_argument("-t", "--table", required = True,  help="table path")
args = vars(ap.parse_args())

x_1 = []
x_2 = []
y_1 = []
y_2 = []
names = []
with open(args["table"]) as inf:
    for line in inf:
        parts = line.split(',') # split line into parts
        if len(parts) > 1:   # if at least 2 parts/columns
            names.append(parts[0])
	    x_1.append(parts[1])
	    x_2.append(parts[3])
	    y_1.append(parts[2])
	    y_2.append(parts[4])

for i in range(0,len(names)):
	name = names[i]
	name = name.split('.')
	name = name[0].split('/')
	save_name = name[0]+'cropped.jpg'
	name = name[0]+'_'+name[1]
	print name
	points = [x_1[i],x_2[i],y_1[i],y_2[i]]
	original = Image.open('/home/elijah/Desktop/dataset_79/'+names[i])
	cropped_size = [299,299]
	size_original = original.size
	w_prime,h_prime = np.divide(size_original,cropped_size)
	w = int(x_2[i])-int(x_1[i])
	h = int(y_2[i])-int(y_1[i])
	x1_new = int(x_1[i])*w_prime
	x2_new = (int(x_1[i])+w)*w_prime
	y1_new = int(y_1[i])*h_prime
	y2_new = (int(y_1[i])+h)*h_prime
	cropped_image = original.crop((x1_new,y1_new,x2_new,y2_new))
	#print cropped_image.size
	#cropped_image.show()
	misc.imsave(name+'_cropped.jpg', cropped_image)


"""
for name in names:
	print '/home/elijah/Desktop/dataset_79/'+name 
"""
