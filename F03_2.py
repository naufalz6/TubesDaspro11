#F03, FUNGSI SAVE FILE
#variabel yang sama mengacu pada F01
#mohon koreksinya temen-temen hehe

import csv

#Hitung jumlah baris pada file
def countdata (a):
    jml_row=0
    for row in open(a)
        jml_row+=1
    return jml_row

def save ():
    A=input("Masukkan nama File User: ")
    openuser=open(A, 'w', newline='')
    count_A=countdata(A)
    writer=csv.writer(openuser, delimiter=',')
    for i in range (count_A):
        writer.writerow(user[i])
    openuser.close()

    B=input("Masukkan nama File Daftar Wahana: ")
    openwahana=open(B, 'w', newline='')
    count_B=countdata(B)
    writer=csv.writer(opendw, delimiter=',')
    for i in range (count_B):
        writer.writerow(wahana[i])
    openwahana.close()

    C=input("Masukkan nama File Pembelian Tiket: ")
    openbeli=open(C, 'w', newline='')
    count_C=countdata(C)
    writer=csv.writer(openbeli, delimiter=',')
    for i in range (count_C):
        writer.writerow(pembelian[i])
    openbeli.close()

    D=input("Masukkan nama File Penggunaan TIket: ")
    openguna=open(D, 'w', newline='')
    count_D=countdata(D)
    writer=csv.writer(openguna, delimiter=',')
    for i in range (count_D):
        writer.writerow(penggunaan[i])
    openguna.close()

    E=input("Masukkan nama File Kepemilikan Tiket: ")
    opentiket=open(E, 'w', newline='')
    count_E=countdata(E)
    writer=csv.writer(opentiket, delimiter=',')
    for i in range (count_E):
        writer.writerow(tiket[i])
    opentiket.close()

    F=input("Masukkan nama File Refund Tiket: ")
    openrefund=open(F, 'w', newline='')
    count_F=countdata(F)
    writer=csv.writer(openrefund, delimiter=',')
    for i in range (count_F):
        writer.writerow(refund[i])
    openrefund.close()

    G=input("Masukkan nama File Kritik dan Saran: ")
    openks=open(G, 'w', newline='')
    count_G=countdata(G)
    writer=csv.writer(openks, delimiter=',')
    for i in range (count_G):
        writer.writerow(kritiksaran[i])
    openks.close()

    print("Data berhasil disimpan!")
