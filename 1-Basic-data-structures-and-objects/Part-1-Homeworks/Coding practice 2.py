print("Enter the height(m) and weight(kg)")

Height = float(input("Height = "))
Weight = int(input("Weight = "))

Bodymassindex = Weight / (Height ** 2)

print("Bodymassindex = {} kg/m^2".format(Bodymassindex))
