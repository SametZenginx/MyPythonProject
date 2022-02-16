def finddivisors(numb):
    dividerlist = []
    for x in range(1,numb+1):
        if numb % x == 0:
            dividerlist.append(x)
    dividerlist.reverse()  
    return dividerlist
while True:
    numb = input("Enter the number for which you want the divisors to be found, type 'quit' to exit. : ")
    numb = numb.lower()
    if numb == "quit":
        print("Exiting...")
        break
    else:
        numb = int(numb)
        control = finddivisors(numb)
        print("Divider List is ",control)


    