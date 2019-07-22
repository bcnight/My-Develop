import os
import time
koin = 0

def tambangkoin():
    global koin
    koin += 10.24
    print("Koin hasil tambang: ", koin)
    print("Koin sekarang: ",koin)

def kurangi_koin():
    global koin
    koin -= 10.24
    print("hasil dari koin yang di kurang: ", koin)

def pilihan():
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+                    TAMBANG KOIN                   +")
    print("+                  [ Masukkan Menu ]                +")
    print("+   [1]. Tambang   [2]. Kurangi Koin   [9]. Quit    +")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print()
    while True:

        user = input("Masukkan Menu: [1/9] > ")

        if user is "1":
            time.sleep(1)
            tambangkoin()

        elif user is "2":
            kurangi_koin()

        elif user is "9":
            quit()

        else:
            print("Masukkan Pilihan dengan benar !")

pilihan()
