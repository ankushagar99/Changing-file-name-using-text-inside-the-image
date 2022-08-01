from logging import exception
from platform import win32_edition
import re
import easyocr
import os
from tkinter import filedialog
from tkinter import *

root = Tk()
root.withdraw()

path = filedialog.askdirectory()

count = 0

dublicate_count = 1

for imageName in os.listdir(path):
    try:
        if imageName.endswith(('.png', '.jpg', '.jpeg')):
            inputPath = os.path.join(path, imageName)

            count += 1
            print("Image "+ str(count) + " Processing...." )

            reader = easyocr.Reader(['en'], gpu=False, verbose=False)
            raw_result = reader.readtext(inputPath, detail=0, paragraph="False")

            result = ''.join(raw_result)

            for ch in ['\\', '/','`','*','_','{','}','[',']','(',')','>','<','#','+','.','!','$','\'', '"', "'",'=',',','?',':','|','@ ','%','^','&']:
                if ch in result:
                    result = result.replace(ch, '')

            file_except = result

            if imageName.endswith('.png'):
                result = path + "/" + result[:20] + '.png'
            elif imageName.endswith('.jpg'):
                result = path + "/" + result[:20] + '.jpg'
            else:
                result = path + "/" + result[:20] + '.jpeg'

            os.rename(inputPath,result)

            print(result)

            print("Image "+ str(count) + " Name Changed" )

    except FileExistsError:
        print("Duplicate File Detected")
        try:
            if imageName.endswith('.png'):
                file_except =  path + "/" + file_except[:20] + '('+ str(dublicate_count) + ')' + '.png'
            elif imageName.endswith('.jpg'):
                file_except =  path + "/" + file_except[:20] + '('+ str(dublicate_count) + ')' + '.jpg'
            else:
                file_except =  path + "/" + file_except[:20] + '('+ str(dublicate_count) + ')' + '.jpeg'

            print(file_except)
            
            os.rename(inputPath,file_except)

            print("Image "+ str(count) + " Name Changed" )

            dublicate_count += 1
        except Exception as e:
            with open("log.txt", "a+",encoding = 'utf-8') as f:
                f.write(str(e))
                f.write('\n')
        pass
     
    except Exception as r:
        with open("log.txt", "a+",encoding = 'utf-8') as f:
            f.write(str(r))
            f.write('\n')
        pass

print("Process Complete")

a = input("Press Enter to exit")