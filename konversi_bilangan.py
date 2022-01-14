tampil = ''
cetak =[]
desimal = int (input('masukan angka desimal : '))
print ('')
while desimal != 0:
    hasil = desimal % 2 #di modulus 2 untuk memperoleh sisa
    cetak.insert(0, str(hasil)) #membalik hasil modulus
    desimal = desimal//2 #bilangan desimal dibagi 2 dan tanpa menghasilkan angka koma
    if desimal == 0:
        for i in range (len(cetak)): #perulangan untuk menggabungkan angka angka hasil modulus yang sebelumnya ada di dalam list menjadi string
            tampil +=  cetak[i]
    print ('hasilnya adalah : ', tampil)
    
                
            
