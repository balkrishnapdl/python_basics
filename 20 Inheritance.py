### Creating the parent class
# class Person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def printname(s):
#         print(s.firstname,s.lastname)
# p1=Person("Ishwor","Poudel")
# Person.printname(p1)

### Creating the child class 
# class Person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def myfunc(abc):
#         print("My name is",abc.firstname,abc.lastname)
# p1=Person("Ishwor","Poudel")
# Person.myfunc(p1)
# class student(Person):     ### child class that inherits all the method of the parent class.
#     pass
# student.myfunc(p1)

### Another Example of child class
# class Person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname
#     def myfunc(abc):
#         print("My name is ",abc.firstname,abc.lastname)
# class student(Person):
#     pass
# p1=Person("Ishwor ","Poudel")
# Person.myfunc(p1)
# s1=student("Balkrishna","Poudel")
# student.myfunc(s1)

### Adding the __init__() function to the child class
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def myfunc(abc):
#         print("My name is ",abc.name)
#         print(f"I am {abc.age} years old")
# p1=Person("Ishwor Poudel",20)
# Person.myfunc(p1)
# class Student(Person):
#     def __init__(self,sname,sage):### If we add only this line to the child class than the methods of the parent class will be overrriden by thethis method but...
#         Person.__init__(self,sname,sage)### Calling the parent's __init__() funtion brings back the method of the parent class
# s1=Student("Balkrishna Poudel",22)
# Student.myfunc(s1)

### Using the super() function
# class Person:
#     def __init__(self,name,age):
#         self.name=name 
#         self.age=age
#     def myfunc(abc):
#         print("My name is ",abc.name)
#         print(f"I am {abc.age} years old")  
# p1=Person("Ishwor Poudel",22)
# Person.myfunc(p1)
# class Student(Person):
#     def __init__(self,sname,sage):
#         super().__init__(sname,sage)
# s1=Student("Balkrishna Poudel",20)
# Student.myfunc(s1)

### Adding Properties
##Example1 
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def myfunc(abc):
#         print("My name is ",abc.name)
#         print(f"I am {abc.age} years old")
# p1=Person("Ishwor Poudel",22)
# Person.myfunc(p1)
# class Student(Person):
#     def __init__(self,sname,sage):
#         super().__init__(sname,sage)
#         self.syear=2022
#         print(f"I grauated in the year{self.syear}")
# s1=Student("Balkrishna podel",25) 
# Student.myfunc(s1)    

###Example 2
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def myfunc(abc):
#         print("My name is ",abc.name)
#         print(f"I am {abc.age} years old")
# p1=Person("Ishwor Poudel",22)
# Person.myfunc(p1)
# class Student(Person):
#     def __init__(self,sname,sage,year):
#         super().__init__(sname,sage)
#         self.graduationyear=year
#         print(f"I graduated in the year{self.graduationyear}")
# s1=Student("Balkrishna Poudel",20,2025)
# Student.myfunc(s1)

###Adding methods
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def myfunc(abc):
#         print("My name is ",abc.name)
#         print(f"I am {abc.age} years old")
# p1=Person("Ishwor Poudel",20)
# Person.myfunc(p1)
# class Student(Person):
#     def __init__(self, name, age,year):
#         super().__init__(name, age)
#         self.graduationyear=year
#     def welcome(self):
#         print(f"Welcome {self.name} to the class of {self.graduationyear}")
# s1=Student("Balkrishna Poudel",25,2025)
# Student.welcome(s1)
