# Write a Python program to input a number and check whether it is prime or not. A number is prime if it has no divisor other than 1 and itself.
a = int(input("Enter a number"))
is_prime = True
if ( a <= 1):
    is_prime = False
else:
    for i in range(2,a):
        if a % i ==0:
            is_prime = False
            break
if is_prime:
    print(a, "is a prime number")
else:
    print(a, "is not a prime number")