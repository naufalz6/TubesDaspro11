import F01 as load
import F03 as sv

def login(username, password):
	user = load.pilihan("user.csv")
	check = False
	while not(check) :
		for i in range(sv.countdata("user.csv")):
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

#Blm di cek ulang per 23/4/2020 jam 1:00 AM
