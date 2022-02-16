print("Enter ax^2 +bx +c and we'll get you find its roots: ")

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

delta = b ** 2 - 4 * a * c
x1 = (-b -delta**0.5) / (2*a)
x2 = (-b +delta**0.5) / (2*a)

print("Calculating...")

print("First root: {}\nSecond root: {}".format(x1,x2))
