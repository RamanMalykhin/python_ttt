#helper function to print the board
def print_board(rows, board):
    for x in range(rows):
        print ("|".join(board[x])) 

#taking an input        
def take_input(player):
        print('Active player:', player, '.')
        print('Input row for your move.')
        rawinputrow = input()
        print('Input column for your move')
        rawinputcolumn = input()
        return rawinputrow, rawinputcolumn


#"technical" input validation
def validate_position(board, rawinputrow, rawinputcolumn):
#        try:
        currentrow = int(rawinputrow)
        currentcolumn = int(rawinputcolumn)
        testvalue = board[currentrow][currentcolumn]
        return currentrow, currentcolumn
#        except (ValueError, IndexError):
#            print('Input invalid. Only 0, 1, 2 are permitted.')
            



#rule-wise input validation            
def validate_empty_cell(board, currentrow, currentcolumn):
        if board[currentrow][currentcolumn] == ' ':
            return
        else:
            raise ValueError('Position not empty. Choose another row-column pair.')

#writes player into selected cell 
def record_input(board, currentrow, currentcolumn, player):
        board[currentrow][currentcolumn] = player
        return board

#switch players    
def switch_players(player):
        if player == "X":
            nextplayer = "O"
        else:
            nextplayer = "X"
        return nextplayer


#win conditions validation
def check_win_conditions(winconditions, player, rows, board):
        for condition in winconditions:
            for ((cell0r,cell0c),(cell1r,cell1c),(cell2r,cell2c))in [condition]:
                if board[cell0r][cell0c] == board[cell1r][cell1c] == board[cell2r][cell2c]:
                    if board[cell0r][cell0c] != ' ':
                        print_board(rows, board)
                        print('Game over:', player, 'wins')
                        gameover = True
                        return gameover

#draw validation
def check_draw(rows, board):
        totallength = 0
        for row in board:
            totallength += len(("".join(row)).replace(" ",""))  
        if totallength == 9:
            print_board(rows, board)
            print('Game over: Draw')
            gameover = True
            return gameover
            
def tictactoe():
    #defining variables

    #winconditions
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

    #board
    rows = 3 
    cols = 3
    board = []
    for x in range(rows):
        row = [" " for i in range(cols)]
        board.append(row)

    #others
    player = "X"
    gameover = False
  

    while True:
	#prints the board at the beginning of each loop and takes input
        print_board(rows, board)
        inputrow, inputcolumn = take_input(player)
        
	#reads technically sanitized inputs or throws an exception
        try:
            inputrow, inputcolumn = validate_position(board, inputrow, inputcolumn)
        except (ValueError, IndexError):
            print('Input invalid. Only 0, 1, 2 are permitted.')
            continue
        
	#proceeds if cell is empty or throws an exception
        try:
            validate_empty_cell(board, inputrow, inputcolumn)
        except ValueError as exception:
            print(str(exception))
            continue
        
	#records a move
        board = record_input(board, inputrow, inputcolumn, player)
        
	#checks for win/draw and breaks loop if true
        if check_win_conditions(winconditions, player, rows, board) or check_draw(rows, board):
            break
	
	#we switch players at the very end to properly print and check earlier
        player = switch_players(player)



tictactoe()



