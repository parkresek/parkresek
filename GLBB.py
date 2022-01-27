print ('='*50)
print ('GLBB(Gaya Gerak Lurus Berubah Beraturan)'.center(50,' '))
print ('='*50)

jarak = int(input('Jarak tempuh (m) = '))
kawal = int(input('Kecapatan awal (m/s) = '))
waktu = int(input('Selang waktu (s) = '))
percepatan = int(input('percepatan (m/s)= '))

hasil = kawal*waktu + 0.5*percepatan*(waktu**2)
print ('total waktu tempuh = ',hasil,'m/s')
