# Write a Python program that asks the user to enter a username and password. The user should get only 3 attempts. If the correct creditals are enetered, display" Login Successful" and stop the loop. If all attempts are used, display "Account Locked"
username = "admin"
password = "123456"
attempts = 3

while attempts > 0:
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    if user == username and pwd == password:
        print("Login Successful")
        break
    else:
        attempts -= 1
        print("Invalid credentials. You have {attempts} attempts left.")

if attempts == 0:
    print("Account Locked")
