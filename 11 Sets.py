# thisset={'apple','banana','cherry'}
# print(thisset)

###Duplicate items # Duplicate items will be ignored
# thisset={'apple','banana','cherry','apple'}
# print(thisset)

###Length of the set
# thisset={'apple','banana','cherry'}
# print(len(thisset))

### Set Items- Data types
# set1={'apple','banana','cherry'}
# set2={1,2,3,4}
# set3={True, False, False}
# set4={'abc',34, True, 40, 'male'}
# print(set1)
# print(set2)
# print(set3)
# print(set4)

### type()
# myset={'apple','banana','cherry'}
# print(type(myset))

### The set() constructor
# thisset=set(('apple','banana','cherry'))
# print(thisset)

###Access items
# thisset={'apple','banana','cherry'}
# for x in thisset:
#     print(x)

# thisset={"apple",'banana','cherry'}
# print('banana'in thisset)

### Add items
# thisset={'apple','banana','cherry'}
# thisset.add('orange')
# print(thisset)

# thisset={'apple','banana','cherry'}
# tropical={'pineapple','mango','papaya'}
# thisset.update(tropical)
# print(thisset)

### Add any iterable
# thisset={'apple','banana','cherry'}
# mylist=['kiwi','orange']
# thisset.update(mylist)
# print(thisset)

###Remove item
# thisset={'apple','banana','cherry'}
# thisset.remove('banana')
# print(thisset)

# thisset={'apple','banana','cherry'}
# thisset.discard('banana')
# print(thisset)

###pop() method
# thisset={'apple','banana','cherry'}
# x=thisset.pop()
# print(x)
# print(thisset)

### Clear () method
# thisset={'apple','banana','cherry'}
# thisset.clear()
# print(thisset)

###Del() meethod to delete the set completely
# thisset={'apple','banana','mango'}
# del thisset
# print(thisset)

### Loop items
# thisset={'apple','banana','cherry'}
# for x in thisset:
#     print(x)

### Join two set
## union() method
# set1={'a','b','c'}
# set2={1,2,3}
# set3=set1.union(set2)
# print(set3)

## update() method
# set1={'a','b','c'}
# set2={1,2,3}
# set1.update(set2)
# print(set1)

### keep only the intersection items
# x={'apple','banana','cherry'}
# y={'google','microsoft','apple'}
# x.intersection_update(y)
# print(x)

# x={'apple','banana','cherry'}
# y={'google','microsoft','apple'}
# z=x.intersection(y)
# print(z)

### keep All,But NOT the Duplicates
# x={'apple','banana','cherry'}
# y={'google','microsoft','apple'}
# x.symmetric_difference_update(y)
# print(x)

# x={'apple','banana','cherrry'}
# y={'google','microsoft','apple'}
# z=x.symmetric_difference(y)
# print(z)

