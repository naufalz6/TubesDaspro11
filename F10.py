def Kritik_Saran (ID,Tanggal,KS):
    import csv
    data = open("kritiksaran.csv",'a')
    data.writelines("\n;"+Tanggal+";"+ID+";"+KS)
    print("\nKritik dan saran Anda kami terima.")
    data.close()
ID = input("Masukkan ID Wahana: ")
Tanggal = input("Masukkan tanggal pelaporan: ")
KS = input("Kritik/saran anda: ")
Kritik_Saran(ID,Tanggal,KS)
