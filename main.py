# author(s): darion
# project: black jack card game

import random

class Card():
    
    # card initializer
    def __init__(self, suit, rank, unicode_value):
        self.suit = suit
        self.rank = rank
        self.unicode_value = unicode_value

    def __str__(self):
        return(self.rank + " of " + self.suit)

class Deck():

    # deck initializer
    def __init__(self):

        self.cards = []
                
        # https://en.wikipedia.org/wiki/Playing_cards_in_Unicode
        unicode_values = [
            "\U0001F0A1", "\U0001F0A2", "\U0001F0A3", "\U0001F0A4", "\U0001F0A5", "\U0001F0A6", "\U0001F0A7",
            "\U0001F0A8", "\U0001F0A9", "\U0001F0AA", "\U0001F0AB", "\U0001F0AD", "\U0001F0AE", "\U0001F0B1",
            "\U0001F0B2", "\U0001F0B3", "\U0001F0B4", "\U0001F0B5", "\U0001F0B6", "\U0001F0B7", "\U0001F0B8",
            "\U0001F0B9", "\U0001F0BA", "\U0001F0BB", "\U0001F0BD", "\U0001F0BE", "\U0001F0C1", "\U0001F0C2",
            "\U0001F0C3", "\U0001F0C4", "\U0001F0C5", "\U0001F0C6", "\U0001F0C7", "\U0001F0C8", "\U0001F0C9",
            "\U0001F0CA", "\U0001F0CB", "\U0001F0CD", "\U0001F0CE", "\U0001F0D1", "\U0001F0D2", "\U0001F0D3",
            "\U0001F0D4", "\U0001F0D5", "\U0001F0D6", "\U0001F0D7", "\U0001F0D8", "\U0001F0D9", "\U0001F0DA",
            "\U0001F0DB", "\U0001F0DD", "\U0001F0DE"]

        # spades, hearts, diamonds, clubs
        suits = ["\u2660", "\u2665", "\u2666", "\u2663"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        
        i = 0
        for suit in suits:
            for rank in ranks:
                
                self.cards.append(Card(suit, rank, unicode_values[i])
                i += i + 1
