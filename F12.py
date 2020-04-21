import csv

def tambah_wahana():
	filewahana = open('wahana.csv', 'a', newline='')
	with filewahana as csvfile:
		filesave = csv.writer(csvfile,delimiter=",")
		filesave.writerow([ID_Wahana,Nama_Wahana,Harga_Tiket,Batasan_Umur,Batasan_Tinggi])
		print("Info wahana telah ditambahkan!")
		return filesave

print("Masukkan Informasi Wahana yang ditambahkan:")
ID_Wahana = input("Masukkan ID Wahana: ")
Nama_Wahana = input("Masukkan Nama Wahana: ")
Harga_Tiket = input("Masukkan Harga Tiket: ")
Batasan_Umur = input("Batasan umur: ")
Batasan_Tinggi = input("Batasan tinggi badan: ")
tambah_wahana()