#import Intro

def Actions(p_action):
    if p_action == "move":
        destination = input("where do you want to go\n>>> ")
        f = open("location.txt", "r")
        location = f.read()
        if location == destination:
            print("You are already there!")
        elif destination == "cave":
            print("traveling to cave...")
            #borrando datos
            f = open("location.txt", "r+")
            f.truncate(0)
            f.close()
            #escribiendo new location
            f = open("location.txt", "a")
            f.write("cave")
            import Cave
    elif p_action == "exit":
        f = open("location.txt", "r+")
        f.truncate(0)
        f.close()
        quit()

Actions("move")



