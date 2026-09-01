#PRINT THE PATTERN --> 1
#  * * * * *
#  * * * * *
#  * * * * *
#  * * * * *

n = 5
for i  in range(4): 
     
    for  j  in range(n):
      print("*", end= " ")
      
    print()

# *
# * *
# * * *
# * * * *
# * * * * *

n = 5

for i in range(n):
   for j in range(i+1):
      print("*", end=" ")
   print()


#  * * * * *
#  * * * *
#  * * *
#  * *
#  * 

n = 5
for i in range(n):
   for j in range(i,n):
      print("*", end=" ")
   print()


#         *
#       * *
#     * * *
#   * * * *
# * * * * *

n = 5
for i in range(n):
   for j in range(i,n):
     print(" ", end= " ")
   for j in range(i+1):
      print("*" , end= " ")
   print()



# * * * * * 
#   * * * *
#     * * * 
#       * *
#         *

# COMBINATION OF INCREASING SPACES AND DECREASING SPACES

n = 5
for i in range(n):
   for j  in range(i+1):
      print(" ", end= " ")
   for j in range(i,n):
      print("*", end= " ")
   print()

# PYRAMID PATTERN 
 
#          *
#        * * *
#      * * * * *
#    * * * * * * *
#  * * * * * * * * *

n = 5
for i in range(n):
   for j in range(i,n):
      print(" ", end=" ")
   for j in range(i):
      print("*", end= " ")
   for j in range(i+1):
      print("*", end=" ")
   print()

# * * * * * * * * * 
#   * * * * * * *
#     * * * * *
#       * * *
#         *

n  = 5
for i in range(n):
   for j in range(i+1):
      print(" ", end= " ")
   for j in range(i,n-1):
      print("*", end=" ")
   for j in range(i,n):
      print("*", end=" ")
   print()  


#          *
#        * * *
#      * * * * *
#    * * * * * * *
#  * * * * * * * * *
#    * * * * * * *
#      * * * * *
#        * * *
#          *

n = 5
for i in range(n-1):
   for j in range(i,n):
      print(" ", end=" ")
   for j in range(i):
      print("*", end=" ")
   for j in range(i+1):
      print("*", end=" ")
   print()
for i in range(n):
   for j in range(i+1):
      print(" ", end= " ")
   for j in range(i,n-1):
      print("*", end=" ")
   for j in range(i,n):
      print("*", end=" ")
   print()
    