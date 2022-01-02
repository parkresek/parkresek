mata_pelajaran ="matematika"
print ("konversi nilai mata pelajaran ", mata_pelajaran, " \n")

#nilai
nilai_tugas = 20
nilai_uts = 20
nilai_uas = 50
total_pertemuan = 10

#kalkulasi hasil nilai
tugas = 35/100*nilai_tugas
uts = 15/100*nilai_uts
uas = 40/100*nilai_uas
kehadiran = 10/18*total_pertemuan

print ("nilai tugas : ", tugas )
print ("nilai uts : ", uts)
print ("nilai uas : ", uas)
print ("kehadiran : ", kehadiran)

#total nilai
nilai = tugas+uts+uas+kehadiran
print ("\nnilai total = ", nilai)

# kondisi if, elif, else
if(nilai >= 90 and nilai <=100):
    print ("predikat A")
elif (nilai >= 70 ):
    print ("predikat B")
elif (nilai >= 60 ):
    print ("predikat C")
elif (nilai >= 40 ):
    print ("predikat D")
else :
    print ("eror")

