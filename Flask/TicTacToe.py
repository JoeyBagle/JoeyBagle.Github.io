import numpy as np

currentrow = int
currentcol = int
global winner

def game():

	# Define the grid

	grid = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
	turn = True
	winner = 0
	gameover = False
	print(grid)
	while not gameover:

		# Determine who's turn it is

		if turn:
			player = 1
		elif not turn:
			player = 2

		# Tell the players

		print("it is "+ str(player) +"'s turn")
		getMove(grid, turn)
		winner = evaluate(grid, player, winner)
		if turn == True:
			turn = False # Switch to O's turn
		else:
			turn = True # Switch to X's turn
		if winner != 0: # Gameover
			gameover = True
	if winner == 3: # Declare Winner
		print("Good game, Tie.")
	else:
		print("Good game, winner is player "+ str(winner))

# Function to get the player move

def getMove(grid, turn):
	currentrow = int(input("Row to change number: "))
	currentcol = int(input("Column to change number: "))

	# Check if square is open, if it is, change it to whoever the current player is

	if grid[currentrow][currentcol] == 0:
		if turn:
			grid[currentrow][currentcol] = 1
		elif not turn:
			grid[currentrow][currentcol] = 2
	elif grid[currentrow][currentcol] != 0:
		print("Square is taken")
		getMove(grid, turn)

def evaluate(grid, player, winner):
	player = player

	# Check horizontal
	if grid[0][0] == grid[0][1] and grid[0][1] == grid[0][2] and grid[0][0] > 0:
		winner = player
	elif grid[1][0] == grid[1][1] and grid[1][1] == grid[1][2] and grid[1][0] > 0:
		winner = player
	elif grid[2][0] == grid[2][1] and grid[2][1] == grid[2][2] and grid[2][0] > 0:
		winner = player

	# Check Vertical
	elif grid[0][0] == grid[1][0] and grid[1][0] == grid[2][0] and grid[0][0] > 0:
		winner = player
	elif grid[0][1] == grid[1][1] and grid[1][1] == grid[2][1] and grid[0][1] > 0:
		winner = player
	elif grid[0][2] == grid[1][2] and grid[1][2] == grid[2][2] and grid[0][2] > 0:
		winner = player

	# Check Diagonal
	elif grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] and grid[0][0] > 0:
		winner = player
	elif grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0] and grid[0][2] > 0:
		winner = player

	# Check for tie
	if np.all(grid > 8):
		winner = 3
	return winner

game()
