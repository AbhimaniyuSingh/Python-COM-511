# Write a Python program to input a decimal number and convert it into binary without using the built -in bin() function.
def convert_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary
