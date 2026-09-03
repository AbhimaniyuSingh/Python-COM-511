# list = [10, 20, 30, 40]

# largest = list[0]
# second = list[0]

# for i in list:
#     if i > largest:
#         second = largest
#         largest = i
# print("The second largest is : ", second)


a = [10,20,30,40,[50,60],70]
a[4][1] = 100
a[1] = 200
print(a)