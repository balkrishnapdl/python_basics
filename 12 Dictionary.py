# thisdict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }
# print(thisdict)
 
### Dictionary items
# thisdict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }
# print(thisdict["brand"])

# thisdict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964,
#     "year":2020
# }
# print(thisdict)

### Dictiinary length
# thisdict={
#     "brand":"ford",
#     "model":"Mustang",
#     "year":1964
# }
# print(len(thisdict))

### Dictionary items-Data types
# thisdict={
#     "brand":"ford",
#     "electric": False,
#     "year":1964,
#     "colors":["red",'white','blue']
# }
# print(thisdict["colors"])

### type()
# thisdict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }
# print(type(thisdict))

### The dict() constructor
# thisdict=dict(name="John",age=36,country="Norway")
# print(thisdict)

### Access items 
# thisdict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }
# x=thisdict["model"]
# print(x)

### get() to access items
# thisdict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }
# x=thisdict.get("model")
# print(x)

### Get Keys
# thisdict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }
# x=thisdict.keys()
# print(x)

### Adding a new item to the original dictionary
# car={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }
# x=car.keys()
# print(x)
# car["color"]="white"
# print(x)
# print(car)

### Get Values
# thisdict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }
# y=thisdict.values()
# print(y)

# car={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1964
# }
# x=car.values()
# print(x)
# car["year"]=2020
# print(x)

# car={
#     "brand":"ford",
#     "model":"mustang",
#     "year":2020
# }
# x=car.values()
# print(x)
# car["color"]="white"
# print(x)

### Get items
# car={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":2020
# }
# x=car.items()
# print(x)
# car["year"]=2012
# print(x)

# car={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":2020
# }
# x=car.items()
# print(x)
# car["color"]='red'
# print(x)

### Check if key exists
# car={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":2020
# }
# if "model" in car:
#     print('yes,"model"is  one of the keys in th car dictionary')

### Change Values
# car={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":2020
# }
# car["year"]=2021
# print(car)

 ### Update dictionary
# thisdict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
#  }
# thisdict.update({"year":2020})
# print(thisdict)

###Adding items
# thisdict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }
# thisdict["color"]='red'
# print(thisdict)

###Update dictionary
# thisdict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year": 1964
# }
# thisdict.update({'color':'red'})
# print(thisdict)

### Removing item 
# thisdict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }
# thisdict.pop("model")
# print(thisdict)

### Use of popitem that may removes any item from the dictionary
# thisdict={
#     "brand":"Ford",
#     "model":"mustang",
#     "year":1964
# }
# thisdict.popitem()
# print(thisdict)

# thisdict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }
# del thisdict["model"]
# print(thisdict)

### Clear() method
# thisdict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }
# thisdict.clear()
# print(thisdict)

### looping the keys of dictionary
# thisdict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }
# for x in thisdict:
#     print(x)

### looping the values of the dictionary
# thisdict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }
# for x in thisdict:
#     print(thisdict[x])

### Other method
# thisdict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }
# for x in thisdict.keys():
#     print(x)

# thisdict={
#     "brand":"ford",
#     "model":"Mustang",
#     "year":1964
# }
# for x in thisdict.values():
#     print(x)

### loop through both keys and values
# thisdict={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1964
# }
# for x,y in thisdict.items():
#     print(x,y)

### Copy a dictionary
# thisdict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }
# mydict=thisdict.copy()
# print(mydict)

# thisdict={
#     "brand":"Ford",
#     "model":"Mustang",
#     "year":1964
# }
# mydict=dict(thisdict)
# print(mydict)

### Nested dictionary
# myfamily={
#     "child1":{
#         "name":"Emil",
#         "year":2004    
#     },
#     "child2":{
#         "name":"Tobias",
#         "year":2007
#     },
#     "child3":{
#         "name":"linus",
#         "year":2011
#     }
# }
# for x,y in myfamily.items():
#     print(x,y)

