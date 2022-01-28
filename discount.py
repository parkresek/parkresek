print ('='*50)
print ('Menghitung Total Bayar'.center(50,' '))
print ('='*50)

harga = int(input('Masuka harga : '))
jumlah = int(input('Jumlah barang : '))
total = jumlah*harga

if total >= 200000:
    diskon = (total*15)/100
    total = total-diskon
    print ('Diskon = 15%')
    
elif total >= 1000000:
    diskon = (total*10)/100
    total = total-diskon
    print ('Diskon = 10%')
    
elif total >= 50000:
    diskon = (total*5)/100
    total = total-diskon
    print ('Diskon = 5%')
    
    if jumlah >= 50:
        diskon = total-((total*5)/100)
        print ('Tambahan diskon 5% total bayar = ',total)
        
else :
    print ('Total bayar = ',total)
