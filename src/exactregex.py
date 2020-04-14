import re
from filehandler import *

# Jumlah
def findNumbers(teks):
    numbers=re.findall(r'[-+]?\d*\.\d+|\d+', teks)
    return numbers

def filterNumbers(teks):
    filternumberwords=re.findall(r'\w*\d+\w*', teks)
    return filternumberwords

# Waktu
def dateregex1(e):
        tanggalbulan = re.findall(r"((Senin|Selasa|Rabu|Kamis|Jumat|Sabtu|Minggu)?\,?\s?[\d]{1,2}\s(Januari|Februari|Maret|April|Apr|Mei|Juni|Juli|Augustus|September|Oktober|November|Desember)(\s\d{4})?(\s[\d]{1,2}[.:][\d]{1,2}\sWI[BT]A?)?)", e)
        return tanggalbulan

def dateregex2(e):
    haritanggal = re.findall(r'((Senin|Selasa|Rabu|Kamis|Jumat|Sabtu|Minggu)?\s?\(\d+[/-]\d+[/-]\d+\)([,]?[ ]?[Pp][Uu][Kk][Uu][Ll])?(\s[\d]{1,2}[.:][\d]{1,2}\sWI[BT]A?)?)', e)
    return haritanggal

# Utility 
def getType(e):
    return str(type(e)).replace("<class ", "").replace(">","")

def getArticleDate(teks):
    getDateArticle=getNewFormattedText(teks).split(".")
    for e in getDateArticle:
        if len(dateregex1(e))!=0 or len(dateregex2(e))!=0:
            if len(dateregex1(e))!=0:
                articledate=dateregex1(e)[0]
            elif len(dateregex2(e))!=0:
                articledate=dateregex2(e)[0]
            break

    return articledate[0]

def removedNonDigits(teks):
    removethis=(' '.join(word for word in teks.split() if not word.isdigit())).split(" ")
    benar=[]
    for el in removethis:
        try:
            float(el)
        except ValueError:
            benar.append(el)

    return benar

def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))

def ilanginNonDigit(a):
    test = ' '.join(word for word in a.split() if not word.isdigit()).split(" ")
    benar=[]
    for el in test:
        try:
            float(el)
        except ValueError:
            benar.append(el)
    
    absolutebenar=[] 
    for el in benar:
        if (hasNumbers(el)):
            absolutebenar.append(el)
    print(absolutebenar)
    for el in absolutebenar:
        a=a.replace(el,"")
    # print(a)
    return a