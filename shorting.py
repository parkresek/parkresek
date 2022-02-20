nilai = [1,6,4,7,9,10,2,5,3,8]
def shorting(nilai):    
    tukar = True
    while tukar:
        tukar = False
        for j in range(len(nilai)-1):
            if nilai[j] > nilai[j+1]:
                nilai[j], nilai[j+1] = nilai[j+1],nilai[j]
                tukar = True
    return nilai
print (shorting(nilai))
