# Take Student full name and roll number. Generate email using first 3 letters of first name, first 3 letters of last name, and last 3 characters of roll number.
name = input("Enter your full name:")
roll = input("Enter your roll number :")

first_name, last_name = name.split(" ",1)

email = first_name[:3] + last_name[:3] + roll[-3:]
print(email+"@gmail.com")


# Take roll number like 2024A1R041 and extract admission year, program code, and roll number digits using slicing.'
roll_number = input("Enter your roll number: ")
admission_year = roll_number[:4]
program_code = roll_number[4:6]
roll_digits = roll_number[6:9]

print("Admission Year:", admission_year)
print("Program Code:", program_code)
print("Roll Number Digits:", roll_digits)

# Take an email address and print username, domain, and reversed domain.
email_address = input("Enter your email address: ")
username = email_address.split("@")[0]
domain = email_address.split("@")[1]
reversed_domain = domain[::-1]

print("Username:", username)
print("Domain:", domain)
print("Reversed Domain:", reversed_domain)

# Take name, branch, and year. Generate a code name using string concatentation, slicing and repetition.
name = input("Enter your name: ")
branch = input("Enter your branch: ")
year = input("Enter your year: ")
code_name = name[:2] + branch[:2] + year[-2:] *2
print("Code Name:", code_name)

# Take a password and check length, presence of @, and whether first and last characters are different.
password = input("Enter your password: ")

has_vaid = "@" in password
has = len(password) >= 8

valid = has_vaid and has
status_message = {
    True : "Password is Valid",
    False : "Invalid Password. It must be at least 8 characters long and conatin '@'."
}
print(status_message[valid])