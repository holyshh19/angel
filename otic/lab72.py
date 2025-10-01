list1 = []
num = int(input("???   "))
for i in range(8):
    num += 10
    list1.append(num)
print(list1)    

list1_copy = []
for i in list1:
    if i % 4 == 0:
        list1_copy.append(i)
print(list1_copy)