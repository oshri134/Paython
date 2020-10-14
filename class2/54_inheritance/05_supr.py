class SchoolMember:
    def __init__(self, name):
        self.name = name

    def tell(self):
        print('hello SchoolMember',self.name, end=" ")

# If subclass contains a constructor
# The subclass must call to the base constructor
class Teacher(SchoolMember):

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def tell(self):
        super().tell()
        print('and Teacher',self.salary)


m = SchoolMember("Bob")
t = Teacher("Alice",200)

t.tell()
m.tell()


"""
OUTPUT:
____________________________________

hello SchoolMember Alice and Teacher 200
hello SchoolMember Bob

"""
