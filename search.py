def mencari(item,daftar):
    ketemu = False
    lokasi = 0
    while lokasi < len(daftar) and not ketemu:
        if daftar[lokasi] == item:
            ketemu = True
        lokasi = lokasi + 1
    return ketemu
lemari = ['baju','celana','jeket','book','dompet']
item = input('apa yang anda cari di lemari ? ')
itemKetemu = mencari(item,lemari)
if itemKetemu:
    print ('ketemu')
else:
    print ('cari di tempat lain')

