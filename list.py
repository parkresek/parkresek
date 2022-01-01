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

# menampilkan  
for larik in larik:  
   print(larik)

# menambahkan isi ke list
tambahan_data = int(input('berapa jumlah data yang ingin di tambahkan : '))
for a in range (tambahan_data) :
    larik.append(value)
print ('data = ',larik)
   
