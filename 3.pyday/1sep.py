# Write a Python program to display a user entered name followed by " Good Afternoon" using input() function ( Use f-string)

a = input("Enter name")
print(f"Good Afternoon,{a}")


# Write a Python program to fill the given letter template with name and date.
letter ='''
Dear <Name>

You are Selected!

<Date>
'''
name = input("Enter name:")
date = input("Enter Date:")

letter = letter.replace("<Name>",name)
letter = letter.replace("<Date>",date)

print(letter)

# Write a Python program to detect double space in a string
n = input("Enter name:")
print(" " in n)

print(n.find(" "))


# Write a Python program to replace double spaces from problem 3 with single spaces
print(replace)
# Write a Python program to format the following letter using escape sequence characters

letter = "Dear Abhimaniyu Singh , this python course is nice. Thanks!"