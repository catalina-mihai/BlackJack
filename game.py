from deck import Deck
from hand import Hand
class Game:
    def play(self):
        user_input = input('Would you like to play a game of Blackjack?\n Y,y/N,n ').lower().strip()
        while user_input == 'y':
            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))

            print()
            print("*" * 50)
            print(r"""  
 _     _              _      _             _     
| |   | |            | |    (_)           | |    
| |__ | | _____  ____| |  _  _ _____  ____| |  _ 
|  _ \| |(____ |/ ___) |_/ )| (____ |/ ___) |_/ )
| |_) ) |/ ___ ( (___|  _ ( | / ___ ( (___|  _ ( 
|____/ \_)_____|\____)_| \_)| \_____|\____)_| \_)
                          (__/                                    
                          """)
            print("*" * 50)
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                user_input = input('Would you like to play another game of Blackjack?\n Y,y/N,n ').lower().strip()
                continue

            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Please choose 'Hit' or 'Stand': ").lower().strip()
                print()
                while choice not in ["h", "s", "hit", "stand"]:
                    choice = input("Please enter 'Hit' or 'Stand' (or H/S) ").lower().strip()
                    print()
                if choice in ["hit", "h"]:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                user_input = input('Would you like to play another game of Blackjack?\n Y,y/N,n ').lower().strip()
                continue

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(show_all_dealer_cards=True)

            if self.check_winner(player_hand, dealer_hand):
                user_input = input('Would you like to play another game of Blackjack?\n Y,y/N,n ').lower().strip()
                continue

            print("Final Results")
            print("Your hand:", player_hand_value)
            print("Dealer's hand:", dealer_hand_value)

            self.check_winner(player_hand, dealer_hand, True)

            print("\nThanks for playing!")
            user_input = input('Would you like to play another game of Blackjack?\n Y,y/N,n ').lower().strip()
        print("\nGreat having you. Thanks for playing!")

    def check_winner(self, player_hand, dealer_hand, game_over=False):
        if not game_over:
            if player_hand.get_value() > 21:
                print("You busted. Dealer wins! 😭")
                return True
            elif dealer_hand.get_value() > 21:
                print("Dealer busted. You win! 😀")
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print("Both players have blackjack! Tie! 😑")
                return True
            elif player_hand.is_blackjack():
                print("You have blackjack. You win! 😀")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer has blackjack. Dealer wins! 😭")
                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You win! 😀")
            elif player_hand.get_value() == dealer_hand.get_value():
                print("Tie! 😑")
            else:
                print("Dealer wins. 😭")
            return True
        return False
