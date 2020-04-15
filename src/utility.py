import re
from filehandler import *
from exactregex import *

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

def ilanginNonDigit(nondigit):
    test = ' '.join(word for word in nondigit.split() if not word.isdigit()).split(" ")
    removedDigit=[]
    for el in test:
        try:
            float(el)
        except ValueError:
            removedDigit.append(el)
    
    getNumberToRemove=[] 
    for el in removedDigit:
        if (hasNumbers(el)):
            if not (',' in el):
                getNumberToRemove.append(el)
            # print(el)
    
    for el in getNumberToRemove:
        nondigit=nondigit.replace(el,"")

    return nondigit

def replacer(s, newstring, index, nofail=False):
    if not nofail and index not in range(len(s)):
        raise ValueError("index di luar panjang string")
    if index < 0:  
        return newstring + s
    if index > len(s):  
        return s + newstring

    return s[:index] + newstring + s[index + 1:]

def getJumlahMin(el, keyword, no):
    startIndex=el.index(keyword)
    endIndex=startIndex+len(keyword)-1

    datamin=[]
    for num in no:
        minNumIdx=el.index(num)
        maxNumIdx=minNumIdx+len(num)-1
        if maxNumIdx<startIndex:
            datamin.append({'angka': num, 'dist': startIndex-maxNumIdx})
        elif minNumIdx>endIndex:
            datamin.append({'angka': num, 'dist': minNumIdx-endIndex})
        el=el[maxNumIdx::]
    
    min = datamin[0]
    # min=a[0]
    for el in datamin:
        if (el['dist'] < min['dist']):
            min = el

    return min['angka']

# def getMinimumNumber(a):
#     min=a[0]
#     for el in a:
#         if (el['dist'] < min['dist']):
#             min = el
#     return min['angka']