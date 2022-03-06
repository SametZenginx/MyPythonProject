onesdigit =  ["","Bir","İki","Üç","Dört","Beş","Alti","Yedi","Sekiz","Dokuz"]
tensdigit = ["","On","Yirmi","Otuz","Kirk","Elli","Altmiş","Yetmiş","Seksen","Doksan"]
def reads(Nums):
    Once = Nums % 10
    Twice = Nums // 10

    return tensdigit[Twice] + " " + onesdigit[Once]

Nums = int(input("Number : "))

print(reads(Nums))

