answer = input("Want to find a triangle or a quadrilateral? : ")

if answer == "quadrilateral":
    x = int(input("1.Edge: "))
    y = int(input("2.Edge: "))
    z = int(input("3.Edge: "))
    t = int(input("4.Edge: "))
    x = abs(x)
    y = abs(y)
    z = abs(z)
    t = abs(t)
    if x==y and x==z and x==t and y==z and y==t and z==t:
        print("The shape is Square.")
    elif x+y+z <= t or x+y+t <= z or x+t+z <= y or y+z+t <= x :
        print("Quadrilateral conditions are not suitable. There is no such thing.")
    elif (x==z and y==t) or (x==t and y==z):
        print("The shape is Rectangle.")
    else:
        print("The shape is quandrilateral")
elif answer == "triangle":
    a = int(input("1.Edge : "))
    b = int(input("2.Edge : "))
    c = int(input("3.Edge : "))
    a = abs(a)
    b = abs(b)
    c = abs(c)
    if a+b <= c or a+c <= b or b+c <= a:
        print("Triangle conditions are not suitable. There is no such thing.")
    else:
        if (a==b and a != c) or (b==c and b !=a) or (c==a and c != b):
            print("Isosceles triangle.")
        elif (a==b and a==c):
            print("Equilateral triangle.")
        else:
            print("Just triangle.")
else:
    print("You didn't type triangle or quadrilateral...\nTry again.")