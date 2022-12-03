# def my_function():
#     print("Hello from a function!")
# my_function()

###passing an arguments into the function 
# def my_function(fname):
#     print(fname+"\t Refsnes")
# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

### passing same number of arguments in the function while calling and defining the function.
# def my_function(fname,lname):
#     print(fname+" "+ lname)
# my_function("Ishwor","Poudel")

### Arbitary arguments, *args
# def my_function(*kids):
#     print("The youngest child is " +kids[2])
# my_function("Ishwor","ram",'Shyam')

### Keyword Arguments
# def my_function(child3, child2, child1):
#     print("The youngest child is "+ child3)
# my_function(child3='Ram', child2="Hari",child1='Harke')

### Arbitary keyword Arguments,**kwargs
# def my_function(**kid):
#     print("His last name is "+ kid['lname'])
# my_function(fname="Ishwor",lname='Poudel')

### Default Parameter value
# def my_function(country='Norway'):
#     print("I am from "+ country)
# my_function('Sweden')
# my_function("India")
# my_function()
# my_function('Brasil')

###Passing a list as an argument
# def my_function(food):
#     for x in food:
#         print(x)
# fruits=['apple','banana','cherry']
# my_function(fruits)

### Return Values
# def my_function(x):
#     return 5*x
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

###The pass statement
# def my_function():
#     pass

### Recursion Example
# def tri_recursion(k):
#     if (k>0):
#         result=k+tri_recursion(k-1)
#         print(result)
#     else:
#         result=0
#     return result
# print("\n\n Recursion Example Results")
# tri_recursion(6)


