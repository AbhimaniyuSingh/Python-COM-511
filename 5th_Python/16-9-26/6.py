# WAP TO INPUT NUMBERS IN A LIST AND CREATE TWO SEPARATE LISTS FOR EVEN AND ODD NUMBERS.
numbers = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)