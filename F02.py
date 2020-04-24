import F01 as load

def login(username, password):
	user = load.pilihan("user.csv")
	check = False
	while not(check) :
		for i in range(11):
			if (user[i][3] == username and user[i][4] == password):
				check = True
				break
		if check == False:
			return("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi")		
	return ("Selamat bersenang - senang, " + username)rname)
