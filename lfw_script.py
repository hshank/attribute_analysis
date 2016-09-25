f = open('lfw_attributes.txt', 'r')

f.readline() # Header
f.readline() # Attributes List

labels = []
data = []
count = 0
for line in f:
	count += 1
	line = line.split("\n")[0]
	arr = line.split("	")
	label = arr[0] 
	features = []
	for elem in arr[2:]:
		if float(elem) <= 0:
			features.append(0)
		else:
			features.append(1)
	labels.append(label)
	data.append(features)
print len(labels)
print str(count)
