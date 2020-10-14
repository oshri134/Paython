class Person:
    pass


class SchoolMember(Person):
    pass


class Student(SchoolMember):
    pass


"""
    __bases__ is a tuple. The tuple contains classes (not class names) which are direct superclasses for the class

    Note: only classes have this attribute - objects don't.

    Note: a class without explicit superclasses points to object (a predefined Python class) as its direct ancestor.

"""
print(Person.__bases__)
print(SchoolMember.__bases__)
print(Student.__bases__)


