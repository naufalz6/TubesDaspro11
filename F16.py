#F06, Fungsi Exit
def exit():
    exit=input("Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ? ")

    while (exit!="Y" and exit!="N"):
        exit = input("Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ? ")

    if (exit == "Y"):
        save()

    return
