# WAP to print
'''* * * *
   * * * *
   * * * *
   * * * *'''
n = int(input("Enter the number of rows/columns: "))
for i in range(n):
    for j in range(n):
        print("* ", end="")
    print()