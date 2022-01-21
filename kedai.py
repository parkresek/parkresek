username = str(input("masukkan username : "))
password = str(input("masukkan password : "))
username_db = "user"
password_db = "admin"
if username == username_db :
    if password == password_db :
     print ("Username dan password cocok ")
     #kondisi awal
     menu = "y"
     #perulangan

     while menu.lower() == "y":
        #heading
        print("="*50)
        print(" Selamat Datang kedai kopi AW".center(50,' '))
        print(" List Menu Restoran".center(50,' '))
        
        #menu
        print("="*50)
        print(" 1. paket ubi goreng      : Rp 13.000")
        print(" 2. paket pisang goreng   : Rp 17.000")
        print(" 3. paket kentang goreng  : Rp 20.000")
        print(" 4. nasi goreng           : Rp 16.000")
        print(" 5. nasi kuning + ayam    : Rp 17.000")
        print("="*50)

        #input pilihan pesanan
        listMenu=str(input(" Masukkan angka sesuai dengan menu yang tersedia = "))

        #input jumlah pesanan
        jumlahPesanan=int(input(" Jumlah dibeli = "))

        #kondisi percabangan dari menu
        if listMenu == "1":
            namaMenu= " paket ubi goreng"
            harga=(13000*jumlahPesanan)
            pajak= int(harga * 0.1)

            #kondisi pesanan dikenakan pajak
            if jumlahPesanan >= 5:
                totalHarga=int(harga+pajak)
            else:
                totalHarga=int(harga+pajak)
        elif listMenu == "2":
            namaMenu= " paket pisang goreng"
            harga = (17000*jumlahPesanan)
            pajak = int(harga * 0.1)

            #kondisi pesanan dikenakan pajak
            if jumlahPesanan >= 5:
                totalHarga =int(harga+pajak)
            else:
                totalHarga =int(harga+pajak)
        elif listMenu == "3":
            namaMenu= " paket kentang goreng"
            harga=int(20000*jumlahPesanan)
            pajak = int(harga * 0.1)
            totalHarga=int(harga+pajak)
        elif listMenu == "4":
            namaMenu= " nasi goreng"
            harga=int(16000*jumlahPesanan)
            pajak = int(harga * 0.1)
            totalHarga = int(harga+pajak)
        elif listMenu == "5":
            namaMenu= " nasi kuning + ayam"
            harga=int(17000*jumlahPesanan)
            pajak = int(harga * 0.1)
            totalHarga = int(harga+pajak)
        else:
            menu=input(" Maaf,Menu yang dipilih tidak tersedia di restoran")

        #rincian pesanan
        print("-"*50)
        print(" Menu :",namaMenu)
        print(" Jumlah Pesanan :", jumlahPesanan)
        print(" Harga :", harga)
        print(" Pajak :", pajak)
        print("-"*50)
        print(" Total Pembayaran :", totalHarga)
        print("-"*50)
        menu=input(" Mau pesan lagi? \n pilih Y jika Ya dan pilih N jika Tidak \n (Y/N) = ")
    else:

        print ("Password salah ")
else:
 print ("User tidak terdaftar")
