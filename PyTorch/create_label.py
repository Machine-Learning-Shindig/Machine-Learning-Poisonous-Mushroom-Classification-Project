# 1 0.500000 0.500000 1.000000 1.000000

import os

if __name__ == '__main__':
    directory = "cnn/Poisonous"
    img_list = os.listdir(directory)
    for i in range(len(img_list)):
        holder = img_list[i]
        imageName = holder[:-4]
        file = open("dataset/labels/" + imageName + ".txt", 'w')
        file.write("0 0.500000 0.500000 1.000000 1.000000")
