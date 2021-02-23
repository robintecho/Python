def decimaltobinary(num):
    if num >=1:
       
        decimaltobinary(num//2)
        print(num % 2)
        
        
        
a=int(input("Enter the character:->"))
decimaltobinary(a)
    
