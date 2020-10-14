class A:  
    def __init__(self):  
        self.name = 'Bob' 
  
  
class B:  
    def __init__(self):  
        self.age = 45 
  
  
class C(A, B): 
    def __init__(self):  
        A.__init__(self)  
        B.__init__(self)  

    def get_name(self):  
        return self.name
    
    def get_age(self):  
        return self.age



c1 = C()  
print(c1.get_name())  # --> Bob
print(c1.get_age())   # --> 45