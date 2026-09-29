# WAP TO INPUT A STUDENTS MARKS IN A CONSECUTIVE TESTS AND STORE IN A LIST. FIND THE LONGESR CONSECUTIVE SEQUENCE IN WHICH EACH MARKS IS STRICTLY GREATER THEN THE PREVIOUS MARKS.
'''Marks : [55,60,68,62,65,70,78,74]
Longest improving sequence [62,65,70,78]
Number of tests : 4
Test range :(4,7)

Conditions : 
- Accept at least one test.
- Equal marks break the improving sequence
- Test numbers begin at 1
- Do not sort the list because the original test order matters.'''

n = int(input("Enter number of seats: "))

seats = list(map(int, input("Seat status: ").split()))

group = int(input("Enter group size: "))

found = False

for i in range(n - group + 1):
    if all(seats[i + j] == 0 for j in range(group)):
        allocated = tuple(range(i + 1, i + group + 1))

        for j in range(i, i + group):
            seats[j] = 1

        print("Allocated seats:", allocated)
        print("Updated seats:", seats)
        found = True
        break

if not found:
    print("Consecutive seats not available")
    print("Original seats:", seats)