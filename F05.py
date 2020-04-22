def cari_pemain(username):
    import csv
    data = open("user.csv",'r')
    reader = csv.reader(data,delimiter=',')
    row =next(data)
    x=0
    nama=""
    tanggal=""
    tinggi=""
    current = ""
    available=False
    while(row[x]!=mark):
        while(row[x]!=";"):
            nama=nama+row[x]
            x+=1
        x+=1
        while(row[x]!=";"):
            tanggal=tanggal+row[x]
            x+=1
        x+=1
        while(row[x]!=";"):
            tinggi=tinggi+row[x]
            x+=1
        x+=1
        while(row[x]!=";"):
            current=current+row[x]
            x+=1
        if(username==current):
            available=True
            break
        else:
            row = next(data)
            nama=""
            tanggal=""
            tinggi=""
            current = ""
            x=0
    if(available==True):
        print("Nama Pemain:",nama)
        print("Tinggi Pemain:",tinggi,"cm")
        print("Tanggal Lahir Pemain:",tanggal)
    else:
        print("Username pemain tidak ditemukan")
    return
        
username = input("Masukkan username: ")
cari_pemain(username)


# Kasih masukan ya
# Kevin, jangan pake import csv ya, perbaiki lagi :)
# Semangat!!!
