# Shir Nava
# CS-UY 1114
# December 10 2018
# Final project

import turtle
import time
import random

# This list represents the board. It's a list
# of nine strings, each of which is either
# "X", "O", "_", representing, respectively,
# a position occupied by an X, by an O, and
# an unoccupied position. The first three
# elements in the list represent the first row,
# and so on. Initially, all positions are
# unoccupied.
the_board = [ "_", "_", "_",
              "_", "_", "_",
              "_", "_", "_"]
gameOver=False; #global variable that is updated according to the state of the game

def draw_board(board):
    """
    signature: list(str) -> NoneType
    Given the current state of the game, draws
    the board on the screen, including the
    lines and the X and O pieces at the position
    indicated by the parameter.
    Hint: Write this function first!
    """
    turtle.resetscreen()
    turtle.ht()
    wind=turtle.Screen()
    wind.title("Tic Tac Toetle")
    wind.setup(width=610, height=610) #window dimensions setup
    turtle.penup() 
    turtle.left(90) #positioning Turtle to draw first grid lines
    turtle.forward(375)
    turtle.left(90)
    turtle.forward(102)
    turtle.left(90)
    drawGridLines()
    
    turtle.right(90) #repositioning Turtle to where it starts drawing the next grid lines
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(272)
    turtle.right(90)
    drawGridLines()
    #all grid lines have been drawn
    
    tcoord=[(-104.0,301.0),(96.0,301.0),(296.0,301.0),(-104.0,101.0),(96.0,101.0),(296.0,101.0),(-104.0,-100.0),(96.0,-100.0),(296.0,-100.0)]
    #tcoord-coordinates of top right corner of each grid box
    #drawing of X or O starts from those coordinates
    
    for i in range(len(board)):
        turtle.penup()
        turtle.goto(tcoord[i][0],tcoord[i][1]) #goes over the board list and turtle head goes to each grid top right corner coordinate
        turtle.ht()
        turtle.speed(0)
        turtle.setheading(0)
        if board[i]=="X": #if there's an "X" in the list, draws an X in the corresponding place with Turtle
            turtle.pendown()
            turtle.color("red")
            turtle.width(3)
            turtle.right(135)
            turtle.forward(278)
            turtle.penup()
            turtle.left(135)
            turtle.forward(196)
            turtle.left(135)
            turtle.pendown()
            turtle.forward(278)
        elif board[i]=="O": #if there's an "O" in the list, draws an O in the corresponding place with Turtle
            turtle.color("green")
            turtle.penup()
            turtle.right(90)
            turtle.forward(98)
            turtle.width(3)
            turtle.pendown()
            turtle.circle(-98)
    turtle.update()

def drawGridLines():
    """
    signature: () -> NoneType
    Function draws the lines of the Tic Tac Toe grid using turtle graphics,
    starts drawing from where the Turtle is before calling the function.

    """
    turtle.pd()
    turtle.forward(700)
    turtle.left(90)
    turtle.pu()
    turtle.forward(200)
    turtle.left(90)
    turtle.pd()
    turtle.forward(700)
    turtle.pu()

    

def do_user_move(board, x, y):
    """
    signature: list(str), int, int -> bool
    Given a list representing the state of the board
    and an x,y screen coordinate pair indicating where
    the user clicked, update the board
    with an O in the corresponding position. Your
    code will need to translate the screen coordinate
    (a pixel position where the user clicked) into the
    corresponding board position (a value between 0 and
    8 inclusive, identifying one of the 9 board positions).
    The function returns a bool indicated if
    the operation was successful: if the user
    clicks on a position that is already occupied
    or outside of the board area, the move is
    invalid, and the function should return False,
    otherise True.
    Function also clears the board when the game is over
    after the user clicks on the board.
    """
    global gameOver
    global the_board
    boxDimens=[(-303,102,-103,304),(-103,102,100,304),(100,102,297,304),(-303,-98,-103,102),(-103,-98,100,102),(100,-98,297,102),(-303,-294,-103,-98),(-103,-295,100,-98),(100,-294,297,-98)]
    #boxDimens is a list of tuples that specifies the bottom left and top right corner coordinates for the boxes(in order, index goes with the box index in the_board)
    #to check if the click was in range. The list contains the tuples (x1,y1,x2,y2), x1,y1- bottom left, x2,y2-top right
    
    print("user clicked at "+str(x)+","+str(y))
    if -318>x>290 or -320>y>269:
        return False
    for i in range(len(board)):
        if boxDimens[i][0]<=x<=boxDimens[i][2] and boxDimens[i][1]<=y<=boxDimens[i][3]:
            if board[i]=="_"and gameOver==False: #if there's an underscore and game isn't over, place O in board list
                board[i]="O"
                return True
            else:
                if gameOver==True: #if game is over and user clicked on board, clears the board and returns the state of the game to incomplete
                    the_board = [ "_", "_", "_",
                              "_", "_", "_",
                              "_", "_", "_"]
                    draw_board(the_board)
                    gameOver=False
                return False #returns false since no O was placed in board list
    

def check_game_over(board):
    """
    signature: list(str) -> bool
    Given the current state of the board, determine
    if the game is over, by checking for
    a three-in-a-row pattern in horizontal,
    vertical, or diagonal lines; and also if the
    game has reached a stalemate, achieved when
    the board is full and no further move is possible.
    If there is a winner or if there is a stalemate, display
    an appropriate message to the user. If the game is over,
    return True, otherwise False.
    """
    global gameOver
    for i in range(0,7,3): #iterates through rows
        row=board[i:i+3]
        if checkIfOver(row): #if the row is full with the same type of character(not space), game is over
            return True
    for i in range(3): #iterates through columns
        row=board[i:len(board):3]
        if checkIfOver(row):
            return True
    row=board[::4] #iterates through diagonal
    if checkIfOver(row):
        return True
    row=board[2:7:2] #iterates through diagonal
    if checkIfOver(row):
        return True
    for i in range(len(board)):  
        if board[i]=="_":
            return False #game is not over if no rows are full with either O or X, and at least one place has an underscore
    print("No Winner!")#if there are no won rows and no more underscores on board, stalemate
    turtle.penup()
    turtle.home()
    turtle.color('#ffd633')
    turtle.write("Stalemate! NO WINNER!",False,align="center",font=("Arial", 35, "bold"))#ADD- display that on turtle as well
    turtle.pu()
    turtle.right(90)
    turtle.forward(15)
    turtle.color("black")
    turtle.write("(click to start over)",False,align="center",font=("Arial", 10, "bold"))
    gameOver=True
    return True;
   
    
def checkIfOver(arr):
    """
    signature: list(str) -> bool
    function recieves list containing 3 values
    representing a specific row/column/diagonal
    (sliced from the the board) and checks if
    there are any different values(or if they are underscores),
    if not it declares the game as over, somebody having won
    """
    win=True
    global gameOver
    for i in range(len(arr)-1):
        if arr[i]!=arr[i+1] or arr[i]=="_" or arr[i+1]=="_":#goes over arr, if there are any underscores in it or if one value doesn't equal the other, row hasn't been won
            win=False
    if win: #if win remained True, someone has won the game. Game is over, and a message is displayed according to who won
        gameOver=True
        print("player "+arr[0]+" has won")
        turtle.penup()
        turtle.home()
        turtle.color('#ffd633')
        if arr[0] == "X":
            turtle.write("Oh no, YOU LOSE! :''(",False,align="center",font=("Arial", 35, "bold"))
        else:
            turtle.write("WOW, YOU WIN!! :D",False,align="center",font=("Arial", 35, "bold"))
        turtle.pu()
        turtle.right(90)
        turtle.forward(15)
        turtle.color("black")
        turtle.write("(click to start over)",False,align="center",font=("Arial", 10, "bold"))
    return win #returns if the game was won or not
            
    

def do_computer_move(board):
    """
    signature: list(str) -> NoneType
    Given a list representing the state of the board,
    select a position for the computer's move and
    update the board with an X in an appropriate
    position. The algorithm for selecting the
    computer's move shall be as follows: if it is
    possible for the computer to win in one move,
    it must do so. If the human player is able 
    to win in the next move, the computer must
    try to block it. Otherwise, the computer's
    next move may be any random, valid position
    (selected with the random.randint function).
    """
    #checking if comp or user is about to win
    if checkIfWinning(board,"X")!=1:#checking for X(first has to check if it's about to win!), if checkIfWinning returns 1 then the computer already did a move
        if checkIfWinning(board,"O")!=1:#checking for O
            pos=random.randint(0,8) 
            while(board[pos]!="_"):
                pos=random.randint(0,8)#while the randomly chosen position is taken on the board, generate another random position
            board[pos]="X" #if theres no place where user or computer is about to win, do random move

        
def checkIfWinning(board,player):
    """
    signature: list(str), string -> int
    goes over entire board by rows, columns and
    diagonals and checks if there a row where theres
    only one underscore left(calls function checkSpace),
    if there is, checks if the player specified is the
    one winning and if yes, places an X in the place where
    the space is. if not keeps on looking and if none
    of them, returns -1
    """
    for i in range(0,len(board),3): #iterates through rows
        placenum=checkSpace(board,i,i+1,i+2)
        if placenum!=-1 and (board[i]==player or board[i+1]==player): #if there's only one underscore left and the other values in row = player value
            board[placenum]="X"
            return 1
    for i in range(3):
        placenum=checkSpace(board,i,i+3,i+6) #iterates through columns
        if placenum!=-1 and(board[i]==player or board[i+3]==player): #if there's only one sunderscore left and the other values in row = player value
            board[placenum]="X"
            return 1
    placenum=checkSpace(board,0,4,8) #checks diagonal
    if placenum!=-1 and(board[0]==player or board[4]==player): #if there's only one underscore left and the other values in row = player value
        board[placenum]="X"
        return 1
    placenum=checkSpace(board,2,4,6) #checks other diagonal
    if placenum!=-1 and(board[2]==player or board[4]==player): #if there's only one underscore left and the other values in row = player value
        board[placenum]="X"
        return 1
    return -1 #if nobody's almost winning return -1

def checkSpace(board,in1,in2,in3):
    """
    signature: list(str), int, int, int -> int
    function returns the index of underscore if there's
    exactly one underscore left, if not returns -1
    """
    numspace=0;
    place=0;
    inlst=[in1,in2,in3] #list of indexes
    for i in range(len(inlst)):
        if(board[inlst[i]]=="_"): #if there's an underscore, increments numspace by 1, index of underscore is recorded in "place" 
            numspace+=1
            place=inlst[i]
    if numspace==1 and (board[in1]==board[in2] or board[in1]==board[in3] or board[in2]==board[in3]):
        #if there's only one underscore left and also the other two values in row are the same, return the place of the underscore
        return place
    else:#returns -1 if theres more than one underscore in the row or if there's one underscore but the other values in row aren't equal to each other
        return -1
            
def clickhandler(x, y):
    """
    signature: int, int -> NoneType
    This function is called by turtle in response
    to a user click. The parameters are the screen
    coordinates indicating where the click happened.
    The function will call other functions. You do not
    need to modify this function, but you do need
    to understand it.
    """
    if do_user_move(the_board,x,y):
        draw_board(the_board)
        if not check_game_over(the_board):
            do_computer_move(the_board)
            draw_board(the_board)
            check_game_over(the_board)

def main():
    """
    signature: () -> NoneType
    Runs the tic-tac-toe game. You shouldn't
    need to modify this function.
    """
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onscreenclick(clickhandler)
    draw_board(the_board)
    turtle.mainloop()

main()
