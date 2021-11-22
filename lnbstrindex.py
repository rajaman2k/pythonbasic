print("Input a string of your choice")
a=str(input())

b=len(a)
if(b>7):
    print("Characters at even index:")
    for i in range(0,b,2):
        print(a[i])
if(b<7):
    print("Characters at odd index:")
    for i in range(1,b,2):
        print(a[i])
