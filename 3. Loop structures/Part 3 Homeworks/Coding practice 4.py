'''
Get a number from the user in each while loop

and add the user-entered numbers to a variable named "sum".

When the user presses the "q" key, end the loop and display the

print the "sum variable".
'''
sum = 0

while True:
    numb = input("Enter the number(Type 'q' for exit.): ")
    if (numb == "q"):
        break
    numb = int(numb)
    sum += numb
print("The sum of the numbers you entered =",sum)



