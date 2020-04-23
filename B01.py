import random

# Fungsi untuk mengenerate key one time pad, terbatas hanya dari nomor 0 sampai 100
def key(Password): 
	key = []
	n = len(password)
	i = 0
	while i < n:
		nilai = random.randint(0,100)
		while not(((ord(password[i]) + nilai) % 127) > 31 and ((ord(password[i]) + nilai) % 127) < 127):
			nilai = random.randint(0,100)
		key.append(nilai)
		i = len(key)
	print(key)
	return key

# Fungsi untuk memorisasi factor dari key dan nilai ordinal password
def factor(key,password):
	factor = []
	for i in range(len(key)):
		factor.append((ord(password[i]) + key[i]) // 127)
	print(factor)
	return(factor)

# Fungsi untuk mengenkripsi password
def encrypt(key,password):
	hasil = ""
	for i in range(len(key)):
		hasil = hasil + chr((key[i] + ord(password[i])) % 127)
	print(hasil)
	return hasil

# Fungsi untuk mendekripsi hasil enkripsi menjadi password
def decrypt(encrypt,key,factor):
	hasil_decrypt = ""
	for i in range(len(encrypt)):
		hasil_decrypt = hasil_decrypt + chr((factor[i]*127) + ord(encrypt[i]) - key[i])
	print(hasil_decrypt)
	return hasil_decrypt


password = input("masukan pass : ")

kunci = key(password)
factor = factor(kunci,password)
enkripsi = encrypt(kunci,password)


decrypt(enkripsi, kunci, factor)
