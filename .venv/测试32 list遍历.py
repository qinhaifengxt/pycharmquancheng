list = [1,2,3,4,5,6,7,8,9,10]
list1 =[]
list2 = []
index = 0
while index < len(list):

    if list[index] %2 == 0:

        list1.append(list[index])
    index += 1

print(list1)
for i in list:
    if list[i-1]%2 ==0:
        list2.append(list[i-1])
print(list2)


