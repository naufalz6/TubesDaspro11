#FUNGSI F06, PENCARIAN WAHANA
import csv

def cari():
    print("Jenis batasan umur:")
    print("1. Anak-anak (<17 tahun)")
    print("2. Dewasa(>=17 tahun)")
    print("3. Semua umur")
    print()
    print("Jenis batasan tinggi badan:")
    print("1. Lebih dari 170 cm")
    print("2. Tanpa batasan")
    print()

    #Mendeklarasikan input pengguna
    BatasUmur = input("Batasan umur pemain: ")
    while ((BatasUmur!="1") and (BatasUmur!="2") and (BatasUmur !="3")):
        print("Batasan umur tidak valid!")
        BatasUmur = input("Batasan umur pemain: ")
    BatasTinggi = input("Batasan tinggi badan:")
    while ((BatasTinggi!="1") and (BatasTinggi!="2")):
        print("Batasan tinggi badan tidak valid!")
        BatasTinggi = input("Batasan tinggi badan: ")

    #Untuk mengubah data yang diinput agar bisa dibandingkan dengan data yang sudah dimiliki
    if BatasUmur == "1":
        BatasUmur = "anak-anak"
    elif BatasUmur == "2":
        BatasUmur = "dewasa"
    else:
        BatasUmur = "semua umur"

    if BatasTinggi == "1" :
        BatasTinggi = ">= 170 cm"
    else:
        BatasTinggi = "tanpa batasan"

    #OUTPUT HASIL
    print()
    print("Hasil pencarian:")
    f=open("wahana.csv","r")
    reader=csv.reader(f,delimiter=";")

    count=0     #mendeklarasikan jumlah wahana yang sesuai kriteria

    with f:
        next(reader)
        for row in reader:
            if (row[3]==BatasUmur and row[4]==BatasTinggi):
                print(row[0] ," | ",row[1] ," | ",row[2])
                count+=1
        if (count==0):
            print("Tidak ada wahana yang sesuai dengan pencarian kamu.")
    return

cari()
