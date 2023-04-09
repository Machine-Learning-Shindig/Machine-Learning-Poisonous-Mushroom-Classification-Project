from PIL import Image
from os import listdir
from sklearn.neural_network import MLPClassifier

pathToPics = "cnn/"

X = [] # Inputs
Y = [] # Ground truths

for image in listdir(pathToPics + "Edible"):
    im = Image.open(pathToPics + "Edible/" + image, 'r')
    X.append([x for sets in list(im.getdata()) for x in sets]) # Will add the list of RGB values
    Y.append(1)
    im.close()

for image in listdir(pathToPics + "Poisonous"):
    im = Image.open(pathToPics + "Poisonous/" + image, 'r')
    X.append([x for sets in list(im.getdata()) for x in sets])
    Y.append(0)
    im.close()
