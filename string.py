# heading
print ('-'*50)
print ('Manipulasi String'.center(50,' '))
print ('-'*50)

#teks awal
teks = str(input('Teks : '))
print ('-'*50)

#pilihan manipulasi
print ('\t menu')
print ('\t 1. capitalize')
print ('\t 2. uppercase')
print ('\t 3. lowercase')
print ('\t 4. replace')
print ('-'*50)
pilihan = int(input('pilih sesuai nomor pada menu : '))

#looping
while pilihan >=1 or pilihan <=4:
    kondisi = pilihan
    if kondisi == 1:
        print ('1')

    elif kondisi == 2:
        print ('2')

    elif kondisi == 3:
        print ('3')

    elif kondisi == 4:
        print ('4')

    else :
        print ('masukan nilai yang benar')
    
    pilihan <= 1
