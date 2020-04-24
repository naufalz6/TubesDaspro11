import F01 as load

def login(username, password):
	#load file user
	user = load.pilihan("user.csv")
	check = False
	#pencarian username di file user
	while not(check) :
		for i in range(11):
			if (user[i][3] == username and user[i][4] == password):
				check = True
				indexuser = i
				break
		if check == False:
			return("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi")		
	return ("Selamat bersenang - senang, " + str(user[indexuser][0]))
