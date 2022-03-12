def asalMi(sayi):
    i = 2
    while i<sayi:
        if sayi%i == 0:
            return False
        i+=1

    return True

def asalGenerator():
    sayi = 2
    while True:
        if asalMi(sayi):
            yield sayi
        sayi+=1

for sayilar in asalGenerator():
    if sayilar>1000:
        break
    print(sayilar)