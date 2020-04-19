import csv

def login(username, password):
	bener = False
	with open("user.csv", 'r') as csvfile:
		baca_data = csv.reader(csvfile)
		data_user = [r for r in baca_data]
		while not(bener):
			for i in range(5):
				if data_user[i][3] == username and data_user[i][4] == password:
					bener = True
					break
			if bener == False:
				print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi! ")
				username = input('Masukan username : ')
				password = input('Masukan password : ')

	return ("Selamat bersenang-senang, " + str(data_user[i][0]) + "!" )

nama = input('Masukan username : ')
passw = input('Masukan password : ')
print(login(nama, passw))
