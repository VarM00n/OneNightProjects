from os import walk, listdir, rename, getcwd
from os import listdir
from os import rename
from os.path import isfile, isdir, join, abspath
from pathlib import Path
import re
import shutil

# SOURCE_FOLDER = 'C:\\Users\\VarMoon\\Pobrane'

# For default download folder
SOURCE_FOLDER = str(join(Path.home(), "Downloads"))

def getCount():
    fileCount, folderCount = (0, 0)
    for base, dirs, files in walk(SOURCE_FOLDER):
        for directories in dirs:
            folderCount += 1
        for filee in files:
            fileCount += 1

    return fileCount, folderCount

def sortItems():
    fileList = [f for f in listdir(SOURCE_FOLDER) if isfile(join(SOURCE_FOLDER, f))]
    folderList = [f for f in listdir(SOURCE_FOLDER) if isdir(join(SOURCE_FOLDER, f))]
    for filee in fileList:
        # DOCX
        if filee.lower().split('.')[-1] in ('doc', 'docx'):
            shutil.move(SOURCE_FOLDER + '\\' + filee, abspath(getcwd()) + '\\DOCX\\' + filee)
        # PDF
        if filee.lower().split('.')[-1] in ('pdf'):
            shutil.move(SOURCE_FOLDER + '\\' + filee, abspath(getcwd()) + '\\PDF\\' + filee)
        # EXECUTABLE
        if filee.lower().split('.')[-1] in ('exe'):
            shutil.move(SOURCE_FOLDER + '\\' + filee, abspath(getcwd()) + '\\EXECUTABLE\\' + filee)
        # IMAGES
        if filee.lower().split('.')[-1] in ('jpg', 'jpeg', 'heic', 'png'):
            shutil.move(SOURCE_FOLDER + '\\' + filee, abspath(getcwd()) + '\\IMAGES\\' + filee)
        # ZIP
        if filee.lower().split('.')[-1] in ('zip', 'rar', '7z'):
            shutil.move(SOURCE_FOLDER + '\\' + filee, abspath(getcwd()) + '\\ZIP\\' + filee)
        # CSV
        if filee.lower().split('.')[-1] in ('csv', 'pptx'):
            shutil.move(SOURCE_FOLDER + '\\' + filee, abspath(getcwd()) + '\\CSV\\' + filee)
        # TXT
        if filee.lower().split('.')[-1] in ('txt'):
            shutil.move(SOURCE_FOLDER + '\\' + filee, abspath(getcwd()) + '\\TXT\\' + filee)
        # MP3
        if filee.lower().split('.')[-1] in ('mp3'):
            shutil.move(SOURCE_FOLDER + '\\' + filee, abspath(getcwd()) + '\\MP3\\' + filee)
    # FOLDERS
    for folder in folderList:
        shutil.move(SOURCE_FOLDER + '\\' + folder, abspath(getcwd()) + '\\FOLDERS\\' + folder)
    # REST FILES
    fileList = [f for f in listdir(SOURCE_FOLDER) if isfile(join(SOURCE_FOLDER, f))]
    for filee in fileList:
        shutil.move(SOURCE_FOLDER + '\\' + filee, abspath(getcwd()) + '\\OTHERS\\' + filee)



###########MAIN###########

print("Script started... ")

fileCount, folderCount = getCount()

print("Found " + str(fileCount) + " files.")
print("Found " + str(folderCount) + " folders.")

print()

try:
    sortItems()
except Exception as e:
    print("Moving files ended with error: " + str(e))
else:
    print("Items sorted.")