'''
Try to print a multiplication table with numbers from 1 to 10. 

Hint: Use 2 nested for loops. 

Also get the numbers using the range() function.
'''
for firstLayer in range(1,11):
    print("**********************")
    for secondLayer in range(1,11):
        print("{} x {} = {}".format(firstLayer,secondLayer,firstLayer*secondLayer))