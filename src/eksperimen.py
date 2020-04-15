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
    
    return datamin


el="31 bla bla bla 31 kontol koa 99"
keyword="kontol"
no=['31','31','99']

print(getJumlahMin(el,keyword,no))


a=getJumlahMin(el,keyword,no)
a.append({'angka':'3', 'dist':3})
def getMinimumNumber(a):
    min=a[0]
    for el in a:
        if (el['dist'] < min['dist']):
            min = el
    return min['angka']

print(getMinimumNumber(a))
        
