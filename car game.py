command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
           print(" car is already start!")
        else:
         started = True
         print("car started ...")
    elif command == "stop":
        if not started:
            print(" car has already stopped!..")
        else:
            started = False
            print("car stopped .")
    elif command == "help":
        print("""
start_ the car start
stop_ the car stop
quit_ to exit
        """)
    elif command == "quit":
        break

    else:
        print("i don't understand that")



