# Write a Python program to determine whether a student is eligible for a Scholarship.
''' The schorashop should be granted if the student satisfies either of the following conditions.
   1. The student has a CGPA of 8.5 or above and attendanceof 85 percent or above
   2. The students has won a national level competition.
   The program should take CGPA , attendance percentage, and national level competition status as 
   input, then display whether the student is eligible for the scholarship.'''

cgpa = float(input("Enter the CGPA: "))
attendance = float(input("Enter the attendance percentage: "))

if (cgpa >= 8.5 and attendance >= 85) or (cgpa >= 9.0 and attendance >= 75):
    print("Student is eligible for Scholarship")
else:
    print("Student is not eligible for Scholarship")

# Write a Python program to simulate a digital lock system.
''' The lock should ask the user to enter a 4 digit PIN. if the entered PIN does not conatin exactly 
    4 digits , the program should display an error message and ask again. If the entered PIN is correct 
     the lock should open. Otherwise the prpgram should ask the user to try again.'''

pin = "1234"

while True:
    p = input("Enter 4 digit PIN: ")

    if len(p) != 4:
        print("Error! Enter exactly 4 digits")
    elif p == pin:
        print("Lock opened")
        break
    else:
        print("Wrong PIN. Try again")

# Write a Python program to create a simple password validation system.
'''The prpgram should repeatedly ask the user to enter a password until a valid password is entered.
A password will be considered valid only if it has at least 8 characters and conatin the @ symbol'''

password = input("Enter password: ")

while len(password) < 8 or "@" not in password:
    print("Invalid password. Try again.")
    password = input("Enter password: ")

print("Valid password")

# Write a Python program to input marks of 5 Students.

'''For each student, the program should check whether the entered marks are valid or invalid. Marks
  are considered valid only if they are between 0 and 100. If the marks are inavlid, the program should
   display "Invalid marks skipped" and move to the next student without printing'''

# Program to input marks of 5 students

for i in range(5):
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        print("Invalid marks skipped")
        continue

    print("Valid marks:", marks)