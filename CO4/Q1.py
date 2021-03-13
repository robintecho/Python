class rect:
    def area(l,b):
        area=l*b
        print("area of rectangle is",area)
        return
    def peri(l,b):
        peri=2*(l+b)
        print("perimeter is",peri)
        return
l1=int(input("enter the length"))
b1=int(input("enter the breadth"))
rect.area(l1,b1)
rect.peri(l1,b1)