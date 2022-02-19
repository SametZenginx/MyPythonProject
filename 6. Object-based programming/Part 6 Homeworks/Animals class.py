import time

class Animals():

    def __init__(self,adi,kilosu,türü):

        self.adi = adi
        self.kilosu = kilosu
        self.türü = türü

    def bilgileriGoster(self):
        print("""
        Hayvanlar ile ilgili ortak bilgiler: 
        1-)Hücre ve hücre yapilari
        2-)Beslenme özelliği.
        3-)Metabolizma.
        4-)Büyüme.
        5-)Hareket etme.
        6-)Çevresel uyarilara tepki.
        7-)Üreme.
        """)
    

class Dogs(Animals):

    def __init__(self,adi,kilosu,türü,belirginOzelligi,boyu,yasamaYili):

        super().__init__(adi,kilosu,türü)
        
        self.belirginOzelligi = belirginOzelligi
        self.boyu = boyu
        self.yasamaYili = yasamaYili
    def __str__(self):
        return """
        Hayvan Bilgileri:
        Adi : {}
        Kilosu : {}kg
        Türü : {}
        Boyu : {}cm
        Ortalama yasama yili : {}
        Belirgin Özellikleri : {}

        """.format(self.adi,self.kilosu,self.türü,self.boyu,self.yasamaYili,self.belirginOzelligi)
    
    def __len__(self):
        time.sleep(0.3)
        print("Kopek harfi {} hanelidir.".format(self.adi))
    
class Birds(Animals):

    def __init__(self,adi,kilosu,türü,belirginOzelligi,boyu,yasamaYili):

        super().__init__(adi,kilosu,türü)
        
        self.belirginOzelligi = belirginOzelligi
        self.boyu = boyu
        self.yasamaYili = yasamaYili
    def __str__(self):
        return """
        Hayvan Bilgileri:
        Adi : {}
        Kilosu : {}kg
        Türü : {}
        Boyu : {}cm
        Ortalama yasama yili : {}
        Belirgin Özellikleri : {}
        

        """.format(self.adi,self.kilosu,self.türü,self.boyu,self.yasamaYili,self.belirginOzelligi)
   
    def __len__(self):
        time.sleep(0.3)
        print("Kus harfi {} hanelidir.".format(self.adi))

class Horses(Animals):

    def __init__(self,adi,kilosu,türü,belirginOzelligi,boyu,yasamaYili):

        super().__init__(adi,kilosu,türü)
        
        self.belirginOzelligi = belirginOzelligi
        self.boyu = boyu
        self.yasamaYili = yasamaYili
    def __str__(self):
        return """
        Hayvan Bilgileri:
        Adi : {}
        Kilosu : {}kg
        Türü : {}
        Boyu : {}cm
        Ortalama yasama yili : {}
        Belirgin Özellikleri : {}

        """.format(self.adi,self.kilosu,self.türü,self.boyu,self.yasamaYili,self.belirginOzelligi)
 
    def __len__(self):
        time.sleep(0.3)
        print("At harfi {} hanelidir.".format(self.adi))

pomeranianDog = Dogs("Pomeranian",4,"Memeli","Almanya ve polonya da bulunan küçük boylu köpek irki",55,14)
sibiryakurduDog = Dogs("Sibirya kurdu",25,"Memeli","Sibirya'da yasarlar. Soguga aliskindir.",100,13)
baykusKus = Birds("Baykus",2.5,"Sürüngenden evrimleşmiş ara geçiş türüdür.","Tüyleri vardir. Gece yirticisidir.",55,65)
penguenKus = Birds("Penguen",12,"Sürüngenden evrimlesmis ara gecis türüdür","Gruplar halinde yasamayi seven canlilardir.",80,13)
arapAti = Horses("Arap ati",400,"Memeli","Zekasi sadakati ve dayanikliligi ile bilinir. Genellikle türkler küheylan der.",150,25)
friesianAti = Horses("Friesian ati",420,"Memeli","Hollandanin gururu olan bol paça pantolon gibi tüyleri vardir.",170,22)
animal = Animals("Bilgi yok",0,"Bilgi yok")
print("""
*******************
Hayvanlar hakkinda bilgi sahibi olmaya hos geldiniz.
1-) Hayvanlarin ortak ozellikleri:

2-) Kopekler:
    a) Pomeranian Irki
    b) Sibirya Kurdu

3-) Kuslar:
    a) Baykus
    b) Penguen

4-) Atlar:
    a) Arap ati(küheylan)
    b) Friesian ati

Bu tuslara basarak onlar hakkinda bilgi sahibi olabilirsiniz.
Cikmak icin 'q' yazabilirsiniz.
*******************
""")

while True:
    islem = input("Yapmak istediginiz islemi seciniz: ")
    islem = islem.lower()
    if islem == "q":
        print("Cikiliyor...")
        time.sleep(0.5)
        break
    elif islem == "1":
        animal.bilgileriGoster()
        time.sleep(6)
    elif islem == "2":
        print("Kopekler kismina basari ile giris yaptiniz lütfen bekleyin...")
        time.sleep(0.3)
        islem1 = input("Bilgi ogrenmek istediginiz kopegin basindaki harfi giriniz: ")
        islem1 = islem1.lower()
        
        if islem1 == "a":
            print(pomeranianDog)
            time.sleep(8)
        elif islem1 == "b":
            print(sibiryakurduDog)
            time.sleep(8)
        else:
            print("Islem basarisiz.")
            time.sleep(0.5)
    elif islem == "3":
        print("Kuslar kismina basari ile giris yaptiniz lütfen bekleyin...")
        time.sleep(0.3)
        islem1 = input("Bilgi ogrenmek istediginiz kusun basindaki harfi giriniz: ")
        islem1 = islem1.lower()
        
        if islem1 == "a":
            print(baykusKus)
            time.sleep(8)
        elif islem1 == "b":
            print(penguenKus)
            time.sleep(8)
        else:
            print("Islem basarisiz.")
            time.sleep(0.5)
    elif islem == "4":
        print("Atlar kismina basari ile giris yaptiniz lütfen bekleyin...")
        time.sleep(0.3)
        islem1 = input("Bilgi ogrenmek istediginiz atin basindaki harfi giriniz: ")
        islem1 = islem1.lower()
        
        if islem1 == "a":
            print(arapAti)
            time.sleep(8)
        elif islem1 == "b":
            print(friesianAti)
            time.sleep(8)
        else:
            print("Islem basarisiz.")
            time.sleep(0.5)
    else:
        print("Hatali tuslama girdiniz. Tekrar deneyin.")
        time.sleep(0.4)

        

        


        
        





