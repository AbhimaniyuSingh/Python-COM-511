# WAP TO INPUT A LIST OF NUMBERS AND CREATE A NEW LIST CONTAINING ONLY UNIQUE ELEMENTS.
numbers = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

unique_numbers = list(set(numbers))
print("Unique elements:", unique_numbers)
