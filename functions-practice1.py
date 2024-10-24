def greet_user(first_name, last_name):
    print(f"Hi, {first_name} {last_name}!")
    print("Welcome")

print("Start")
greet_user("Ahad", "Ali")
print("Finish.")

#keywords Arguments

print("Start")
greet_user(first_name="Ali", last_name="Ahad")
print("Finish")

#return keyword

def square(num):
    return num*num

result = square(2)
print(result)