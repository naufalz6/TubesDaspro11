#F13, FUNGSI TOP UP SALDO

import csv

def topup():

    uname=input("Masukkan username: ")
    up=int(input("Masukkan saldo yang di-top up: ")
    
    f=open("user.csv", "w")
    reader=csv.reader(f, delimiter=";")

    with f:
           next(reader)
           for row in reader:
               if (row[3]==uname):
                   row[6]=str(int(row[6])+up)
                   print("Top up berhasil. Saldo "+uname+" bertambah menjadi "+row[6])
    f.close()
    return

# Kasih masukan ya
# programnya gak usah import csv lagi, jadi kita di programnya mainin array aja
# ubah lagi ya Ren :), semangatttt!!!!!
    
