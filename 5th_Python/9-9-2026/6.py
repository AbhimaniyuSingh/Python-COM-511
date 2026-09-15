# Write a Python program to check whether a number is a perfect number. A number is perfect if the sum of its proper divisiors is equal to the number itself.
def is_perfect_number(n):
    if n <= 1:
        return False
    divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum == n
