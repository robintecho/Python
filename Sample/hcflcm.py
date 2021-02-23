def hcf(x,y):
    if x>y:
        smaller=x
    else:
        smaller=y
    for i in range(1,smaller+1):
        if((x%i==0)and(y%i==0)):
            hcf=i
    return hcf

def lcm(z,u):
    if z>u:
        greater=z
    else:
        greater=u
    while(True):
        if((greater%z==0)and(greater%u==0)):
            lcm=greater
            break
        greater+=1
    return lcm

num1=int(input("Enter the 1 number:"))
num2=int(input("Enter the 2 number:"))
print("HCF",hcf(num1,num2))
print("LCM",lcm(num1,num2))
