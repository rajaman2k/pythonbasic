print("Enter elements for list 1, seperated by a space:")
a=input()
L1=list(a.split(" "))
L1=list(map(int,L1))

print("Enter elements for list 2, seperated by a space:")
a=input()
L2=list(a.split(" "))
L2=list(map(int,L2))

L3=[]

for i in range(0,len(L1),2):
    x=L1[i]
    L3.append(x)

for i in range(1,len(L2),2):
    x=L2[i]
    L3.append(x)

print(L3)        

