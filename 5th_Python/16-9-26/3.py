# WAP TO INPUT MARKS OF 10 STUDENTS. STORE ONLY VALID MARKS BETWEEN 0 AND 100 IN A LIST. SKIP INVALID MARKS.
marks = []

for i in range(10):
    mark = int(input(f"Enter marks for student {i + 1}: "))
    if 0 <= mark <= 100:
        marks.append(mark)

print("Valid marks:", marks)