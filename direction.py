class Player(object):
    def __init__(self,name):
        self.name = name
        self.list_of_special_attributes = []



    def establish_player_attributes(self):
        address_assignment = 0
        self.dealer = self.list_of_players_not_out[address_assignment]
        self.dealer.list_of_special_attributes.append("dealer")
        address_assignment += 1
        address_assignment %= len(self.list_of_players_not_out)
        self.small_blind = self.list_of_players_not_out[address_assignment]
        self.small_blind.list_of_special_attributes.append("small blind")
        address_assignment += 1
        address_assignment %= len(self.list_of_players_not_out)
        self.big_blind = self.list_of_players_not_out[address_assignment]
        self.big_blind.list_of_special_attributes.append("big blind")
        address_assignment += 1
        address_assignment %= len(self.list_of_players_not_out)
        self.first_actor = self.list_of_players_not_out[address_assignment]
        self.first_actor.list_of_special_attributes.append("first actor")
        self.list_of_players_not_out.append(self.list_of_players_not_out.pop(0))

    #def deal_players(self):
    #    for player in self.list_of_player_not_out


