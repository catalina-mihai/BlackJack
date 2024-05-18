############### Thomas' and Catalina's Blackjack Project #####################


############### Our Blackjack House Rules #####################

## We play with just one deck of 52 cards.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1. -> The first ACE dealt is of value 11 and subsequent ACEs of value 1.
##                                   -> Should the score of a player exceed 21 then the value of the ACE is changed to 1.
## The cards in the list have equal probability of being drawn to begin with.
## But cards are removed from the deck as they are drawn.

## NOTE to the lead developer (aka Thomas :) ). When I am referring to 'dealer' I mean a virtual player for which the computer takes decisions.
# I also refer to the 'computer' and by computer I mean the program/mechanism and all code behind. So not to be confused with the dealer.
## Let me give you an example. When the 'computer' deals 2 cards to the player called 'dealer' it is the computer/mechanism that peaks
## into the cards dealt and checks automatically for blackjack. So the 'dealer-player' is blind to the card that is hidden.

##################### USER STORIES ##############

## nouns: the dealer, player, the computer, card, deck, score, hand, game
## verbs: start new game, end game, check score, check blackjack, check gameover, deal new card, print results

## As a player I want to draw more cards. So that my score gets closer to 21.
## As a player I want the highest score.
## As a player I want to keep the cards I have. So that I don't risk getting over 21 and so that I see the opponents cards
## As a player I want to restart the game.
## As a player I don't want to play another game.
## As a player I want to

## As a dealer I want to draw more cards if my score is under 17.
## As a dealer I want to keep the cards I have if my score is over 17.
## As a dealer

## As the computer ask for user input: 'Do you want to play a game of Blackjack?'
## As the computer deal randomly two cards to each player and extract them from the deck.
## As the computer add up the card values. So that you check the score.
## As the computer check both hands for game over.
## As the computer check both hands for blackjack.
## As the computer conceal one of the dealer's cards.
## As the computer print the cards dealt and current score.
## As the computer ask the player 'Type Y to get another card, type N to keep the cards you have.'
## As the computer compare scores. So that you determine winner.
## As the computer print the results of the game.
## As the computer ask player for input. So that you end the game or clear console for new game.

##################### STEPS #####################


## initialising steps:
## create a DECK and shuffle it
## after each step the score needs to update and be printed. Check for BlackJack or Game Over

## STEP 1: DEAL CARDS
## Deal 2 cards to player
## Deal 2 cards to dealer. One card is hidden but computer peaks for the next step where we check for Blackjack.

## STEP 2: BLACKJACK?
## If dealer was dealt a 10 card or ACE then computer checks for BLACKJACK. If BlackJAck -> check for TIE
## If player has BLACKJACK -> check for TIE
## (If the summed value of the cards is 21 then it's a BLACKJACK)
##Then reveal dealers cards too and check if it is a TIE (if both have blackjack)

## STEP 3. GAME OVER?
## A player is BUST or in other words the GAME is OVER when the score exceeds 21 points
## We check the player's score. If sum over 21 then we check for any ACEs.
## If there is an ACE we change the value of it from 11 to 1.
## If the sum of the player's score is still over 21 then the player loses the game regardless of the dealer's hand

## STEP 4. PLAYER'S TURN
## Ask for user input.

## STEP 5. DEALER'S TURN
## Once the user is done, it's time to let the dealer play. The dealer should keep drawing cards as long as it has a score less than 17.


## STEP 6. WIN, LOSS OR TIE?

## STEP 7. PLAY AGAIN?
## We ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


import random as rand
class Card:
    """ Defining the class Card with a string return describing the card"""
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"

class Deck:
    """Defining the class Deck, returning a shuffled deck of 52 cards"""
    suits = ['heart', 'spade', 'diamond', 'club']
    ranks = [{"rank": "2", "value": "2"},
                 {"rank": "3", "value": "3"},
                 {"rank": "4", "value": "4"},
                 {"rank": "5", "value": "5"},
                 {"rank": "6", "value": "6"},
                 {"rank": "7", "value": "7"},
                 {"rank": "8", "value": "8"},
                 {"rank": "9", "value": "9"},
                 {"rank": "10", "value": "10"},
                 {"rank": "J", "value": "10"},
                 {"rank": "Q", "value": "10"},
                 {"rank": "K", "value": "10"},
                 {"rank": "A", "value": "11"}]
    def __init__(self):
        self.deck = []
        self.build_deck()
        self.shuffle()

    def build_deck(self):
        for rank in self.ranks:
            for suit in self.suits:
                self.deck.append(Card(rank, suit))

    def shuffle(self):
        if len(self.deck) > 1:
            rand.shuffle(self.deck)

    def deal(self, number):
        """A method that deals a number of cards"""
        try:
            dealt_cards = []
            for _ in range(number):
                dealt_cards.append(self.deck.pop())
        except IndexError:
            return print("Not enough cards in the deck to deal the requested number of cards")
        else:
            return dealt_cards
    def cards_count(self):
        print(f"Deck of {len(self.deck)} cards")


