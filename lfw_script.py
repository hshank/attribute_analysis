f = open('lfw_attributes.txt', 'r')

f.readline() # Header
f.readline() # Attributes List

labels = []
data = []

for line in f:
	line = line.split("\n")[0]
	arr = line.split("	")
	label = arr[0] 
	arr = arr[2:] # Take out image_num
	labels.append(label)
	data.append(arr)

