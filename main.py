from deck import Deck
def main():
    deck = Deck()
    deck.cards_count()
    dealt_card = deck.deal(2)
    for card in dealt_card:
        print(f'You are dealt a {card}')
    print('The remaining cards in the deck are:')
    for card in deck.deck:
        print(card)
    deck.cards_count()


if __name__ == '__main__':
    main()