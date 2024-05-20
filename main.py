import random as rand
class Card:
    """ Defining the class Card with a string return describing the card"""
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"

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

    def deal(self, number):
        """A method that deals a number of cards"""
        try:
            dealt_cards = []
            for _ in range(number):
                dealt_cards.append(self.deck.pop())
        except IndexError:
            return print("Not enough cards in the deck to deal the requested number of cards")
        else:
            return dealt_cards
    def cards_count(self):
        print(f"Deck of {len(self.deck)} cards")


