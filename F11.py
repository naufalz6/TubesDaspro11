#FUNGSI F11, FUNGSI MELIHAT KRITIK SARAN
import csv

def lihat_laporan():
    length = 0
    print("Kritik dan saran:")
    f = open('kritiksaran.csv', 'r')

    with f:
        reader = csv.reader(f,delimiter=';')
        # Agar row pertama tidak termasuk
        next(reader)
        listreader = list(reader)

        # Mengukur panjang baris
        for row in listreader:
            length+=1

        # Menampung ID wahana ke dalam array
        array = [0 for i in range(length)]
        i=0
        for row in listreader:
            array[i] = row[2]
            i+=1
        j=0
        mini = 0

        #Fungsi Sort Kode
        for x in range(length):
            min = "ZZZ999"
            for i in range(length):
                if array[i] <= min:
                    min = array[i]
                    mini = i
            #Output sesuai dengan urutan yang sudah di sort
            print((listreader[mini])[2] + " | " + (listreader[mini])[1] + " | " + (listreader[mini])[0] + " | " + (listreader[mini])[3])
            j+=1
            array[mini] = "ZZZ999"
            min = "ZZZ999"
    return
lihat_laporan()

# Kasih masukan ya
# Stella, jangan import csv, pake array aja :)
# semangat!!!
