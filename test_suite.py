import pytest

def test_print_board():
	#Arrange
	from ttt import print_board
	import sys
	import io
	

	old_stdout = sys.stdout
	new_stdout = io.StringIO()
	sys.stdout = new_stdout
	test_board_1_move = [[" "," "," "],[" ","X"," "],[" "," "," "]]

	#Act
	print_board(3, test_board_1_move)
	output = new_stdout.getvalue()
	sys.stdout = old_stdout

	#Assert
	assert output == ' | | \n |X| \n | | \n'

def test_write():
	#Arrange
	from ttt import validate_position
	from ttt import validate_empty_cell
	from ttt import record_input
	
	test_board_pre_move = [[" "," "," "],[" ","X"," "],[" "," "," "]]
	test_input_row = 0
	test_input_column = 0
	test_player = 'O'
	
	#Act
	board = test_board_pre_move
	inputrow = test_input_row
	inputcolumn = test_input_column
	player = test_player

	try:
		inputrow, inputcolumn = validate_position(board, inputrow, inputcolumn)
	except (ValueError, IndexError):
		print('Input invalid. Only 0, 1, 2 are permitted.')
		
	        
	try:
		validate_empty_cell(board, inputrow, inputcolumn)
	except ValueError as exception:
		print(str(exception))
		
	        
	board = record_input(board, inputrow, inputcolumn, player)

	#Assert
	board[test_input_row][test_input_column] == 'O'
