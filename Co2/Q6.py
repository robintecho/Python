a=input("Enter the String")
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1

print("",str(b))
