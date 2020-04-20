#B03, Best Wahana
import csv

def best_wahana():
    tiket = open("tiket.csv","r")
    wahana = open("wahana.csv","r")
    tiketreader=csv.reader(tiket,delimiter=";")
    wahanareader=csv.reader(wahana,delimiter=";")
    next(tiketreader)
    next(wahanareader)

    with tiket:
        data1 = list(tiketreader)
    with wahana:
        data2 = list(wahanareader)

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

    max = 0
    arrayBaru = [["" for i in range(3)] for i in range(3)]
    #FUNGSI SORT
    for j in range(3):
        for i in range(length):
            if (int(array[i][2]) >= int(max)):
                max = array[i][2]
                maxi = i
        arrayBaru[j] = [array[maxi][0],array[maxi][1],array[maxi][2]]
        array[maxi] = [0,0,0]
        max = 0

    for i in range(3):
        print(i+1,end=" | ")
        print(arrayBaru[i][0] , " | ", arrayBaru[i][1] , " | ", arrayBaru[i][2])
    return

best_wahana()
