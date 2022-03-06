print("Enter two numbers. Let me swap the values of those numbers with each other.")

FirstNumber = int(input("1. :"))
SecondNumber = int(input("2. :"))

FirstNumber,SecondNumber = SecondNumber,FirstNumber

print("First Number ={}\nSecond Number = {}".format(FirstNumber,SecondNumber))