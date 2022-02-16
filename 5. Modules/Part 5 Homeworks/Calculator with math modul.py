import math
import time
import SametsModul
print("""
Welcome to the calculator with which you can make most of the calculations you want.
1.Factorial
2.Trigonometry
3.Exponential Number
4.Sqrt
5.Addition
6.Subtraction
7.Multiplication
8.Division
9.Logarithm
""")

a = input("Select the mathematical operation you will do: ")
if a == "1":
    Numb1 = int(input("Enter the Number(Greater than 0): "))
    print("Calculating...")
    time.sleep(1)
    print(math.factorial(Numb1))
elif a == "2":
    print("""
    1.Sin
    2.Cos
    3.Tan
    4.Cot 
    """)
    b = input("Choose one: ")
    if b == "1":
        Numb1 = int(input("Enter the number. sin"))
        print("Calculating...")
        time.sleep(1)
        print("in radians:",math.sin(Numb1),"pi")
    elif b == "2":
        Numb1 = int(input("Enter the number. cos"))
        print("Calculating...")
        time.sleep(1)
        print("in radians:",math.cos(Numb1),"pi")
    elif b == "3":
        Numb1 = int(input("Enter the number. tan"))
        print("Calculating...")
        time.sleep(1)
        print("in radians:",math.tan(Numb1),"pi")
    elif b == "4":
        Numb1 = int(input("Enter the number. cot"))
        print("Calculating...")
        time.sleep(1)
        print("in radians:",math.cot(Numb1))
    else:
        print("Invalid option.")
elif a == "3":
    Numb1 = int(input("Choose number: "))
    Numb2 = int(input("Choose it's multiple: "))
    print("Calculating...")
    time.sleep(1)
    print(SametsModul.Exponential(Numb1,Numb2))
elif a == "4":
    Numb1 = int(input("Choose number: "))
    print("Calculating...")
    time.sleep(1)
    print(math.sqrt(Numb1))
elif a == "5":
    Numb1 = float(input("Enter the Number-1: "))
    Numb2 = float(input("Enter the Number-2: "))
    print("Calculating...")
    time.sleep(1)
    print(SametsModul.Addition(Numb1,Numb2))
elif a == "6":
    Numb1 = float(input("Enter the Number-1: "))
    Numb2 = float(input("Enter the Number-2: "))
    print("Calculating...")
    time.sleep(1)
    print(SametsModul.Division(Numb1,Numb2))
elif a == "7":
    Numb1 = float(input("Enter the Number-1: "))
    Numb2 = float(input("Enter the Number-2: "))
    print("Calculating...")
    time.sleep(1)
    print(SametsModul.Multiplication(Numb1,Numb2))
elif a == "8":
    Numb1 = float(input("Enter the Number-1: "))
    Numb2 = float(input("Enter the Number-2: "))
    print("Calculating...")
    time.sleep(1)
    print(SametsModul.Multiplication(Numb1,Numb2))
elif a == "9":
    print("Reminder: x in ln(x) has to be x>0.")
    time.sleep(1)
    Numb1 = float(input("Enter numbers into ln(x):"))
    time.sleep(1)
    print(math.log(Numb1))
else:
    print("Invalid option.")