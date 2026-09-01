# LECTURE 3

marks = [94.4 , 80 , 78 , 56]
print(marks)
print(len(marks))
print(marks[0])

student = ["Karan", 95.4 , "Hlo"]
print(student[0])
student[0] = "Om"
print(student)

# LIST METHODS

list = [2,1,3]

# ADD ONE ELEMENT TO END
list.append(4) 
print(list)

# SORTS IN ASCENDING ORDER
list.sort()
print(list)

# SORTS IN DESCENDING ORDER
new = ['b', 'a', 'd', 'n']
new.sort(reverse = True)
print(new)

# FOR REVERSE
list.reverse()
print(list)

# INSERT SOMETHING IN LIST
list.insert(0,5)
print(list)

# REMOVE METHOD
list.remove(1)
print(list)

# POP PARTICULAR INDEX P VALIE DELETE
list.pop(0)
print(list)

# TUPLE
tup =(2,1,3)
print(type(tup))
print(tup[0])
print(tup[1:2])

# TUPLE METHODS

# RETURN INDEX OF FIRST OCCURENCE
tup = (1,2,3,4,5,2,2,2)
print(tup.index(2))

# COUNT METHODS
print(tup.count(2))


# PRACTICE QUESTION

# # WAP TO ASK THE USER TO ENTER NAMES OF THEIR 3 FAVOURITE MOVIES AND STORE IN A LIST.
# mov1 = input("Enter your 1st favourite movie")
# mov2 = input("Enter your 2nd Favourite movie")
# mov3 = input("Enter your 3rd Favourite movie")
# movies = []
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

# WAP TTO CHECK IF A LIST IS PALINDROME OR NOO=T
list1 = ["m" , "a", "a", "m"]
copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("Not Palindrome")

# WAP TO COUNT THE NUMBER OF STUDENTS WITH THE A GRADE IN THE FOLLOWING
tup = ("C", "A", "D","A","B","B")
print(tup.count("A"))

# STORE THE ABOVE VALUE IN LIST AND SORT
store = ["C", "A", "D","A","B","B"]
store.sort()
print(store)