a = []
for i in range(1,6):
    a.append(i*2)


#CONVERTING INTO LIST COMPREHENSION

a =[i*2 for i in range(1,6)]
print(a)


# EXAMPLE 2 
a =[]
for i in range(1,50):
    if i % 7 == 0:
        a.append(i)

# CONVERT IN LC
a =[ i for i in range(1,50) if i % 7 == 0]
print(a)

# EXAMPLE 2
a= [ num if num<5 else num*2 for num in range(2,9)]
print(a)

# ANS
a=[]
for i in range(2,9):
    if i < 5:
     print(i,end=" ")
    elif i > 5:
        sum = i*2
        print(sum,end=" ")     

# QUESTION 3

list = [ 35 , 63 , 22, 15 , 9 , 88 ,77]
t = [i for i in list if i % 3 == 0]
print(t)

# QUESTION 4
result = []
for x in [10,5,2]:
    for y in [2,3,4]:
        result.append(x**y)
print(result)

# LIST COMPREHENSION
a = [ x**y  for x in[10,5,2] for y in [2,3,4]]
print(a)