liste = [(3,4,5),(6,8,10),(3,10,7)]

def ucgenMi(liste):
    if liste[0] + liste[1] > liste[2] and liste[0] + liste[2] > liste[1] and liste[1] + liste[2] > liste[0]:
        return True
    else:
        return False

print(list(filter(ucgenMi,liste)))