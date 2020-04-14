import re
from boyermore import *
from kmpsearch import *
from filehandler import *

# Jumlah
def findNumbers(teks):
    filternumberwords=re.findall(r'\S*\d+\S*', teks)
    numbers=re.findall(r'[-+]?\d*\.\d+|\d+', teks)

# Tanggal
def findDate(tanggal):
    # tanggal="11 Apr 2020 20:07 WIB"
    tanggalbulan = re.findall(r"((Senin|Selasa|Rabu|Kamis|Jumat|Sabtu|Minggu)?\s?[\d]{1,2}\s(Januari|Februari|Maret|April|Apr|Mei|Juni|Juli|Augustus|September|Oktober|November|Desember)(\s\d{4})?(\s[\d]{1,2}[.:][\d]{1,2}\sWI[BT]A?)?)", tanggal)
    haritanggal = re.findall(r'((Senin|Selasa|Rabu|Kamis|Jumat|Sabtu|Minggu)?\s?\(\d+[/-]\d+[/-]\d+\)(\s[Pp][Uu][Kk][Uu][Ll])?(\s[\d]{1,2}[.:][\d]{1,2}\sWI[BT]A?)?)',tanggal)
    # print(tanggalbulan)

# EXACT MATCHING Boyer More / KMP
def exactMatchBM(teks,pat):
    result=[]
    b=getNewFormattedText(teks)
    
    start=bmsearch(teks.lower(),pat)
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
        # print(sentecekiri[::-1].replace("NEOF",".")+sentencekanan.replace("NEOF",".")+".")
        result.append(sentecekiri[::-1].replace("NEOF",".")+sentencekanan.replace("NEOF",".")+".")
    
    for el in result:
        print(el)

    return result

def exactMatchKMP(teks,pat):
    result=[]
    b=getNewFormattedText(teks)
    
    start=kmpsearch(teks.lower(),pat)
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
        # print(sentecekiri[::-1].replace("NEOF",".")+sentencekanan.replace("NEOF",".")+".")
        result.append(sentecekiri[::-1].replace("NEOF",".")+sentencekanan.replace("NEOF",".")+".")
    
    for el in result:
        print(el)

    return result

# EXACT MATCHING REGEX
def exactMatchREGEX(teks,pat):
    result=[]
    b = getNewFormattedText(teks)
    sentences = re.findall(r"([^.]*\.)" ,b.lower())
    pat="terkonfirmasi positif"
    if (".")==pat[-1]:
        pat=pat.replace(".","NEOF").split(" ")
    else:
        pat=pat.replace(".","NEOF").split(" ")

    for sentence in sentences:
        if all(word in sentence for word in pat):
            # print(sentence.replace("neof","."))
            result.append(sentence.replace("neof","."))
    
    for el in result:
        print(el)

    return result

# main
def main():
    # teks=openstring("beritacontoh.txt")
    # pat="terkonfirmasi positif"
    
    # tanggal="Selasa (14/4/2020), pukul 12.00 WIB"
    # tanggalbulan = re.findall(r"((Senin|Selasa|Rabu|Kamis|Jumat|Sabtu|Minggu)?\s?[\d]{1,2}\s(Januari|Februari|Maret|April|Apr|Mei|Juni|Juli|Augustus|September|Oktober|November|Desember)(\s\d{4})?(\s[\d]{1,2}[.:][\d]{1,2}\sWI[BT]A?)?)", tanggal)
    # haritanggal = re.findall(r'((Senin|Selasa|Rabu|Kamis|Jumat|Sabtu|Minggu)?\s?\(\d+[/-]\d+[/-]\d+\)([,]?[ ]?[Pp][Uu][Kk][Uu][Ll])?(\s[\d]{1,2}[.:][\d]{1,2}\sWI[BT]A?)?)',tanggal)
    # print(haritanggal)
    # teks="75.17 persen, 75,1"
    # numbers=re.findall(r'[-+]?\d*[.,]\d+|\d+', teks)
    # print(numbers)

    # ekstrak = exactMatchKMP(teks,pat)
    # ekstrak = exactMatchBM(teks,pat)
    # ekstrak = exactMatchREGEX(teks,pat)


if __name__ == "__main__":
    main()
    


        





