class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day

    def print_date(self):
        print(f"{self.day}.{self.month}.{self.year}")

class Person:
    def __init__(self,name,birth_date):
        self.name=name
        self.birth_date=birth_date


class Teacher(Person):
    def __init__(self,name,birth_date, salary):
        Person.__init__(self,name,birth_date)
        self.salary=salary

d=Date(1900,8,3)
p=Person("Bob",d)
print(p.birth_date.year)

t=Teacher("Alice",d,20000)