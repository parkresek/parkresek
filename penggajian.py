nama = str(input("Masukan Nama :"))
print ("Golongan Kerja : \n 1. manager \n 2. sales marketing \n 3. office boy")
gol = input("Pilihan Golongan Kerja :")
jam = int(input("Masukan jam Kerja :"))
print ("1. SMA \n2. D1 \n3. D3 \n4. S1")
golpen=input("Masukan Pendidikan \t: ")
gaji = 300000

#Menghitung Golongan Jabatan

if gol == "1":
    upah =0.05*gaji;
elif gol == "2":
    upah =0.10*gaji;
elif gol == "3":
    upah =0.15*gaji;
else:
    upah =0;
 
#Menghitung Golongan Pendidikan
if golpen == "SMA":
    tunpen =0.025*gaji;
elif golpen == "D1":
    tunpen =0.05*gaji;
elif golpen == "D3":
    tunpen =0.20*gaji;
elif golpen == "S1":
    tunpen =0.30*gaji;
else:
    tunpen =0;
    
#menghitung rumus
if jam > 8:
    lembur = jam - 8
    hlembur = lembur * 3500
    rumus = tunpen + upah + gaji + hlembur
else :
    print ("tidak ada golongan Pendidikan")
    hlembur = 0
    rumus = tunpen + upah + gaji 

print ("="*50)
print ("Hitung Gaji Karyawan".center(50,' '))
print ("="*50)
print ("Nama \t\t\t\t: ",nama)
print ("Golongan Kerja \t\t\t: ",gol)
print ("Jumlah Jam Kerja \t\t: ",jam)
print ("Pendidikan \t\t\t: ",golpen)
print ("Gaji Pokok \t\t\t: ",gaji)
print ("Tunjangan Jabatan \t\t: ",upah)
print ("Tunjangan Pendidikan \t\t: ",tunpen)
print ("Honor Lembur \t\t\t: ",hlembur)
print ("Total Gaji Dan Tunjangan \t: ",rumus)
