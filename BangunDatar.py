print ('='*50)
print ('kalkulator bagun datar'.center(50,' '))
print ('='*50)
print ('MENU'.center(50,' '))
print ('1. lingkaran')
print ('2. persegi')
print ('3. persegi panjang')
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
elif pilihan == 3:
    print ('mencari')
    print (' 1. luas \n 2. panjang \n 3. lebar')
    mencari = int (input('masukan pilihan = '))
    if mencari == 1:
        p = int(input('panjang sisi persegi panjang = '))
        l = int(input('lebar persegi panjang = '))
        luas = p*l
        print ('luas persegi panjang = ',luas)
    elif mencari == 2:
        luas = int(input('luas persegi panjang = '))
        l = int(input('lebar persegi panjang = '))
        panjang = luas/l
        print ('panjang persegi panjang = ',panjang)
    elif mencari == 3:
        luas = int(input('luas persegi panjang = '))
        p = int(input('panajag persegi panjang = '))
        lebar = luas/p
        print ('lebar persegi panjang = ',lebar)
    else :
        print ('masukan salah')
        
else :
    print ("selesai")
