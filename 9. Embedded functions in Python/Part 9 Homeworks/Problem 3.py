from functools import reduce

liste = [1,2,3,4,5,6,7,8,9,10]

def ciftMi(x):
    return x%2 == 0

filtrelenmisSayilar = list(filter(ciftMi,liste))

print(reduce(lambda x,y : x+y,filtrelenmisSayilar))