import deck
from deck import Deck
from logic import Logic
def main():
    user_input = input('Would you like to play a game of Blackjack?\n y/n ')
    if user_input == 'n':
        pass
    else:
        playerScore = 0
        dealerScore = 0
        logic = Logic()
        # deck = Deck()
        logic.deck.cards_count()
        dealt_card = logic.deck.deal()
        print(f'You are dealt a {dealt_card}')
        print(f'Your score is {dealt_card.rank}')
        print('The remaining cards in the deck are:')
        for card in logic.deck.deck:
            print(card)
        logic.deck.cards_count()
    userInput = input('Would you like to receive one more card?\n y/n ')
    if userInput == 'y':
        dealt_card = logic.deck.deal()
        playerScore = playerScore + dealt_card.rank
        print(f'You are dealt a {dealt_card}')
    else:
        print('You chose not to get a new card')
    deck.cards_count()




if __name__ == '__main__':
    main()

