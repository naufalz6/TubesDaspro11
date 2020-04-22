#FUNGSI F01, FUNGSI LOAD FILE
import csv

#Fungsi untuk membaca csv dan mengubah bentuk menjadi array
def imp(a):
	csvfile = open(a, "r")
	with csvfile:
        # FUNGSI MEMBACA FILE BENTUK CSV
		reader = csv.reader(csvfile, delimiter=',')
		listreader = [i for i in reader]
	return listreader
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

	#Fungsi untuk digunakan dalam program utama
def pilihan(A):
	if A == "User.csv":
		return user
	elif A == "wahana.csv":
		return wahana
	elif A == "pembelian.csv":
		return pembelian
	elif A == "penggunaan.csv":
		return penggunaan
	elif A == "tiket.csv":
		return tiket
	elif A == "refund.csv":
		return refund
	elif A == "kritiksaran.csv":
		return kritiksaran

# Mantap
