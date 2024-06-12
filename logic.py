import playerHand
from deck import Deck
from playerHand import PlayerHand


class Logic:
    def __init__(self):
        deck = Deck() # Creates 52 cards and shuffles
        playerScore = 0
        dealerScore = 0
        #player hand and score
        dealtCard = Deck.deal()
        player.draw(dealtCard)
        playerScore += dealtCard.rank["value"]
        print(dealtCard)
        dealtCard = Deck.deal()
        playerScore += dealtCard.rank["value"]
        print(dealtCard)

        #dealer hand and score
        dealtCard = Deck.deal()
        dealerScore += dealtCard.rank["value"]
        print(dealtCard)
        dealtCard = Deck.deal()
        dealerScore += dealtCard.rank["value"]

    def checkWinner(self, playerHand, dealerHand):
        if playerHand.score == 21:
            print("Player wins")
        if dealerHand.score == 21:
            print("Dealer wins")

        if playerHand.PlayerHand.gameOver():
            print("Game Over: Player loses (over 21)")


    #Shuffle
    #Deal 2 cards to each
    #Check Blackjack
    #Check GameOver
    #Input Player (hit/keep) from Player
    #Input Dealer (hit/keep) >17
    #eval score
    #Win/Loss/Tie?
    #Input Player (play again?) from Player


