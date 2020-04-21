import F01

def kritik_saran():
	kritiksaran = F01.pilihan("kritiksaran.csv")
	sorting = F01.pilihan("kritiksaran.csv")
	print("Kritik dan saran: ")
	kosong = False
	m = 0
	while not(kosong) and m <= 11: #untuk menghitung panjang array
		if kritiksaran[m][0] == "":
			kosong = True
		m = m + 1
	m = m - 1
	if m == 1:
		print("maaf, belum terdapat kritik dan saran")
	elif m > 1:
		for i in range(1,m-1): #melakukan sorting
			Imax = i
			for j in range(Imax+1, m):
				if ord(sorting[Imax][2][0]) == ord(sorting[j][2][0]):
					if ord(sorting[Imax][2][1]) == ord(sorting[j][2][1]):
						if ord(sorting[Imax][2][2]) < ord(sorting[j][2][2]):
							Imax = j
					elif ord(sorting[Imax][2][1]) < ord(sorting[j][2][1]):
						Imax = j
				elif ord(sorting[Imax][2][0]) < ord(sorting[j][2][0]):
					Imax = j
			passing = sorting[Imax]
			sorting[Imax] = sorting[i]
			sorting[i] = passing

		for i in range(m-1, 0,-1):
			print(sorting[i][2] + " | " + sorting[i][1] + " | " + sorting[i][0] + " | " + sorting[i][3])

		return kritiksaran

kritik_saran()


				

