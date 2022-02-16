print("""
********************


Factorial Finding Program


Press 'q' to exit.

********************
""")
while True:
    numb = input("Enter the number: ")
    if numb == "q":
        print("Exiting...")
        break
    else:
        numb = int(numb)
        fact = 1
        for x in range(2,numb+1):
            fact *= x
        print("The result of {}! is = {}.".format(numb,fact))




