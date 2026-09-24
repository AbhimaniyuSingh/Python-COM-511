# WAP TO STORE ALL MONTH NAMES IN A TUPLE. INPUT A MONTH NUMBER AND DISPLAY THE CORRESPONDING MONTH NAME.
months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")

month_number = int(input("Enter month number (1-12): "))
if 1 <= month_number <= 12:
    print("Month name:", months[month_number - 1])
else:
    print("Invalid month number.")

