# Write a Python program to input two numbers and find their greatest common divisor using a loop.
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
while b:
    a, b = b, a % b
print("Greatest common divisor is:", a)
