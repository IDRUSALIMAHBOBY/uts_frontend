

print("\n======  Rental Playstation  =======")
print("====  Menyediakan Penyenyawaan playstation dari ps 1 ps 2 , ps 3 , ps4 , dan ps 5  ====")

ps = input("Silahkan Masukkan nama penyewa : ")
print("Nama Penyewa = ", ps)
alamat = input("Masukkan Alamat Rumah Anda  : ")
print("Alamat Rumah = ", alamat)


jawab= 'iya'
while(True):

    nama = ["Playstation 1 ", "Playstation 2" , "Playstation 3" , "Playstation 4" , "Playstation 5" ]
 
    for list in nama:
        print("\n==== 1. ", nama[0],"====")
        print("\n==== 2. ", nama[1],"====")
        print("\n==== 3. ", nama[2],"====") 
        print("\n==== 4. ", nama[3],"====") 
        print("\n==== 5. ", nama[4],"====") 
        break   


    sewa = int(input("Silahkan Pilih Playstation yang akan di sewa : "))
    lama = int(input("Berapa Hari : " ))


    if  sewa == 1:
        biaya1= lama*10000
        print("Biaya sewa Playstation 1 Rp : ",biaya1 )

    elif sewa == 2:
        biaya1 = lama*15000
        print("Biaya Sewa Playstation 2 Rp : ", biaya1)

    elif sewa == 3:
        biaya1 = lama*23000
        print("Biaya Sewa Playstation 3 Rp : ", biaya1)

    elif sewa == 4:
        biaya1 = lama*30000
        print("Biaya Sewa Playstation 4 Rp : ", biaya1)


    elif sewa == 5:
        biaya1 = lama*35000
        print("Biaya Sewa Playstation 5 Rp : ", biaya1)

    else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")

    print("\n==========================================")
    print("========== S T R U K   S E W A ===========")
    print("\n==========================================")
    print (" Nama                        :",ps)
    print (" Alamat Rumah                :",alamat)
    print (" Biaya                       :",biaya1)
    print("\n======== T E R I M A   K A S I H =========")
    print("==========================================")




    jawab= input("Apakah anda ingin menyewa playstation jenis lainnya ? ")
    if jawab == 'tidak':
        print("=======  T E R I M A   K A S I H  =======")
        break