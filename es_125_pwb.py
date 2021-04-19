#shuffling a deck of cards

from random import randint

def createDeck():
    deck = []
    #suits = ["s", "h", "d", "c"]
    suits = ["♠", "♥", "♦", "♣"]
    numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

    for suit in suits:
        for n in numbers:
            card = n + suit
            deck.append(card)

    return deck


def shuffle(t):
    r = len(t) - 1
    shuffled = []
    for i in range(0, len(t)):
        random_index = randint(i, r)
        t[i], t[random_index] = t[random_index], t[i]
        
    return t


def main():
    deck = createDeck()
    shuffled_deck = shuffle(deck)
    print(shuffled_deck)


if __name__ == '__main__':
    main()