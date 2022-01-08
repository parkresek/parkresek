print ('='*50)
print ('kalkulator bagun datar'.center(50,' '))
print ('='*50)
print ('MENU'.center(50,' '))
print ('1. lingkaran')
print ('2. persegi')
pilihan = int (input('masukan pilihan anda = '))

# rumus
if pilihan == 1 :
    phie = (3.14)
    r= int(input("\t masukkan nilai jari-jari = "))
    luas = (phie*r*r)
    print("\t luas lingkaran =", luas, "cm2")
elif pilihan == 2:
    s = int(input ("\t masukan panjang sisi = "))
    luas = s**2
    print ("\t luas persegi = ",luas)
else :
    print ("selesai")
