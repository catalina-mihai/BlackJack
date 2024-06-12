import deck


class PlayerHand:
    """A class for player having a value and the option to ask for a card
     Take Ace into account
     """
    def __init__(self):
        self.score = 0
        self.cards = []

    def draw(self, dealtCard):
        self.cards.append(dealtCard)

    def score(self):
        self.score = 0
        hasAce = False
        for card in self.cards:
            self.score += card.rank["value"]
            if card.rank["rank"] == "A":
                hasAce = True
        if hasAce and self.score >21:
            self.score = self.score-10

    def isBlackJack(self):
        return self.score == 21

    def gameOver(self):
        return self.score > 21

    def diplay(self):
        print(self.score())
