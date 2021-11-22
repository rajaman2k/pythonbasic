import numpy as np

print("Enter 5 integers:")

a=[6]
for i in range(1,6):
    print("Enter element at index",i)
    x=int(input())
    a.append(x)

sum=0
for i in range(1,6):
    if (a[i]>9):
        sum=sum+a[i]
    else:
        sum=sum

print("The sum of integers > 9 =",sum)
