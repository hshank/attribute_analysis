# Parses from a file that gives mapping from file names to labels
def parse_celeba_labels(path):
	f = open(path, 'r')
	count = 0
	file_to_label = {}
	for line in f:
		arr = line.split(" ")
		if len(arr) == 2:
			file_to_label[arr[0]] = int(arr[1].split("\n")[0])
	return file_to_label

# Returns data and corresponding labels
def get_celeb_a_dataset(path_data, path_labels):
	# Dictionary mapping file names to labels
	file_to_label = parse_celeba_labels(path_labels)
	f = open(path_data, 'r')

	# Skip first two lines of the file
	f.readline()
	f.readline()

	count = 0
	labels = []
	data = []
	for line in f:
		temp = []
		arr = line.split()
		for elem in arr[1:]:
			if int(elem) < 0:
				temp.append(0)
			else:
				temp.append(1)
		data.append(temp)
		labels.append(file_to_label[arr[0]])
	return data, labels

# Testing
data, labels = get_celeb_a_dataset("celeb_a_data.txt", "celeb_a_labels.txt")


