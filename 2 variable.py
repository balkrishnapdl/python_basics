# x=5
# y="Ishwor"
# print(x)
# print(y)


# F="Orange"
# N="Ishwor Poudel"
# print("My favourite fruit is",F)
# print("My name is",N)


# x=4
# x="Sally"
# print(x)  # here x is first assigned as the integer type after that it is assigned and stored as the string type.



## casting to assign the type and type command in the print to know the type of the variable.
# x=str(3)
# y=int(3)
# z=float(3)
# a=5
# b="Ishwor"
# print("\nThe string looks like",x)
# print("The integer looks like",y)
# print("The float looks like",z)
# print("The type of the variable a is",type(a))
# print("The type of the variable b is",type(b))


## Declaration of the string variable and the case sensitibve variable are different
# a='Michael'
# A='Jackson'
# print(a,A)

## Legal variable name
# myvar="Michael"
# my_var="Jackson"
# _my_var="is"
# myVar='my'
# MYAVR='favourite'
# myvar2="Actor"  
# print(_my_var)

# # Illegal variable name
# 2myvar='john'
# my-var="Hello"
# my var=5
# print("2myvar")

## Multiwords variable name
#A. Camel case = myVariableName
#B. Pascal Case = MyVariableName
#C. Snake Case= my_variable_name

### ASSIGN MULTIPLE VARIABLES
## Many Values to Multiple Variables
# x, y, z='Orange','Apple','Banana'
# print( x,y,z)

## One value to the multiple variable 
# x=y=z="Fruits"
# print(x,y,z)

## Unpacking the collection of the variable 
# fruits = ("apple",'orange','mango')
# x,y,z=fruits
# print(x,y,z)

## simple print of the variable
# x= " Python is awesome "
# print(x)

# x='python'
# y='is'
# z='awesome'
# print(x,y,z)


# x='python'
# y='is'
# z='awesome'
# print(x+y+z)

# x='python'
# y='is'
# z='awesome'
# print(x + y + z)


# x=5
# y=10
# print(x+y)

### GLOBAL AND LOCAL VARIABLE
## Global Variable
# x='awesome'

# def myfunc():
#     print("Python is:"+x)

# myfunc()
# print("Python is",x)

##local Variable
# x='awesome'
# def myfunc():
#     x='AWESOME'
#     print("PYTHON IS",x)

# myfunc()
# print("python is",x)
# exit()

### making variable global inside the function or changing the global variable
#declaring the global variable inside the function 
# def myfunc():
#     global x
#     x='awesome'
# myfunc()
# print("python is " +x)
# exit()

#Changing the global variable inside the function 
# x='awesome'
# print("python is f",x)
# def myfunc():
#     global x
#     x='fanstastic'
#     print("Python is",x)
# myfunc()
# print("python is",x)
# exit()