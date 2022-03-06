'''
Try to find out if a number you get from the user is perfect.
A number is called a "perfect number" if the sum of its divisors excluding itself is equal to itself.
For example, 6 is a perfect number. (1 + 2 + 3 = 6)
'''
numb = int(input("Enter a number and see if it's a perfect number or not: "))
sum = 0
for x in range(1,numb):
    if numb % x == 0:
        sum += x
if (numb == sum):
    print("{} is a perfect number.".format(numb))
elif (numb != sum):
    print("{} is not a perfect number.".format((numb)))
else:
    print("Please enter a valid positive number.")
