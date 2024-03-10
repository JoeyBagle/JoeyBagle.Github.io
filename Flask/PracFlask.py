from flask import Flask, render_template, request, redirect, url_for
from logging.config import dictConfig
import math
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

@app.route("/testcards/", methods=["GET", "POST"])
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