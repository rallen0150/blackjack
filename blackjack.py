import random

suits = (['Club'], ['Spade'], ['Heart'], ['Diamond'])
ranks = (['A'], ['2'], ['3'], ['4'], ['5'], ['6'], ['7'], ['8'], ['9'], ['10'], ['J'], ['Q'], ['K'])

class Player:

    def __init__(self, name, bet):
        self.name = name
        self.bet = bet


# class Cards:
#
#     def __init__(self):
#         self.suit = ['Club', 'Spade', 'Heart', 'Diamond']
#         self.rank = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
#
#     def get_card(self):
#         card_hand = random.choice(cards.rank), random.choice(cards.suit)
#         return card_hand


class Deck:

    def __init__(self):
        self.cards = [(rank, suit) for suit in suits for rank in ranks]

    def deck_shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop(0)


class Hand:

    def __init__(self):
        self.hand = []

    def dealt_card(self, card):
        self.hand.append(card)
        return self.hand


user = Player("Robbie", 100)
dealer = Player("Dealer", 0)

# cards = Cards()
deck = Deck()
hand = Hand()
dealer_hand = Hand()

print(user.name)
print(dealer.name)

# card_hand = cards.get_card(), cards.get_card()

deck.deck_shuffle()

print(deck.cards)


hand.dealt_card(deck.deal_card())
dealer_hand.dealt_card(deck.deal_card())
print("Robbie's Hand")
print(hand.dealt_card(deck.deal_card()))
print("Dealer's Hand")
print(dealer_hand.dealt_card(deck.deal_card()))
