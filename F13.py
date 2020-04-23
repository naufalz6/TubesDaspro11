#F13, FUNGSI TOP UP SALDO

import F01

def topup():

    uname=input("Masukkan username: ")
    up=int(input("Masukkan saldo yang di-top up: ")
    
    user = F01.pilihan("user.csv")
    i = 0
    for i in range (11):
           if(user[i][3]==uname):
           user[i][6]=str(int(user[i][6])+up)
           print("Top up berhasil. Saldo "+uname+" bertambah menjadi "+user[i][6])
    
    return

# Kasih masukan ya
# programnya gak usah import csv lagi, jadi kita di programnya mainin array aja
# ubah lagi ya Ren :), semangatttt!!!!!
    
# 24/4/2020 udah diubah sal, coba diperiksa lagi, thankss:))
