from deck import Deck


class Logic:
    def __init__(self):
        deck = Deck()
        player = Player()
        dealer = Dealer()
        playerScore = 0
        dealerScore = 0
        #player hand and score
        dealtCard = Deck.deal()
        playerScore += dealtCard
        print(dealtCard)
        dealtCard = Deck.deal()
        playerScore += dealtCard
        print(dealtCard)
        #dealer hand and score
        dealtCard = Deck.deal()
        dealerScore += dealtCard
        print(dealtCard)
        dealtCard = Deck.deal()
        dealerScore += dealtCard

    #Shuffle
    #Deal 2 cards to each
    #Check Blackjack
    #Check GameOver
    #Input Player (hit/keep) from Player
    #Input Dealer (hit/keep) >17
    #eval score
    #Win/Loss/Tie?
    #Input Player (play again?) from Player


