list = [5,6,4,2,3,110,2,3]

maxi = 0
for i in range(len(list)):
    if list[i] > list[maxi]:
        maxi = i

print(list[maxi])