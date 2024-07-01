# Python-Blackjack-game

To clone the repository and run it locally, follow these steps:
1) Open your terminal or command prompt. <br>
2) Navigate to the directory where you want to clone the repository using the cd command. <br> 
3) Use the git clone command:<br>
'https://github.com/tommydrengen/BlackJack.git'
4) Once the repository is cloned, navigate into the repository directory using the cd command. <br>
5) You can now run the script locally. Depending on the programming language, you might need to have the necessary runtime or dependencies installed on your system. <br>
6) Execute the script using the appropriate command or interpreter for the specific language. For example, if it's a Python script, you can run it using the python command followed by the script name:

<hr>
Introduction to Blackjack:

Blackjack, or 21, is a casino card game where players aim to beat the dealer by getting a hand value close to 21 without exceeding it. Number cards are worth their face value, face cards 10 points, and Aces 1 or 11 points

# Final code
This Python script implements a text-based Blackjack game with several classes:

Card: Represents a playing card with a suit and rank.
Deck: Represents a deck of cards, which can be shuffled and dealt.
Hand: Represents a hand of cards, managing dealt cards and calculating their value.
Logic: Manages the overall Blackjack game logic.
'checkWinner' function determines the winner based on the player's and dealer's hand values.
https://github.com/tommydrengen/BlackJack/blob/main/card.py

https://github.com/tommydrengen/BlackJack/blob/main/card.pyL1-L5

The main part of the script creates a Logic object and calls its start method to start the game. The start method prompts the user to say whether they would like to play or not, then plays each game by dealing two cards to both the player and the dealer, allowing the player to hit or stand, and determining the winner based on the final hand values.
