#  WAP TO INPUT MARKS OF N STUDENTS IN A LIST. DISPLAY HIGHEST MARKS, LOWEST MARKS, AVERAGE MARKS, AND NUMBER OF STUDENTS WHO PASSED.
n = int(input("Enter the number of students: "))
marks = []

for i in range(n):
    mark = float(input(f"Enter marks for student {i + 1}: "))
    marks.append(mark) 

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)
passed = sum(1 for mark in marks if mark >= 40)

print(f"Highest marks: {highest}")
print(f"Lowest marks: {lowest}")
print(f"Average marks: {average}")
print(f"Number of students who passed: {passed}")