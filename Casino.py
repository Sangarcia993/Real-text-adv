
import random

class Casino():
    def __init__(self, p_player_coins):
        self.wallet = p_player_coins
        self.card = 0
        self.debt = 0
        self.playing = False
        self.bet = 0
        self.quit = False
        self.ab = False
        self.amount = 10

    def Betting(self):
        try:
            print("NEW FEATURE: Turn on auto-bet to not disturbe youre playing (automatically bet)")
            self.bet = input("How much money do you want to bet or auto-bet (ab)? (exit)")
            if self.bet == "0" or int(self.bet) < 0:
                self.print("Next time actually bet something")
            elif int(self.bet) > self.wallet:
                print("You cant bet more than what you have:", self.wallet)
            else:
                print(f"LETS PLAY! You beted {self.bet} coins")
                print("What game do you whant to play? (RPS or bet to re bet or exit)")
                while True:
                    game_choice = input(">>> ")
                    if game_choice == "RPS":
                        self.playing = True
                        self.quit = True
                        self.RPS()
                        break
                    elif game_choice == "exit" or game_choice == "bet":
                        break
        except:
            if self.bet == "exit":
                self.quit = True
            elif self.bet == "ab":
                self.ab = True
                try:
                    autobet = int(input("do you wish to always bet what amount?"))
                    if autobet > self.wallet or autobet < 1:
                        print("thats not alowed, because of your uncoperativness we will put the amount to 10 and take a fee")
                        error = "lol"
                        int(error)
                    else:
                        self.bet = autobet
                except:
                    self.bet = self.wallet / 10
                    self.wallet -= 10
                    autobet = 10
                self.amount = autobet
                self.playing = True
                self.quit = True
            else:
                print("put a number")

    #Rock-paper-scicors game
    def RPS(self):
        while self.playing == False:
            self.Betting()
            if self.quit == True:
                break
        while  self.playing == True:
            moves = ["rock", "paper", "tijeras"]
            cchoice = input("Now playing rps (rock, paper, tijeras, cash, bet, exit)\n>>> ")
            try:
                p = moves.index(cchoice)
                c = random.randint(0, 2)
                if (c + 1) == p:
                    print("player wins")
                    print("your money is DOUBLED!!!")
                    self.wallet += int(self.bet)
                    self.bet = 0
                elif c == p:
                    print("draw") 
                    print("Your money and bet stays the same")
                else:
                    print("player lost")
                    print(f"You lost {self.bet} coins")
                    self.wallet -= int(self.bet)
                    self.bet = 0
                    
                
                #re beting
                if self.ab == True:
                    self.bet = self.amount
                    if self.wallet < 1:
                        print("Seems that you are poor, there is no more money left in your wallet")
                        print("proceeding to kick you out of casino")
                        #add wait
                        cchoice = "exit"
                        error = "lol"
                        int(error)
                else:
                    self.Betting()
            except:
                if cchoice == "exit":
                    self.playing = False
                    self.quit = True
                    break
                if cchoice == "cash":
                    print(f"Money in you: {self.wallet}")
                    print(f"Money on bet: {self.bet}")
                if cchoice == "bet":
                    self.playing = False
                    self.quit = False
                    while self.quit == False:
                        self.Betting()

    def truncate(n, decimals=0):
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier
        
        
            
            
            



Casino1 = Casino(100)
"""
Casino1.wallet /= Casino1.porcentage
print(Casino1.wallet)
"""
Casino1.RPS()


"""
moves = ["rock", "paper", "tijeras"]
p = moves.index(input(">>> "))
c = random.randint(0, 2)
if (c + 1) == p:
    print("player wins")
elif c == p:
    print("draw")
else:
    print("player lost")
    """