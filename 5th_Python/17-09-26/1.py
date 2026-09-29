# WRITE A PYTHON PROGRAM TO STORE TWO POINTS AS TUPLES AND CALCULATE THE DISTANCE BETWEEN THEM.
x1 = int(input("Enter x-coordinate of point 1: "))
y1 = int(input("Enter y-coordinate of point 1: "))
x2 = int(input("Enter x-coordinate of point 2: "))
y2 = int(input("Enter y-coordinate of point 2: "))

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Distance between the points:", distance)