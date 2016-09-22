import random

suits = (['Club'], ['Spade'], ['Heart'], ['Diamond'])
ranks = (['A'], ['2'], ['3'], ['4'], ['5'], ['6'], ['7'], ['8'], ['9'], ['10'], ['J'], ['Q'], ['K'])

class Player:

    def __init__(self, name):
        self.name = name


class Cards:

    def __init__(self):
        self.suit = ['Club', 'Spade', 'Heart', 'Diamond']
        self.rank = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def get_card(self):
        card_hand = random.choice(cards.rank), random.choice(cards.suit)
        return card_hand


class Deck:

    def __init__(self):
        self.cards = [(rank, suit) for suit in suits for rank in ranks]

    def deck_shuffle(self):
        random.shuffle(self.cards)



user = Player("Robbie")
dealer = Player("Dealer")

cards = Cards()
deck = Deck()
print(user.name)
print(dealer.name)

card_hand = cards.get_card(), cards.get_card()

print(*card_hand)
print(deck.cards)

deck.deck_shuffle()
print(deck.cards)
