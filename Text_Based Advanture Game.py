weapon = False

def intro_scene():
    direction = ["left", "right", "forward"]
    print("\nYou are at a crossroad, and you can choose to go down any of the four hallways.")
    print("Where would you like to go?")
    
    user_input = ""
    
    while user_input not in direction:
        print("Options: left/right/backward/forward")
        user_input = input()
        if user_input == "left":
            show_shadow_figure()
        elif user_input == "right":
            show_skeleton()
        elif user_input == "forward":
            haunted_room()
        elif user_input == "backward":
            print("You find that this door opens into a wall.")
        else:
            print("Please enter a valid option.")

def show_shadow_figure():
    direction = ["right", "backward"]
    print("\nYou see a dark shadowy figure appear in the distance. You are creeped out.")
    print("Where would you like to go?")
    
    user_input = ""
    
    while user_input not in direction:
        print("Options: right/left/backward")
        user_input = input()
        if user_input == "right":
            camera_scene()
        if user_input == "left" :
            print(" You find that this door opens into wall ")  
        elif user_input == "backward":
            intro_scene()
        else:
            print("Please enter a valid option.")

def camera_scene():
    direction = ["forward", "backward"]
    print("\nYou see a camera that has been dropped on the ground. Someone has been here recently.")
    print("Where would you like to go?")
    
    user_input = ""
    
    while user_input not in direction:
        print("Options: forward/backward")
        user_input = input()
        if user_input == "forward":
            print("\nYou made it! You have found an exit. ")
            quit()
        elif user_input == "backward":
            show_shadow_figure()
        else:
            print("Please enter a valid option.")

def haunted_room():
    direction = [ "right","left", "backward"]
    print("\nYou hear strange voices. You think you have awoken some of the dead.")
    print("Where would you like to go?")
    
    user_input = ""
    
    while user_input not in direction:
        print("Options: right/left/backward")
        user_input = input()
        if user_input == "right":
            print("Multiple ghoul-like creatures start emerging as you enter the room. You are killed.")
            quit()
        elif user_input == "left":
            print("You find an exit and escape the haunted room. Congratulations!")
            quit()
        elif user_input == "backward":
            intro_scene()
        else:
            print("Please enter a valid option.")

def show_skeleton():
    direction = [ "backward","forward"]
    global weapon
    print("\nYou see a wall of skeletons as you walk into the room. Someone is watching you.")
    print("Where would you like to go?")
    
    user_input = ""
    
    while user_input not in direction:
        print("Options: left/backward/forward")
        user_input = input()
        if user_input == "left":
            print("\nYou find that this door opens into a wall. You open some of the drywall to discover a knife.")
            weapon = True
        elif user_input == "forward":
            intro_scene()
        elif user_input == "backward":
            strange_creature()
        else:
            print("Please enter a valid option.")

def strange_creature():
    action = ["fight", "flee"]
    global weapon
    print("\nA strange ghoul-like creature has appeared. You can either run or fight it.")
    print("What would you like to do?")
    
    user_input = ""
    
    while user_input not in action:
        print("Options: fight/flee")
        user_input = input()
        if user_input == "fight":
            if weapon:
                print("\nYou kill the ghoul with the knife you found earlier. After moving forward, you find one of the exits. Congrats!")
            else:
                print("The ghoul-like creature has killed you.")
            quit()
        elif user_input == "flee":
            show_skeleton()
        else:
            print("Please enter a valid option.")

while True:
        print("(^_^) Welcome to the Adventure Game! (^_^)")
        print("\nAs an avid traveler, you have decided to visit the Catacombs of Paris.")
        print("However, during your exploration, you find yourself lost.")
        print("You can choose to walk in multiple directions to find a way out.")
        print("Let's start with your name. :)")
        name = input()
        print("Good luck,", name, ";)")
        intro_scene()