import Intro


def Move():
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

    elif destination == "city":
        print("traveling to city...")
        #borrando datos
        f = open("location.txt", "r+")
        f.truncate(0)
        f.close()
        #escribiendo new location
        f = open("location.txt", "a")
        f.write("city")
        

def Actions(p_action):
    if p_action == "move":
        Move()
    elif p_action == "exit":
        f = open("location.txt", "r+")
        f.truncate(0)
        f.close()
        quit()

while True:
    Actions(input("what do you whant to do [move]"))
    #crea un function llamada "encaunters" la cual se llame despues de actions
    #la variable encaunters


