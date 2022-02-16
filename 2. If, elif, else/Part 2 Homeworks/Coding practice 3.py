# Calculate the letter grade according to the grades of the user's MidTerm exam1, MidTerm exam2, final grades.

print("Enter the grade for Midterm 1, Midterm 2 and Final. Let's calculate the letter grade.")

midterm1 = float(input("MidTerm1: "))
midterm2 = float(input("MidTerm2: "))
final = float(input("Final: "))

lettergrade = midterm1*0.3 + midterm2*0.3 + final*0.4

if lettergrade >= 90:
    print("AA")
elif lettergrade < 90 and lettergrade >=85:
    print("BA")
elif lettergrade < 85 and lettergrade >=80:
    print("BB")
elif lettergrade < 80 and lettergrade >=75:
    print("CB")
elif lettergrade < 75 and lettergrade >=70:
    print("CC")
elif lettergrade < 70 and lettergrade >=65:
    print("DC")
elif lettergrade < 65 and lettergrade >=60:
    print("DD")
elif lettergrade < 60 and lettergrade >=55:
    print("FD")
else:
    print("FF")
