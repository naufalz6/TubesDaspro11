import F01

def signup(nama, tanggal_lahir, tinggi_badan, username, password):
	user = F01.pilihan("User.csv")
	i = 1
	while i < 10 and user[i][0] != "":
		i = i + 1 
	kosong = i
	user[kosong][0] = user[kosong][0] + nama
	user[kosong][1] = user[kosong][1] + tanggal_lahir
	user[kosong][2] = user[kosong][2] +  tinggi_badan
	user[kosong][3] = user[kosong][3] + username
	user[kosong][4] = user[kosong][4] + password
	user[kosong][5] = user[kosong][5] + "pemain"
	user[kosong][6] = user[kosong][6] + "0"
	return user
nama = input("Masukan nama pemain : ")
tanggal_lahir = input("Masukan tanggal lahir pemain (DD/MM/YYYY) : ")
tinggi_badan = input("Masukan tinggi badan pemain (cm) : ")
username = input("Masukan username pemain : ")
password = input("Masukan password pemain : ")

signup(nama, tanggal_lahir, tinggi_badan, username, password)


