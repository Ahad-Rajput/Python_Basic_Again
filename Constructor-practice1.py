class Student:
    def __init__(self):
        self.name = input("Enter name : ")
        self.rollno = int(input("Enter roll no. : "))
        self.marks = int(input("Enter marks : "))
    
    def show(self):
        print("Name : ", self.name)
        print("Roll no. : ", self.rollno)
        print("Marks : ", self.marks)

print('\n--------------------------------\n')
std1 = Student()
print('---------------------------------')
std2 = Student()
print('---------------------------------')
std1.show()
print('---------------------------------')
std2.show()