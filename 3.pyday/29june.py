# LECTURE 2 ONLINE
string  = " This is a String. \n I am Studing Today"
print(string)

str1 = "apna"
str2 = "College"
print(str1 + " "+ str2)

# TO PRINT LENGTH
len1 = len(str1)
print(len1)

# TO ACCESS ONE CHARACTER
print(str1[1])

# HOW TO USE SLICING - ACCESSING PARTS OF STRING
print(str2[1:4])
print(str2[:4])
print(str2[4:len(str2)])

# BACKWARD COUNTING
print(str2[-3:-1])

# CHECK STRING END WITH SPECIFIC ALPHABET
print(string.endswith("app"))

# REPLACE
print(string.replace("This","Now"))

# SEARCH ANYWORD IN STRING RETURN INDEX
print(string.find("T"))

# COUNT HOW MANY TIMES A WORD IN A STRING
print(string.count("i"))

# WAP TO ENTER NAME AND FIND ITS LENGTH
a  = input("Enter users name :")
print(len(a))

# WAP TO FIND THE OCCURANCE OF DOLLAR IN STRING
v = "HI I AM $$$$$"
print(v.count("$"))



