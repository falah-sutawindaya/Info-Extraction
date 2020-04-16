import re
from filehandler import *

# Jumlah
def findNumbers(teks):
    numbers=re.findall(r'[-+]?\d*[,.]\d+|\d+', teks)
    return numbers

def filterNumbers(teks):
    filternumberwords=re.findall(r'\w*\d+\w*', teks)
    return filternumberwords

# Waktu
def dateregex1(e):
        tanggalbulan = re.findall(r"((Senin|Selasa|Rabu|Kamis|Jumat|Sabtu|Minggu)?\,?\s?[\d]{1,2}\s(Januari|Februari|Maret|April|Apr|Mei|Juni|Juli|Augustus|September|Oktober|November|Desember)(\s\d{4})?(\s[\d]{1,2}[.:][\d]{1,2}\sWI[BT]A?)?)", e)
        return tanggalbulan

def dateregex2(e):
    haritanggal = re.findall(r'((Senin|Selasa|Rabu|Kamis|Jumat|Sabtu|Minggu)?\s?\(\d+[/-]\d+[/-]\d+\)([,]?[ ]?[Pp][Uu][Kk][Uu][Ll])?(\s[\d]{1,2}[.:][\d]{1,2}\sWI[BT]A?)?)', e)
    return haritanggal

