import random as rand
from card import Card
class Deck:
    """Defining the class Deck, returning a shuffled deck of 52 cards"""
    suits = ['heart', 'spade', 'diamond', 'club']
    ranks = [{"rank": "2", "value": "2"},
                 {"rank": "3", "value": "3"},
                 {"rank": "4", "value": "4"},
                 {"rank": "5", "value": "5"},
                 {"rank": "6", "value": "6"},
                 {"rank": "7", "value": "7"},
                 {"rank": "8", "value": "8"},
                 {"rank": "9", "value": "9"},
                 {"rank": "10", "value": "10"},
                 {"rank": "J", "value": "10"},
                 {"rank": "Q", "value": "10"},
                 {"rank": "K", "value": "10"},
                 {"rank": "A", "value": "11"}]
    def __init__(self):
        self.deck = []
        self.build_deck()
        self.shuffle()

    def build_deck(self):
        for rank in self.ranks:
            for suit in self.suits:
                self.deck.append(Card(rank, suit))

    def shuffle(self):
        if len(self.deck) > 1:
            rand.shuffle(self.deck)

    def deal(self):
        """A method that deals one card and pops it from the deck"""
        try:
            dealtCard = self.deck.pop()
        except IndexError:
            return print("Not enough cards in the deck to deal the card")
        else:
            return dealtCard
    def cards_count(self):
        print(f"Deck of {len(self.deck)} cards")


