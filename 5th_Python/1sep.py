# Write a Python program to display a user entered name followed by " Good Afternoon" using input() function ( Use f-string)

a = input("Enter name")
print(f"Good Afternoon,{a}")


# Write a Python program to fill the given letter template with name and date.
letter ='''
Dear <Name>

You are Selected!

<Date>
'''
name = input("Enter name:")
date = input("Enter Date:")

letter = letter.replace("<Name>",name)
letter = letter.replace("<Date>",date)

print(letter)

# Write a Python program to detect double space in a string
n = input("Enter name:")
print(n.find(" "))


# Write a Python program to replace double spaces from problem 3 with single spaces.
text = n.replace("  ", " ")
print(text)


# Write a Python program to format the following letter using escape sequence characters
letter = "Dear Abhimaniyu Singh , \n\tThis python course is nice. \nThanks!"
print(letter)

# Write a Python Program to take a Student's full name and display.
''' Total number of characters
     First character
     last character
     Name in uppercase Form
     '''

name = input ("Enter Student name : ")
print("Total Characters = ",len(name))
print("First Character = ", name[0])
print("Last Character",name[-1])
print("Capitalized name = ",name.upper())

# Write a Python program to take a student name and roll number, then generate a username using the first 3 letters of the name and last 2 digits of the roll number
name1 = input("Enter name:")
roll = input("Enter roll number")

username = name[:3] + roll[-2:]
print("Generated Username = ",username)

# Write a python a program to take an email address and print the domain name.
email = input("Enter email :")
index =  email.find("@")
domain = email[index + 1:]
print("Domain = ", domain)

# Write a proogram to check whether an email ends with mietjammu.in
hlo = input("Enter email address")
print(email.endswith("mietjammu.in"))

# Write a python program to take a 10 digit mobile number and display only the last 4 digits. Replace the first 6 digits with ******
cv = input("Enter number")
print("******"+cv[-4:])
