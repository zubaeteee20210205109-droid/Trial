#start- to start the car
#stop - to stop the car
#quit_ to exit
from operator import truediv
from turtledemo.penrose import start
from xmlrpc.client import FastParser

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Cae is already stopped.")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car 
stop  - to stop the car
quit  - to exit 
        """)
    elif command == "quit":
        break
    else:
        print("Invalid command.")
