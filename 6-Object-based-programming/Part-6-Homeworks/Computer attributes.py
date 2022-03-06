import time

class Computer():

    def __init__(self,pcAdi = "Bilgi yok",pcCekirdek = 0,pcRam = 0,pcEkrankart = "Bilgi yok",pcRenk = "Bilgi yok"):

        self.pcAdi = pcAdi
        self.pcCekirdek = pcCekirdek
        self.pcRam = pcRam
        self.pcEkrankart = pcEkrankart
        self.pcRenk = pcRenk

    def pcEkle(self):

        a = input("Eklemek istediginiz pc'nin Adini giriniz: ")
        time.sleep(0.5)
        print("Bilgi kaydediliyor.")
        time.sleep(0.5)
        b = input("Eklemek istediginiz pc'nin Cekirdek sayisini giriniz: ")
        time.sleep(0.5)
        print("Bilgi kaydediliyor.")
        time.sleep(0.5)
        c = input("Eklemek istediginiz pc'nin Ramini giriniz: ")
        time.sleep(0.5)
        print("Bilgi kaydediliyor.")
        time.sleep(0.5)
        d = input("Eklemek istediginiz pc'nin Ekrankartinin adini giriniz: ")
        time.sleep(0.5)
        print("Bilgi kaydediliyor")
        time.sleep(0.5)
        e = input("Eklemek istediginiz pc'nin Rengini giriniz: ")
        time.sleep(0.5)
        print("Bilgi kaydediliyor")
        time.sleep(0.5)

        pc.pcAdi = a
        pc.pcCekirdek = b
        pc.pcRam = c
        pc.pcEkrankart = d
        pc.pcRenk = e
        

    def __str__(self):
        return "PC Adi: {}\nPC Cekirdegi: {}\nPC Rami: {}\nPC Ekran Karti: {}\nPC Rengi: {}".format(self.pcAdi,self.pcCekirdek,self.pcRam,self.pcEkrankart,self.pcRenk)
    
    def __len__(self):
        return self.pcAdi
    
    def __del__(self):

        print("Pc siliniyor.")

        time.sleep(0.3)

    def pcramArttirma(self):
        sum = float(input("Rami eskisine gore ne kadar arttirdiniz? : "))
        print("Bilgi kaydediliyor.")
        self.pcRam += sum
        time.sleep(0.4)
        print("Bilgi kaydedildi. Artik raminiz: ",self.pcRam)

pc1 = Computer("Monster",8,8,"Nvidia Geforce GTX 1080","Siyah")
pc2 = Computer("Asus Tuf Gaming",8,16,"Nvidia Geforce GTX 1650","Siyah")
pc3 = Computer("Asus Rog Gaming",8,12,"Amd RX 560","Kirmizi")

pc = Computer()

print("""
Bilgisayarlarla ilgili bilgilerin oldugu uygulamaya hos geldiniz.
1-) Pc eklemek
2-) Sectigin bir bilgisayarin ozelliklerine bakmak
3-) Sectigin bir bilgisayari sistemden silmek
4-) PC ram arttirma
Cikmak icin 'q' yazin.
""")


pcListe = [pc1.pcAdi,pc2.pcAdi,pc3.pcAdi,pc.pcAdi]

while True:
    islem = input("Yapmak istediginiz islemi secin: ")
    if islem == "q":
        print("Uygulamadan cikiliyor...")
        time.sleep(0.4)
        break
    elif islem == "1":
        print("Pc ekleme yerine hos geldiniz... Lütfen bekleyin.")
        time.sleep(0.5)
        pc.pcEkle()
    elif islem == "2":
        x = input("Bilgi edinmek istedigin bilgisayarin markasini gir(kucuk harflerle): ")
        x = x.lower()
        if x == "monster":
            print(pc1)
        elif x == "asus tuf gaming":
            print(pc2)
        elif x == "asus rog gaming":
            print(pc3)
        else:
            print(pc)
    elif islem == "3":
        print(pcListe)

        xx = input("Yukaridan silmek istediginiz pcnin adini giriniz.")

        xx = xx.lower()

        if xx == "monster":
            pc1.__del__()
            del pc1.pcAdi,pc1.pcCekirdek,pc1.pcRam,pc1.pcEkrankart,pc1.pcRenk
            pcListe.remove("Monster")
        elif xx == "asus tuf gaming":
            pc2.__del__()
            del pc2.pcAdi,pc2.pcCekirdek,pc2.pcRam,pc2.pcEkrankart,pc2.pcRenk
            pcListe.remove("Asus Tuf Gaming")
        else:
            pc3.__del__()
            del pc3.pcAdi,pc3.pcCekirdek,pc3.pcRam,pc3.pcEkrankart,pc3.pcRenk
            pcListe.remove("Asus Rog Gaming")
        print(pcListe)

    elif islem == "4":
        print(pcListe)
        xxx = input("Ramini arttiracagin pcyi yaz: ")
        xxx = xxx.lower()
        if xxx == "monster":
            pc1.pcramArttirma()

        elif xxx == "asus tuf gaming":
            pc2.pcramArttirma()

        else:
            pc3.pcramArttirma()

    else:
        print("Gecersiz islem.")

    