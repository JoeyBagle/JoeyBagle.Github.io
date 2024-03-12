from flask import Flask, render_template, request, redirect, url_for
from logging.config import dictConfig
import math
import numpy as np
# import jinja2

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

# to run:
# open terminal
# run "cd documents/flask"
# run "py -m flask --app PracFlask.py run"
# open a browser and go to "http://127.0.0.1:5000"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/testcards", methods=["GET", "POST"])
def testcards():
    total = 0
    valid = False
    if request.method == 'POST':
        cardnum = request.form["cardnum"]
        cardnumarray = list(cardnum)
        app.logger.info(cardnumarray)
        if len(cardnum) == 16 and not math.isnan(int(cardnum)):
            for i in range(0, len(cardnumarray), 1):
                cardnumarray[i] = int(cardnumarray[i])
                pass
            app.logger.info(cardnumarray)
            for x in range(0, len(cardnumarray), 2):
              cardnumarray[x] = cardnumarray[x] * 2
              if cardnumarray[x] >= 10:
                cardnumarray[x] = sum(divmod(cardnumarray[x], 10))
            app.logger.info(cardnumarray)
            for r in range(0, len(cardnumarray), 1):
                total = total + cardnumarray[r]
            app.logger.info(total)
        if total % 10 == 0:
            valid = True
        if len(cardnum) != 16 or math.isnan(int(cardnum)):
            app.logger.error("bad input")
            valid = False

        app.logger.info(valid)
        if valid == True:
            iscardvalid = 'valid'
        else:
            iscardvalid = 'invalid'
        return render_template("testcards.html", iscardvalid = iscardvalid)
            
    return render_template("testcards.html")

@app.route("/tictactoe", methods=["GET", "POST"])
def tictactoe():
    grid = np.array([[0,0,0],[0,0,0],[0,0,0]])
    turn = 1
    gameover = False
    app.logger.info(grid)
    if request.method == 'POST':
        move = request.form('value')
        app.logger.info(value)

    return render_template("tictactoe.html")

# def game():

#     # Define the grid

#     grid = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
#     turn = True
#     winner = 0
#     gameover = False
#     print(grid)
#     if winner == 3: # Declare Winner
#         print("Good game, Tie.")
#     else:
#         print("Good game, winner is player "+ str(winner))

# # Function to get the player move

# def getMove(grid, turn):
#     currentrow = int(input("Row to change number: "))
#     currentcol = int(input("Column to change number: "))

#     # Check if square is open, if it is, change it to whoever the current player is

#     if grid[currentrow][currentcol] == 0:
#         if turn:
#             grid[currentrow][currentcol] = 1
#         elif not turn:
#             grid[currentrow][currentcol] = 2
#     elif grid[currentrow][currentcol] != 0:
#         print("Square is taken")
#         getMove(grid, turn)

# def evaluate(grid, player, winner):
#     player = player

#     # Check horizontal
#     if grid[0][0] == grid[0][1] and grid[0][1] == grid[0][2] and grid[0][0] > 0:
#         winner = player
#     elif grid[1][0] == grid[1][1] and grid[1][1] == grid[1][2] and grid[1][0] > 0:
#         winner = player
#     elif grid[2][0] == grid[2][1] and grid[2][1] == grid[2][2] and grid[2][0] > 0:
#         winner = player

#     # Check Vertical
#     elif grid[0][0] == grid[1][0] and grid[1][0] == grid[2][0] and grid[0][0] > 0:
#         winner = player
#     elif grid[0][1] == grid[1][1] and grid[1][1] == grid[2][1] and grid[0][1] > 0:
#         winner = player
#     elif grid[0][2] == grid[1][2] and grid[1][2] == grid[2][2] and grid[0][2] > 0:
#         winner = player

#     # Check Diagonal
#     elif grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] and grid[0][0] > 0:
#         winner = player
#     elif grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0] and grid[0][2] > 0:
#         winner = player

#     # Check for tie
#     if np.all(grid > 8):
#         winner = 3
#     return winner