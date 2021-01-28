#import Intro


def Move():
    destination = input("where do you want to go\n>>> ")
    location = Filer("location.txt").reader()      
    if location == destination:
        print("You are already there!")

    elif destination == "cave":
        print("traveling to cave...")
        #borrando datos
        Filer("location.txt").clean()        
        #escribiendo new location
        Filer("location.txt").writer("cave")

    elif destination == "city":
        print("traveling to city...")
        #borrando datos
        Filer("location.txt").clean()
        #escribiendo new location
        Filer("location.txt").writer("city")
        
class Filer():
    def __init__(self, p_file_name):
        self.file_name = p_file_name
    
    def clean(self):
        f = open(self.file_name, "r+")
        f.truncate(0)
        f.close()
    
    def writer(self, p_thing_to_write):
        f = open(self.file_name, "a")
        f.write(p_thing_to_write)
    
    def reader(self):
        f = open(self.file_name, "r")
        data = f.read()
        return data

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


