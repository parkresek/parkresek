print ('='*50)
print ('RENTAL MOBIL'.center(50,' '))
print ('='*50)

print ('pilihan mobil'.center(50,' '))
print ('1. Fajerox : Rp.200.000/Hari')
print ('2. Abanza  : Rp.150.000/Hari')
print ('3. Seniah  : Rp.100.000/Hari')
mobil = int(input('Masukan pilihan mobil : '))
print ('='*50)

print ('pilihan tujuan'.center(50,' '))
print ('1. Makassar')
print ('2. Pare-pare')
print ('3. Polewali')
tujuan = int(input('Tujuan : '))
print ('='*50)

print ('Hari'.center(50,' '))
print ('1. Senin')
print ('2. Selasa')
print ('3. Rabu')
print ('4. Kamis')
print ('5. Jumat')
print ('6. Sabtu')
print ('7. Mingggu')
lama = int (input('hari mulai rental : '))
kembali = int (input('hari kembali : '))
print ('='*50)

if mobil == 1:
    tarif = 200000
    waktu = kembali-lama
    total = waktu*tarif
    print ('mobil = Fajerox')
    print ('lama rental = ',abs(waktu),' hari')
    print ('tarif = ',abs(total))
elif mobil == 2:
    tarif = 150000
    waktu = kembali-lama
    total = waktu*tarif
    print ('mobil = Abanza')
    print ('lama rental = ',abs(waktu),' hari')
    print ('tarif = ',abs(total))
elif mobil == 3:
    tarif = 100000
    waktu = kembali-lama
    total = waktu*tarif
    print ('mobil = seniah')
    print ('lama rental = ',abs(waktu),' hari')
    print ('tarif = ',abs(total))
else :
    print ('Pilihan tidak ada')
    
    
