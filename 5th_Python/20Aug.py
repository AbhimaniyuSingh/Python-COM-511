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

# PRACTICE PROBLEMS

# 1. Write a Python program to determine whether a student is eligible for a scholarship.

''' The scholarship should be granted if the student satisfies either of the following conditions.
    a. The student has a CGPA of 8.5 or above the attendance of 85 percent or above.
    b. The student has won a national level competiton.
    
    The program should take CGPA, attendance percentage, and national-level competition status as input
    then display whether the student is eligible for the scholarship.
    
    2. Write a Python program to simulate a digital lock system.
    
       The lock should ask the user to enter a 4 digit PIN. If the entered PIN does not conatin exactly
       4 digits, the program should display an error message and ask again. If the entered PIN is correct,
       the lock should open. Otherwise, the program should ask the user to try again.'''

a = float(input("Enter the CGPA: "))
b = float(input("Enter the attendance: "))
c = input("Enter the level status (Yes/No): ")

if a > 8.5 and b >= 85:
    if c == "Yes":
        print("Student is eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")