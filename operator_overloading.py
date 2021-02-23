class A:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=A(m1,m2)
        return s3
s1=A(3,4)
s2=A(4,7)
s3=s1+s2
print(s3)
