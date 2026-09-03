# # LECTURE 5

# # Loops / while / For


# # WHILE LOOP
count = 1
while count <=5:
    print("hello")
    count += 1

i = 1
while i<=10:
    print("Apna College",i)
    i += 1

# # IN REVERSE
i = 5
while i >=1:
    print(i)
    i -= 1

# # PRINT NUMBER FROM 1 TO 100
# # PRINT NUMBER FROM 100 TO 1
i = 100
while i >= 1:
    print(i)
    i -= 1

# # PRINT THE MULTIPLICATION NUMBER TABLE OF A NUMBER N
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(n,"*",i,"=",n*i)
    i += 1


# # PRINT THE FOLLOWING ELEMENTS
nums = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i < len(nums):
    print(nums[i])
    i += 1

# # SEARCH FOR A NUMBER IN A TUPLE
tup = (1,4,9,16,25,36,49,64,81,100)
i = 0
n = int(input("Enter number : "))
while i < len(tup):
    if n == tup[i]:
        print("Founded",tup[i])
    i += 1


# # BREAK 
# # CONTINUE

i = 1
while i <= 10:
    if (i%2 == 0):
        i+= 1
        continue
    print(i)
    i += 1

# FOR LOOPS

vege = ["brinjal" , "tomato", "ladyfingerr"]
for i in vege:
    print(i)

word = "apnacollege"
for i in word:
    print(i)

# PRINT THE ELEMENTS OF LIST USE LOOP
list = [1,4,9,16,25,36,40,49,64,81,100,49]
for i in list:
    print(i)

# SEARCH FOR A NUMBER X IN THIS
list1 = [1,4,9,16,25,36,40,49,64,81,100,49]
x = 49
idx = 0
for i in list1:
    if x == i:
        print("Founded at index",idx)
    idx += 1

# RANGE
seq = range(5)
for i in seq:
    print(i)

for k in range(2,10,2): # range(start,stop,inc/dec)
    print(k)

# PRINT 1 TO 100
for i in range(1,101):
    print(i)

# PRINT 100 T0 1;
for i in range(100,0,-1):
    print(i)

# PRINT TABLE OF A NUMBER
n = int(input("Enter a number :"))
for i in range(1,11):
    print(n*i)
i += 1

# PASS STATEMENT -  USE FOR NO USE 
for i in range(5):
    pass # SKIP
print("END")


# WAP TO FIND THE SUM OF FIRST N NUMBER
n = int(input("ENTER A NUMBER :"))
sum  = 0
for i in range(n):
    print(i)
    sum += i
print("SUM OF FIRST",n,"NUMBER IS :",sum)


n  = 7
sum = 0 
i  =1
while i < n:
    sum += i
    i += 1
print("SUM OF FIRST",n,"NUMBER IS :",sum)


# FACTORIAL OF A NUMBER
n = int(input("Enter a number : "))
sum = 1
i  = 1
while i <= n:
    sum *= i
    i += 1
print("FACTORIAL OF",n,"IS :",sum)

n = 5
fact = 1
for i in range(1,n+1):
    fact *= i
print("FACTORIAL OF",n,"IS :",fact)