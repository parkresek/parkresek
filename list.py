# membuat array
larik = []
 
#banyaknya elemen (range)
data = int(input("Banyaknya Data : "))
 
# perulangan menurut jumlah range
print ('masukan data : ')
for i in range(0, data):
    value = str(input())

# menambah elemen 
    larik.append(value) 
     
print(larik)

# mengurutkan sesuai abjad   
larik.sort()

# menampilkan  
for larik in larik:  
   print(larik)

