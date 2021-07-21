# Tic Tac Toe Christmas Edition
Tic Tac Toe one-player game written in Python using Turtle graphics. This game is Christmas themed for a special holiday twist! Make your holiday game dreams come true by playing this game and you might just be able to beat the computer player. Good luck! 🎅 


# Computer Player Algorithm and Additional Functions
do_computer_move: the function first uses the checkIfWinning function to check if there are rows/columns/diagonals on 
grid where there are two X's in one row and one underscore(checkIfWinning does that using function checkSpace), and if there are, 
an X is placed in the row where the underscore is(to win the game). 

If there isn't any instance where computer is about to win, it checks if there are rows where there are two O's
(and one underscore), signaling the player O is about to win, and if yes places an X where the underscore is (blocking the 
user from winning). All of this is done with the use of the checkIfWinning function, which given the board and the player("X" or "O") checks if the given player is about to win and if yes places the "X" in the correct spot(as explained above).
The function checkSpace that checkIfWinning uses gets the board and three indexes and checks if there is only one space 
left between the three boxes.(one slot that isn't taken) This function returns -1 if there is more than one space
or there's one space but the rest of the values in the row aren't equal, so the computer "knows" 
it doesn't need to occupy a space there to block a move.

checkIfOver is a function that checks if a given list of values contains values that are equal and aren't underscores
(list of 3 that represents a row or column or diagonal) If it does, it declares the game as over and displays winner/loser messages 
(updates gameOver global variable).
