import random
from deck import Deck
from player import Player
from card import Card
from enums.cardValue import CardValue
from enums.playerstatus import PlayerStatus
from enums.suit import Suit

myDeck = Deck()

cards = [Card(CardValue.TWO, Suit.DIAMONDS), Card(CardValue.ACE, Suit.HEARTS),
         Card(CardValue.THREE, Suit.CLUBS)]

player1 = Player("Player 1")

player1.accept_card(Card(CardValue.TWO, Suit.DIAMONDS))
player1.accept_card(Card(CardValue.THREE, Suit.DIAMONDS))

print("Total value of cards;",  player1.get_total_cards_value())

print("Player Status", player1.get_player_status())

print("Cards in hand ", player1.get_cards_in_hand())