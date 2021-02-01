#import Intro
import random
from Cave import Bat
from Player import Playerr
from City import Casino

P1 = Playerr()
Casino = Casino(P1.coins)

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
        Filer("location.txt").clean()
        quit()
    else:
        Actions(input("what do you whant to do [move, exit]"))


def Battle(p_enemy, P1):
    print("You have entered a battle with:", p_enemy.name)
    while P1.hp > 0 and p_enemy.hp > 0:
        choice = input("What do you do [atk, analyse, retret]")
        if choice == "atk":
            p_enemy.hp -= P1.atk 
            print("Enemy health remaining =", p_enemy.hp)
            print("The enemy strikes back, it deals", p_enemy.atk)
            P1.hp -= p_enemy.atk
            print("Remaining health:", P1.hp)

        if choice == "analyse":
            print("You analyse the enemy and...")
            p_enemy.getData()
        
        if choice == "retret":
            print("While you cowerdly run the", p_enemy.name, "atacks you from behind")
            P1.hp -= p_enemy.atk
            print("It deals", p_enemy.atk, "hit points")
            break

    #after battle ends
    if P1.hp < 1:
        P1.status = "Dead"
    elif p_enemy.hp < 1:
        print("you have won")
        print("you gain", p_enemy.coins, "coins and", p_enemy.exp, "exp")
        P1.coins += p_enemy.coins
        P1.exp += p_enemy.exp
        



while P1.status == "Alive":
    Actions(input("what do you whant to do [move, exit]"))
    if Filer("location.txt").reader() == "city":
        print("in da city")

    #Cave
    else:
        dice = random.randint(1, 100)
        if dice < 1011:
            bat1 = Bat()
            Battle(bat1, P1)


print("you dead")
Filer("location.txt").clean()





