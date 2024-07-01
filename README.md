</p>
<h1 align="center"> Blackjack </h1>

<p align="center"> 
  <img src="blackjack.jpg" alt="Animated gif pacman game" height="282px" width="637">
</p>


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- ABOUT THE PROJECT -->
<h2 id="about-the-project"> :pencil: About The Project</h2>

<p align="justify"> 
  For those of you not familiar with Blackjack, or 21 it's a casino card where your aim as a player is to beat the dealer by getting a hand value close to 21 without exceeding it. Number cards are worth their face value, face cards 10 points, and Aces 1 or 11 points

</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- OVERVIEW -->
<h2 id="overview"> :cloud: Overview</h2>

<p align="justify"> 

  ![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!--   The house rules for this Blackjack project are: -->
<h2 id="project-files-description"> :floppy_disk: Project Files Description</h2>

<ul>
  <li><b>Only one deck is used, of a total of 52 cards. </b> 
  <li><b>There are no jokers</b> 
  <li><b>The Jack/Queen/King all count as 10.</b> - 
  <li><b>The the Ace can count as 11 or 1.</b> 
  <li><b>Cards are removed from the deck as they are drawn.</b> 
  <li><b>The cards have equal probability of being drawn.</b> 
</ul>




</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- PROJECT FILES DESCRIPTION -->
<h2 id="project-files-description"> :floppy_disk: Project Files Description</h2>

<ul>
  <li><b>logic.py</b> - Manages the overall Blackjack game logic.</li>
  <li><b>playerHand.py</b> - Represents the player's hand of cards, managing dealt cards and calculating their value.</li>
  <li><b>dealerHand.py</b> - Represents the dealer's hand of cards, managing dealt cards and calculating their value.</li>
  <li><b>deck.py</b> - Represents a deck of cards, which can be shuffled and dealt.</li>
  <li><b>card.py</b> - Represents a playing card with a suit and rank.</li>
  <li><b>main.py</b> - The main part of the script creates a Logic object and calls its start method to start the game. The start method prompts the user to say whether they would like to play or not, then plays each game by dealing two cards to both the player and the dealer, allowing the player to hit or stand, and determining the winner based on the final hand values.</li>

</ul>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- GETTING STARTED -->
<h2 id="getting-started"> :book: Getting Started</h2>

<p>You are able to start the game by typing the following commands in the command line:</p>
<pre><code>$ python main.py</code></pre>

<p>You can see the list of all options and their default values via:</p>
<pre><code>$ python main.py -h</code></pre>


To clone the repository and run it locally, follow these steps:
1) Open your terminal or command prompt. <br>
2) Navigate to the directory where you want to clone the repository using the cd command. <br> 
3) Use the git clone command:<br>
'https://github.com/tommydrengen/BlackJack.git'
4) Once the repository is cloned, navigate into the repository directory using the cd command. <br>
5) You can now run the script locally. Depending on the programming language, you might need to have the necessary runtime or dependencies installed on your system. <br>
6) Execute the script using the appropriate command or interpreter for the specific language. For example, if it's a Python script, you can run it using the python command followed by the script name:

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- SCENARIO1 -->
<h2 id="scenario1"> :small_orange_diamond: Scenario 1: Finding a Fixed Food Dot using Depth First Search</h2>

<p>I have implemented the depth-first search (DFS) algorithm in the depthFirstSearch function in <code>search.py</code>.</p>
<p>TThis Python script implements a text-based Blackjack game with several classes:


:</p>


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- CREDITS -->
<h2 id="credits"> :scroll: Credits</h2>

Oana-Catalina Mihai and Thomas Halkier Nikolajsen

[![GitHub Badge](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Catalina-Mihai)
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/catalina-oana-m/)

[![GitHub Badge](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/tommydrengen/)
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/thomas-halkier-nicolajsen-60b7a4126/)





<p align="center"> 
  <img src="gif/Pacman Logo2.jpg" alt="Pacman Logo" width="80px" height="80px">
</p>
<h1 align="center"> Pacman Agent </h1>
<h3 align="center"> COMP 6721 - Artificial Intelligence </h3>
<h5 align="center"> Project Assignment 1 - <a href="https://www.concordia.ca/">Concordia University</a> (Winter 2020) </h5>

<p align="center"> 
  <img src="gif/pacman_game.gif" alt="Animated gif pacman game" height="282px" width="637">
</p>

<!-- TABLE OF CONTENTS -->
<h2 id="table-of-contents"> :book: Table of Contents</h2>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project"> ➤ About The Project</a></li>
    <li><a href="#overview"> ➤ Overview</a></li>
    <li><a href="#project-files-description"> ➤ Project Files Description</a></li>
    <li><a href="#getting-started"> ➤ Getting Started</a></li>
    <li><a href="#scenario1"> ➤ Scenario 1: Depth First Search </a></li>
    <li><a href="#scenario2"> ➤ Scenario 2: Breadth First Search </a></li>
    <li><a href="#scenario3"> ➤ Scenario 3: Uniform Cost Search </a></li>
    <li><a href="#scenario4"> ➤ Scenario 4: A* search algorithm </a></li>
    <li><a href="#scenario5"> ➤ Scenario 5: Finding All Corners </a></li>
    <li><a href="#scenario6"> ➤ Scenario 6: Admissible and Consistent Heuristic </a></li>
    <li><a href="#scenario7"> ➤ Scenario 7: Eating All Dots </a></li>
    <li><a href="#scenario8"> ➤ Scenario 8: Suboptimal Search </a></li>
    <li><a href="#references"> ➤ References</a></li>
    <li><a href="#credits"> ➤ Credits</a></li>
  </ol>
</details>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- ABOUT THE PROJECT -->
<h2 id="about-the-project"> :pencil: About The Project</h2>

<p align="justify"> 
  For those of you not familiar with Pacman, it's a game where Pacman (the yellow circle with a mouth in the above figure) moves around in a maze and tries to eat as many food pellets (the small white dots) as possible, while avoiding the ghosts (the other two agents with eyes in the above figure). If Pacman eats all the food in a maze, it wins.
</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- OVERVIEW -->
<h2 id="overview"> :cloud: Overview</h2>

<p align="justify"> 
  In this project, the Pacman agent will find paths through his maze world, both to reach a particular location and to collect food efficiently. I implemented general search algorithms such as depth-first, breadth-first, uniform cost, and A* search algorithms which are used to solve navigation problems in the Pacman world.
</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- PROJECT FILES DESCRIPTION -->
<h2 id="project-files-description"> :floppy_disk: Project Files Description</h2>

<ul>
  <li><b>search.py</b> - Where all of the search algorithms reside.</li>
  <li><b>searchAgents.py</b> - Where all of the search-based agents reside.</li>
  <li><b>pacman.py</b> - The main file that runs Pacman games. This file also describes a Pacman GameState types.</li>
  <li><b>game.py</b> - The logic behind how the Pacman world works.</li>
  <li><b>util.py</b> - Useful data structures for implementing search algorithms.</li>
</ul>

<h3>Some other supporting files</h3>
<ul>
  <li><b>graphicsDisplay.py</b> - Graphics for Pacman.</li>
  <li><b>graphicsUtils.py</b> - Support for Pacman graphics.</li>
  <li><b>textDisplay.py</b> - ASCII graphics for Pacman.</li>
  <li><b>ghostAgents.py</b> - Agents to control ghosts.</li>
  <li><b>keyboardAgents.py</b> - Keyboard interfaces to control Pacman.</li>
  <li><b>layout.py</b> - Code for reading layout files and storing their contents.</li>
  <li><b>autograder.py</b> - Project autograder.</li>
  <li><b>testParser.py</b> - Parses autograder test and solution files.</li>
  <li><b>testClasses.py</b> - General autograding test classes.</li>
  <li><b>test_cases/</b> - Directory containing the test cases for each scenario.</li>
  <li><b>searchTestClasses.py</b> - Project specific autograding test classes.</li>
</ul>

