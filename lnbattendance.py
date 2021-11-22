
print("Enter number of employees e(1<=e<=10):")
e=int(input())

print("Enter number of working days w(1<=w<=31):")
w=int(input())

print("Enter the attendance details of",e,"employees for",w,"days \
in string format seperating each day's log with a space\
(P denotes present and A denotes absent)")
x=str(input())
L1=list(x.split())


p="P"*e
a=[]

for i in range(0,w):
    if(L1[i]==p):
        a.append(i+1)

print("Days recording full attendance are days:",a)

        
    
    

