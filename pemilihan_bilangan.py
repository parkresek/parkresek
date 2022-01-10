for i in range(1,100):
    sisa = 0
    for j in range(1,i+1):
        jumlah = i%j

        if jumlah == 0:
            sisa = sisa+1
    if sisa == 2:
        print(i, "adalah bilangan prima")
    else :
        print(i, "bukan bilangan prima")
    
