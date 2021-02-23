p=int(input("Enter range from:"))
g=int(input("Enter range to:"))
a=[]
for i in range(p,g+1):
    if i%2==0 and i**2:
        a.append(i)
print(a)
