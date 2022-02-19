jumlah = 0
n = int (input('Masukan Angka : '))

for i in range (1,n+1) :
    print (i,end =' ')
    if i == n :
        print ('=',end =' ')
    else :
        print ('+',end =' ')
    jumlah = jumlah + i
print (jumlah)
