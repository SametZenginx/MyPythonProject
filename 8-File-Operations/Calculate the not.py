def notHesapla(satir):
    
    satir = satir[:-1]
    
    liste = satir.split(",")

    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    sonNot = not1*(3/10) + not2*(3/10) + not3*(4/10)

    if sonNot>=90:
        harf == "AA"
    elif sonNot>=85:
        harf == "BA"
    elif sonNot>=80:
        harf == "BB"
    elif sonNot>=70:
        harf = "CB"
    elif sonNot>=60:
        harf = "CC"   
    elif sonNot>=55:
        harf = "DC"   
    elif sonNot>=50:
        harf = "DD"
    else:
        harf = "FF"
        
    return isim + "-------------->" + harf + "\n"


with open("Notlar.txt","r",encoding="utf-8") as file:

    ekleneceklerListesi = []

    for i in file:
        ekleneceklerListesi.append(notHesapla(i))
    
    print(ekleneceklerListesi)

