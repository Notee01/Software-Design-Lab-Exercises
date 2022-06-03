from os import listdir
from os. path import isfile, join

def find(path, filename):
    for f in listdir(path):
        if isfile(join(path, f)):
            if filename in f:
                print(f)
    else:
        find(join(path, f), filename)

#put the path and filename here
find("C:/Users/Marlon/Desktop/2nd Year/2nd Sem/SD/Laboratories", "lab 4.docx" )