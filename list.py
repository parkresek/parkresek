# membuat array
larik = []
 
#banyaknya elemen (range)
data = int(input("Banyaknya Data : "))
 
# perulangan menurut jumlah range
print ('Masukan Data : ')
for i in range(0, data):
    value = str(input())

# menambah elemen 
    larik.append(value) 
print ('-'*50)     
print('DATA : ',larik)

# menghitung banyak data
print ('-'*50)
print ('JUMLAH DATA : ',len(larik))

# mengurutkan sesuai abjad
print ('-'*50)
print ('ÚRUTAN DATA SESUAI ABJAD : ')
larik.sort()
print ('-'*50)

# menampilkan  
for larik in larik:  
   print(larik)

#manipulasi
   
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
            print (larik.capitalize())
            pilihan = larik
                    
        elif pilihan == 2:
            print (larik.upper())
            pilihan = larik
                        
        elif pilihan == 3:
            print (larik.lower())
            pilihan = larik

        elif pilihan == 4:
            replace = larik.replace(str(input ('asal kata : ')),str(input ('menjadi : ')))
            print (replace)
            pilihan = larik

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
