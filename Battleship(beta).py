import random as rnd
from random import randint
from Functions.battleship_functions import check
from Functions.battleship_functions import print_board
from Functions.battleship_functions import placeship

board1 = []

for x in range(5):
    board1.append(["O"] * 5)

board2 = []

for x in range(5):
    board2.append(["O"] * 5)

print ("Let's play Battleship!")
print ("Computer")
print_board(board1)
print ("")
print ("-------")
print ("")
print ("Human")
print_board(board2)
print ("")

print ("Place your ship. Go on I won't look. Pick the coordinates, and the orientation (vertical or horizontal)")

urship_row = int((input("Row:"))) - 1
urship_col = int((input("Col:"))) - 1
urorientation =  input("Orientation:") == "vertical"
if urorientation == True:
    urship_row2,urship_row3 = placeship(urship_row,urship_col,urorientation)
    urship_col2 = urship_col
    urship_col3 = urship_col
if urorientation == False:
    urship_col2,urship_col3 = placeship(urship_row,urship_col,urorientation)
    urship_row2 = urship_row
    urship_row3 = urship_row

print ("Done? Good I'll place my ship.")
print("Alright. You get to guess first.")
  
ship_row = randint(0, len(board1) - 1)
ship_col = randint(0, len(board1[0]) - 1)
orientation = rnd.random() > 0.5

if orientation == True:
    ship_row2,ship_row3 = placeship(ship_row,ship_col,orientation)
    ship_col2 = ship_col
    ship_col3 =ship_col
if orientation == False:
    ship_col2,ship_col3 = placeship(ship_row,ship_col,orientation)
    ship_row2 = ship_row
    ship_row3 = ship_row

print("")
   
count1 = 0
count2 = 0
turn = 0
while (count1 < 3) and (count2 < 3):
    turn = turn + 1
    print ("Turn", turn)
    guess_row = int(input("Guess Row:"))-1
    guess_col = int(input("Guess Col:"))-1
    count1 = count1 + check(board1,guess_row,guess_col,ship_row,ship_col,ship_row2,ship_row3,ship_col2,ship_col3)
    if count1 < 3:
        print("")
        print ("Now its my turn.")
        print ("")
        compguessrow =  randint(0, len(board2) - 1)
        compguesscol =  randint(0, len(board2[0]) - 1)
        while (board2[compguessrow][compguesscol] == "#" or board2[compguessrow][compguesscol] == "X" ):
            compguessrow =  randint(0, len(board2) - 1)
            compguesscol =  randint(0, len(board2[0]) - 1)
        count2 = count2 + check(board2,compguessrow,compguesscol,urship_row,urship_col,urship_row2,urship_row3,urship_col2,urship_col3)
                   
    print ("Computer")
    print_board(board1)
    print ("")
    print ("-------")
    print ("")
    print ("Human")
    print_board(board2)
    print ("")

if count1 == 3:
    print ("You have sunk my battleship. It took you " + str(turn) + " tries.")
if count2 == 3:
    print ("I have sunk your battleship. It took me " + str(turn) + " tries.")