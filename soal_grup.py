batasan = list(range(0,101))
matematika = int(input('masukan nilai matematika: '))
b_inggris = int(input('masukan nilai bahasa inggris: '))
b_indonesia = int(input('masukan nilai bahasa indonesia: '))
skor = (matematika+b_inggris+b_indonesia)/3


if (matematika and b_inggris and b_indonesia in batasan ):
    print ('MINAT')
    print ('1. Teknik Elektro')
    print ('2. Teknik Mesin')
    print ('3. Bidang Pariwisata')
    minat = int(input('masukan minat anda : '))
    print ('rata-rata nilai anda : ',skor)

    if skor < 70 :
        print ('Anda dinyatakan tidak lolos karena skor anda adalah ',rata_rata)
    elif skor == 70 :
        if minat == 1:
            print ('skor anda adalah ',rata_rata,'anda lolos ke TEKNIK ELEKTRO')
        elif minat == 2:
            print ('skor anda adalah ',rata_rata,'anda lolos ke TEKNIK MESIN')
        else :
            print ('skor anda adalah ',rata_rata,'anda lolos ke BIDANG PARIWISATA')
    else :
            print ('anda bebas memilih yang di sukai')
while (matematika and b_inggris and b_indonesia != batasan ) :
    print ('masukan inputan rentang 1 sampai 100')
    matematika = int(input('masukan nilai matematika: '))
    b_inggris = int(input('masukan nilai bahasa inggris: '))
    b_indonesia = int(input('masukan nilai bahasa indonesia: '))
else :
        print ('salah')
