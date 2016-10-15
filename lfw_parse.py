# Get the data and respective labels
def get_lfw_dataset(path):
    f = open(path, 'r')

    f.readline() # Header
    f.readline() # Attributes List

    labels = []
    data = []
    counter = 0

    for line in f:
        # First take out new line character
        line1 = line.split("\n")[0]
        arr = line1.split()

        # Some names have multiple middle names
        name = arr[0]
        count = 1
        while count < len(arr) - 73 - 1:
            name = name + '_' + arr[count]
            count += 1
        labels.append(name+'_'+arr[count].zfill(4) + '.jpg')

        f_arr = arr[count + 1: len(arr)]
        values = []
        for elem in f_arr:
            if float(elem) < 0:
                values.append(0)
            else:
                values.append(1)
        data.append(values)
    return data, labels

# Testing
data, labels = get_lfw_dataset('lfw_data.txt')

