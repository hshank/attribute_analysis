sex = [0]
ethnicity = [1,2,3,57]
age = [4,5,6,7,8]
hair_color = [9,10,11,12,58]
glasses = [13,14]
facial_hair = [16,45,46]
hair_style = [25,26,27,28,29,30]
eyebrows = [34,35]
eye = [36,69]
facial_structure = [19,38,39,40,47,48,50,51,52,68]

identity = set(sex+ethnicity+age+hair_color+glasses+facial_hair+hair_style+eyebrows+eye+facial_structure)

picture_quality = [20,21,22,23,53,54]
click_specifics = [31,32,33,37,41,42,43,44]
makeup = [59,60,61,62,63,64,65,66,67]
attractiveness = [55,56]
emotions = [17,18]
accessories = [15,24,49,70,71,72]

irrelevant = set(picture_quality+click_specifics+makeup+attractiveness+emotions+accessories)


import numpy as np
import scipy
import scipy.io as sio
import sys
from scipy.spatial import distance

hashcodes_name = 'LFW_hash512_randomcrop_prelu_newproto_rgb_notV7.3.mat'
hashcodes_file_full = hashcodes_name
hashcodes_mat = sio.loadmat(hashcodes_file_full)
all_templates = hashcodes_mat['templates']
nb_samples = hashcodes_mat['templates'].shape[1]
all_samples_files = []
for i in range(nb_samples):
    all_samples_files.append(str(np.squeeze(all_templates[0,i][2])))



def calculate_difference(attr_set):

    fulldist_name = 'LFW_full_hamming_dist.mat'
    fulldist_file = fulldist_name
    fulldist = sio.loadmat(fulldist_file)
    fulldist_np = fulldist['full_hamming_dist']

    f = open('lfw_attributes.txt', 'r')
    f.readline()
    f.readline()
    labels = []
    data = []
    count = 0
    for line in f:
        count += 1
        line = line.split("\n")[0]
        arr = line.split("	")
        label = arr[0] 
        features = []
        attribute_num = 0
        for elem in arr[2:]:
            if attribute_num in attr_set:
                if float(elem) <= 0:
                    features.append(0)
                else:
                    features.append(1)
            attribute_num+=1
        retVal = []
        for elem in label.split():
            retVal.append(elem)
        labels.append("_".join(retVal) + "_" + str(arr[1]).zfill(4) + ".jpg")
        data.append(np.array(features))
    data = np.array(data)


    labels_count = 0
    hash_count = 0
    count = 0
    dictionary = {}
    for elem in labels:
        dictionary[elem] = True
    count = 0
    colDel = []
    for elem in all_samples_files:
        if elem not in dictionary:
            colDel.append(count)
        count += 1
    count = len(colDel) - 1
    while count >= 0:
        fulldist_np = scipy.delete(fulldist_np, colDel[count], 0)  # delete second row of A
        fulldist_np = scipy.delete(fulldist_np, colDel[count], 1)  # delete second column of C
        count = count - 1

    print len(fulldist_np)
    print len(fulldist_np[0])  
    fulldist_np = fulldist_np/512.0
    best = 0
    lest = 1000
    for elem in fulldist_np:
        best = max(max(elem), best)
        lest = min(min(elem), lest)

    print str(best)
    print str(lest)

    data_dist = distance.cdist(data, data, 'hamming')


    for elem in data_dist:
        best = max(max(elem), best)
        lest = min(min(elem), lest)

    print str(best)
    print str(lest)

    hello = np.absolute(np.subtract(fulldist_np, data_dist))
    
    for elem in hello:
        best = max(max(elem), best)
        lest = min(min(elem), lest)

    print str(best)
    print str(lest)


    #return np.sum(hello)/(len(labels) * len(labels) - len(labels))
    return 'hi'

print calculate_difference(identity)