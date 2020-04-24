# Mantap

#F08, FUNGSI PENGGUNAAN TIKET

import F01

def main():
    
    idw=input("Masukkan ID wahana:")
    tgl=input("Masukkan tanggal hari ini:")
    jml=int(input("Jumlah tiket yang digunakan:"))
    
    penggunaan = F01.pilihan("penggunaan.csv") 
    i = 0
    for i in range (11):
        if ((penggunaan[i][2]==idw) and (penggunaan[i][1]==tgl)):
            if(jml<=(int(penggunaan[i][3]))):
                print("Terima kasih telah bermain.")
            else :
                print("Tiket anda tidak valid dalam sistem kami")
        else :
            print("Tiket anda tidak valid dalam sistem kami")
    
    # ubah isi file kepemilikan tiket
    tiket = F01.pilihan("tiket.csv")
    i = 0
    for i in range (11):
        if (tiket[i][1]==idw):
            tiket[i][2]==str(int(tiket[i][2])-jml)
    
    return 


