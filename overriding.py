class A:
    z=10
    def add(self,x,y):
        self.p=10
        print(x+y+self.z+self.p)
    def sub(self,x,y):
        print(x-y+self.z)
class B(A):
    def add(self,x,y):
        print(x*y*self.z)
    def sub(self,x,y):
        print(x/y)

obj=B()
obj.add(10,5)
obj.sub(10,5)