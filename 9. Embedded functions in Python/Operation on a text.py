import time
class Dosya():
    def __init__(self):
        with open("metin.txt","r",encoding="utf-8") as file:
            dosyaIcerigi = file.read()
            kelimeler = dosyaIcerigi.split()
            self.sadeKelimeler = []
            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(",")
                i = i.strip(".")
                self.sadeKelimeler.append(i)
    def tumKelimeler(self):
        kelimelerKumesi = set()

        for i in self.sadeKelimeler:
            kelimelerKumesi.add(i)
        
        print("Tüm kelimeler......")

        for i in kelimelerKumesi:
            print(i)
            print("*******")

    def kelimeFrekansi(self):

        kelimeSozluk = dict()


        for i in self.sadeKelimeler:
            if (i in kelimeSozluk):
                kelimeSozluk[i] += 1
            else:
                kelimeSozluk[i] = 1 #Ekler.
        
        for kelime,sayi in kelimeSozluk.items():
            print("{} kelimesi {} defa geciyor.".format(kelime,sayi))

            print("-----------------")
    
    def findWord(self):
        count = 0
        for i in self.sadeKelimeler:
            if a == i:
                count += 1
        if count == 0:
            return "Boyle bir kelime metinde gecmiyor."
        else:
            return count
dosya = Dosya()
print("""
****************
Dosya işlemlerine hoş geldiniz...
Çıkmak için 'q' ya basabilirsiniz.
Islemler:
1-)Yazdiginiz kelime kac defa geciyor.
""")
while True:
    islem = input("Yapmak istediginiz islemi secin: ")
    if islem == "q":
        time.sleep(0.2)
        print("Cikiliyor...")
        time.sleep(0.5)
        break
    elif islem == "1":
        a = input("Hangi kelime: ")
        donenDeger = dosya.findWord()
        print("{} kelimesi {} defa geciyor.".format(a,donenDeger))
    elif islem == "2":
        print("Her kelimenin ne kadar gectiginin tamamini gormek istiyorsaniz bekleyin: ")
        time.sleep(2.5)
        dosya.kelimeFrekansi()
    else:
        print("Gecersiz deger girildi.")