print("""
****************
User Login Programme
****************
""")
sysName = "Mustafa Samet"
sysPassword = "12345"
rightoftrial = 3
while True:
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    if (username != sysName and password == sysPassword):
        rightoftrial -= 1
        print("Wrong username")
    elif (username == sysName and password != sysPassword):
        rightoftrial -= 1
        print("Wrong password")
    elif (username != sysName and password != sysPassword):
        rightoftrial -=1
        print("Wrong username and password")
    else:
        print ("Correctly the username and password. Thanks.")
        break
    if (rightoftrial == 0):
        print("No more trial rights")
