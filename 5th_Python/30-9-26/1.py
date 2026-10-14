# Write a program to reverse every kth row in a matrix.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15]
]

k = int(input("Enter k: "))

for i in range(k - 1, len(matrix), k):
    matrix[i].reverse()

print("Matrix after reversing every kth row:")

for row in matrix:
    print(row)