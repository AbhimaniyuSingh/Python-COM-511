# LECTURE 4

# Dictionary used to store data values in key value pairs
dict = {
    "key" : "value",
    "key1" : "value1",
    "key2" : "value3",
    "age" : 20
}

# VALUES METHOD
print(list(dict.values()))

# ITEMS METHOD
print(list(dict.items()))

# GET METHOD
print(dict.get("key1"))

# UPDATE METHOD
dict.update({"city" : "Jammu"})
print(dict)



# SETS IN PYTHON
collection = { 1,2,3,4,"Hello","World" }
print(collection)
print(type(collection))

# ADD METHOD
collection.add("Python")
print(collection)

# REMOVE METHOD
collection.remove(1)
print(collection)


# PRACTICE 
dict ={}
x = int(input("Enter PHYSICS:"))
dict.update({"PHYSICS" : x})
y = int(input("Enter Chemistry"))
dict.update({"Chemistry" : y})
print(dict)
