from app import *

mypath="C:\\Users\\sutaw\\tucil4\\test"
keyword = "terkonfirmasi positif"

# hasil = Apps(mypath, keyword)
# a=exactMatchREGEX(openstring("berita1.txt"),"terkonfirmasi positif")
# print(hasil)
a=bmsearch(openstring("berita1.txt"), keyword)
b=openstring("berita1.txt")
print(b[a[0]::])

# for i in hasil:
#     print("Keyword: " + keyword)
#     print("Hasil Ekstrasi Informasi: ")
#     if (len(i["jumlah"])>1):
#         print("Jumlah: " + getJumlahMin(i["user"], keyword, i["jumlah"]))
#     else:
#         print("Jumlah: " + i["jumlah"][0])
#     print(i["user"])
#     print("Tanggal: " + i["tanggal"][0])




    






        





