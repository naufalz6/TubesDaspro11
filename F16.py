#F06, Fungsi Exit
def exit():
    pilihan=input("Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ? ")

    while (pilihan!="Y" and pilihan!="N"):
        pilihan = input("Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ? ")

    if (pilihan == "Y"):
        save()

    return

# Mantap
