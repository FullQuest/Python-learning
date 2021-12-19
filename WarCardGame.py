# SUIT,RANK,VALUE
# Названия мастей: Clubs = крести, Diamond = бубны, Spades = Пики, Hearts = Черви
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
         'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


# CARD class
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


# DECK CLASS
class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Crate the card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

    def __len__(self):
        return len(self.all_cards)

    def __str__(self):
        return "\n".join([str(card) for card in self.all_cards])


# PLAYER
class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # List of multiple card objects
            self.all_cards.extend(new_cards)
        else:
            # For a single card object
            self.all_cards.append(new_cards)

    def show_cards(self):
        return [str(card) for card in self.all_cards]

    def shuffle_cards(self):
        random.shuffle(self.all_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'

    def has_no_cards(self):
        return len(self.all_cards) == 0


# Game setup
player_one = Player("Synthapella")
player_two = Player("Auria")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

cards_needed_for_war = 5
round_number = 0
game_on = True

while game_on:

    round_number += 1
    print(f'Current round  {round_number}')

    if player_one.has_no_cards():
        print(f'Player {player_one.name}, out of Cards, Player {player_two.name} Wins!')
        game_on = False
        break

    if player_two.has_no_cards():
        print(f'Player {player_two.name}, out of Cards, Player {player_one.name} Wins!')
        game_on = False
        break

    # Start a new round
    player_one.shuffle_cards()
    player_two.shuffle_cards()

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:

            player_one.add_cards(player_one_cards + player_two_cards)
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:

            player_two.add_cards(player_one_cards + player_two_cards)
            at_war = False

        else:
            print('WAR!')

            if len(player_one.all_cards) < cards_needed_for_war:
                print(f'Player {player_one.name} unable to declare war.\nPlayer {player_two.name} wins!')
                game_on = False
                break

            elif len(player_two.all_cards) < cards_needed_for_war:
                print(f'Player {player_two.name} unable to declare war.\nPlayer {player_one.name} wins!')
                game_on = False
                break

            else:
                for num in range(cards_needed_for_war):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())


