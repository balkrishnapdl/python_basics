# thislist=["apple","banana",'cherry']
# print(thislist)

### Lists allow duplicates
# thislist=['apple','banana','cherry','apple','cherry']
# print(thislist)

### List length
# thislist=['apple','bananana','cherry','orange']
# print(len(thislist))

# list1=[1,2,3,4]
# list2=['apple','banana','cherry']
# list3=[True,False,False]
# list4=['abc',34,True,40,'male']
# print(list1)
# print(list2)
# print(list3)
# print(list4)

###Type of list
# mylist=['apple','banana','cherry']
# print(type(mylist))

# thislist=list(('apple','banana','cherry')) # note the double round-bracckets
# print(thislist)

###Access list item 
# thislist=['apple','banana','cherry']
# print(thislist[1])
# print(thislist[-1])

### Range of indexes
# thislist=['apple','banana','cherry','orange','kiwi','melon','mango']
# print(thislist[2:5])
# print(thislist[:4])
# print(thislist[2:])
# print(thislist[-4:-1])

###check if item exist
# thislist=['apple','banana','cherry']
# if'apple'in thislist:
#     print("Yes,'apple' is in the fruits list.")

### Change Item Value
# thislist=['apple','banana','cherry']
# thislist[1]='orange'
# print(thislist)

# thislist=['apple','banana','cherry','orange','kiwi','mango']
# thislist[1:3]=['lemon','grapes']
# print(thislist)

### Inserting more items than you replace 
# thislist=['apple','banana','cherry']
# thislist[1:2]=['blackcurrent','waterlemon']
# print(thislist)

###Inserting less items than you replace
# thislist=['apple','banana','cherry']
# thislist[1:3]=["watermaelon"]
# print(thislist)

###Inserting the new item without changing the existing values
# thislist=['apple','banana','cherry']
# thislist.insert(2,'watermelon')
# print(thislist)

### Appending the item
# thislist=['apple','banana','cherry']
# thislist.append("orange")
# print(thislist)

### Inserting the new item 
# thislist=['apple','banana','cherry']
# thislist.insert(1,'orange')
# print(thislist)

### apExtending the list
# thislist=['apple','banana','cherry']
# tropical=['mango','pineapple','papaya']
# thislist.extend(tropical)
# print(thislist)

### Adding any iterable
# thislist=['apple','banana','cherry']
# thistuple=('kiwi','orange')
# thislist.extend(thistuple)
# print(thislist)

### Removing tthe specified item 
# thislist=['apple','banana','cherry']
# thislist.remove(thislist[0]) # or you can use thislist.remove ("apple")
# print(thislist)

# thislist=['apple','banana','cherry']
# thislist.pop(1)
# print(thislist)

###If you do not specify the index, the pop ( ) method removes the last item.
# thislist=['apple','banana','cherry']
# thislist.pop()
# print(thislist)

# thislist=['apple','banana','cherry']
# del thislist[0]
# print(thislist)

### Using the del keyword to delete the entire list.
# thislist=['apple','banana','cherry']
# del thislist
# print(thislist)

### clearing the list
# thislist=['apple','banana','cherry']
# thislist.clear()
# print(thislist)

### Loop through the list
# thislist=['apple','banana','cherry']
# for x in thislist:
#     print(x)

### Loop through the index numbers
# thislist=['apple','banana','cherry']
# for i in range(len(thislist)):
#     print(thislist[i])

### Loop through a while loop 
# thislist=['apple','banana','cherry']
# i=0
# while i< len(thislist):
#     print(thislist[i])
#     i=i+1

# thislist=['apple','banana','cherry']
# [print(x)for x in thislist]

### List comprehension 
# fruits=['apple','banana','cherry','kiwi','mango']
# newlist=[]
# for x in fruits:
#     if "a"  in x:
#         newlist.append(x)

# print(newlist)


# fruits=['apple','banana','cherry','kiwi','mango']
# newlist=[x for x in fruits if "a" in x]
# print(newlist)

# fruits=['apple','banana','cherry','mango','orange']
# newlist=[x for x in fruits if x!='apple']
# print(newlist)

# newlist=[x for x in range(10)if x< 5]
# print(newlist)

# fruits=['apple','banana','cherry']
# newlist=[x.upper() for x in fruits]
# print(newlist)

# fruits=['apple','banana','cherry']
# newlist=['hello' for x in fruits]
# print(newlist)

# fruits=['apple','banana','cherry','melon']
# newlist=[x if x!='banana'else 'orange' for x in fruits]
# print(newlist)

###Sort list alphabetically
# thislist=['orange','mango','kiwi','pineapple','banana']
# thislist.sort()
# print(thislist)

# thislist=[100,50,65,82,23]
# thislist.sort()
# print(thislist)

# thislist=['orange','mango','kiwi','pineapple','banana']
# thislist.sort(reverse=True)
# print(thislist)

# thislist=[100,50,65,82,23]
# thislist.sort(reverse = True)
# print(thislist)

# def myfunc(n):
#     return abs(n-50)
# thislist =[100,50,65,82,23]
# thislist.sort(key=myfunc)
# print(thislist)

### Case Insensitive Sort
# thislist=['banana','Orange','Kiwi','cherry']
# thislist.sort()
# print(thislist)
# thislist.sort(key=str.lower)
# print(thislist)

# thislist=['banana','orange','kiwi','cherry']
# thislist.reverse()
# print(thislist)

### Copy a list
# thislist=['apple','banana','cherry']
# mylist=thislist.copy()
# print(mylist)

### Another way of copying a list
# thislist=['apple','banana','cherry']
# mylist=list(thislist)
# print(mylist)

### Joining two list
# list1=['a','b','c']
# list2=[1,2,3]
# list3=list1+list2
# print(list3)

# list1=['a','b','c']
# list2=[1,2,3]
# for x in list2:
#     list1.append(x)
# print(list1)

# list1=['a','b','c']
# list2=[1,2,3]
# list1.extend(list2)
# print(list1)

