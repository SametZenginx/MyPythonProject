'''

Print only the numbers divisible by 3 from the numbers from 1 to 100.
Try to do this with 'continue'.

'''

for x in range(1,101):
    if (x % 3 != 0):
        continue
    else:
        print(x)
