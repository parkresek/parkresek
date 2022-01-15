tampil = ''
cetak =[]
desimal = int (input('masukan angka desimal : '))
print ('')

desimal = int (input('masukan angka desimal :'))
print ('')
while desimal != 0:
    hasil = desimal % 16 
    if hasil == 10:
        hasil = 'A'
    if hasil == 11:
        hasil = 'B'
    if hasil == 12:
        hasil = 'C'
    if hasil == 13:
        hasil = 'D'
    if hasil == 14:
        hasil = 'E'
    if hasil == 15:
        hasil = 'F'
    cetak.insert(0, str(hasil))
    desimal = desimal//16  
    if desimal == 0:
        for i in range (len(cetak)):
            tampil +=  cetak[i]
print ('hasilnya adalah : ',tampil)
print ('')                
            
