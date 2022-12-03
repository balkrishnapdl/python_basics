### Creating a class
# class Myclass:
#     x=5
#     print(x)
# ram=Myclass()

### Creating an object
# class Myclass:
#     x=5
# p1=Myclass()
# print(p1.x)

### The __init__() function
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=Person("John",36)
# print(p1.name)
# print(p1.age)

### String representstion of an ovject withput the __str__() function.
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=Person("John",36)
# print(p1)

### String representation of an object with the __str__() function.
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"{self.name},{self.age}"
# p1=Person("John",36)
# print(p1)

###Object MEthods
# class Person:
#     def __init__(self,name,age):
#         self.name=name 
#         self.age=age
#     def myfunc(self):
#         print("Hello my name is "+ self.name)
# p1=Person("John",36)
# Person.myfunc(p1) ### The function also can be called as p1.myfunc()

### The self parameter
# class Person:
#     def __init__(mysillyobject,name,age):
#         mysillyobject.name=name
#         mysillyobject.age=age
#     def myfunc(abc):
#         print("Hello my name is "+abc.name)
#         print("I am ",abc.age,"years old.")
# p1=Person("Ishwor",22)
# Person.myfunc(p1)

### modify object properties
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def myfunc(self):
#         print("my name is "+self.name)
#         print(f"I am {self.age} years old.",)
# p1=Person("Ishwor",22)
# p1.age=20
# p1.myfunc()

### Delete object properties
# class Person:
#     def __init__(self,name,age):
#         self.age=age
#         self.name=name
#     def myfunc(abc):
#         print("My name is "+abc.name)
#         print("I am ",abc.age,"years old")
# p1=Person("Ishwor",22)
# del p1.age
# Person.myfunc(p1)

###Deleting the entire object
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def myfunc(abc):
#         print("My name is "+abc.name)
#         print("I am",abc.age,"years old.")
# p1=Person("Ishwor",22)
# del p1
# Person.myfunc(p1)

