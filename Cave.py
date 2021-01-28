import random


#bat
class Bat():
    def __init__(self):
        self.hp = 15 #random.randint(1, 15)
        self.name = "Bat"
        if self.hp > 10:
            self.name +=  "Healthy"
        
            
bat1 = Bat()
print(bat1.name)
