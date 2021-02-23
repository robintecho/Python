def sumoffact(d):
     sum=1
     #print(d)
     for x in range(3,d+1,2):
          n=0
          #print(x)
          #n=x+2
          #print(n)
          temp=x  
          s=1
          for i in range(1,x+1):
               s=s*i
         # print(s)
          g=temp/s
          sum+=g
          
     return sum
a=int(input("Enter the limit:"))
print("Sum of factorial",sumoffact(a))

     
     
     




         
     
         

