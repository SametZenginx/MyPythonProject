print("How much fuel does your car burn per kilometer ?")

Fuel = float(input("Fuel : "))

print("How many kilometers did you travel with your vehicle?")

Kilometers = float(input("Kilometers : "))

Totalamount =  Fuel * Kilometers

print("Amount you have to pay: {}TL".format(Totalamount))