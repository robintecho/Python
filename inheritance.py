class A():
    def feature(self):
        print("Feature1")
class B():
    def feature1(self):
        print("feature2")
class C(A,B):
    def feat(self):
        print("feature2")
    
ob1=C()
ob1.feature()
