'''
We will write fibonacci with for.
Itt goes like fibonacci = 1 1 2 3 5 8 13...
'''

a = 1
b = 1

fibonacci = [a,b]

for x in range(20):
    a,b = b,a+b
    print("a: {} b: {}".format(a,b))
    fibonacci.append(b)

print(fibonacci)