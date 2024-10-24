try:
    age = int(input("Age : "))
    amount = 10000
    result = amount/age
    print(result)
except ValueError:
    print("Invalid value!")
except ZeroDivisionError:
    print("Age can't be 0")
