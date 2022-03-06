#Calculate the body mass index according to the height and weight values obtained from the user and print the following texts on the screen according to these rules.

print("Enter your height(m) and weight(kg), let's calculate your body mass index and whether you are underweight or overweight : ")

height = float(input("Height = "))
weight = float(input("Weight = "))

bodymassindex = weight / (height *height)

if (bodymassindex < 18.5):
    print("Underweight")
elif (bodymassindex >= 18.5) and (bodymassindex < 25):
    print("Normal")
elif (bodymassindex < 30) and (bodymassindex >= 25):
    print("Overweight")
else:
    print("Obese")

