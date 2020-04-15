from app import *

mypath="C:\\Users\\sutaw\\tucil4\\test"
keyword = "terkonfirmasi positif"
hasil = Apps(mypath, keyword)

print("Keyword: " + keyword)
for i in hasil:
    print("Hasil Ekstrasi Informasi: ")
    if (len(i["jumlah"])>1):
        print("Jumlah: " + getJumlahMin(i["user"], keyword, i["jumlah"]))
    elif (len(i["jumlah"])==0):
        print("Jumlah: ")
    else:
        print("Jumlah: " + i["jumlah"][0])
    print("Waktu: " + i["tanggal"][0])
    if i["user"][0]==" ":
        i["user"]=replacer(i["user"],"",0)
    print("{} ({})".format(i["user"], i["filename"]))
    print("")






    






        





