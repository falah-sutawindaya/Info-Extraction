import re
from os import listdir
from os.path import isfile, join
from boyermore import *
from kmpsearch import *
from filehandler import *
from matchingexact import *
from exactregex import *
from utility import *


def Apps(mypath, keyword, option):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    articles=[]
    for i in onlyfiles:
        currPath=mypath+'/'+i
        f = open(currPath, 'r')
        article = f.read()
        articles.append({'article': article, 'namafile':i})

    hasil=[]
    for berita in articles:
        newstringart=berita['article']
        if (option == 'option1'):
            ekstrasi=exactMatchBM(newstringart, keyword)
        elif (option == 'option2'):
            ekstrasi=exactMatchKMP(newstringart, keyword)
        elif (option == 'option3'):
            ekstrasi=exactMatchREGEX(newstringart, keyword)

        for el in ekstrasi:
            new={}
            total=[]
            tanggal=[]

            new["filename"] = berita['namafile']
            new["user"]=el.replace("\n","")
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
               
            new["jumlah"]=total
            if (len(tanggal)==0):
                new["tanggal"]=[getArticleDate(newstringart)]
            else:
                new["tanggal"]=tanggal
            hasil.append(new)

    b=[]
    for i in hasil:
        a={}
        if (len(i["jumlah"])>1):
            a["jumlah"]=getJumlahMin(i["user"], keyword, i["jumlah"])
        elif (len(i["jumlah"])==0):
            a["jumlah"]=None
        else:
            a["jumlah"]=i["jumlah"][0]
        a["tanggal"]=i["tanggal"][0]
        if i["user"][0]==" ":
            a["info"]=replacer(i["user"],"",0)
        else:
            a["info"]=i["user"]
        a["filename"]=i["filename"]
        
        b.append(a)
    
    return b
