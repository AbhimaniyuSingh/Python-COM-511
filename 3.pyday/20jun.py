# PRINT THE PATTERN OF STAR
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()         


# SECOND LARGEST ELEMENT IN A LIST 

list = [60, -10, -50, -20, -30, 0, 15]

largest =  second = float("-inf")
for i in list:
    if i> largest:
        second = largest
        largest = i
    else:
        if i> second and i != largest:
            second = i

print("The second largest is:", second)


#SECOND SMALLEST ELEMENT IN A LIST
list = [60, -10 , -50, -20, -30 , 0, 15]
smallest = second = float("inf")
for i in list:
     if i < smallest :
          second = smallest
          smallest = i
     else :
         if i < second and i != smallest:
             second = i
print("The second smallest is:", second)


#LARGEST ELEMENT IN A LIST
list = [60, -10, -50, -20, -30, 0, 15]
largest = float("-inf")
for i in list:
    if i > largest:
        largest = i
print("The Largest Element is : " , largest)


#WITHOUT LOOP
list = [60, -10, -50, -20, -30, 0, 15]
list.sort()
print("The Largest Element is :", list[-1])


#SMALLEST ELEMENT IN A LIST
list = [60, -10, -50, -20, -30, 0, 15]
list.sort()
print("The Smallest Element is :", list[0])


# WITH LOOP
list = [60, -10, -50, -20, -30, 0, 15]
smallest = float("inf")
for i in list:
    if i < smallest:
        smallest = i
print("The Smallest Element is :",smallest)

# WAP TO CALCULATE SUM OF POSITIVE NUMBERS OF A LIST
list = [-10 , 20 , -30 , -40 ,60]
sum = 0
for i in list:
    if i > 0:
     sum += i
print("Sum is :",sum)

#WAP TO CALCULATE SUM OF NEGATIVE NUMBER OF A LIST
list = [-10 , 20 , -30 , -40 ,60]
sum = 0
for i in list:
    if i < 0:
     sum += i
print("Sum is :",sum)

#WAP TO FIND OUT THE MISSING NUMBER
list = [1,2,4,5]
for i in range (1,5):
  if i not in list:
      print("Missing element is : ",i)

