# WAP TO SHOW THAT TUPLE VALUES CANNOT BE CHANGED DIRECTLY. CONVERT TUPLE INTO LIST, UPDATE IT, AND CONVERT IT BACK INTO TUPLE
numbers = (10,20,30,40,50)
print("Original tuple:", numbers)

temp = list(numbers)
temp[1] = 200

numbers = tuple(temp)
print("Updated tuple:", numbers)