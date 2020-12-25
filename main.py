from cards import deck
from players import player1

deck.shuffle()
print(deck)

deck.deal(player1)
print(player1.cards)