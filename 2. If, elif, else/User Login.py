print("""************
User login
************
""")

sysUsername = "Mustafa Samet"
sysPassword = "12345"

Username = input("AccountName : ")
Password = input("Password : ")

if sysUsername == Username and sysPassword != Password:
    print("Password is incorrent.")

elif sysUsername != Username and sysPassword == Password:
    print("Username is incorrent.")

elif sysUsername != Username and sysPassword != Password:
    print("Username and Password are incorrent.")

else:
    print("Login Successful")

