import random
from random import randint
from classes.deck import Deck
from classes.card import Card

"""
split the deck -- first step
each player draws one card -- "face down"
the players then flip their cards and reveal their power
the player(s) with the highest nymber wins, and takes both cards
if both cards are the same, it is "war"
        ->> each player turns a card up and one card down, the player with the higher card takes both piles
"""

bicycle = Deck()

# bicycle.show_cards()

cards = Card(random, random, random)

my_cards, opp_cards = bicycle.split_deck()


# test for printing out each deck
# print(repr(my_cards))
# print(repr(opp_cards))

def draw_cards(cards):
        return cards.pop(0)

def play_turn(mine = my_cards, opp = opp_cards):
        my_play = draw_cards(mine)
        opp_play = draw_cards(opp)
        my_value = cards.point_val 
        print(my_value)
        

play_turn()

# option = input("select an option! -- ") 

# while option != '0':
#         if option == '1':
#                 pass
#         elif option == '2':
#                 pass
#         elif option > '2':
#                 print("please press 1 or 2")

#         option = input ("press '1' for player 1's turn, and press '2' for player 2's turn: ")













