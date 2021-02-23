for x in range(1,500):
        sum=0
        temp=x
        while temp>0:
            di=temp%10
            sum+=di**3
            temp//=10

        if x==sum:
            print(x)


