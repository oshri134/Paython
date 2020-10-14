class A:  
    def __init__(self):  
        self.name = 'Bob' 
  
  
class B:  
    def __init__(self):  
        self.age = 45 
  
  
class C(A, B):    
    def get_name(self):  
        return self.name
    
    def get_age(self):  
        return self.age



c1 = C()  
print(c1.get_name())  # --> Bob
print(c1.get_age())   # --> RunTime Error: AttributeError: 'C' object has no attribute 'age'