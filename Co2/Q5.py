def part(n):
    for i in range(0,n):
        for j in range(0,i+1):
            x=i+1
            print("",x+(x*j), end="")
        print("\n")
a=int(input("Enter the number:"))
part(a)
