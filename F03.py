import csv

def save(namafile):
	with open(namafile, 'a', newline='') as csvfile:
		filesave = csv.writer(csvfile,delimiter=",")
		if namafile == "user.csv":
			filesave.writerow([Nama,Tanggal_Lahir,Tinggi_Badan,Username,Password,Role,Saldo])
			return filesave
		elif namafile == 'wahana.csv':
			filesave.writerow([ID_Wahana,Nama_Wahana,Harga_Tiket,Batasan_Umur,Batasan_Tinggi])
			return filesave
		elif namafile == 'pembelian.csv':
			filesave.writerow([Username,Tanggal_Pembelian,ID_Wahana,Jumlah_Tiket])
			return filesave
		elif namafile == 'penggunaan.csv':
			filesave.writerow([Username,Tanggal_Penggunaan,ID_Wahana,Jumlah_Tiket])
			return filesave
		elif namafile == 'tiket.csv':
			filesave.writerow([Username,ID_Wahana,Jumlah_Tiket])
			return filesave
		elif namafile == 'refund.csv':
			filesave.writerow([Username,Tanggal_Refund,ID_Wahana,Jumlah_Tiket])
			return filesave
		else:
			filesave.write([Username,Tanggal_Kritik,ID_Wahana,Isi_Kritik])
			return filesave