command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "quit":
        break
    elif command == "start":
        if started:
            print("Car is already started")
        else:
            print("Car Started")
            started = True
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            print("Car Stopped")
            started = False
    elif command == "help":
        print("Enter :")
        print("start -> start the car")
        print("stop -> stop the car")
        print("quit -> exit the program") 
    else:
        print("Sorry, I don't understand this....")
