def perfect(n):
    sum=0
    for x in range(1,n):
        
        if n%x==0: 
            sum+=x
    return sum==n
a=int(input("Enter the number"))
print(perfect(a))
    
