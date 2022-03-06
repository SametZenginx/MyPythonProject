print("""
*************************
Welcome to ATM Machine.

Transactions;

1. Balance Inquiry

2. Deposit

3. Withdrawal

Press 'q' to exit the program.
*************************
""")

balance = 1000

while True:
    işlem = input("Enter the action to be taken: ")
    if (işlem == "q"):
        print("We are waiting for you again...")
        break
    elif (işlem == "1"):
        print ("Your balance: {}".format(balance))
    elif (işlem == "2"):
        miktar = int(input("Yatiracağiniz miktari giriniz: "))
        balance += miktar
        print("Remanining balance: {}".format(balance))
    elif (işlem == "3"):
        cekmiktar = int(input("Enter the amount to withdraw from your account: "))
        if (cekmiktar >= balance):
            print("The money you withdraw is more than the money in your account. Unsuccessful.")
            continue
        balance -= cekmiktar
        print("Get your money, Your remaining balance: {}".format(balance))
    else:
        print("Invalid transaction...")
