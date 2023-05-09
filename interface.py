# img_viewer.py

import PySimpleGUI as sg #pip3 install pysimplegui
import os 
from PIL import Image
import re
import detect_code
import time

# First the window layout in 2 columns
def convertToPNG(path):
    im1 = Image.open(r'{}'.format(path))
    newPath = re.sub(r'.{3}$', 'png', path)
    im1.save(r'{}'.format(newPath))
    return newPath

dataSet = []
textFiles = []
dir ="demo_images/images" #directory for test data set
files = os.listdir(dir)
for f in files:
    l = os.path.join(dir, f)
    l = convertToPNG(l)
    dataSet.append(l)


file_list_column = [
    [
        sg.Text("Enter Shroom Path"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
    
            values=dataSet, enable_events=True, size=(40, 20), key="-FILE LIST-" #relative path to the image
        )
    ],
]
# For now will only show the name of the file that was chosen
image_viewer_column = [
    [sg.Text("Choose an image from list on left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]
# ----- Full layout -----
layout = [
     [
        sg.Column(file_list_column),
        sg.Column(image_viewer_column),
    ],
    [
        sg.Text("Classfication: ", key="-CLASSIFICATION-", visible=False), 
         sg.Button("Poisonous?",enable_events=True, key="-POISONOUS?-", visible=False),
        sg.Text("Actual: ", key="-ACTUAL-", visible = False),

    ],
]

window = sg.Window("Poisonous Mushroom Detector", layout)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-POISONOUS?-": #Put the terminal code here 
        try:

            ###INSTRUCTIONS###

            current = values["-FILE LIST-"][0]
            classification = detect_code.detect([current], 'inference/output')

            time.sleep(2)

            actual = None
            
            inference = "inference/output"

            actualLabel = "demo_images/labels"

            replace = re.sub(r'demo_images/images',actualLabel, current)
            textFile = re.sub(r'.{3}$','txt', replace)
            
            modelInference = re.sub(r'demo_images/images', inference, current)
            modelInference = re.sub(r'.{3}$','jpg', modelInference)

            # print(textFile)
            with open(textFile) as f:
                actual = f.read()
            print(actual)
            print(classification)

            #another open and close text file (inference file), set classified to the value in the text file 

            window["-CLASSIFICATION-"].update("Classification: {}".format(classification),visible=True)
            window["-ACTUAL-"].update("Actual: {}".format(actual), visible=True)
        except:
            pass
    
    elif event == "-FILE LIST-":  # A file was chosen from the listbox
        try:
            window["-POISONOUS?-"].update(visible=True)
            window["-CLASSIFICATION-"].update(visible=False)
            window["-ACTUAL-"].update(visible=False)

            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename, visible=False)
            window["-IMAGE-"].update(filename=filename)

        except:
            pass

window.close()