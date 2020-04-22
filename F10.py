# Kasih masukan
# Stella, jangan import csv, perbaiki lagi
# ganbatte!!!!

#FUNGSI F10, FUNGSI MELIHAT KRITIK SARAN
import csv

def lihat_laporan(a):
    print("Kritik dan saran:")
    f = open('kritiksaran.csv', 'r')
    with f:
        reader = csv.reader(f,delimiter=';')
        next(reader)        #agar row pertama tidak termasuk di output
        for row in reader:
            print(row[2]+" | " + row[1] +" | " +row[0]+" | " + row[3]) #output kritik
    f.close()
    return

lihat_laporan("")
