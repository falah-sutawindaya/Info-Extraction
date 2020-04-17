import pathlib
from boyermore import *

def openandformat(namaFile):
    # open file / read string untuk melihat satuan kalimat
    currPath = str(pathlib.Path(__file__).parent.absolute())
    f = open(currPath.replace('src', 'test\\').replace('\\','/') +namaFile, 'r')
    berita = f.read().replace("\n","").split(".")
    return berita

def openstring(namaFile):
    # open file / read string
    currPath = str(pathlib.Path(__file__).parent.absolute())
    f = open(currPath.replace('src', 'test\\').replace('\\','/') +namaFile, 'r')
    berita = f.read()
    return berita

def getNewFormattedText(teks):
    # Format string yang lebih memudahkan untuk pengambilan kalimat
    titikpos = bmsearch(teks.lower(),".")
    change=[]
    for index in titikpos:
        if index!=len(teks)-1:
            if (teks[index+1] != " " and teks[index+1] != "\n"):
                change.append(index)

    # mendapatkan kalimat bersesuaian
    b=''            
    for i in range(0,len(teks)):
        if i in change:
            b+="NEOF"
        else:
            b+=teks[i]

    return b
