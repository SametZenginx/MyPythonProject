# Get 3 numbers from the user and print the largest number on the screen.

print("Enter three numbers. Let's write the biggest one.")

number1 = float(input("1.Number = "))
number2 = float(input("2.Number = "))
number3 = float(input("3.Number = "))

if number1>number2 and number1>number3:
    print("The largest number is {}".format(number1))
elif number2>number1 and number2>number3:
    print("The largest number is {}".format(number2))
else:
    print("The largest number is {}".format(number3))


