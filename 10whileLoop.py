i = 0
while i < 11:
    print(i)
    i += 1


available_exits=["north","south","east","west"]
chosen_exit = ""

userInput = input("Enter : ")
while True:
    print("Your In")

    if userInput not in available_exits and userInput != "quit":
        userInput = input("Enter again : ")
        continue
    elif userInput == 'quit':
        print("you have quited the game")
        break
    else:
        print("you have successfully exited")
    break




