# dealing hands of cards
from es_125_pwb import *

hands = 4
cards = 5
deck = shuffle(createDeck())

def deal(hands, cards, deck):

    for h in range(hands):
        player = []
        for c in range(cards):
            card_from_deck = deck[c]
            del deck[c]
            player.append(card_from_deck)
        print("Cards for player",h+1)
        print(player)

    print("There are %d cards left in the deck: " % len(deck))
    print(deck)


deal(hands, cards, deck)




