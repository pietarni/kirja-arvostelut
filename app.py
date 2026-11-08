import sqlite3

from flask import Flask
from flask import abort, flash, redirect, render_template, request, session

import books
import config
import users

app = Flask(__name__)
app.secret_key = config.secret_key

def require_login():
    if "user_id" not in session:
        abort(403)

def read_book_form():
    return (request.form["title"], request.form["author"],
            request.form["year"], request.form["description"])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new_book")
def new_book():
    require_login()
    return render_template("new_book.html")

@app.route("/create_book", methods=["POST"])
def create_book():
    require_login()
    title, author, year, description = read_book_form()
    user_id = session["user_id"]
    books.add_book(title, author, year, description, user_id)
    return redirect("/")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        flash("VIRHE: salasanat eivät ole samat")
        return redirect("/register")

    try:
        users.create_user(username, password1)
    except sqlite3.IntegrityError:
        flash("VIRHE: tunnus on jo varattu")
        return redirect("/register")

    flash("Tunnus luotu, voit nyt kirjautua sisään")
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    username = request.form["username"]
    password = request.form["password"]

    user_id = users.check_login(username, password)
    if user_id:
        session["user_id"] = user_id
        session["username"] = username
        return redirect("/")

    flash("VIRHE: väärä tunnus tai salasana")
    return redirect("/login")

@app.route("/logout")
def logout():
    if "user_id" in session:
        del session["user_id"]
        del session["username"]
    return redirect("/")
