string = ""
x = int(input("input jumlah baris : "))

# Looping Baris
baris = x-1
while baris >= 0:
	# Looping Kolom Spasi Kosong
	kiri = baris
	while kiri > 0:
		string = string + "  0  "
		kiri = kiri - 1
		
	# Looping Kolom Bintang Sisi Kiri	
	kanan = 1
	while kanan < (x - (baris-1)):
		string = string + "  1  "
		kanan = kanan + 1	

	string = string + "\n\n"
	baris = baris - 1
	
print (string)
