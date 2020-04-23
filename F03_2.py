# Aku hapus dikit ya

import csv

#Hitung jumlah baris pada file (Ini panjangnya 11 ya)
# def countdata (a):
#     jml_row=0
#     for row in open(a, "r"):
#         jml_row+=1
#     return jml_row

def save ():
    A=input("Masukkan nama File User: ")
    openuser=open(A, 'w', newline='')
    writer=csv.writer(openuser, delimiter=',')
    for i in range (11):
        writer.writerow(user[i])
    openuser.close()

    B=input("Masukkan nama File Daftar Wahana: ")
    openwahana=open(B, 'w', newline='')
    writer=csv.writer(openwahana, delimiter=',')
    for i in range (11):
        writer.writerow(wahana[i])
    openwahana.close()

    C=input("Masukkan nama File Pembelian Tiket: ")
    openbeli=open(C, 'w', newline='')
    writer=csv.writer(openbeli, delimiter=',')
    for i in range (11):
        writer.writerow(pembelian[i])
    openbeli.close()

    D=input("Masukkan nama File Penggunaan TIket: ")
    openguna=open(D, 'w', newline='')
    writer=csv.writer(openguna, delimiter=',')
    for i in range (11):
        writer.writerow(penggunaan[i])
    openguna.close()

    E=input("Masukkan nama File Kepemilikan Tiket: ")
    opentiket=open(E, 'w', newline='')
    writer=csv.writer(opentiket, delimiter=',')
    for i in range (11):
        writer.writerow(tiket[i])
    opentiket.close()

    F=input("Masukkan nama File Refund Tiket: ")
    openrefund=open(F, 'w', newline='')
    writer=csv.writer(openrefund, delimiter=',')
    for i in range (11):
        writer.writerow(refund[i])
    openrefund.close()

    G=input("Masukkan nama File Kritik dan Saran: ")
    openks=open(G, 'w', newline='')
    writer=csv.writer(openks, delimiter=',')
    for i in range (11):
        writer.writerow(kritiksaran[i])
    openks.close()

    print("Data berhasil disimpan!")

    #edit 23/4/2020 jam 1:08AM
    #log  : mengganti typo pada baris 22, tadinya writer(opendw) menjadi writer(openwahana)
    #Mantap Rena
