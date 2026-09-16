# WAP TO INPUT NUMBERS IN A LIST AND FIND THE SECOND LARGEST NUMBER

numbers = []
n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Remove duplicates and sort in descending order
unique_numbers = list(set(numbers))
unique_numbers.sort(reverse=True)

if len(unique_numbers) >= 2:
    second_largest = unique_numbers[1]
    print(f"The second largest number is: {second_largest}")
else:
    print("There is no second largest number.")