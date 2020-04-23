# Mantap

#B03, Best Wahana

def best_wahana():
    #Membuang baris pertama array
    data1 = ((pilihan("tiket.csv"))[1:])
    data2 = ((pilihan("wahana.csv"))[1:])

    length=0
    for row in data1:
        length+=1

    array = [[0 for i in range(3)] for j in range (length)]
    i=0

    #MENGUBAH BAGIAN YANG INGIN DISORTIR MENJADI ARRAY

    for row in data1:
        array [i][0] = row [1]
        array[i][2] = row[2]

        for rowbaru in data2:
            if row[1] == rowbaru[0]:
                array[i][1] = rowbaru[1]
        i+=1
    Z=0
    sum=0

    #Membuat Array yang menampung total Pembelian Tiket per Wahana
    arrayWahana = [["" for i in range(3)] for j in range (100)]
    current = array[0][0]
    for x in range(length):
        current = array[x][0]
        for u in range(length):
            if (array[u][0] == current) and (array[u][0]!= ""):
                arrayWahana[Z][0] = array[u][0]
                arrayWahana[Z][1] = array[u][1]
                sum+=(int(array[u][2]))
                array[u][0] = ""
            if (sum!=0):
                arrayWahana[Z][2] = sum
        Z += 1
        sum = 0


    maxx= 0
    #Array yang menampung 3 pembelian tertinggi
    arrayBaru = [["" for i in range(3)] for i in range(3)]


    #FUNGSI SORT
    for j in range(3):
        for i in range(100):
            if(arrayWahana[i][2]!=""):
                if (int(arrayWahana[i][2]) >= int(maxx)):
                    maxx = int(arrayWahana[i][2])
                    maxi = i

        arrayBaru[j] = [arrayWahana[maxi][0],arrayWahana[maxi][1],arrayWahana[maxi][2]]
        arrayWahana[maxi] = [0,0,0]
        maxx = 0

    for i in range(3):
        print(i+1,end=" | ")
        print(arrayBaru[i][0] , " | ", arrayBaru[i][1] , " | ", arrayBaru[i][2])
    return
