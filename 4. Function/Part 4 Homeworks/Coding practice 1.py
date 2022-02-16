'''
Print perfect numbers from 1 to 1000 on the screen. 

For this, write a function that returns whether a number is perfect.

A number is a perfect number if the sum of its divisors is equal to itself. 

For example, 6 is a perfect number (1 + 2 + 3 = 6).
'''
def perfectNums(Num):
    counter = 0
    for x in range(1,Num):
        if (Num % x == 0):
            counter += x
    return counter == Num
for i in range(1,1001):
    if perfectNums(i):
        print(i," Perfect Number.")





        




    