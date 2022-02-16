# Write a function that prints the numbers from
# 1 to 100 forming a pythagorean triangle.(a <= 100,b <= 100)
def findPythagoras():
    pythagorasList = []
    for x in range(1,101):
        for y in range(1,101):
            c = (x**2 + y**2) ** 0.5

            if (c == int(c)):
                pythagorasList.append([x,y,int(c)])
    return pythagorasList
for i in findPythagoras():
    print(i)
