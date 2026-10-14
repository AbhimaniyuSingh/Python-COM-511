# Write a program to perform searching activity using linear and binary search.

# Program to perform Linear Search and Binary Search

numbers = [10, 20, 30, 40, 50, 60, 70]

key = int(input("Enter the element to search: "))

# Linear Search
found = False

for i in range(len(numbers)):
    if numbers[i] == key:
        print("Linear Search: Element found at position", i + 1)
        found = True
        break

if not found:
    print("Linear Search: Element not found")


# Binary Search
low = 0
high = len(numbers) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if numbers[mid] == key:
        print("Binary Search: Element found at position", mid + 1)
        found = True
        break
    elif key > numbers[mid]:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Binary Search: Element not found")


