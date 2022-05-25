import easyocr
import os
from tkinter import filedialog
from tkinter import *
root = Tk()
root.withdraw()

path = filedialog.askdirectory()

count = 0

for imageName in os.listdir(path):
    if imageName.endswith(('.png', '.jpg', '.jpeg')):
        inputPath = os.path.join(path, imageName)

        count += 1
        print("Image "+ str(count) + " Processing...." )

        reader = easyocr.Reader(['en'], gpu=False, verbose=False)
        raw_result = reader.readtext(inputPath, detail=0, paragraph="False")

        '''strip_result = raw_result[0][1].split()

        if '-' in strip_result:
            strip_result.remove('-')

            result = "-".join(strip_result)

            result = path + "/" + result + '.png'''
        result = ' '.join(raw_result)

        for ch in ['\\ ', '/','` ','* ','_ ','{ ','} ','[ ','] ','( ',') ','> ','< ','# ','+ ','- ','. ','! ','$ ','\' ', '" ', "' ",'= ',', ','? ',': ','| ','@ ','% ','^ ','& ']:
            if ch in result:
                result = result.replace(ch, '')


        if imageName.endswith('.png'):
            result = path + "/" + result + '.png'
        elif imageName.endswith('.jpg'):
            result = path + "/" + result + '.jpg'
        else:
            result = path + "/" + result + '.jpeg'


        '''result = path + "/" + result + '.png'''


        os.rename(inputPath,result)

        print("Image "+ str(count) + " Name Changed" )


print("Process Complete")

a = input("Press Enter to exit")