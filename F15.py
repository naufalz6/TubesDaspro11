def JumlahTiket(username):
    tiket = open("tiket.csv",'r')
    wahana = open("wahana.csv",'r')
    user =""
    x=0
    print("Riwayat:")
    for row in (tiket):
        user = ""
        ID = ""
        Jumlah =""
        count=0
        for i in row:
            if(i != ";"):
                if(count == 0):
                    user+=i
                elif(count == 1):
                    ID+=i
                else:
                    Jumlah = str(Jumlah)+str(i)
            else:
                count+=1
        if(user==username):
            for row in wahana:
                ID_Wahana = ""
                Nama_Wahana =""
                count = 0
                for i in row:
                    if(i != ";"):
                        if(count == 0):
                            ID_Wahana+=i
                        elif(count == 1):
                            Nama_Wahana+=i
                        else:
                            break
                    else:
                        count+=1
                if(ID==ID_Wahana):
                    print(ID,"|",Nama_Wahana,"|",Jumlah.strip())
                    break
    tiket.close()
    wahana.close()
    return
username = input("Masukkan username: ")
JumlahTiket(username)
                
                
        
    
