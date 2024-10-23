list = [2,5,3,1,9,5]
# list.append(3)
# print(list)
list.sort()
print(list)
# list.remove(2)
# print(list)
list.reverse()
print(list)

print(50 in list)

list.insert(0, 10)
print(list)

# remove duplicate numbers
nums = [2,2,2,4,5,1,6,6]
temp = []
for num in nums:
    if num not in temp:
        temp.append(num)
print(temp)