import random as rd

print ("="*50)
print ("Pembagian Kelompok".center(50," "))
print ("="*50)
# jumlah mahasiswa
mahasiswa = int(input("jumlah mahasiswa : "))

#nama mahasiswa
while mahasiswa > 0:
    mhs =[]
    for a in range (mahasiswa):
        nama = str(input("Nama : "))
        mhs.append(nama)
        mahasiswa-=1  
nma = mhs

#pemberian index
angka = [] 
for num in range (0, len(nma)):
    angka.append(num)

#membagi kelompok
print ("_"*50)
total = int(input("Berapa Kelompok : "))
kel = [] 
for x in range(total): 
    sub= [] 
    kel.append(sub)

#mengacak data
count = 0 
while len(angka) > 0: 
 
    acak = rd.randint(0, len(angka)-1) 
    hasil = angka[acak]
    del (angka[acak])

    kel[count].append(nma[hasil])
    if count == len(kel)-1:  
        count = 0 
    else:  
        count+=1
print ("="*50)
print("Hasil Pembagian Kelompok".center(50," "))
#menampilkan hasil
nm = total-1 
for kel_sub in kel:
    print("_"*50) 
    print(f"Kelompok {total-nm}") 
    for name in kel_sub: 
        print(f"-{name}") 
    nm = nm - 1 
