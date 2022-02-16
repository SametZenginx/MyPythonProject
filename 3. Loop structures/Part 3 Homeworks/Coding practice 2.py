'''
Try to find out if a number you received from the user is the "Armstrong" number.

For example, if a number has 4 digits and each of its constituent digits
If the sum of the 4th power (3rd power for 3-digit numbers) is equal to that number
this number is called the "Armstrong" number.

For example: 1634 = 1^4 + 6^4 + 3^4 + 4^4
'''

numb = input("Enter the number you want to know if it is an Armstrong number: ")
numbOfdigit = len(numb)
numb = int(numb)
sum = 0
numbInloop = numb

while (numbInloop > 0):
    digitInnumb = numbInloop % 10
    sum += digitInnumb ** numbOfdigit
    numbInloop = numbInloop // 10
if sum == numb:
    print("The number {} is the Armstrong number.".format(numb))
else:
    print("The number {} is not the Armstrong number.".format(numb))

