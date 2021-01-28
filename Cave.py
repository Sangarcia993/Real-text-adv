import random


#bat
class Bat():
    def __init__(self):
        self.hp = random.randint(5, 15)
        self.atk = random.randint(1, 10)
        self.name = "Bat"
        self.coins = random.randint(1, 10)
        self.exp = random.randint(1, 10)
        if self.hp > 10:
            self.name +=  " (Healthy)"
        if self.atk > 5:
            self.name += " (Stroong)"
        if self.hp > 10 and self.atk > 5:
            self.name = "Legendary bat"
            self.coins = 25
            self.exp = 15

    def getData(self):
        print("Name:", self.name)
        print("Hp:", self.hp)
        print("Atk:", self.atk)
        print("Coins:", self.coins)
        print("Exp:", self.exp)

        
        
"""            
bat1 = Bat()
print(bat1.name, bat1.coins)
"""