from random import shuffle

J = 10
Q = 10
K = 10
A = 11

suits = ('Club', 'Spade', 'Heart', 'Diamond')
ranks = (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K)
# values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
#          '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
# ranks = values.items()

class Player:

    def __init__(self, name, bet):
        self.name = name
        self.bet = bet

    def  new_bet(self):
        bet = self.bet - 10
        return bet


class Cards:

    def __init__(self, suit, rank):
        pass

class Deck:

    def __init__(self):
        self.cards = [(rank, suit) for suit in suits for rank in ranks]

    def deck_shuffle(self):
        shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop(0)


class Hand:

    def __init__(self):
        self.hand = []

    def dealt_card(self, card):
        self.hand.append(card)
        return self.hand

    # def add_values(self):
    #     value = 0
    #     for card in self.hand:
    #         value += card[0]
    #     return value




user_name = input("Player, what's your name?  ")
user = Player(user_name, 100)
dealer = Player("Dealer", 0)

# cards = Cards()

deck = Deck()

hand = Hand()
dealer_hand = Hand()
hand_value = 0

deck.deck_shuffle()

# Prints the shuffled deck of cards
# print(deck.cards)

# print("You have ${} to bet".format(user.bet))
# Bet loses $10
user.new_bet()
print("Now you have ${} to bet".format(user.new_bet()))

for i in range(1):
    hand.dealt_card(deck.deal_card())
    dealer_hand.dealt_card(deck.deal_card())

# hand_value += hand.add_values()
#
# print("the value of hand is: {}".format(hand_value))


print("{}'s Hand".format(user.name))
print(*hand.dealt_card(deck.deal_card()))

print("Dealer's Hand")
print(*dealer_hand.dealt_card(deck.deal_card()))

while True:
# while user.hand.add_values() <= 21:
    move = input("Would you like to (h)it or (s)tand? ").lower()
    if move == 'h':
        print("{}'s Hand".format(user.name))
        print(*hand.dealt_card(deck.deal_card()))
        # Add the values here
        continue
    else:
        print("You chose to stand. Now it's my turn!")
        break
