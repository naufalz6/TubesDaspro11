import F01

def login(username, password):
	user = F01.pilihan("user.csv")
	check = False
	while not(check) :
		for i in range(11):
			if (user[i][3] == username and user[i][4] == password):
				check = True
				break
		if check == False:
			print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi")
			username = input("Masukkan username: ")
			password = input("Masukkan password: ")			
	return ("Selamat bersenang - senang, " + username)

username = input("Masukkan username: ")
password = input("Masukkan password: ")
print(login(username,password))
