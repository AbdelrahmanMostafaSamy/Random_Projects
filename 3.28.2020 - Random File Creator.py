import random
import string
import os
import pathlib

allformats = ["aa", "aac", "aax", "m4a", "mmf", "mp3", "ogg", "wav", "wma", "webm", "mp4", "avi", "mov", "flv", "ts", "mk4", "txt", "doc", "docx", "odt", "pdf", "rtf", "tex", "wpd", "tif", "tiff", "bmp", "jpg", "jpeg", "gif", "png", "eps", "raw", "cr2", "nef", "orf", "sr2"]

def randomString(stringLength):
    letters = string.ascii_letters + "~!@#$%^&()_-+=.,;`'"
    return ''.join(random.choice(letters) for i in range(stringLength))

folder = input("Please input the path of the output folder, (Or enter default to use the default path) ")
if folder.lower() == "default":
    folder = "Output folder"
if pathlib.Path(folder).exists() == False:
    os.mkdir(folder)

for i in range(int(input("How many random files do you want to create? "))):
    with open(f"{folder}\\{randomString(random.randint(3,20))}.{random.choice(allformats)}", "w") as f:
        for i in range(1, random.randint(1,10)):
            f.writelines(randomString(random.randint(1,200)))
