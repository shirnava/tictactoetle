# MyProjects
Projects
Name: Shir Nava
NetID: Sn2571
Section: EXL2

##-State of assignment: Complete

My project completely meets the project requirements. Artistic liberties that I implemented were changing the colors 
of the X's, O's and game over/winner messages to fit a Christmas theme(red, green and yellow).
An additional feature I implemented was in order to start a new game you click on the board and only then it resets.
(It also displays a message telling the user to click in order to restart the game)
I would have liked to create the more complex algorithm for the computer AI but due to time constraints I wasn't able to.
I'm very satisfied with the final result!

-My retrospective on the development process:
The most challenging part for me was eliminating repetitive code, as I previously had many repetitive parts. But I found a way to 
eliminate those parts through the use of functions and loops.
The part of the assignment that was easier than I expected was drawing the X's and O's, I dreaded that part but my solution 
wasn't very difficult to come up with. Turtle graphics has never been my strong suit, but I quickly learned how to deal with it.
I'm proud of the CheckGameOver function! I first approached it in a different way and then thought of slicing the list, which was much easier.

-Additional thoughts:
The instructions were clear except I would have liked to be given a certain guideline for the window size, I wasn't really sure what to make it at first
and I wasn't sure if it mattered that much since the window is maximizable either way.
The assignment was very interesting! I didn't know I would be able to create a game using Turtle so successfully creating one was very satisfying.
This project has given me insight on the endless possibilities in the hands of programmers, and the process of creation and usage of a complex algorithm.

-Additional functions I created: checkIfOver, checkIfWinning, checkSpace

-Computer Algorithm: do_computer_move: the function first uses the checkIfWinning function to check if there are rows/columns/diagonals on 
grid where there are two X's in one row and one underscore(checkIfWinning does that using function checkSpace), and if there are, 
an X is placed in the row where the underscore is(to win the game). 
If there isn't any instance where computer is about to win, it checks if there are rows where there are two O's
(and one underscore), signaling the player O is about to win, and if yes places an X where the underscore is (blocking the 
user from winning). All of this is done with the use of the checkIfWinning function, which given the board and the player("X" or "O") checks
if the given player is about to win and if yes places the "X" in the correct spot(as explained above).
The function checkSpace that checkIfWinning uses gets the board and three indexes and checks if there is only one space 
left between the three boxes.(one slot that isn't taken) This function returns -1 if there is more than one space
or there's one space but the rest of the values in the row aren't equal, so the computer "knows" 
it doesn't need to occupy a space there to block a move.

checkIfOver is a function that checks if a given list of values contains values that are equal and aren't underscores
(list of 3 that represents a row or column or diagonal) If it does, it declares the game as over and displays winner/loser messages.
(updates gameOver global variable)
