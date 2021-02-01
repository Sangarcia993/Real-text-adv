
class Casino():
    def __init__(self, p_player_coins):
        self.wallet = p_player_coins
        self.card = 0
        self.debt = 0

    #Rock-paper-scicors game
    def RPS(self):
        bet = input("How much money do you want to bet?")
        if bet == "0":
            print("Next time actually bet something")
        elif int(bet) > self.wallet:
            print("You cant bet more than what you have:", self.wallet)
        


Casino1 = Casino(100)

Casino1.RPS()