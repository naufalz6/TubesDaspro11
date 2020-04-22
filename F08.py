#F08, FUNGSI PENGGUNAAN TIKET
# belom jadi

import csv

def main():
    
    idw=input("Masukkan ID wahana:")
    tgl=input("Masukkan tanggal hari ini:")
    jml=int(input("Jumlah tiket yang digunakan:"))

    f=open("penggunaan.csv", "r")
    reader=csv.reader(f, delimiter=";")

    with f:
        next(reader)
        for row in reader:
            if ((row[2]==idw) and (row[1]==tgl)):
                if (jml<=row[3]):
                    print("Terima kasih telah bermain.")
                else :
                    print("Tiket anda tidak valid dalam sistem kami")
            else :
                print("Tiket anda tidak valid dalam sistem kami")

    return
