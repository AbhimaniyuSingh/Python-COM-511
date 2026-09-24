# WRITE A PYTHON PROGRAM TO STORE TWO POINTS AS TUPLES AND CALCULATE THE DISTANCE BETWEEN THEM.
import math


point1 =  input("Enter coordinates of first point (x y): ").split()
point2 =  input("Enter coordinates of second point (x y): ").split()

distance = math.hypot(float(point2[0]) - float(point1[0]), float(point2[1]) - float(point1[1]))
print("Distance between the points:", distance)
