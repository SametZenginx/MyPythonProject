import random
import time

class Kumanda():

    def __init__(self,tvDurum = "Kapali",tvSes = 0,kanalListesi = ["TRT"],kanal = "TRT"):
        
        self.tvDurum = tvDurum
        self.tvSes = tvSes
        self.kanalListesi = kanalListesi
        self.kanal = kanal

    def tvAc(self):

        if (self.tvDurum == "Acik"):
            print("Televizyon zaten acik")
        else:
            print("Televizyon aciliyor.")
            self.tvDurum = "Acik"
    def tvKapat(self):

        if self.tvDurum == "Kapali":
            print("Televizyon zaten kapali")
        else:
            print("Televizyon kapatiliyor.")
            self.tvDurum == "Kapali"
    def sesAyari(self):
        while True:
            artazalt = input("Sesi arttirmak icin '>' azaltmak icin '<' cikmak icin 'q' yaz.")
            if (artazalt == ">"):
                if self.tvSes != 100:
                    self.tvSes += 1
                    print("Ses: ",self.tvSes)
            elif (artazalt == "<"):
                if self.tvSes != 0:
                    self.tvSes -= 1
                    print("Ses: ",self.tvSes)
            else:
                print("Ses ayarindan cikiliyor.")
                break
    def kanalEkle(self,kanalIsmi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanalListesi.append(kanalIsmi)
        print("Kanal eklendi.")
    def rastgeleKanal(self):
        rastgele = random.randint(0,len(self.kanalListesi)-1)
        self.kanal = self.kanalListesi[rastgele]
        print("Su anki kanal: {} kanal degistirildi".format(self.kanal))
    def __len__(self):
        return len(self.kanalListesi)
    def __str__(self):
        return "Tv Durumu: {}\nTv Ses {}\nKanal listesi: {}\nSu anki kanal: {}\n".format(self.tvDurum,self.tvSes,self.kanalListesi,self.kanal)

kumanda = Kumanda()

print("""

Televizyon Uygulamasi: 

1. Tv aç

2. Tv kapat

3. Ses ayarlari

4. Kanal ekle

5. Kanal sayisi ogrenme

6. Rastgele kanal degistirme

7. Televizyon bilgileri

Cikmak icin 'q' ya basin.

""")

while True:

    islem = input("Yapmak istediginiz islemi secin: ")

    if islem == "q":
        print("Program kapatiliyor...")
        break
    elif islem == "1":
        kumanda.tvAc()
    elif islem == "2":
        kumanda.tvKapat()
    elif islem == "3":
        kumanda.sesAyari()
    elif islem == "4":
        kanalIsimlerii = input("Kanal isimlerini ',' ile ayirarak giriniz.")

        kanalListesi = kanalIsimlerii.split(",")

        for eklenecekler in kanalListesi:
            kumanda.kanalEkle(eklenecekler)
    elif islem == "5":
        print("Kanal sayisi: ",kumanda.__len__())
    elif islem == "6":
        kumanda.rastgeleKanal()
    elif islem == "7":
        print(kumanda)
    else:
        print("Gecersiz islem girdiniz. ") 

    


    
        
    


            

            
        

