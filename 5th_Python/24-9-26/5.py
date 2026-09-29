students = [
    ("Rahul", "2024A1R001",82),
    ("Priya","2024A1R002",91),
    ("Amit","2024A1R003",65),
    ("Suman","2024A1R004",78)
]

print("Students Scoring 75 :")
for student in students:
    name,roll_no,marks = student

    if marks > 75:
        print(name,roll_no,marks)