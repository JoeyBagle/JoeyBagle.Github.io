import numpy as np

currentrow = int
currentcol = int

def game():
	grid = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
	turn = True
	winner = 0
	gameover = False
	while not gameover:
		if turn:
			player = 1
		elif not turn:
			player = 2
		print("it is "+ str(player) +"'s turn")
		getMove(grid, turn)
		print(grid)
		# evaluate(grid, player)
		if turn == True:
			turn = False # Switch to O's turn
		else:
			turn = True # Switch to X's turn
		if winner != 0:
			gameover = True
	print("Good game, winner is player "+ winner)

def getMove(grid, turn):
	currentrow = int(input("Row to change number: "))
	currentcol = int(input("Column to change number: "))
	if turn:
		grid[currentrow][currentcol] = 1
	elif not turn:
		grid[currentrow][currentcol] = 2

def evaluate(grid, player):



game()
