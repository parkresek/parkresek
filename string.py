# heading
print ('-'*50)
print ('Manipulasi String'.center(50,' '))
print ('-'*50)

#teks awal
teks = str(input('Teks : '))
print ('-'*50)

print ('Konfirmasi manipulasi data')
print ('\t 1. yes')
print ('\t 2. no')
pilihan = int(input('apakah ingin lanjut ? masukan nilai yang ada pada pilihan : '))
print ('-'*50)
while pilihan <1 or pilihan >2:
        print ('Masukan pilihan yang ada pada menu')
        pilihan = int(input('apakah ingin lanjut ? masukan nilai yang ada pada pilihan : '))
        print ('-'*50)
while pilihan != 0:
        if pilihan == 1:
            #pilihan manipulasi
            print ('\t Menu')
            print ('\t 1. capitalize')
            print ('\t 2. uppercase')
            print ('\t 3. lowercase')
            print ('\t 4. replace')
            print ('\t 5. exit')
            print ('-'*50)
            pilihan = int(input('pilih sesuai nomor pada menu : '))
            #looping
            while pilihan >5 or pilihan <1:
                print ('Masukan pilihan yang ada pada menu')
                pilihan = int(input('pilih sesuai nomor pada menu : '))
            while pilihan !=0:    
                if pilihan == 1:
                        print (teks.capitalize())
                        pilihan = teks
                    
                elif pilihan == 2:
                        print (teks.upper())
                        pilihan = teks
                        
                elif pilihan == 3:
                        print (teks.lower())
                        pilihan = teks

                elif pilihan == 4:
                        replace = teks.replace(str(input ('asal kata : ')),str(input ('menjadi : ')))
                        print (replace)
                        pilihan = teks

                else :
                        print ('TERIMAKASIH')
                        break
                print ('\t Menu')
                print ('\t 1. capitalize')
                print ('\t 2. uppercase')
                print ('\t 3. lowercase')
                print ('\t 4. replace')
                print ('\t 5. exit')
                print ('-'*50)
                pilihan = int(input('pilih sesuai nomor pada menu : '))
        
