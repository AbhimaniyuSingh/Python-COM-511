
# DICTIONARY - These are used to store data values in key : values pairs.
#  . unordered
#  . Mutable
#  . They don't allow duplicate keys

# Dictionary Methods: 
#  1. dict.keys(): - returns all the keys of the dictionary
#  2. dict.values() - returns all the values 
#  3. dict.items(): - return all (key,val) pairs as tuples
#  4. dict.get("key") - 


dict = {
    "name" : "Abhimaniyu",
    "cgpa" : "8.2",
    "marks" : 88
}
print(dict)

dict["name"] = "raj"
print(dict)
print(dict["name"])
print(dict["cgpa"])
print(dict["marks"])
print(type(dict))

# NULL DICTIONARY :

null_dict = {}
print(null_dict)

null_dict["name"] = "Abhimaniyu"
print(null_dict)


# NESTED DICTIONARY - Nested Dictionary means dictionary inside the dictionary

student = {
    "name" : "Abhimaniyu Singh",
    "age" : 20,
    "score" : {
        "c" : 98,
        "cyber" : 56
    }
}
print(student)

# IF WE WANT THE INSIDE DICTIONARY

print(student["score"]["c"])
print(student.keys())
print(student.values())
print(list(student.values()))
print(student.items())

pairs = list(student.items())

print(pairs[0])
print(pairs[2][1])

jatin = list(pairs[2][1].items())

print(jatin[0])
print(jatin[1])

print(student.get("name2"))
print(student)

student.update({"city" : "jammu"})
print(student)

# SETS - Set is a collection of data in unordered method.
#      . Each element in a set must be unique.
#      . mutuable
#      . each element in a set must be immutable.
#      . (string , int , tuple , float , boolean etc.)
       #. ( list , dictionary not allowed)

# EXAMPLES :
            # 1. nums = { 1,2,3}
            # 2. marks = { "raj", "ravi" , "rahul"}
            # 3. ram = { "raj", 55 , "True", 0 , True}
            # 4. ram = {(1,2,3), "r", 1,2,3}

collection = {1,2,3,4}
print(collection)
print(type(collection))



# SET METHODS - 
#              1 = set.add(e1) -  adds an element in set
#              2 = set.remove(e1) - removes the element.
#              3 = set.pop() - removes a random values
#              4 = set.union(set2) - combines both set values and returns new set


# ADD METHOD
collection.add(5)
print(collection)

# REMOVE METHOD
collection.remove(2)
print(collection)

# POP METHOD
collection.pop()
print(collection)

# CLEAR METHOD
collection.clear()
print(collection)

set1 =  { 1,2,3,4}
set2 = {3,4,5,6}

# UNION METHOD
set3 = set1.union(set2)
print(set3)

# INTERSECTION METHOD
set4 = set1.intersection(set2)
print(set4)

