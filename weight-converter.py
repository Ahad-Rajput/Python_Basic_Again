weight = input("Enter weight : ")
choice = input("(L)bs or (K)g : ")

if choice.lower() == 'l':
    ans = int(weight)*0.45
    print(f"{ans} kilos")
elif choice.lower() == 'k':
    ans = int(weight)/0.45
    print(f"{ans} pounds")
else:
    print("Error !!")