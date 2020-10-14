# Reflection and introspection
* introspection, which is the ability of a program to examine the type or properties of an object at runtime
* reflection, which goes a step further, and is the ability of a program to manipulate the values, properties or functions of an object at runtime

NOTE: Introspection is passive, the purpose is to examine; Reflection is active, and it’s not only able examine, but also to modify.


## usefull reflection functions 
- hasattr(obj,'') - finds out if a class variable is available, The function returns True if the specified class contains a given attribute, and False otherwise.
 - dir(obj) — Returns all the attributes and methods of an object in a list.
 - vars(obj) — Returns all the instance variables of an object in a dictionary.
## usefull introspection functions
 - getattr() takes two arguments: an object, and its property name (as a string), and returns the current attribute's value
 - setattr() - takes three arguments: an object, the property name (as a string), and the property's new value.
 
