from random import shuffle

J = 10
Q = 10
K = 10
A = 11



suits = ('Club', 'Spade', 'Heart', 'Diamond')
ranks = (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K)
# values = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
#          '10': 10, 'J': 10, 'Q': 10, 'K': 10}
# ranks = values.items()

class Player:

    def __init__(self, name, bet):
        self.name = name
        self.bet = bet

    def lose_bet(self):
        bet = self.bet - 10
        return bet

    def win_bet(self):
        bet = self.bet + 10
        return bet

    def win_blackjack(self):
        bet = self.bet + 20
        return bet

# class Card:
#     def __init__(self, suit, rank):
#         pass

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


    def add_values(self):
        value = 0
        for card in self.hand:
            value += card[0]
            # Changes the Ace value from 11 to 1
            if card[0] == 11 and value > 21:
                value -= 10
        return value


def check_game():
    if dealer_hand_value >= hand_value:
        print("The Dealer Wins. YOU LOSE!")
        user.lose_bet()
        print("Now you have ${} to bet".format(user.lose_bet()))
    elif hand_value > dealer_hand_value:
        print("YOU WIN!")
        user.win_bet()
        print("Now you have ${} to bet".format(user.win_bet()))


user_name = input("Player, what's your name?  ")
user = Player(user_name, 100)
dealer = Player("Dealer", 0)

# cards = Cards()

deck = Deck()

hand = Hand()
dealer_hand = Hand()
hand_value = 0
dealer_hand_value = 0

deck.deck_shuffle()

# Prints the shuffled deck of cards
# print(deck.cards)


for i in range(1):
    hand.dealt_card(deck.deal_card())
    dealer_hand.dealt_card(deck.deal_card())


print("{}'s Hand".format(user.name))
print(*hand.dealt_card(deck.deal_card()))

hand_value += hand.add_values()
print("the value of hand is: {}".format(hand_value))

print("Dealer's Hand")
print(*dealer_hand.dealt_card(deck.deal_card()))
dealer_hand_value += dealer_hand.add_values()


# Now the GamePlay for 1 turn
for x in range(1):

    # Checks to see if blackjack is hit.
    if dealer_hand_value == 21:
        print("Dealer got blackjack! YOU LOSE!")
        user.lose_bet()
        print("Now you have ${} to bet".format(user.lose_bet()))
        break
    elif hand_value == 21 and dealer_hand_value < 21:
        print("YOU GOT BLACKJACK!!! YOU WIN!!!")
        user.win_blackjack()
        print("Now you have ${} to bet".format(user.win_blackjack()))
        break

    # Starts the player's move.
    while hand.add_values() <= 21:
        move = input("Would you like to (h)it or (s)tand? ").lower()
        if move == 'h':
            print("{}'s Hand".format(user.name))
            print(*hand.dealt_card(deck.deal_card()))
            hand_value = hand.add_values()
            print("the value of hand is: {}".format(hand_value))
            # Add the values here
            continue
        elif move == "s":
            print("You chose to stand. Your hand's value is {}\nNow it's my turn!".format(hand_value))
            break

    # If you busted, you automatically lose and the game is over.
    if hand_value > 21:
        print("You Busted, You Lose!")
        user.lose_bet()
        print("Now you have ${} to bet".format(user.lose_bet()))
        break

    while dealer_hand.add_values() < 17 or dealer_hand_value < hand_value:
        print("Dealer's Hand")
        print(*dealer_hand.dealt_card(deck.deal_card()))
        dealer_hand_value = dealer_hand.add_values()

    print("The value of the dealer's hand is {}".format(dealer_hand_value))

    if dealer_hand_value > 21:
        print("The Dealer Busted! YOU WIN!")
        user.win_bet()
        print("Now you have ${} to bet".format(user.win_bet()))
        break

    check_game()
