def primenumbs(x):
    counters = 0
    if x == 1:
        return False
    elif x > 1:
        for i in range(2,x):
            if x % i == 0:
                counters += 1
        if counters == 0:
            return True
        else:
            return False
while True:
    x = input("Enter the number find out whether it is prime or not, Type quit to exit : ")
    x = x.lower()
    if (x == "quit"):
        print("Exiting...")
        break
    else:
        x = int(x)
        a = primenumbs(x)
        if a == True:
            print("Prime Number")
        else:
            print("Not prime number")