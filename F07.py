import F01
import F03 

def beli_tiket(username,Tanggal,Jumlah):
	user = F01.pilihan("user.csv")
	wahana = F01.pilihan("wahana.csv")
	for i in range(11):
		if user[i][0] == username:
			p = i
			break
	for i in range(11):
		if wahana[i][0] == ID_Wahana:
			ind = i
			break
	arrtglluser = [user[p][1]]
	arrtglwhn = [Tanggal]
	if int(user[p][2]) < int(wahana[ind][4]):
		return("Anda tidak memenuhi persyaratan untuk memainkan wahana ini. Silakan menggunakan wahana lain yang tersedia")
	else:
		if(int(arrtglwhn[0][:6]) - int(arrtglluser[0][:6]))*12 < (wahana[ind][3])*12 :#cek umur ga memenuhi
			return("Anda tidak memenuhi persyaratan untuk memainkan wahana ini. Silakan menggunakan wahana lain yang tersedia")
		else:
			if (int(user[p][6]) - (int(wahana[ind][2])*Jumlah)) < 0 :
				return("Saldo Anda tidak cukup. Silakan mengisi saldo Anda")
			else:
				save # save nama,IDwahana,tanggal beli, jumlah tiket pke fungsi F03 ke file pembelian tiket
				return("Selamat bersenang-senang di" + wahana[ind][1])
