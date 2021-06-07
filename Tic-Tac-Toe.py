#!/usr/bin/env python
# coding: utf-8

# In[14]:


#win conditions initialization
#doing this still feels stupid
#but at least this will let me check them  algorithmically later
winconditions = [[] for i in range(8)]
#vertical
winconditions[0] = ((0,0),(1,0),(2,0))
winconditions[1] = ((0,1),(1,1),(2,1))
winconditions[2] = ((0,2),(1,2),(2,2))
#horizontal
winconditions[3] = ((0,0),(0,1),(0,2))
winconditions[4] = ((1,0),(1,1),(1,2))
winconditions[5] = ((2,0),(2,1),(2,2))
#diagonal
winconditions[6] = ((0,0),(1,1),(2,2))
winconditions[7] = ((0,2),(1,1),(2,0))

#board initialization
rows = 3 
cols = 3
board = []
for x in range(rows):
    row = [" " for i in range(cols)]
    board.append(row)


#helper function to print the board
def currentstate():
    for x in range(rows):
        print ("|".join(board[x])) 
        
def tictactoe():
        
    #variables initialization
    player = "X"
    gameover = False

    while True:
        #printing the board
        currentstate()
        
        #taking an input
        print('Active player:', player, '.')
        print('Input row for your move.')
        rawinputrow = input()
        print('Input column for your move')
        rawinputcolumn = input()
        
        #input value validation
        try:
            currentrow = int(rawinputrow)
            currentcolumn = int(rawinputcolumn)
            testvalue = board[currentrow][currentcolumn]
        except (ValueError, IndexError):
            print('Input invalid. Only 0, 1, 2 are permitted.')
            continue
                    
        #rule-wise input validation and writing
        if board[currentrow][currentcolumn] == ' ':
            board[currentrow][currentcolumn] = player
            if player == "X":
                nextplayer = "O"
            else:
                nextplayer = "X"
        else:
            print('Position not empty. Choose another row-column pair.')   
        
        #win conditions validation
        for condition in winconditions:
            for ((cell0r,cell0c),(cell1r,cell1c),(cell2r,cell2c))in [condition]:
                if board[cell0r][cell0c] == board[cell1r][cell1c] == board[cell2r][cell2c]:
                    if board[cell0r][cell0c] != ' ':
                        currentstate()
                        print('Game over:', player, 'wins')
                        gameover = True
        
        totallength = 0
        for row in board:
            totallength += len(("".join(row)).replace(" ",""))  
        if totallength == 9:
            currentstate()
            print('Game over: Draw')
            gameover = True

        if gameover:
            break
        
        player = nextplayer


# In[15]:


tictactoe()
