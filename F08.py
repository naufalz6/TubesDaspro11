# Kasih masukan
# Rena, jangan pake import csv ya, perbaiki lagi
# ganbatte!!!!

#F08, FUNGSI PENGGUNAAN TIKET

import csv

def main():
    
    idw=input("Masukkan ID wahana:")
    tgl=input("Masukkan tanggal hari ini:")
    jml=int(input("Jumlah tiket yang digunakan:"))
    
    #Ubah file penggunaan tiket
    f=open("penggunaan.csv", "r")
    reader=csv.reader(f, delimiter=";")

    with f:
        next(reader)
        for row in reader:
            if ((row[2]==idw) and (row[1]==tgl)):
                if (jml<=(int(row[3]))):
                    print("Terima kasih telah bermain.")
                else :
                    print("Tiket anda tidak valid dalam sistem kami")
            else :
                print("Tiket anda tidak valid dalam sistem kami")
    f.close()

    #Ubah file kepemilikan tiket
    y=open("tiket.csv", "w")
    reader=csv.reader(y, delimiter=";")
    
    with y:
        next(reader)
        for row in reader:
            if (row[1]==idw):
                row[2]=str(int(row[2])-jml)
    y.close()
    
    return
