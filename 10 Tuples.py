# thistuple=('apple','banana','cherry')
# print(thistuple)

# thistuple=('apple','banana','cherry','apple','cherry') #Though tuples items arenot changeable, it allows duplicate value
# print(thistuple)

# thistuple=('apple','banana','cherry')
# print(len(thistuple))

# thistuple=('apple',)
# print(type(thistuple))
# #Not a tuple
# thistuple=('apple')
# print(type(thistuple))

# tuple1=("apple",'banana','cherry')
# tuple2=(1,5,7,9,3)
# tuple3=(True,False,True)
# print(tuple1)
# print(tuple2)
# print(tuple3)

# tuple1=("abc",34,True,40,'male')
# print(tuple1)

### type of the tuple
# mytuple=('apple','banana','cherry')
# print(type(mytuple))

### The tuple( ) constructor
# thistuple=tuple(('apple','banana','cherry'))
# print(thistuple)

###Acess Tuple item
# thistuple=('apple','banana','cherry')
# print(thistuple[1])

# thistuple=('apple','banana','cherry')
# print(thistuple[-1])

### Range of indexes
# thistuple=("apple",'banana','cherry','orange','kiwi','melon','mango')
# print(thistuple[2:5])

# thistuple=('apple','banana','cherry','orange','kiwi','melon','mango')
# print(thistuple[:4])

# thistuple=('apple','banana','cherry','orange','kiwi','melon','mango')
# print(thistuple[2:])

### Negative indexes
# thistuple=('apple','banana','cherry','orange','kiwi','melon','mango')
# print(thistuple[-4:-1])

# thistuple=('apple','banana','cherry')
# if 'apple' in thistuple:
#     print('Yes,apple is in the fruits tuple')

# thistuple=('apple','mango','banana')
# thislist=list(thistuple)
# thislist[1]="orange"
# thistuple=tuple(thislist)

# print(thistuple)

### ADD ITEMS
##Convert into a list
# thistuple=('apple','banana','cherry')
# thislist=list(thistuple)
# thislist.append('orange')
# thistuple=tuple(thislist)
# print(thistuple)

## Add tuple to tuple
# thistuple1=('apple','banana')
# thistuple=('orange',)
# thistuple1=thistuple1+thistuple
# print(thistuple1)

 ### REMOVE ITEMS
# thistuple=('apple','banana','cherry','mango')
# thislist=list(thistuple)
# thislist.remove('mango')
# thistuple=tuple(thislist)
# print(thistuple)

# thistuple=("apple",'banana','cherry')
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exist

### Unpacking a tuple
# fruits=("apple",'banana','cherry')
# (green,yellow,red)=fruits
# print(green)
# print(yellow)
# print(red)

### Using a asterisk
# fruits=('apple','banana','cherry','mango','kiwi')
# (green,yellow,*red)=fruits
# print(green)
# print(yellow)
# print(red)

# fruits=('apple','mango','banana','papaya','pineapple')
# (green,*yellow,red)=fruits
# print(green)
# print(yellow)
# print(red)

###Loop through a Tuple
# thistuple=('apple','banana','cherry')
# for x in thistuple:
#     print (x)

# thistuple=("apple",'banana','cherry')
# for i in range(len(thistuple)):
#     print(thistuple[i])

### using while to loop the tuple
# thistuple=("apple",'banana','cherry')
# i=0
# while i<len(thistuple):
#     print(thistuple[i])
#     i=i+1

###Join two tuples
# tuple1=('a','b','c')
# tuple2=(1,2,3)
# tuple3=tuple1+tuple2
# print(tuple3)

###Multiply Tuple
# fruits=('apple','banana','cherry')
# mytuple=fruits*2
# print(mytuple)
