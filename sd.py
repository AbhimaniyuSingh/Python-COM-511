# print the sum of first n umbers

n = int(input("Enter a number: "))              
sum = 0
for i in range(1, n+1): 
    sum += i
print("The sum of first", n, "numbers is:", sum)

