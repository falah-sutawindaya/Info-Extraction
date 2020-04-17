import re
from kmpsearch import *
from filehandler import *

# EXACT MATCHING Boyer More 
def exactMatchBM(teks,pat):
    result=[]
    b=getNewFormattedText(teks)
    
    start=bmsearch(b.lower(),pat)
    for index in start:
        sentencekanan=''    
        newIndex=index
        # print(index)
        while b[newIndex]!='.':
            sentencekanan+=b[newIndex]
            newIndex+=1

        # print("sentence kanan: " + sentencekanan)
        sentecekiri=''
        newIndex=index-1
        while newIndex>=0 and b[newIndex]!='.':
            sentecekiri+=b[newIndex]
            newIndex-=1
        
        
        # print(sentecekiri[::-1].replace("NEOF",".")+sentencekanan.replace("NEOF",".")+".")
        result.append(sentecekiri[::-1].replace("NEOF",".")+sentencekanan.replace("NEOF",".")+".")
    
    # for el in result:
        # print(el)

    
    return result



# EXACT MATCHING KMP
def exactMatchKMP(teks,pat):
    result=[]
    b=getNewFormattedText(teks)
    
    start=kmpsearch(b.lower(),pat)
    for index in start:
        sentencekanan=''    
        newIndex=index
        while b[newIndex]!='.':
            sentencekanan+=b[newIndex]
            newIndex+=1

        sentecekiri=''
        newIndex=index-1
        while newIndex>=0 and b[newIndex]!='.':
            sentecekiri+=b[newIndex]
            newIndex-=1

        result.append(sentecekiri[::-1].replace("NEOF",".")+sentencekanan.replace("NEOF",".")+".")
    
    # for el in result:
    #     print(el)

    return result

# EXACT MATCHING REGEX
def exactMatchREGEX(teks,pat):
    result=[]
    b = getNewFormattedText(teks)
    sentences = re.findall(r"([^.]*\.)" ,b)
    
    if (".")==pat[-1]:
        pat=pat.replace(".","NEOF").split(" ")
    else:
        pat=pat.replace(".","NEOF").split(" ")

    for sentence in sentences:
        if all(word in sentence.lower() for word in pat):
            result.append(sentence.replace("NEOF","."))
    
    # for el in result:
    #     print(el)

    return result

def exactMatchREGEX2(teks, pat):
    # inisiasi dan format teks 
    teksFormat = getNewFormattedText(teks)
    keywordregex=''

    # Case Sensitive Handler
    for i in range(0,len(keyword)):
        if keyword[i]==' ':
            keywordregex+='[ ]'
        else:
            keywordregex+='['
            keywordregex+=keyword[i]
            keywordregex+=keyword[i].upper()
            keywordregex+=']'
    
    # Kalimat Processing Regex
    reg=r'[.]?.+\s?{}\s?.*\.'.format(keywordregex)
    search=re.findall(reg, teksFormat)

    return reg



