class Employee:
    def setData(self):
        self.name = input("Enter your name : ")
        self.id = int(input("Enter your id : "))
        self.salary = float(input("Enter your salary : "))

    def getData(self):
        print("Name : ", self.name)
        print("ID : ", self.id)
        print("Salary : ", self.salary)


obj = Employee()
print("-------------------------")
print("\n\tEnter Data\n\n")
obj.setData()
print("-------------------------")
print("\n\tGet Data\n\n")
obj.getData()
print("-------------------------")