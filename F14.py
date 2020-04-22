import F01

def riwayat(ID):
	penggunaan = F01.pilihan("penggunaan.csv")
	hitung = 0
	print("Riwayat:")
	for i in range(11):
		if penggunaan[i][2] == ID :
			hitung = hitung + 1
			print(penggunaan[i][1] + " | " + penggunaan[i][0] + " | " + penggunaan[i][3])
	if hitung == 0:
		print("Maaf, belum ada riwayat untuk wahana ini.")
	return penggunaan

x  = input("Masukan ID wahana : ")

riwayat(x)

# mantap
