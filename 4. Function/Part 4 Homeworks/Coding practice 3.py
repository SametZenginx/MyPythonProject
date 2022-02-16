'''
Write a function that takes 2 numbers from the user and returns
the least common multiple of these numbers.
'''
def findEkok(Num1,Num2):
    i = 2
    ekok = 1
    while True:
        if (Num1 % i == 0 and Num2 % i == 0):
            ekok *= i
            Num1 //= i
            Num2 //= i
        elif (Num1 % i == 0 and Num2 % i != 0):
            ekok *= i
            Num1 //= i
        elif (Num1 % i != 0 and Num2 % i == 0):
            ekok *= i
            Num2 //= i
        else:
            i+=1
        if (Num1 == 1 and Num2 == 1):
            break
    return ekok
Num1 = int(input("Num-1 = "))
Num2 = int(input("Num-2 = "))   
print("Ekok : ",findEkok(Num1,Num2))
