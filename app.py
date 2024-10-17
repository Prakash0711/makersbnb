import os
from flask import (
    Flask,
    request,
    render_template,
    redirect,
    flash,
    jsonify,
    url_for,
    session,
)
from lib.database_connection import get_flask_database_connection
from lib.space import Space
from lib.space_repository import SpaceRepository
from lib.user_repository import UserRepository
from lib.user import User
from lib.booking import Booking
from lib.booking_repository import BookingRepository
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = os.urandom(24)
bcrypt = Bcrypt(app)


@app.route("/home", methods=["GET"])
def get_home():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    space_list = repository.all()
    return render_template("home.html", spaces=space_list)


def is_logged_in():
    return "user_id" in session


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["user_password"]
        fullname = request.form["full_name"]

        # Hash password
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        # Create user object
        new_user = User(
            id=None,
            username=username,
            user_password=hashed_password,
            email=email,
            full_name=fullname,
        )

        # Save user
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection)
        repository.add_user(new_user)

        flash(f"Welcome! Please login")
        return redirect(url_for("login"))
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["user_password"]

        # Get user from database by email
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection)
        new_user = repository.find_by_username(username)

        if new_user and bcrypt.check_password_hash(new_user.user_password, password):
            # Session management
            session["user_id"] = new_user.id
            session["username"] = new_user.username
            session["full_name"] = new_user.full_name
            flash("Login succesful!")
            return redirect(url_for("userhome"))
        else:
            flash("Invalid input")
    return render_template("login.html")


@app.route("/userhome", methods=["GET"])
def userhome():
    if not is_logged_in():
        flash("Please login first")
        return redirect(url_for("login"))

    return render_template("userhome.html")


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5001)))
