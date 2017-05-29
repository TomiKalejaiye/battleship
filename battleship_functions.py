# -*- coding: utf-8 -*-
"""
Created on Sat May 27 11:16:00 2017

@author: Tomi
"""

def print_board(board):
    for row in board:
        print (" ".join(row))
        
def placeship(shiprow, shipcol, orientation):
    
    if (orientation == True) and ((shiprow in {0,4}) == False):
        shiprow2 = shiprow + 1
        shiprow3 = shiprow - 1
        return shiprow2,shiprow3
        
    if orientation == False and ((shipcol in {0,4}) == False):
        shipcol2 = shipcol + 1
        shipcol3 = shipcol - 1
        return shipcol2,shipcol3
            
    if (orientation == True) and (shiprow == 0):
        shiprow2 = shiprow + 1
        shiprow3 = shiprow + 2
        return shiprow2,shiprow3
    
    if (orientation == True) and (shiprow == 4):
        shiprow2 = shiprow - 1
        shiprow3 = shiprow - 2
        return shiprow2,shiprow3

    if (orientation == False) and (shipcol == 0):
        shipcol2 = shipcol + 1
        shipcol3 = shipcol + 2
        return shipcol2,shipcol3
        
    if (orientation == False) and (shipcol == 4):
        shipcol2 = shipcol - 1
        shipcol3 = shipcol - 2
        return shipcol2,shipcol3
        
def check(board,guess_row,guess_col,rlrow,rlcol,rlrow2,rlrow3,rlcol2,rlcol3):
    if(board[guess_row][guess_col] == "X") or board[guess_row][guess_col] == "#" :
            print ("You guessed that one already.")
            return 0

    elif (guess_row in {rlrow, rlrow2, rlrow3}) and (guess_col in {rlcol, rlcol2, rlcol3}):
        board[guess_row][guess_col] = "#"
        print ("Boom! Thats a hit!")
        return 1
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print ("Oops, that's not even in the ocean.")
        else:
            print ("Oops! Thats a miss!")
            board[guess_row][guess_col] = "X"
        
        return 0