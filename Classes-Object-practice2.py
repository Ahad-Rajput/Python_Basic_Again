class Student:
    def __init__(self, my_rollno, my_name, my_marks):
        self.rollno = my_rollno
        self.name = my_name
        self.marks = my_marks
    
    def average(self):
        return sum(self.marks)/(len(self.marks))
    

first_student = Student(223, "Ahad", [47,66,68,46])
print("Student Name : ",first_student.name)
print("Student Roll no. : ", first_student.rollno)
print("Average of marks : ", first_student.average())