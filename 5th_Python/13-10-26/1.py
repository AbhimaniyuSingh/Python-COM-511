# CREATE A CLASS AND OBJECT : STUDENT DETAILS
class Student:
    def _init_(self,name,roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll: {self.roll}")
Student1 = Student("Aman",97)
Student1.display()