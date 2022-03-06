'''
Write a function that takes 2 numbers from the user 
and returns the greatest common divisor (EBOB) of these numbers.
'''
def findEbob(Num1,Num2):
    i = 1
    ebob = 1
    while (i <= Num1 and i <= Num2):
        if (not(Num1 % i) and not(Num2 % i)):
            ebob = i
        i += 1
    return ebob
Num1 = int(input("Num-1: "))
Num2 = int(input("Num-2: "))
print("Ebob: ",findEbob(Num1,Num2))


    
            

