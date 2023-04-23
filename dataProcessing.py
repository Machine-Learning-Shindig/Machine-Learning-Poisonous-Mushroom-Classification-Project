import os, cv2
from sklearn.utils import shuffle
import numpy as np

def getData():
    edible = []
    poisonous = []
    dataset = []
    key = []
    path = 'dataset/Edible/'
    fileList = os.listdir(path)

    #read in edible dataset
    for image in fileList:
        sample = cv2.imread(path + image)
        edible.append(sample)

    #print(img.shape)
    # cv2.imshow("image", edible[10])
    # cv2.waitkey(0)'

    print("there should be 1473 images in edible: " + str( len(edible) ) )

    #Reading in data from poisonous dataset
    path = 'dataset/Poisonous/'
    fileList = os.listdir(path)
    #read in dataset as a [n][2] array. 
    for image in fileList:
        sample = cv2.imread(path + image)
        poisonous.append(sample)

    print("there should be 527 images in poisonous: " + str( len(poisonous) ) )

    key = [1]*len(edible)
    key.extend([0]*len(poisonous))

    edible.extend(poisonous)
    dataset, key = shuffle(edible, key)
    print(sample.shape)

    return dataset, key

# getData()