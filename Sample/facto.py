def sumoffact(n):
    x=0
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        if(i%2!=0):
            x=x+(i/fact)
    return x
a=int(input("Enter the Number"))
print("Sum of factorial",sumoffact(a))
        
