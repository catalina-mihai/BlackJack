import deck


class Player:
    """A class for player having a value and the option to ask for a card """
    def __init__(self):
        self.score = 0

    def draw(self):
        self.score += deck.deal()

