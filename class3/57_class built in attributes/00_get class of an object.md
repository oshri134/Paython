# finding the class of a particular object
If you want to find the class of a particular object, you can use:
* a function named type(), which is able to find a class which has been used to instantiate any object.
* using attributes `__class__` that is automatically added to an object on creation and stores the type object

for example:
```
class Person:
    pass

p1=Person

print((type(p1)).__bases__)
print(p1.__class__.__bases__)

```