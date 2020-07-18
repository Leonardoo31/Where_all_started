#...............................................................................
greet()
command = ""
started = False
running = False

while command.lower() != "quit" :
    command = input("choose Start , stop , Quit or run if car is started >   ").lower()

    if command == "start":
        if started == False:
            print("car started")
            started = True
        else :
            print("car already started")

    elif command == "stop" :
        if started == False:
            print("already stopped")
        else:
            print("now we stop")
            started = False

    elif command == "run" :
        if started == True and running == False:
            print("running")
            running = True
        elif started == False:
            print("car not started")

        elif running == True:
            print("fine , i will run faster")



else:
    if started == True:
        print("Stopping the engine ")
        print("Good ride")
    else:
        print("good ride")
