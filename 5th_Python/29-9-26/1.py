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

marks = list(map(int, input("Enter marks: ").split()))

longest = [marks[0]]
current = [marks[0]]

for i in range(1, len(marks)):
    if marks[i] > marks[i - 1]:
        current.append(marks[i])
    else:
        current = [marks[i]]

    if len(current) > len(longest):
        longest = current

print("Longest improving sequence:", longest)
print("Number of tests:", len(longest))

start = marks.index(longest[0]) + 1
end = start + len(longest) - 1
print("Test range:", (start, end))