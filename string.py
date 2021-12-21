print ("manipulasi string pada python")
text =  input("Text : ")
print ('\n''manipulasi text \n 1. yes \n 0. no')
manipulasi = int(input('pilihan : '))
                 
while manipulasi == 1  :
    print ("\n""MENU")
    print ("1. capitalisasi")
    print ("2. center")
    print ("3. count")
    print ("4. index")
    print ("5. periksa")
    print ("6. isalpha")
    print ("7. isspace")
    print ("8. isdigit")
    print ("9. replace")
    print ("10. swapcase")
    print ("0. EXIT")
    print ('\n''masukan angka yang ada pada menu ; ')
    pilihan = int(input('pilihan : '))
    
    if (pilihan == 1):
        capitalize = text.capitalize()
        print(capitalize)
        
    elif (pilihan == 2):
        center = text.center(50,' ')
        print(center)

    elif (pilihan ==3):
        huruf = str(input('\n''karakter yang ingin di ketahui kemunculannya : '))
        count = text.count(huruf)
        print ('karakter', huruf, 'muncul sebanyak', count,'kali') 
    elif (pilihan ==4):
        huruf = str(input('\n''karakter yang ingin di cari : '))
        index = text.index(huruf)
        print ('karakter', huruf, 'berada pada inndex ke ', count)
    elif (pilihan ==5):
        print ('periksa apakah')
        print ('1. teks terdiri dari alfabet dan numerik')
        print ('2. teks hanya alfabet')
        print ('3. teks terdapat spasi')
        print ('4. teks hanya numerik')
        periksa = int(input('masukan nilai yang ada pada menu : '))
        
        while periksa >=1 and periksa <=4:
            if (periksa == 1):
                alnum = text.isalnum()
                print (alnum)
            elif (periksa == 2):
                alpha = text.isalpha()
                print (alpha)
            elif (periksa == 3):
                space = text.isspace()
                print (space)
            elif (periksa == 4):
                numerik = text.isnumeric()
                print (numerik)
            else :
                print ('pilihan menu salah, maaf program berhenti')
    else :
        print ("salah")

        

    


