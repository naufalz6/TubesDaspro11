import F01


def refund(Username, ID, Jumlah):
	tiket = F01.pilihan("tiket.csv")
	wahana = F01.pilihan("wahana.csv")
	harga_tiket = 0
	valid  = False
	while not(valid):
		for i in range(11):
			if tiket[i][0] == Username:
				if tiket[i][1] == ID and tiket[i][2] == Jumlah:
					print("Uang refund sudah kami berikan pada akun Anda.")
					valid = True
					break
				else:
					print("Anda tidak memiliki tiket terkait.")
					break
	if valid == True:
		refund = F01.pilihan("refund.csv")
		i = 1
		while i <= 10 and refund[i][0] != "":
			i = i + 1
		kosong = i
		refund[kosong][0] = refund[kosong][0] + Username
		refund[kosong][1] = refund[kosong][1] + "20/04/2020" #Tinggal menyesuaikan tanggal
		refund[kosong][2] = refund[kosong][2] + ID
		refund[kosong][3] = refund[kosong][3] + Jumlah
	
		for i in range(11):
			if wahana[i][0] == ID:
				harga_tiket = wahana[i][2]
				break
		user = F01.pilihan("user.csv")
		for i in range(11):
			if user[i][3] == Username:
				user[i][6] = str(int(user[i][6]) + int(int(harga_tiket) * int(Jumlah) * 0.7)) #Mendapat Potongan 70% dari harga sebenarnya
	return refund
	return user

n = input("Masukan Username : ")
m = input("Masukan id wahana : ")
x = input("Masukan jumlah tiket : ")

refund(n,m,x)

# Mantap
