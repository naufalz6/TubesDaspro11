#B04, Fungsi Laporan Kehilangan Tiket

import F01 as load
import csv

def tiket_hilang():

    uname=input("Masukkan username: ")
    date=input("Tanggal kehilangan tiket: ")
    idw=input("ID Wahana: ")
    n=int(input("Jumlah tiket yang dihilangkan: ")

    tiket=load.pilihan("tiket.csv")
    i=0
    for i in range (11):
          if (tiket[i][0]==uname) and (tiket[i][1]==idw):
              tiket[i][3]=str(int(tiket[i][2])-n)

    with open("kehilangan.csv", "w") as f:
          reader=csv.reader(f, delimiter=";")
          i=0
          while i<11 :
              i+=1
              kehilangan[i][0]=kehilangan[i][0]+uname
              kehilangan[i][1]=kehilangan[i][1]+date
              kehilangan[i][2]=kehilangan[i][2]+idw
              kehilangan[i][3]=kehilangan[i][3]+n
              print("Laporan kehilangan tiket Anda telah direkam.")
    f.close()
    return
