import re
from os import listdir
from os.path import isfile, join
from boyermore import *
from kmpsearch import *
from filehandler import *
from matchingexact import *
from exactregex import *
from utility import *
from app import *

def Apps(mypath, keyword):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    articles=[]
    for i in onlyfiles:
        currPath=mypath+'/'+i
        f = open(currPath, 'r')
        article = f.read()
        articles.append(article)

    display=[]
    for berita in articles:
        ekstrasi=exactMatchKMP(berita, keyword)
        a=bmsearch(berita,keyword)
        new={}
        for el in ekstrasi:
            total=[]
            tanggal=[]

            # get date
            date=dateregex1(el)
            if (len(date)==0):
                date=dateregex2(el)
            if (len(date)!=0):
                for i in date:
                    el=el.replace(i[0],"")
                    tanggal.append(i[0])
            
            # get jumlah
            baru = ilanginNonDigit(el)
            arrayofnum=findNumbers(baru)
            for i in arrayofnum:
                total.append(i)
            
            new["user"]=el.replace("\n","")
            new["jumlah"]=total
            if (len(tanggal)==0):
                new["tanggal"]=[getArticleDate(berita)]
            else:
                new["tanggal"]=tanggal
            display.append(new)

    # print(display)
    return display