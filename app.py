from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "replace_me"

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/games")
def games():
    return render_template("games.html")

@app.route("/coinflip")
def coinflip():
    return render_template("coinflip.html")

@app.route("/play_coinflip", methods=["POST"])
def play_coinflip():
    choice = request.form.get("choice")  # heads or tails
    result = random.choice(["heads", "tails"])
    win = (choice == result)
    return {"result": result, "win": win}

@app.route("/roulette")
def roulette():
    return render_template("roulette.html")

@app.route("/slot")
def slot():
    return render_template("slot.html")
