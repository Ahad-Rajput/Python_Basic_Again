dict = {
    'name': "Ahad_Ali",
    'age' : 19,
    'passion' : 'Coding'
}
print(dict.get('name'))
print(dict.get('passion'))
print(dict.get('passionate'))
print(dict)

#Exercise

nums = {
    '1' : 'One',
    '2' : 'Two',
    '3' : 'Three',
    '4' : 'Four'
}
number = input("Enter Number : ")
for i in number:
    print(nums.get(i, "!"), end=" ")
