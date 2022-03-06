def tekCift(sayi):

    if sayi%2 == 0:
        return sayi
    else:
        raise ValueError

Liste = [1,2,3,4,5,6,7,8,9,12]

for x in Liste:

    try:
        print(tekCift(x))
    except:
        pass
