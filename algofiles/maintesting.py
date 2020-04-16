from algos import *

mypath="C:\\Users\\sutaw\\tucil4\\test"
keyword = "terkonfirmasi positif"
hasil = Apps(mypath, keyword)

print("Keyword: " + keyword)
for i in hasil:
    print("Hasil Ekstrasi Informasi: ")
    print("Jumlah: " + i["jumlah"])
    print("Waktu: " + i["tanggal"])
    print("{} ({})".format(i["info"], i["filename"]))
    print("")
    







    






        





