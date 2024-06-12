from deck import Deck
def main():
    user_input = input('Would you like to play a game of Blackjack?\n y/n ')
    if user_input == 'n':
        pass
    else:
        deck = Deck()
        deck.cards_count()
        dealt_card = deck.deal()
        print(f'You are dealt a {dealt_card}')
        print('The remaining cards in the deck are:')
        for card in deck.deck:
            print(card)
        deck.cards_count()
    user = input('Would you like to receive one more card?\n y/n ')
    if user == 'y':
        dealt_card = deck.deal()
        print(f'You are dealt a {dealt_card}')
    else:
        print('You chose not to get a new card')
    deck.cards_count()




if __name__ == '__main__':
    main()

