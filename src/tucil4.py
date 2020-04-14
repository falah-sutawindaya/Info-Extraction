import re
from os import listdir
from os.path import isfile, join
from boyermore import *
from kmpsearch import *
from filehandler import *
from matchingexact import *
from exactregex import *


mypath="C:\\Users\\sutaw\\tucil4\\test"
keyword = "terkonfirmasi positif"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
articles=[]
for i in onlyfiles:
    currPath=mypath+'/'+i
    f = open(currPath, 'r')
    article = f.read()
    articles.append(article)

display=[]
for berita in articles:
    ekstrasi=exactMatchBM(berita,keyword)
    new={}
    for el in ekstrasi:
        new["user"]=el
        display.append(new)
        baru = ilanginNonDigit(el)
        arrayofnum=findNumbers(baru)
        for i in arrayofnum:
            print("jumlah: "+i)
            




        
        
# ilangin=""

b=' Laman Pusat Informasi dan Koordinasi COVID-19 Jabar (Pikobar) pada Sabtu (11/4/2020) pukul 18.43 WIB, mencatat terdapat 421 orang yang terkonfirmasi positif COVID-19.'
date=dateregex1(b)
if (len(date)==0):
    date=dateregex2(b)

for i in date:
    b=b.replace(i[0],"")
# print(date)
print(b)
# baru=ilanginNonDigit(b)
# print(baru)
# for i in baru:
#     k=b.replace(i,"")

# print(k)

    






        





