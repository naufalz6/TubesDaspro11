import F01 as load

def login(username, password):
	user = load.pilihan("user.csv")
	check = False
	while not(check) :
		for i in range(load.countdata("user.csv")):
			if (user[i][3] == username and user[i][4] == password):
				check = True
				break
		if check == False:
			return("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi")		
	return ("Selamat bersenang - senang, " + username)


#Blm di cek ulang per 23/4/2020 jam 1:00 AM
#tolong di cek karena ada yang berubah per 23/4/2020 jam 1:00 AM
