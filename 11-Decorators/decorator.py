def ekstra(fonk):

    def wrapper(sayilar):

        ciftlerToplami = 0
        ciftSayilar = 0
        teklerToplami = 0
        tekSayilar = 0

        for sayi in sayilar:
            if (sayi%2 == 0):
                ciftlerToplami += sayi
                ciftSayilar += 1
            else:
                teklerToplami += sayi
                tekSayilar +=1
        
        print("Teklerin Ortalamasi: ",teklerToplami/tekSayilar)

        print("Ciftlerin Ortalamasi: ",ciftlerToplami/ciftSayilar)

        fonk(sayilar)
    
    return wrapper
    
@ekstra
def ortalamabul(sayilar):
    toplam = 0
    for i in sayilar:
        toplam += i
    print("Genel ortalama: ",toplam/len(sayilar))

ortalamabul([1,2,3,4,5,1,2,5,6])