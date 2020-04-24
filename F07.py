

import F01
import F03 

def beli_tiket(ID_Wahana,Tanggal,Jumlah):
	user = F01.pilihan("user.csv")
	wahana = F01.pilihan("wahana.csv")
	nEff = F03.countdata("wahana.csv")
	for i in range(nEff):
		if wahana[i][0] == ID_Wahana:
			ind = i
			break
	if int(user[][2]) < int(wahana[ind][4]):
		return("Anda tidak memenuhi persyaratan untuk memainkan wahana ini. Silakan menggunakan wahana lain yang tersedia")
	else:
		if :#cek umur ga memenuhi
			return("Anda tidak memenuhi persyaratan untuk memainkan wahana ini. Silakan menggunakan wahana lain yang tersedia")
		else:
			if (int(user[][6]) - (int(wahana[ind][2])*Jumlah))<0 :
				return("Saldo Anda tidak cukup. Silakan mengisi saldo Anda")
			else:
				save # save nama,IDwahana,tanggal beli, jumlah tiket pke fungsi F03
				return("Selamat bersenang-senang di" + wahana[ind][1])



ID_Wahana = input("Masukkan ID wahana: ")
Tanggal = input("Masukkan tanggal hari ini: ")
Jumlah = input("Jumlah tiket yan dibeli")
print(beli_tiket())

#BELUM SELESAI HEHEHE TINGGAL UMUR SAMA SAVENYA
