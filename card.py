class Card:
    """ Defining the class Card with a string return describing the card"""
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"
