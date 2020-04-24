import F01 as ld

def tambah_wahana(ID_Wahana,Nama_Wahana,Harga_Tiket,Batasan_Umur,Batasan_Tinggi):
	wahana = ld.pilihan("wahana.csv")
	for i in range(11):
		if wahana[i][0] != "":
			p = i
			break
	wahana[p][0] = ID_Wahana
	wahana[p][1] = Nama_Wahana
	wahana[p][2] = Harga_Tiket
	wahana[p][3] = Batasan_Umur
	wahana[p][4] = Batasan_Tinggi
	print("Info wahana telah ditambahkan!")
	return wahana

print("Masukkan Informasi Wahana yang ditambahkan:")
ID_Wahana = input("Masukkan ID Wahana: ")
Nama_Wahana = input("Masukkan Nama Wahana: ")
Harga_Tiket = input("Masukkan Harga Tiket: ")
Batasan_Umur = input("Batasan umur: ")
Batasan_Tinggi = input("Batasan tinggi badan: ")
tambah_wahana(ID_Wahana,Nama_Wahana,Harga_Tiket,Batasan_Umur,Batasan_Tinggi)
