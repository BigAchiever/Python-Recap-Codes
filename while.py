"""
i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print("Done")
"""

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == 'start':
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started... Let's Go!")

    elif command == 'help':
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit the game    
        """)
    elif command == 'stop':
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car Stopped!")

    elif command == 'quit':
        print("Thank you for playing :)")
    else:
        print("Sorry, I don't understand what is written here :(")


