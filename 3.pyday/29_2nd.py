# IF ELSE PROBLEMS :
age  = 16
if (age >= 18):
    print("Eligible")
else :
     print("Not Eligible")

# NESTING PROBLEM / IF ELSE IN AGAIN IF ELSE
agee = 34
if ( agee >= 18):
     if ( agee >= 80):
          print("Cannot Drive")
     else:
          print("Can Drive")
else:
     print("Cannot Drive")

# EVEN / ODD PROBLEMS USING IF ELSE STATEMENT
a = int(input("Enter any number :"))
rem = a % 2
if ( rem == 0):
     print("EVEN")
else:
     print("ODD")

# PRACTICE THE CALCULATOR 

a = int(input("Enter First Number :"))
b = int(input("Enter Second Number :"))
c = input("Enter the Operand")

if ( c =='+'):
     print("Sum is :", a+b)
elif ( c =='-'):
     print("Subtraction is : ", a-b)
elif ( c =='*'):
     print("Multiplication is :", a*b)
elif ( c =='/'):
     print("Division is :", a/b)
else:
     print("Invalid :")

# WAP TO FIND GREATEST OF THREE NUMBER
d= input("Enter First number: ")
b = input("Enter Second number :")
c = input("Enter Third number " )

if ( d > b  and d >c) :
     print(d,"is Greater")
elif(b >d and b > c):
     print(b,"is Greater")
else:
     print(c,"is Greater")
