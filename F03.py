import F01

def login(username, password):
	user = F01.pilihan("user.csv")
	check = False
	while check == False :
		i = 0
		while i <=9:
			if (user[i][3] == username and user[i][4] == password):
				check = True
				break
			i = i + 1
		if check == False:
			print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi")
			username = input("Masukkan username: ")
			password = input("Masukkan password: ")			
	return ("Selamat bersenang - senang, " + username)

username = input("Masukkan username: ")
password = input("Masukkan password: ")
print(login(username,password))
