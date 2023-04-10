# 1 0.500000 0.500000 1.000000 1.000000

import os
import cv2

if __name__ == '__main__':
    directory = "cnn/Edible"
    img_list = os.listdir(directory)
    for i in range(len(img_list)):
        holder = img_list[i]
        image = cv2.imread("cnn/Edible/" + holder)
        dim = (256, 256)
        fImage = cv2.resize(image, dim)
        cv2.imwrite("dataset/image/" + holder, fImage)
        imageName = holder[:-4]
        file = open("dataset/labels/" + imageName + ".txt", 'w')
        file.write("0 0.500000 0.500000 1.000000 1.000000")
