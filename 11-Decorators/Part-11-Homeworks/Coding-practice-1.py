
def ekstra(func):


    def perfectNumbs():
        print("Perfect Numbs:")
        for numb in range(2,1001):
            toplam = 0
            i = 1
            while i<numb:
                if numb%i == 0:
                    toplam += i
                i+=1
            if toplam==numb:
                print(numb)
        
        func()

    return perfectNumbs

@ekstra
def primeNumbers():
    print("Prime Numbs: ")

    for numb in range(2,1001):
        i = 2
        count = 0
        while (i<numb):
            if numb%i == 0:
                count += 1
            i+=1
        if count == 0:
            print(numb)

primeNumbers()

