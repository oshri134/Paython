"""
the situation in which the subclass is able to modify its superclass behavior is called polymorphism. 
which means that one and the same class can take various forms depending on the redefinitions done by any of its subclasses.
polymorphism helps the developer to keep the code clean and consistent.
"""

class SchoolMember:
    def tell(self):
        print("hello SchoolMember")

    def start(self):
        self.tell()

class Teacher(SchoolMember):
    def tell(self):
        print("hello Teacher")



m = SchoolMember()
t = Teacher()

t.start()
m.start()


"""
OUTPUT:
____________________________________

hello Teacher
hello SchoolMember

"""
