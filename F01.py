#FUNGSI F01, FUNGSI LOAD FILE
import csv

def load():
    def imp(a):
        #FUNGSI MENDEFINISIKAN IMPORT FILE BENTUK CSV
        csvfile = open(a,"r")
        with csvfile:
            # FUNGSI MEMBACA FILE BENTUK CSV
            reader = csv.reader(csvfile, delimiter=';')
        return reader

    #INPUT UNTUK MEMASUKKAN NAMA FILE
    A=input("Masukkan nama File User: ")
    user=imp(A)
    B=input("Masukkan nama File Daftar Wahana: ")
    wahana=imp(B)
    C=input("Masukkan nama File Pembelian Tiket: ")
    pembelian=imp(C)
    D=input("Masukkan nama File Penggunaan Tiket: ")
    penggunaan=imp(D)
    E=input("Masukkan nama File Kepemilikan Tiket: ")
    tiket=imp(E)
    F=input("Masukkan nama File Refund Tiket: ")
    refund=imp(F)
    G=input("Masukkan nama File Kritik dan Saran: ")
    kritiksaran=imp(G)
    print("File perusahaan Willy Wangky's Chocolate Factory telah di-load.")

    return

load()
