# Write a Python program to repeatedly calculate the sum of digits of a number until the result becomes a single digit.
a  = int(input("Enter a number: "))
while a >= 10:
    a = sum(int(digit) for digit in str(a))
print(a)