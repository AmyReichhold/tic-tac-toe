# tic-tac-toe
### By Amy Reichhold

## How to run tic-tac-toe
On the command line, run the following command:
```
python3 main.py
```
The program will ask you if you would like to play single player or multi-
player by typing 'S' or 'M', respectively. Player 1 will then be prompted to 
choose 'X' or 'O' and Player 2 will be given the symbol that isn't chosen by 
player one. Once the game mode and player symbols are chosen, the game 
is started by displaying the game heading, instructions and an empty board.
The cells of the board grid are numbered as follows:
> &nbsp; 1 &nbsp;| &nbsp; 2 &nbsp;|&nbsp; 3 &nbsp;| \
> -------------- \
> &nbsp; 4 &nbsp;| &nbsp; 5 &nbsp;|&nbsp; 6 &nbsp;| \
> -------------- \
> &nbsp; 7 &nbsp;| &nbsp; 8 &nbsp;|&nbsp; 9 &nbsp;| 


## Multiplayer
The current player is prompted to choose a cell on the board by entering a
number from one to nine. The player has to enter a valid cell number, which
means the input has to be an integer from one to nine and there can't be an
existing player mark in the chosen cell. Once the player enters a valid cell
number, the program will first check for a win and if there is no winner, 
then it will check for a tie. If neither are found, then there are remaining 
moves to make. The program will switch the players, display an updated 
board and prompt the new player to choose a cell.


## Single player
The user is Player 1 and the computer is Player 2. If the current player is
Player 1, then the user is prompted to choose a cell on the board by entering 
a number from one to nine. As described above, Player 1 must enter a valid 
cell number. Once the player enters a valid cell number, the program will 
first check for a win and if no winner is found, then it will check for a tie.
If there is neither a win or tie, the program will switch the players and 
display an updated board. If the current player is Player 2, then the 
computer chooses a cell, and the game proceeds as described previously.
> ### The aiMove function\
> The purpose of the function is to find the best cell for the AI to place\
> its mark. The function uses exhaustive search and loops through the\
> numbered cells in ascending order, starting at cell one in the top-left\
> corner of the board grid. At each cell, we first check if the AI will win\
> by placing a mark. If the AI will win, then we place the AI’s mark and the\ 
> game is over. If the AI will not win, then we check if Player 1 will win by\ 
> placing a mark. If Player 1 will win, then the AI will place a mark to\
> prevent Player 1 from winning. If Player 2 will not win, then we will move\ 
> on to the next cell. If we have looped through every cell and no marks were\ 
> placed, then the AI places a mark in the first open cell.

This project is a simple object-oriented game programmed in Python. The 
purpose of the project was to create a game that features both single player 
and multiplayer options and to get additional practice working with classes. 
I thought it would be fun to explore the single player version and create my 
own AI function.


### Future work
I would like to review my Game Theory class and find an applicable algorithm
to implement in place of my AI function. My function doesn't take a traditional
game theory approach by weighing the gains and losses of every decision. If
there will not be a win for either player, my approach places a mark for the
AI at the first open cell. I would like to implement an algorithm that will
find the best cell based on gains and losses.

