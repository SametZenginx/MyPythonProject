print("Player Registration Program")

ad = input("Player's Name: ")
soyad = input("Player's Surname: ")
takim = input("Player's team: ")

bilgiler = [ad,soyad,takim]

print("Saving Information...")

print("Player's Name: {}\nPlayer's Surname: {}\nPlayer's Team: {}\n".format (bilgiler[0],bilgiler[1],bilgiler[2]))

print ("Information Saved.")
