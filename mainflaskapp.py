"""
Para rodar o programa, é só seguir a ordem abaixo:

$ export FLASK_APP=mainflaskapp.py
$ export FLASK_ENV=development
$ flask run

"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
  return render_template("carrefour_telegram.html")

if __name__ == '__main__':
    app.run()