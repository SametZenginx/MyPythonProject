print("""This is a calculator.

1.  Addition   
2.  Subtraction
3.  Multiplication
4.  Division

Enter the numbers first, then the operation.

""")

a = int(input("1.Number: "))
b = int(input("2.Number: "))

operation = input("Operation(1,2,3,4): ")

if operation == "1":
    print("Sum of {} and {} is {}".format(a, b, a + b))
elif operation =="2":
    print("Difference of {} and {} is {}".format(a, b, a - b))
elif operation == "3":
    print("Multiplication of {} and {} is {}".format(a, b, a * b))
elif operation == "4":
    print("Division of {] and {} is {}".format(a, b, a / b))
else:
    print("The operation is invalid.")
