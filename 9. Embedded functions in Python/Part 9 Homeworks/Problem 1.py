liste = [(3,4),(10,3),(5,6),(1,9)]

def dikAlan(listes):
    return listes[0] * listes[1]

print(list(map(dikAlan,liste)))