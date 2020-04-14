import pathlib
from boyermore import *

def openandformat(namaFile):
    currPath = str(pathlib.Path(__file__).parent.absolute())
    f = open(currPath.replace('src', 'test\\').replace('\\','/') +namaFile, 'r')
    berita = f.read().replace("\n","").split(".")
    print(currPath)
    return berita

def openstring(namaFile):
    currPath = str(pathlib.Path(__file__).parent.absolute())
    print(currPath)
    f = open(currPath.replace('src', 'test\\').replace('\\','/') +namaFile, 'r')
    berita = f.read()
    return berita

# def openfrom(namaFile,path):
#     selectedPath = 
#     f=open(path+'\'+namaFile,'r')
#     return f.read()

def getNewFormattedText(teks):
    titikpos=bmsearch(teks.lower(),".")
    change=[]
    for index in titikpos:
        if index!=len(teks)-1:
            if (teks[index+1] != " " and teks[index+1] != "\n"):
                change.append(index)

    b=''            
    for i in range(0,len(teks)):
        if i in change:
            b+="NEOF"
        else:
            b+=teks[i]

    return b
