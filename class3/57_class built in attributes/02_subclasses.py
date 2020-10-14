class Person:
    pass


class SchoolMember(Person):
    pass


class Student(SchoolMember):
    pass

class Teacher(SchoolMember):
    pass



print(Person.__subclasses__())
print(SchoolMember.__subclasses__())
print(Student.__subclasses__())

