from deck import Deck
def main():
    user_input = input('Would you like to play a game of Blackjack? y/n')
    if user_input == 'n':
        pass
    else:
        deck = Deck()
        deck.cards_count()
        dealt_cards = deck.deal(2)
        for card in dealt_cards:
            print(f'You are dealt a {card}')
        print('The remaining cards in the deck are:')
        for card in deck.deck:
            print(card)
        deck.cards_count()
    user = input('Would you like to receive one more card? y/n')
    if user == 'y':
        dealt_card = deck.deal(1)
        print(f'You are dealt a {card}')
    else:
        print('You chose not to get a new card')
    deck.cards_count()




if __name__ == '__main__':
    main()

