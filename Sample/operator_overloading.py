class A:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=A(m1,m2)
        return s3
    def __gt__(self,other):
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if r1>r2:
            return True
        else:
            return False
s1=A(9,4)
s2=A(4,7)
s3=s1+s2
print(s3.m1)
if s1>s2:
    print("s1 is greater")
else:
    print("s2 is greater")
