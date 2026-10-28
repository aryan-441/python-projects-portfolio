"""
Milestone Project 2- Blackjack
"""
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {
    'Two':2,
    'Three':3,
    'Four':4,
    'Five':5,
    'Six':6,
    'Seven':7,
    'Eight':8,
    'Nine':9,
    'Ten':10,
    'Jack':10,
    'Queen':10,
    'King':10,
    'Ace':11  #default ace value
    }

game_on = True

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_composition = ''
        for card in self.deck:
            deck_composition += '\n'+ card.__str__()
        return "The deck has:" + deck_composition
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []  #default values
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        #card passed in is from Deck.deal(), not the Card Class
        self.value += values[card.rank]  #adds the value of the new card to find sum

        if card.rank == 'Ace':
            self.aces = 1
            
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:  #checks for aces and if value is greater than 21
            self.value -= 10 #then changes ace to 1 instead of 11
            self.aces -= 1

class Chips:
    def __init__(self,total=100): #default total of 100 chips
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet

#Functions
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet?"))
        except ValueError as e:
            print(f"Sorry, please provide an integer. an error occured: {e}.")
        else:
            if chips.bet > chips.total:
                print("Sorry, you do not have enough chips! Available amount: {}".format(chips.total))
            else:
                break

def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global game_on

    while True:
        x = input("Hit or stand? Enter h or s.")
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player Stands; Dealer's turn.")
            game_on = False
        else:
            print("Invalid input.")
            continue
        break

def show_card(player,dealer):
    print("\nDealer's Hand: ")
    print("First card hidden!")
    print(dealer.cards[1]) #shows the second card
    print("\nPlayer's hand: ")
    for card in player.cards:
        print(card)

def show_all_cards(player,dealer):
    print("\nDealer's hand: ")
    for card in dealer.cards:
        print(card)

    print(f"Value of Dealer's hand is: {dealer.value}")

    print("\nPlayer's hand:  ")
    for card in player.cards:
        print(card)

    print(f"Value of Player's hand is: {player.value}.")

#Situational functions

def player_busts(player,dealer,chips):
    print("Bust player!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Bust dealer! Player wins")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins! Player busted.")
    chips.lose_bet()
def push(player,dealer):
    print("Player and Dealer have a tie. Push.")

#GAME LOGIC

while True:
    print("Welcome to blackjack!")
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)
    show_card(player_hand,dealer_hand)

    while game_on:
        hit_or_stand(deck,player_hand)
        show_card(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    if player_hand.value <= 21:
        while dealer_hand.value < player_hand.value:
            hit(deck,dealer_hand)

        show_all_cards(player_hand,dealer_hand)
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)

    print("\n Player's total chips are: {}".format(player_chips.total))

    new_game = input("Would you like to play another hand? (y/n)").lower()
    if new_game[0].lower() == 'y':
        game_on = True
        continue
    else:
        print("Thank you for playing!")
        break
    
        
    
    

        
        
