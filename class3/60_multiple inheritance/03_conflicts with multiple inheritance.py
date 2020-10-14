class A:  
    def __init__(self):  
        self.name = 'Bob'  
   
class B:  
    def __init__(self):  
        self.name = 'Alice'  
  
  
class C(A, B):  
    def __init__(self):  
        A.__init__(self)  
        B.__init__(self)  
  
    def getName(self):  
        return self.name  


class D(A, B):  
    def __init__(self): 
        B.__init__(self)   
        A.__init__(self)  
 
    def getName(self):  
        return self.name 


c1 = C()  
print(c1.getName())  # --> Alice

d1 = D()  
print(d1.getName())  # --> Bob