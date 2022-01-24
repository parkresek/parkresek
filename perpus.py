print ('='*50)
print ('PERPUSTAKAAN'.center(50,' '))
print ('='*50)
username = str(input("masukkan username : "))
nim = str(input("masukkan password : "))
username_from_db = "Wiranto"
nim_from_db = "D0219997"
if username.capitalize() == username_from_db :
    if nim.capitalize() == nim_from_db :
        print ("Username dan nim cocok ")
    else:
        print ("nim salah ")
    print ('='*50)
    print ('Bulan Peminjaman'.center(50,' '))
    print ('1. Januari')
    print ('2. Februari')
    print ('3. Maret')
    print ('4. April')
    print ('5. Mei')
    print ('6. Juni')
    print ('7. Juli')
    print ('8. Agustus')
    print ('9. September')
    print ('10. Oktober')
    print ('11. November')
    print ('12. Desember')
    print ('='*50)
    pinjam = int(input('Pilih bulan peminjaman : '))
    print ('='*50)
    print ('Bulan Pengembalian'.center(50,' '))
    print ('1. Januari')
    print ('2. Februari')
    print ('3. Maret')
    print ('4. April')
    print ('5. Mei')
    print ('6. Juni')
    print ('7. Juli')
    print ('8. Agustus')
    print ('9. September')
    print ('10. Oktober')
    print ('11. November')
    print ('12. Desember')
    print ('='*50)
    kembali = int(input('Pilih bulan pengembalian : '))
    print ('='*50)
    batas = pinjam + 3
    tunggakan = kembali-batas
    denda = 10000
    denda_total = tunggakan*denda
    print ('Info'.center(50,' '))
    print ('batas sampai bulan : ',batas)
    print ('tunggakan batas peminjaman : ',tunggakan,'bulan')
    print ('denda perbulan : Rp.',denda)
    print ('total denda yang harus di bayar : Rp.',denda_total)
    
        
    
else:
 print ("User tidak terdaftar")
