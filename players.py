class Player(object):
    def __init__(self,name = None, ):
        self.name = name
        self.buy_in = 0

        self.stake = 0
        self.stake_min = 0
        self.cards = []
        self.score = 0
        self.fold = False
        self.check = False
        self.all_in = False
        self.big_small_dealer = []
player1 = Player("mike")
    # def __repr__(self):
    #     name = self.name
    #     return name
