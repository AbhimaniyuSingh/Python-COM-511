# WAP TO CHECK WHETHER A GIVEN VALUE IS PRESENT IN A TUPLE, IF PRESENT DISPLAY ITS POSITION.
t = (10, 20, 30, 40, 50)

x = int(input("Enter value: "))

if x in t:
    print("Position:", t.index(x))
else:
    print("Value not found")