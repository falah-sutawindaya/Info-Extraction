import re
from filehandler import *

b=openstring("beritacontoh.txt")
# a='421 Orang di Jabar Terkonfirmasi Positif COVID-19.'
# print(b)
keyword='terkonfirmasi positif'
#Terkonfirmasi Positif
keywordregex=''
for i in range(0,len(keyword)):
    if keyword[i]==' ':
        keywordregex+='[ ]'
    else:
        keywordregex+='['
        keywordregex+=keyword[i]
        keywordregex+=keyword[i].upper()
        keywordregex+=']'

print(keywordregex)
# reg=r'[.]?.+\s?{}\s?.*\.'.format(keywordregex)
# search=re.findall('\..+\s?terkonfirmasi positif\s?.*\.',b)
# search=re.findall(reg, b)
# print(reg)
sentences = re.findall(r"([^.]*\.)" ,b)
print(sentences)
